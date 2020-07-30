"""
A ship is created on hit
A tree is also created on a hit based on the location

After that, the root node it self should create it's childs

"""


class node:
    """."""

    def __init__(self, coordinates):
        """."""
        self.coordinates = coordinates
        self.children = []
        self.parent = None  # pointer to parent node in tree

class tree:
    """."""

    def __init__(self):
        """."""
        self.root = None

    def insert(self, child_node):
        """."""
        if self.root is None:
            self.root = child_node
        else:
            child_node.parent = self.root
            self.root.children.append(child_node)

    def print(self):
        """."""
        if self.root is not None:
            self._print(self.root)
        # # else:
        # #     print(node.coordinates)

    def _print(self, n):
        if n is not None:
            print(n.coordinates)
            for child in n.children:
                self._print(child)
