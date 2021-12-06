from collections import Counter
import re

NUMBER_REGEX = re.compile('[0-9]+')


def get_input_data(input_file, return_diagonals = False):
    with open(input_file) as f:
        for line in f.readlines():
            line_clean = line.strip()
            yield line_clean

def get_range(start, end, required_length):
    ''' Two step function:
        1) Generate range of numbers, inclusive of endpoints, regardless of
            whether or not the start is larger/smaller than the end
        2) If the length of the raw range is 1, this is evidence of a horizontal
            or vertical line. Extend the single-item list to a padded list filled
            with that constant `required_length` number of times
    '''
    raw_range = None
    if start < end:
        raw_range = range(start, end+1)
    else:
        raw_range = range(start, end-1, -1)

    if len(raw_range) == 1:
        return [raw_range[0]] * required_length
    else:
        return raw_range

def get_points_from_input(input_gen, yield_diagonals=False):
    for line in input_gen:
        start_x, start_y, end_x, end_y = [
            int(coordinate)
            for coordinate
            in NUMBER_REGEX.findall(line)
        ]

        if (start_x == end_x) or (start_y == end_y) or yield_diagonals:
            required_length = max(
                abs(start_x - end_x) + 1,
                abs(start_y - end_y) + 1
            )

            x_range = get_range(start_x, end_x, required_length)
            y_range = get_range(start_y, end_y, required_length)

            for coordinates in zip(x_range, y_range):
                yield coordinates

        else:
            continue

def part1(input_gen):
    all_points_gen = get_points_from_input(input_gen)
    point_counter = Counter(all_points_gen)

    counts_greater_than_two = [count for coordinates, count in point_counter.items() if count >= 2]
    return len(counts_greater_than_two)

def part2(input_gen):
    all_points_gen = get_points_from_input(input_gen, yield_diagonals=True)
    point_counter = Counter(all_points_gen)

    counts_greater_than_two = [count for coordinates, count in point_counter.items() if count >= 2]
    return len(counts_greater_than_two)

if __name__ == '__main__':
    input_gen = get_input_data('input.txt')

    # solution_part1 = part1(input_gen)
    # print(solution_part1)

    solution_part2 = part2(input_gen)
    print(solution_part2)
