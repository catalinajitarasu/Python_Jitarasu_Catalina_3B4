import functions as test

# 1
print(test.list_fibonacci(10))

# 2
print(test.prime_list_number(test.list_fibonacci(10)))


# 4
notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2]
start_position = 2
print(test.ex_4(notes, moves, start_position))

# 5
matrix = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]
print(test.modify_matrix(matrix))

# 6
print(test.list_exactly_x_times([1, 2, 3], [1, 2, 3], [4, 3, 4], [5, 5, 4, 5], x=3))

# 7
print(test.tuple_palindrome([12321, 111, 289, 14141]))

# 11
print(test.ex_11([('abc', 'bcd'), ('abc', 'zza')]))
