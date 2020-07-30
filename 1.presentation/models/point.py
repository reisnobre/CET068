"""."""
import random


class Point:
    """."""
    def __init__(self):
        self.x = random.randrange(1, 600)
        self.y = random.randrange(1, 600)
        self.label = 1 if self.x > self.y else -1
