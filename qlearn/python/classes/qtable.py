"""."""
import numpy as np
import pickle
import time

LEARNING_RATE = 0.1
DISCOUNT = 0.95

MOVE_PENALTY = 1  # feel free to tinker with these!
ENEMY_PENALTY = 300  # feel free to tinker with these!
DOOR_REWARD = 25  # feel free to tinker with these!


class QTable:
    """."""

    def __init__(self, SIZE, start_q_table=None):
        """."""
        self.table = self.create_q_table(SIZE, start_q_table)
        pass

    def create_q_table(self, SIZE, start_q_table):
        """Se eu não tiver uma tabela inicial, crie uma com valores aleatórios."""
        if start_q_table is None:
            q_table = {}
            for i in range(-SIZE + 1, SIZE):
                for ii in range(-SIZE + 1, SIZE):
                    for iii in range(-SIZE + 1, SIZE):
                        for iiii in range(-SIZE + 1, SIZE):
                            q_table[((i, ii), (iii, iiii))] = [np.random.uniform(-5, 0) for i in range(4)]
        else:
            with open(start_q_table, "rb") as f:
                q_table = pickle.load(f)
        return q_table

    def get_action(self, observation):
        """Retorna a ação com o maior q_value."""
        return np.argmax(self.table[observation])

    def get_q_value(self, observation, action):
        """Retorna o q_value para um certo estado e uma ação."""
        return self.table[observation][action]

    def get_new_q(self, reward, new_observation, observation, action):
        """Cria um novo q_value, dado as variáveis acima."""
        current_q = self.get_q_value(observation, action)
        max_future_q = self.get_max_future_q(new_observation)

        if reward == DOOR_REWARD:
            new_q = DOOR_REWARD
        elif reward == -ENEMY_PENALTY:
            new_q = -ENEMY_PENALTY
        else:
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
        return new_q

    def get_max_future_q(self, new_observation):
        """Retorna o maior q_value para um dado estado."""
        return np.max(self.table[new_observation])

    def set_q_value(self, observation, action, value):
        """Preenche o valor de um dado q_value para um estado com um novo valor."""
        self.table[observation][action] = value

    def make_picke(self):
        """Salva a tabela para um arquivo para posterior uso."""
        with open(f"qtable-{int(time.time())}.pickle", "wb") as f:
            pickle.dump(self.table, f)
