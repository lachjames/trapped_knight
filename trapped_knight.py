import numpy as np

ROTATIONS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]

KNIGHT_MOVES = []

for i_move in (1, 2):
    j_move = 3 - i_move
    for i_dir in (1, -1):
        for j_dir in (1, -1):
            KNIGHT_MOVES += [(i_dir * i_move, j_dir * j_move)]

print(KNIGHT_MOVES)

class SpiralBoard:

    def __init__(self, init_dim=100, dir = "counter_clockwise"):
        self.dimension = init_dim
        self.dir = dir
        if self.dir == "clockwise":
            self.i_additive = 0
            self.i_mult = 1
        elif self.dir == "counter_clockwise":
            self.i_additive = self.dimension - 1
            self.i_mult = -1
        else:
            print("Unexpected direction {} found - please use 'clockwise' or 'counter_clockwise'")

        self.initialize()

    def initialize(self):
        self.array = np.asarray(
            [
                [0] * self.dimension
            ] * self.dimension
        )

        i = self.dimension // 2
        j = i

        x = 1
        next_square_root = 1

        cur_rotation_idx = 0
        cur_length = 1

        while i >= 0 and i < self.dimension and j >= 0 and j < self.dimension:
            cur_rotation = ROTATIONS[cur_rotation_idx % 4]
            for _ in range(cur_length):
                i += cur_rotation[0]
                j += cur_rotation[1]
                self.array[self.i_additive + self.i_mult * i, j] = x
                if x == 1:
                    self.center = (self.i_additive + self.i_mult * i, j)
                #print("Length={}, x={}, rot={}, arr=:".format(cur_length, x, cur_rotation))
                #print(self.array)

                if x != 1 and x == next_square_root * next_square_root:
                    # We have completed a full square
                    #print("Full square done")
                    next_square_root += 2
                    cur_length += 2
                    self.cur_rotation_idx = 0
                    i -= 1
                    j += 1
                elif x == 1:
                    next_square_root = 3
                    cur_length = 1
                    self.cur_rotation_idx = 1
                elif x == 3:
                    cur_length += 1

                x += 1

            cur_rotation_idx += 1

    def __getitem__(self, item):
        return self.array[item[0], item[1]]


    def __setitem__(self, key, item):
        self.array[key[0], key[1]] = item

    def __str__(self):
        return str(self.array)

class TrappedKnight:
    def __init__(self, dim, not_allowed = []):
        self.dim = dim
        self.not_allowed = not_allowed

        self.board = SpiralBoard(self.dim)
        self.cur_i, self.cur_j = self.board.center

        self.visited = set()
        for pos in not_allowed:
            self.visited.add(pos)
        self.visited.add((self.cur_i, self.cur_j))

        self.move_list = [(self.cur_i, self.cur_j)]

    def move(self):
        allowed_moves = self.potential_moves()

        if len(allowed_moves) == 0:
            return False

        min_value = float("Inf")
        min_move = None
        for move in allowed_moves:
            if self.board[move] < min_value:
                min_value = self.board[move]
                min_move = move

        self.move_list += [min_move]

        self.cur_i = min_move[0]
        self.cur_j = min_move[1]
        self.visited.add((self.cur_i, self.cur_j))

        return True

    def potential_moves(self):
        moves = []

        for move in KNIGHT_MOVES:
            move_i = self.cur_i + move[0]
            move_j = self.cur_j + move[1]

            if (move_i, move_j) not in self.visited:
                moves += [(move_i, move_j)]
            # else:
            #     print("Been to {} already".format((move_i, move_j)))

        return moves

    def list_to_values(self, list):
        path_list = []
        for move in list:
            print(move)
            move_value = self.board[move]
            print(move_value)
            path_list += [str(move_value)]
        return " -- ".join(path_list)

    def undo_move(self):
        self.cur_i, self.cur_j = self.move_list[-2]

    def disallow_position(self, pos):
        self.visited.add(pos)

test_board = SpiralBoard(12)
print(test_board)

not_allowed_list = []
for _ in range(100):
    game = TrappedKnight(1000, not_allowed_list)
    while game.move():
        #print(game.board)
        pass

    stop_val = game.board[game.cur_i, game.cur_j]
    stop_pos = (game.cur_i, game.cur_j)
    print("Stopped at value {}, at position {}".format(stop_val, stop_pos))

    not_allowed_list += [stop_pos]

# TODO: Rewrite as recursive implementation (roadblock is when to backtrack; will require some thought)
# not_allowed_list = []
# game = TrappedKnight(2000, not_allowed_list)
# print("Generated board")
# for _ in range(100):
#     while game.move():
#         #print(game.board)
#         pass
#
#
#     stop_val = game.board[game.cur_i, game.cur_j]
#     stop_pos = (game.cur_i, game.cur_j)
#     print("Stopped at value {}, at position {}".format(stop_val, stop_pos))
#
#     game.disallow_position(stop_pos)
#     game.undo_move()