"""."""

# The first step is check
# if the state is not true
# generate the childs

INITIAL_STATE = '11001'
KNOW_STATES = []


class Node:
    def __init__(self, value=None, parent=None):
        self.value = value if value is not None else '11001'
        self.childs = []
        self.parent = None  # pointer to parent node in tree


class Tree:
    """."""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        # crie um novo nó
        # diga a aquele no, que seu pai é o nó atual
        _ = Node(value)
        _.parent = node
        self.root.childs.append(_)

    def print_tree(self):
        """."""
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            for child in cur_node.childs:
                self._print_tree(child)
            print(cur_node.value)


def flip(state, index):
    """."""
    state[index] = '0' if state[index] == '1' else '1'
    #
    left = index - 1
    right = index + 1
    if right < len(INITIAL_STATE):
        state[right] = '0' if state[right] == '1' else '1'
    if left >= 0:
        state[left] = '0' if state[left] == '1' else '1'

    state = ''.join(state)
    return state
    # KNOW_STATES.append(state)

# def check(state):
#     """."""
#     target = state[0]
#
#     for _ in state[1:]:
#         if _ != target:
#             return False
#     return True


def generate(state):
    """."""
    tree = Tree()

    KNOW_STATES.append(state)
    tree.insert(state)

    state = list(state)
    for _, index in enumerate(state):
        generated_state = flip(state, int(index))

        try:
            KNOW_STATES.index(generated_state)
        except ValueError:
            KNOW_STATES.append(Node(generated_state))
            tree.insert(generated_state)
            # self.root.childs.append(generated_state)
    tree.print_tree()


generate(INITIAL_STATE)
