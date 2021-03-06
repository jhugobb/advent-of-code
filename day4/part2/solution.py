from collections import OrderedDict


class Bingo:
    def __init__(self, draws):
        self.draws = draws
        self.num_info = OrderedDict()
        self.boards = []

    def add_num(self, number, board_number, pos_x, pos_y):
        if number not in self.num_info:
            self.num_info[number] = []

        self.num_info[number].append((board_number, pos_x, pos_y))

    def add_board(self, board):
        self.boards.append(board)

        for num, info_list in self.num_info.items():
            for info in info_list:
                if info[0] == (len(self.boards) - 1):
                    self.boards[len(self.boards) - 1].num_board[info[2]][info[1]] = num

    def draw_number(self, number):
        return_score = -1
        for info in self.num_info[number]:
            if self.boards[info[0]].has_won:
                continue

            self.boards[info[0]].board[info[2]][info[1]] = 1

            # check if Y is full
            is_full = True
            for i in range(0, 5):
                if self.boards[info[0]].board[i][info[1]] == 0:
                    is_full = False
                    break

            if is_full:
                print(
                    str(info[0])
                    + ": y-> "
                    + str(info[2])
                    + " after "
                    + str(number)
                    + " was called."
                )
                unmarked_sum = self.boards[info[0]].get_unmarked_sum()
                return_score = unmarked_sum * number

            # check if X is full
            is_full = True
            for i in range(0, 5):
                if self.boards[info[0]].board[info[2]][i] == 0:
                    is_full = False
                    break

            if is_full:
                print(
                    str(info[0])
                    + ": x-> "
                    + str(info[1])
                    + " after "
                    + str(number)
                    + " was called."
                )

                unmarked_sum = self.boards[info[0]].get_unmarked_sum()
                return_score = unmarked_sum * number

        return return_score


class Board:
    def __init__(self):
        # 0 if number not drawn, 1 otherwise
        self.board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        self.num_board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        self.has_won = False

    def draw_num(self, pos_x, pos_y):
        self.board[pos_y, pos_x] = 1

    def get_unmarked_sum(self):
        self.has_won = True
        total = 0
        for i in range(0, 5):
            for j in range(0, 5):
                if self.board[i][j] == 0:
                    total += self.num_board[i][j]
        return total


def main():

    with open("../input.txt", "r") as file:
        input = file.readlines()

        # Draws
        draws = input[0].split(",")

        draws_int = []

        for i in range(0, len(draws)):
            draws_int.append(int(draws[i]))

        bingo = Bingo(draws_int)

        board_num = 0
        pos_x = 0
        pos_y = 0
        for i in range(2, len(input)):
            line = input[i]
            pos_x = 0

            if line == "\n":
                board_num += 1
                pos_y = 0
                continue

            board_line = line.split(" ")

            for index in range(0, len(board_line)):
                if board_line[index] == "":
                    continue
                bingo.add_num(int(board_line[index]), board_num, pos_x, pos_y)
                pos_x += 1

            pos_y += 1

        for i in range(0, board_num + 1):
            bingo.add_board(Board())

        last_winning_score = 0
        for draw in draws_int:
            winner = bingo.draw_number(draw)
            if winner != -1:
                last_winning_score = winner

        print(last_winning_score)


if __name__ == "__main__":
    main()
