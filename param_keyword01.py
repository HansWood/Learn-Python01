def print_n_times(*values, n=2):

    for i in range(n):

        for value in values:
            print(value)

        print()

print_n_times("morning", "noon", "night", n=3)

# print_n_times("morning", "noon", "night")