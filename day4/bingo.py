class Board:
    def __init__(self):
        self.all_numbers = None
        self.numbers_set = None
        self.marked = None
        self.is_complete = False

    def set_board_from_numbers(self, number_list):
        self.all_numbers = number_list
        self.numbers_set = set(number_list)
        self.marked = [0] * len(number_list)

    def mark_number(self, number_to_mark):
        if number_to_mark not in self.numbers_set:
            return

        index_of_input = self.all_numbers.index(number_to_mark)
        self.marked[index_of_input] = 1
        self.numbers_set.remove(number_to_mark)
        # print(self.marked)
        self.check_is_complete()
        # print(self.is_complete)

    def check_is_complete(self):
        # check for row completion
        for i in range(0, 25, 5):
            row = self.marked[i:i+5]
            if sum(row) == 5:
                self.is_complete = True
                pass

        # check for column completion
        for i in range(5):
            column = [self.marked[i+j] for j in range(0, 25, 5)]
            if sum(column) == 5:
                self.is_complete = True
                pass

    def get_sum_unmarked_numbers(self):
        return sum(self.numbers_set)

    def __repr__(self):
        return self.all_numbers.__repr__() + '\n' + self.marked.__repr__() + '\n'

    def print_marked(self):
        pass

class Bingo:
    def __init__(self):
        self.boards = []
        self.number_list = None
        self.boards_incomplete = None

    def set_numbers(self, numbers):
        self.number_list = numbers

    def _make_num_list_from_input(self, input_rows):
        return [int(row_num) for row in input_rows for row_num in row.split()]

    def init_game_from_input(self, input_gen):
        numbers = next(input_gen)
        self.number_list = [int(number) for number in numbers.split(',')]

        for row in input_gen:
            if not row:
                board_input = [next(input_gen) for _ in range(5)]
                new_numbers = self._make_num_list_from_input(board_input)

                new_board = Board()
                new_board.set_board_from_numbers(new_numbers)
                self.boards.append(new_board)

            else:
                assert False, f'Expected empty row, current row: {row}'

        self.boards_incomplete = set(range(len(self.boards)))

    def mark_number_on_boards(self, number):
        for board in self.boards:
            board.mark_number(number)

    def check_boards_for_completion(self):
        first_board_complete = None
        for i, board in enumerate(self.boards):
            if board.is_complete:
                if i in self.boards_incomplete:
                    self.boards_incomplete.remove(i)

                if not first_board_complete:
                    first_board_complete = i

        return first_board_complete

    def run_the_numbers_part1(self):
        for next_num in self.number_list:
            self.mark_number_on_boards(next_num)

            finished_board = self.check_boards_for_completion()
            if finished_board:
                # game over
                winning_board = self.boards[finished_board]
                return winning_board.get_sum_unmarked_numbers() * next_num

    def run_the_numbers_part2(self):
        last_board_index = None

        for next_num in self.number_list:
            self.mark_number_on_boards(next_num)

            finished_board = self.check_boards_for_completion()
            if len(self.boards_incomplete) == 1:
                last_board_index = self.boards_incomplete.pop()
                self.boards_incomplete.add(last_board_index)
            if len(self.boards_incomplete) == 0:
                # game over
                last_board = self.boards[last_board_index]
                return last_board.get_sum_unmarked_numbers() * next_num

    def __repr__(self):
        return self.number_list.__repr__() + '\n' + self.boards.__repr__()
