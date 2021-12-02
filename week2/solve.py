def get_input_data(input_file):
    with open(input_file) as f:
        for line in f.readlines():
            direction, magnitude = line.split(' ')
            yield direction.strip(), int(magnitude)

def part1(input_gen):
    x, y = 0, 0
    movement_map = {
        'forward': (1, 0),
        'up': (0, -1),
        'down': (0, 1),
    }
    for direction, magnitude in input_gen:
        x_multiplier, y_multiplier = movement_map[direction]
        x_delta, y_delta = magnitude*x_multiplier, magnitude*y_multiplier
        x, y = x + x_delta, y + y_delta

    return x*y

def part2(input_gen):
    x, y, aim = 0, 0, 0
    aim_map = {
        'up': -1,
        'down': 1
    }
    for input in input_gen:
        match input:
            case tuple((('up'|'down') as direction, magnitude)):
                aim_delta = magnitude * aim_map[direction]
                aim += aim_delta
            case tuple(('forward', magnitude)):
                x += magnitude
                y += (magnitude * aim)
    return x*y

if __name__ == '__main__':
    input_data = get_input_data('input.txt')
    # solution_part1 = part1(input_data)
    # print(solution_part1)
    solution_part2 = part2(input_data)
    print(solution_part2)
