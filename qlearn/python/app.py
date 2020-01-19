"""."""
from classes.entity import Entity
from classes.qtable import QTable
import numpy as np  # for array stuff and random
from PIL import Image  # for creating visual of our env
import cv2  # for showing our visual live
import matplotlib.pyplot as plt  # for graphing our mean rewards over time
from matplotlib import style  # to make pretty charts because it matters.
style.use("ggplot")  # setting our style!")


SIZE = 10

HM_EPISODES = 25000

MOVE_PENALTY = 1  # feel free to tinker with these!
ENEMY_PENALTY = 300  # feel free to tinker with these!
DOOR_REWARD = 25  # feel free to tinker with these!

epsilon = 0.5  # randomness
EPS_DECAY = 0.9999  # Every episode will be epsilon*EPS_DECAY
SHOW_EVERY = 2000  # how often to play through env visually.

start_q_table = 'qtable-1579431776.pickle'  # if we have a pickled Q table, we'll put the filename of it here.

PLAYER_N = 1  # player key in dict
DOOR_N = 2  # door key in dict
ENEMY_N = 3  # enemy key in dict

# the dict! Using just for colors
d = {1: (255, 175, 0),  # blueish color
     2: (0, 255, 0),  # green
     3: (0, 0, 255)}  # red

episode_rewards = []

q_table = QTable(SIZE)
for episode in range(HM_EPISODES):
    # Crie os individuos
    player = Entity(SIZE)
    door = Entity(SIZE)
    enemy = Entity(SIZE)
    # se necessário renderize a tela e imprima certas informações
    if episode % SHOW_EVERY == 0:
        print(f"on #{episode}, epsilon is {epsilon}")
        print(f"{SHOW_EVERY} ep mean: {np.mean(episode_rewards[-SHOW_EVERY:])}")
        show = True
    else:
        show = False

    episode_reward = 0
    for i in range(200):
        # observação é uma tupla que contem a distância relativa entre o jogador e o alimento e o inimigo no formato (7, 2)
        observation = (player - door, player - enemy)

        # Se necessário, realize uma ação aleatória para procurar outras soluções, mesmo que já tenha encontrado uma solução
        if np.random.random() > epsilon:
            action = q_table.get_action(observation)
        else:
            action = np.random.randint(0, 4)
        # Realize a ação, atualização a posição da entidade
        player.action(action)

        # Mova os outros individuos para introduzir complexidade
        enemy.move()
        # door.move()

        # Penalidades e recomenpensas
        if player.x == enemy.x and player.y == enemy.y:
            reward = -ENEMY_PENALTY
        elif player.x == door.x and player.y == door.y:
            reward = DOOR_REWARD
        else:
            reward = -MOVE_PENALTY

        # Nova observação baseada na posição atual do player
        new_observation = (player - door, player - enemy)

        # máximo q_value para tal observação
        max_future_q = q_table.get_max_future_q(new_observation)

        # q_value para a observação atual
        current_q = q_table.get_q_value(observation, action)

        # novo q_value baseado nas informações coletadas
        new_q = q_table.get_new_q(reward, new_observation, observation, action)

        # atualize o q_value para o novo q_value para a observação
        q_table.set_q_value(observation, action, new_q)

        # tirado do tutorial do cv2
        if show:
            env = np.zeros((SIZE, SIZE, 3), dtype=np.uint8)  # starts an rbg of our size
            env[door.x][door.y] = d[DOOR_N]  # sets the door location tile to green color
            env[player.x][player.y] = d[PLAYER_N]  # sets the player tile to blue
            env[enemy.x][enemy.y] = d[ENEMY_N]  # sets the enemy location to red
            img = Image.fromarray(env, 'RGB')  # reading to rgb. Apparently. Even tho color definitions are bgr. ???
            img = img.resize((300, 300))  # resizing so we can see our agent in all its glory.
            cv2.imshow("image", np.array(img))  # show it!
            if reward == DOOR_REWARD or reward == -ENEMY_PENALTY:  # crummy code to hang at the end if we reach abrupt end for good reasons or not.
                if cv2.waitKey(500) & 0xFF == ord('q'):
                    break
            else:
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        # armazenando informações para plotagem do grafico
        episode_reward += reward
        # se atingiu o objetivo ou perdeu, break
        if reward == DOOR_REWARD or reward == -ENEMY_PENALTY:
            break

    episode_rewards.append(episode_reward)
    epsilon *= EPS_DECAY

q_table.make_picke()
moving_avg = np.convolve(episode_rewards, np.ones((SHOW_EVERY,)) / SHOW_EVERY, mode='valid')

plt.plot([i for i in range(len(moving_avg))], moving_avg)
plt.ylabel(f"Reward {SHOW_EVERY}ma")
plt.xlabel("episode #")
plt.show()
