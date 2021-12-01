def get_input_data(input_file):
    with open(input_file) as f:
        for line in f.readlines():
            yield int(line)

def part1(input_gen):
    deeper_counter = 0
    last_depth = next(input_gen)
    for next_depth in input_gen:
        if next_depth > last_depth:
            deeper_counter += 1
        last_depth = next_depth

    return deeper_counter

def part2(input_gen):
    deeper_counter = 0
    curr_3 = [next(input_gen), next(input_gen), next(input_gen)]
    curr_sum = sum(curr_3)

    for next_depth in input_gen:
        next_3 = curr_3[1:] + [next_depth]
        if sum(next_3) > sum(curr_3):
            deeper_counter += 1
        curr_3 = next_3

    return deeper_counter

if __name__ == '__main__':
    input_data = get_input_data('input.txt')
    # solution_part1 = part1(input_data)
    # print(solution_part1)
    solution_part2 = part2(input_data)
    print(solution_part2)
