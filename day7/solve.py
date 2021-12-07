import matplotlib.pyplot as plt
import numpy as np
import statistics

def get_input_data(input_file):
    with open(input_file) as f:
        contents = f.read()
        return [int(crab_position) for crab_position in contents.split(',')]


def part1(input_list):
    center_point = int(statistics.median(input_list))
    return calculate_total_cost(center_point, input_list)

def calculate_total_cost(point_of_convergence, other_points, linear_cost=False):
    if linear_cost:
        cumsum_dict = dict(
            zip(
                range(0, max(input_list)+1),
                np.cumsum(range(0, max(input_list)+1))
            )
        )
        individual_movement_costs = map(
            lambda position: cumsum_dict[abs(point_of_convergence - position)],
            input_list
        )
        total_fuel_cost = sum(individual_movement_costs)
    else:
        individual_movements = map(
            lambda position: abs(point_of_convergence - position),
            input_list
        )
        total_fuel_cost = sum(individual_movements)
    return total_fuel_cost

def part2(input_list):
    all_guesses = list(range(min(input_list), max(input_list) + 1))
    all_scores = map(
        lambda v: calculate_total_cost(v, input_list, True),
        all_guesses
    )
    all_scores_list = list(all_scores)
    plt.plot(all_guesses, all_scores_list)
    plt.show()

    return min(all_scores_list)


if __name__ == '__main__':
    input_list = get_input_data('input.txt')

    # solution_part1 = part1(input_list)
    # print(solution_part1)

    solution_part2 = part2(input_list)
    print(solution_part2)
