from collections import Counter

def get_input_data(input_file):
    with open(input_file) as f:
        contents = f.read()
        return [int(new_fish) for new_fish in contents.split(',')]

class FishRegister:
    def __init__(self, fish_list):
        self.timer_dict = self.init_timer_dict(fish_list)

    def init_timer_dict(self, fish_list):
        timer_counter = Counter({key:0 for key in range(9)})
        timer_counter.update(fish_list)
        return dict(timer_counter)

    def increment_day(self):
        ''' For each timer, assign the timer's counter to `timer-1`

            2 special cases:
            a) The value at 0 will be assigned to the value for 8 (new fish)
            b) The value at zero will also be assigned to value at 6. This causes
               a collision at the key 6 by fish that were previously at either
               0 or 7. Sum these two counts to get the correct value
        '''
        num_zeroes = self.timer_dict[0]
        num_sevens = self.timer_dict[7]

        self.timer_dict = {
            (key-1):val for key, val in self.timer_dict.items() if key > 0
        }
        
        self.timer_dict[8] = num_zeroes
        self.timer_dict[6] = num_zeroes + num_sevens

    def increment_days(self, num_days, verbose=False):
        if verbose: print(f'Initial State: {self}')
        for i in range(num_days):
            self.increment_day()
            if verbose: print(f'After {i+1} days: {self}')

    def __len__(self):
        return sum(self.timer_dict.values())

    def __repr__(self):
        return self.timer_dict.__repr__()

def part1(input_list):
    register = FishRegister(input_list)
    register.increment_days(80)
    return len(register)

def part2(input_list):
    register = FishRegister(input_list)
    register.increment_days(256)
    return len(register)

if __name__ == '__main__':
    input_list = get_input_data('input.txt')

    # solution_part1 = part1(input_list)
    # print(solution_part1)

    solution_part2 = part2(input_list)
    print(solution_part2)
