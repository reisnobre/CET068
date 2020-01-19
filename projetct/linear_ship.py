"""."""

from tree import node, tree


class Linear_Ship:
    """."""

    def __init__(self, coordinates, length):
        """."""
        self.length = length  # the length defines the ship type
        self.coordinates = coordinates
        self.tree = None
        # self.generate

    def create(self):
        """."""
    
    def generate(self, BOARD):
        """
            If there's no tree I need to generate all rotations
        """
        line = self.coordinates[0]
        col = self.coordinates[1]
        grid = BOARD.last_grid()

        if self.tree is None:
            self.tree = tree()
            self.tree.insert(node(self.coordinates))

            # set the water

            if line + 1 <= 9:
                if col + 1 <= 9:
                    grid[line+1, col+1].value = 0  # up and right
                if col - 1 >= 0:
                    grid[line+1, col-1].value = 0  # down and right
            if line - 1 >= 0:
                if col + 1 <= 9:
                    grid[line-1, col+1].value = 0  # up and left
                if col - 1 >= 0:
                    grid[line-1, col-1].value = 0  # down and left
# #
            # generate all 4 rotations
        node_ir = node((line, col + 1))
        node_il = node((line, col - 1))
        node_iu = node((line + 1, col))
        node_id = node((line - 1, col))
        if BOARD.check_bounds(node_ir):
            self.tree.insert(node_ir)
        if BOARD.check_bounds(node_il):
            self.tree.insert(node_il)
        if BOARD.check_bounds(node_iu):
            self.tree.insert(node_iu)
        if BOARD.check_bounds(node_id):
            self.tree.insert(node_id)

            # call generate on the children of the tree based on the length of the ship

    # def rotations(self):
    #     """."""
    #     line = self.coordinates[0]
    #     col = self.coordinates[1]
    #     temp_a = self.length
    #     stack = []
    #
        # # generate the rotations, if a rotation fails
        # # I have to cancel that rotation completly
        #
        # # Lock the line and increment the col by the amount
        # _ = board
        # for i in range(boat_length):
        #     local_col = col + i + 1
        #     if local_col <= 9:
        #         stack.append([line, local_col])
        #         if _[line, local_col] == 1:
        #             _[line, local_col] = temp_a
        #             temp_a = temp_a - 1
        #         else:
        #             _ = reverse(stack, _)
        #             break
        #     else:
        #         _ = reverse(stack, _)
        #         break
        #
        # stack = []
        #
        # temp_a = amount
        # # Lock the line and decrement the col by the amount
        # for i in range(boat_length):
        #     local_col = col - i - 1
        #     if local_col >= 0:
        #         stack.append([line, local_col])
        #         if _[line, local_col] == 1:
        #             _[line, local_col] = temp_a
        #             temp_a = temp_a - 1
        #         else:
        #             _ = reverse(stack, _)
        #             break
        #     else:
        #         _ = reverse(stack, _)
        #         break
        #
        # stack = []
        #
        # temp_a = amount
        # # Lock the  col and increment the y by the amount
        # for i in range(boat_length):
        #     local_line = line + i + 1
        #     if local_line <= 9:
        #         stack.append([local_line, col])
        #         if _[local_line, col] == 1:
        #             _[local_line, col] = temp_a
        #             temp_a = temp_a - 1
        #         else:
        #             _ = reverse(stack, _)
        #             break
        #     else:
        #         _ = reverse(stack, _)
        #         break
        #
        # stack = []
        # #
        # temp_a = amount
        # for i in range(boat_length):
        #     local_line = line - i - 1
        #     if local_line >= 0:
        #         stack.append([local_line, col])
        #         if _[local_line, col] == 1:
        #             _[local_line, col] = temp_a
        #             temp_a = temp_a - 1
        #         else:
        #             _ = reverse(stack, _)
        #             break
        #     else:
        #         _ = reverse(stack, _)
        #         break
        #
        # stack = []
        # return _
