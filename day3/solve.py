def get_input_data(input_file):
    with open(input_file) as f:
        for line in f.readlines():
            yield line.strip()

class BitCounter:
    def __init__(self):
        self.dict = {
            '0':0,
            '1':0,
        }

    def add_new_observation(self, observation):
        self.dict[observation] += 1

    def get_most_common_value(self):
        if self.dict['0'] > self.dict['1']:
            return '0'
        else:
            return '1'

    def get_least_common_value(self):
        if self.dict['0'] > self.dict['1']:
            return '1'
        else:
            return '0'

    def __repr__(self):
        return self.dict.__repr__()

def part1(input_gen):
    first_line = next(input_gen)
    counters = [BitCounter() for _ in range(len(first_line))]

    for bit, counter in zip(first_line, counters):
        counter.add_new_observation(bit)
    for line in input_gen:
        for bit, counter in zip(line, counters):
            counter.add_new_observation(bit)

    gamma_str = ''.join([counter.get_most_common_value() for counter in counters])
    gamma = int(gamma_str, 2)

    epsilon_str = ''.join([counter.get_least_common_value() for counter in counters])
    epsilon = int(epsilon_str, 2)
    print(
        f'Gamma:\t\t{gamma_str}\t{gamma}\n',
        f'Epsilon:\t{epsilon_str}\t{epsilon}',
    )
    return gamma*epsilon

def part2(input_gen):
    ox_str = None
    ox_gen_rating = None
    co2_str = None
    co2_scrubber_rating = None
    input_list = list(input_gen)

    ##### First pass to get ox_gen_rating #####
    survivors = input_list.copy()
    first_line = survivors[0]

    for position in range(len(first_line)):
        counter = BitCounter()
        value_at_position_map = map(lambda v: v[position], survivors)
        _ = [counter.add_new_observation(v) for v in value_at_position_map]

        most_common_value = counter.get_most_common_value()

        survivors = [survivor for survivor in survivors if survivor[position] == most_common_value]

        if len(survivors) == 1:
            ox_str = survivors[0]
            ox_gen_rating = int(ox_str, 2)

    ##### Second pass to get co2_scrubber_rating #####
    # #DuplicateCode
    survivors = input_list.copy()
    first_line = survivors[0]
    for position in range(len(first_line)):
        counter = BitCounter()
        value_at_position_map = map(lambda v: v[position], survivors)
        _ = [counter.add_new_observation(v) for v in value_at_position_map]

        least_common_value = counter.get_least_common_value()

        survivors = [survivor for survivor in survivors if survivor[position] == least_common_value]

        if len(survivors) == 1:
            co2_str = survivors[0]
            co2_scrubber_rating = int(co2_str, 2)

    print(
        f'Ox:\t{ox_str}\t{ox_gen_rating}\n',
        f'CO2:\t{co2_str}\t{co2_scrubber_rating}',
    )
    return ox_gen_rating * co2_scrubber_rating

if __name__ == '__main__':
    input_data = get_input_data('input.txt')
    # solution_part1 = part1(input_data)
    # print(solution_part1)
    solution_part2 = part2(input_data)
    print(solution_part2)
