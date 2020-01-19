"""."""
import numpy as np


class Entity:
    """."""

    def __init__(self, SIZE):
        """."""
        self.x = np.random.randint(0, SIZE)
        self.y = np.random.randint(0, SIZE)
        self.board_size = SIZE

    def __sub__(self, target):
        """Redefinição da operação de subtração para individuos dessa classe para facilitar certas operações."""
        return (self.x - target.x, self.y - target.y)

    def action(self, choice):
        """Dado uma escolha, mova o individuo através do método move."""
        if choice == 0:
            self.move(x=1, y=1)
        elif choice == 1:
            self.move(x=-1, y=-1)
        elif choice == 2:
            self.move(x=-1, y=1)
        elif choice == 3:
            self.move(x=1, y=-1)

    def move(self, x=False, y=False):
        """Dado um x e y mova o individuo, se algo não for informado, mova aleatóriamente."""
        if not x:
            self.x += np.random.randint(-1, 2)
        else:
            self.x += x

        if not y:
            self.y += np.random.randint(-1, 2)
        else:
            self.y += y

        if self.x < 0:
            self.x = 0
        elif self.x > self.board_size - 1:
            self.x = self.board_size - 1
        if self.y < 0:
            self.y = 0
        elif self.y > self.board_size - 1:
            self.y = self.board_size - 1
