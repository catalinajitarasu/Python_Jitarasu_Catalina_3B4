from main import anonymous_function, my_function, ex_3_first, ex_3_second_anonymous, ex_3_third_filter, ex_4, ex_5,\
    ex_6, process, sum_digits, ex_9, print_arguments, multiply_by_two, add_numbers, multiply_output, \
    multiply_by_three, augment_function

# ex 2
result_1 = anonymous_function(2, 3, d=2, e=3, a=1)
result_2 = my_function(2, 3, d=2, e=3, a=1)
print(result_1, result_2)

# ex 3
v_1 = ex_3_first("Programming in Python is fun")
v_2 = ex_3_second_anonymous("Programming in Python is fun")
v_3 = ex_3_third_filter("Programming in Python is fun")
print(v_1, v_2, v_3, sep='\n')

# ex 4
print(ex_4(
    {1: 2, 3: 4, 5: 6},
    {'a': 5, 'b': 7, 'c': 'e'},
    {2: 3},
    [1, 2, 3],
    {'abc': 4, 'def': 5},
    3764,
    dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
    test={1: 1, 'test': True}
))

# ex 5
print(ex_5([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))

# ex 6
print(ex_6(
    [1, 3, 5, 2, 8, 7, 4, 10, 9, 2]
))

# ex 7
print(
    process(
        filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
        limit=2,
        offset=2
    )
)

# ex 8 a

print("Ex 8 a")
augmented_multiply_by_two = print_arguments(multiply_by_two)
print(augmented_multiply_by_two(10))

augmented_add_numbers = print_arguments(add_numbers)
print(augmented_add_numbers(3, 4))

# ex 8 b

print("Ex 8 b")
augmented_multiply_by_three = multiply_output(multiply_by_three)
print(augmented_multiply_by_three(10))

# ex 8 c

print("Ex 8 c")
decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])
print(decorated_function(3, 4))

# ex 9
print(ex_9(pairs=[(5, 2), (19, 1), (30, 6), (2, 2)]))
