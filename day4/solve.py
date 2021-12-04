from bingo import Bingo

def get_input_data(input_file):
    with open(input_file) as f:
        for line in f.readlines():
            yield line.strip()

def part1(input_gen):
    game = Bingo()
    game.init_game_from_input(input_gen)
    result = game.run_the_numbers_part1()
    return result

def part2(input_gen):
    game = Bingo()
    game.init_game_from_input(input_gen)
    result = game.run_the_numbers_part2()
    return result

if __name__ == '__main__':
    input_data = get_input_data('input.txt')
    # solution_part1 = part1(input_data)
    # print(solution_part1)
    solution_part2 = part2(input_data)
    print(solution_part2)
