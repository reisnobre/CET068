"""."""
import gym
import numpy as np
import matplotlib.pyplot as plt

env = gym.make('MountainCar-v0')

# Top values
# print(env.observation_space.high)

# Top lower values of position and velocity
# print(env.observation_space.low)

# Number of actions possible
# print(env.action_space.n)

LEARNING_RATE = 0.1
# weight of how important we find future actions over the current action
DISCOUNT = 0.95
EPISODES = 2000
SHOW_EVERY = 500
# Discrete observation space size, from 0.6 to -1.2 separate the range in 20 range (buckets) discrete values
DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)

# Size of each one of the chunks, buckets go from 0.09 to 0.007 velocity
discrete_os_win_size = (env.observation_space.high - env.observation_space.low) / DISCRETE_OS_SIZE

# Chance of random action for finding better results
epsilon = 0.5
START_EPSILON_DECAYING = 1
END_EPSILON_DECAYING = EPISODES // 2
epsilon_decay_value = epsilon / (END_EPSILON_DECAYING - START_EPSILON_DECAYING)

# Rewards is going to be -1 until the flag is reached thats equals to 0
"""
For each action theres a combination of position and velocity that has a value on my q_table.
"""
q_table = np.random.uniform(low=-2, high=0, size=(DISCRETE_OS_SIZE + [env.action_space.n]))

ep_rewards = []
aggr_ep_rewards = {'ep': [], 'avg': [], 'min': [], 'max': []}


def get_discrite_state(state):
    """
    Return a tuple with discrete values of a state.

    Function that creates of values buckets the values into discrete values to avoid massive amounts of data.
    """
    discrete_state = (state - env.observation_space.low) / discrete_os_win_size
    return tuple(discrete_state.astype(np.int))


"""
For my discrete_state, I have my q_values on my q_table on position q_table[discrete_state], one for each action
Using np.argmax I can find the action that has the largest q_value
"""
for episode in range(EPISODES):
    episode_reward = 0
    if not episode % SHOW_EVERY:
        render = True
        print(episode)
    else:
        render = False

    discrete_state = get_discrite_state(env.reset())
    done = False
    while not done:
        # get the action that has the max q_value of my discrete_state as mentioned on line 8
        if np.random.random() > epsilon:
            action = np.argmax(q_table[discrete_state])
        else:
            action = np.random.randint(0, env.action_space.n)
        new_state, reward, done, _ = env.step(action)
        # print(new_state)

        episode_reward += reward

        new_discrete_state = get_discrite_state(new_state)
        print(new_discrete_state)
        if render:
            env.render()
        if not done:
            # here I need the max q_value it self, not the action that gives me the max q_value
            """
            with time max_future_q gets back propagated into my values
            """
            max_future_q = np.max(q_table[new_discrete_state])
            # get the q_value for the action
            current_q = q_table[discrete_state + (action, )]
            # apply the formula, the back propagation occurs using the DISCOUNT * max_future_q
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)

            """
            after making the step on line 58, update the q_value for that state on that action
            """
            q_table[discrete_state + (action, )] = new_q

        elif new_state[0] >= env.goal_position:
            # define the reward for achieving the goal, on that state for that action
            print(f"We made it on episode {episode}")
            q_table[discrete_state + (action,)] = 0

        discrete_state = new_discrete_state

    if END_EPSILON_DECAYING >= episode >= START_EPSILON_DECAYING:
        epsilon -= epsilon_decay_value

    ep_rewards.append(episode_reward)

    if not episode % SHOW_EVERY:
        average_reward = sum(ep_rewards[-SHOW_EVERY:]) / len(ep_rewards[-SHOW_EVERY:])
        aggr_ep_rewards['ep'].append(episode)
        aggr_ep_rewards['avg'].append(average_reward)
        aggr_ep_rewards['min'].append(min(ep_rewards[-SHOW_EVERY:]))
        aggr_ep_rewards['max'].append(max(ep_rewards[-SHOW_EVERY:]))
        print(f"Episode: {episode} avg: {average_reward} min: {min(ep_rewards[-SHOW_EVERY:])} max: {max(ep_rewards[-SHOW_EVERY:])}")

env.close()

plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['avg'], label='avg')
plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['min'], label='min')
plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['max'], label='max')
plt.legend(loc=4)
plt.show()
