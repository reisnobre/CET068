"""."""
import numpy as np
import pickle


class QLearning:
    """."""

    def __init__(self, SIZE, start_q_table=None):
        """."""
        pass

    @staticmethod
    def create_q_table(SIZE, start_q_table=None):
        """."""
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
