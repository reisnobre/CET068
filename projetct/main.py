"""

create the main board
create a ship

The code runs from the perspective of a captain
When he lands a hit the computer generates for him
A array of possible locations
This is done based on the idea that from a hit, a tree of hits is problable

"""
# from tree import node, tree
from board import Board
from linear_ship import Linear_Ship

BOARD = Board()

# This is where
coordinates = (4, 4)
ship_length = 5
linear_ship = Linear_Ship(coordinates, ship_length)


BOARD.set_cell(linear_ship.coordinates, linear_ship.length)

linear_ship.generate(BOARD)
linear_ship.tree.print()

BOARD.print()


# import numpy as np

#
# def gen_board():
#     """."""
#     _ = np.ones([10, 10], dtype=int)
#
#     return _
#
#
# def gen_cruzer(coor, board):
#     """."""
#     cruzer_length = 4
#     cruzer_range = 4
#
#     line = coor[0]
#     col = coor[1]
#     _ = board
#     _[line, col] = 0  # where the hit occured
#
#     if line + 1 <= 9:
#         if col + 1 <= 9:
#             _[line+1, col+1] = 0  # up and right
#         if col - 1 >= 0:
#             _[line+1, col-1] = 0  # down and right
#     if line - 1 >= 0:
#         if col + 1 <= 9:
#             _[line-1, col+1] = 0  # up and left
#         if col - 1 >= 0:
#             _[line-1, col-1] = 0  # down and left
#
#     #
#     _ = rotations([line, col], cruzer_length, cruzer_range, _)
#
#     return _
#
#
# def rotations(start, boat_length, amount, board):
#     """."""
#     line = start[0]
#     col = start[1]
#     temp_a = amount
#     stack = []
#
#     # generate the rotations, if a rotation fails
#     # I have to cancel that rotation completly
#
#     # Lock the line and increment the col by the amount
#     _ = board
#     for i in range(boat_length):
#         local_col = col + i + 1
#         if local_col <= 9:
#             stack.append([line, local_col])
#             if _[line, local_col] == 1:
#                 _[line, local_col] = temp_a
#                 temp_a = temp_a - 1
#             else:
#                 _ = reverse(stack, _)
#                 break
#         else:
#             _ = reverse(stack, _)
#             break
#
#     stack = []
#
#     temp_a = amount
#     # Lock the line and decrement the col by the amount
#     for i in range(boat_length):
#         local_col = col - i - 1
#         if local_col >= 0:
#             stack.append([line, local_col])
#             if _[line, local_col] == 1:
#                 _[line, local_col] = temp_a
#                 temp_a = temp_a - 1
#             else:
#                 _ = reverse(stack, _)
#                 break
#         else:
#             _ = reverse(stack, _)
#             break
#
#     stack = []
#
#     temp_a = amount
#     # Lock the  col and increment the y by the amount
#     for i in range(boat_length):
#         local_line = line + i + 1
#         if local_line <= 9:
#             stack.append([local_line, col])
#             if _[local_line, col] == 1:
#                 _[local_line, col] = temp_a
#                 temp_a = temp_a - 1
#             else:
#                 _ = reverse(stack, _)
#                 break
#         else:
#             _ = reverse(stack, _)
#             break
#
#     stack = []
#     #
#     temp_a = amount
#     for i in range(boat_length):
#         local_line = line - i - 1
#         if local_line >= 0:
#             stack.append([local_line, col])
#             if _[local_line, col] == 1:
#                 _[local_line, col] = temp_a
#                 temp_a = temp_a - 1
#             else:
#                 _ = reverse(stack, _)
#                 break
#         else:
#             _ = reverse(stack, _)
#             break
#
#     stack = []
#     return _
#
#
# def reverse(stack, board):
#     """."""
#     for coor in stack:
#         board[coor[0], coor[1]] = 1
#     return board
# #
# # def check(coor, board):
#
#
#
# BOARD = gen_board()
# BOARDS = []
# X = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
#
#
# # At this point the board is empty and read to search
#
# # Here I'll simulate a HIT on 4,3
#
# coord = input('Coords: linha coluna from 0 to 9:\n')
# hit_line = int(coord.split(' ')[0])
# hit_col = int(coord.split(' ')[1])
#
#
# #
# # BOARD[guess_x][guess_y] = 0
# #
#
#
# # I have to generate the guesses and generate water where is necessary
# # the first guess is corr[x][y+1]
# # the second guess is corr[x][y-1]
# # the third guess is corr[x+1][y]
# # the fourth guess is corr[x-1][y]
#
# # print(gen_cruzer([hit_line, hit_col], BOARD))
#
# BOARDS.append(gen_cruzer([hit_line, hit_col], BOARD))
# arr = BOARDS[0]
# print(arr)
# results = np.where(arr == np.amax(arr))
# #
# guesses = list(zip(results[0], results[1]))
# print(guesses)
