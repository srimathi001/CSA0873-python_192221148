import itertools
def generate_combinations(dictionary):
    keys = list(dictionary.keys())
    combinations = itertools.product(*(dictionary[key] for key in keys))
    return combinations
def main():
    dictionary = {
        'A': ['a', 'b', 'c'],
        'B': ['x', 'y'],
        'C': ['m', 'n', 'o']
    }
    combinations = generate_combinations(dictionary)
    for combination in combinations:
        print(''.join(combination))
if __name__ == "__main__":
    main()

