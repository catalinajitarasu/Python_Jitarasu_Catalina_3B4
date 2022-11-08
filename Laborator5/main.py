from typing import List

# https://www.geeksforgeeks.org/args-kwargs-python/

anonymous_function = lambda *args, **kwargs: sum([val for val in kwargs.values()])


# ex 2

def my_function(*args, **kwargs):
    summ = 0
    for kw in kwargs.keys():
        summ += int(kwargs[kw])
    return summ


def ex_3_first(string: str) -> list:
    # aici doar am parcurs  stringul si am verificat daca un caracter x este in stringul "aeiou"
    return [x for x in string if x.lower() in "aeiou"]


def ex_3_second_anonymous(input_string: str) -> list:
    # aici am folosit lambda
    return list(filter(lambda x: x in "aeiou", input_string))


def ex_3_third_filter(input_string: str) -> list:
    # avem in functia filter_array pentru fiecare caracter din input_string daca este vacala sau nu
    # cu functia zip luam perechile (i,j) (filter_array[1] cu input_string[1])
    # daca filter_array[j] este true atunci este vocala deci adaugam in lista de return
    filter_array = [True if x in "aeiou" else False for x in input_string]
    return [i for (i, j) in zip(input_string, filter_array) if j]


def ex_4(*args, **kwargs):
    return [
               i for i in args
               if type(i) == dict and len(i) > 1 and max([0] + [len(x) for x in i.keys() if type(x) == str]) > 2
           ] + [
               i for i in kwargs.values()
               if type(i) == dict and len(i) > 1 and max([0] + [len(x) for x in i.keys() if type(x) == str]) > 2
           ]


def ex_5(input_list: list) -> list:
    # verific tipul fiecarui element din lista si daca e numar il adaug in noua lista
    new_list = []
    for el in input_list:
        if type(el) in [int, float, complex]:
            new_list.append(el)
    return new_list


def ex_6(input_list: List[int]) -> List[tuple]:
    """"
    formez doua liste care sa contina numerele pare/impare din lista input
    folosesc functia zip https://www.w3schools.com/python/ref_func_zip.asp pentru a lua perechile
    """
    odd_numbers = [x for x in input_list if x % 2 == 0]
    even_numbers = [x for x in input_list if x % 2 == 1]
    return list(zip(odd_numbers, even_numbers))


def generate_fibonacci(n: int) -> list:
    # adaug numerele din sirul lui fibonacci in return_list
    return_list = [0, 1]
    if n < 0:
        raise ValueError("generating first n fibonacci numbers failed, n is negative")
    else:
        for i in range(2, n):
            return_list.append(return_list[i - 2] + return_list[i - 1])
    return return_list[0:n]


def sum_digits(x):
    return sum(map(int, str(x)))


def process(**kwargs) -> list:
    fibonacci_sequence = generate_fibonacci(1000)
    try:
        if "filters" in kwargs.keys():
            for f in kwargs["filters"]:
                fibonacci_sequence = list(filter(f, fibonacci_sequence))
        if "offset" in kwargs.keys():
            fibonacci_sequence = fibonacci_sequence[kwargs["offset"]:]
        if "limit" in kwargs.keys():
            fibonacci_sequence = fibonacci_sequence[:kwargs["limit"]]
    except Exception as e:
        print("Error at processing:", e)
    return fibonacci_sequence


# ex 8 a
def multiply_by_two(x):
    return x * 2


def add_numbers(a, b):
    return a + b


def print_arguments(function):
    def f(*args, **kwargs):
        print(args, kwargs)
        return function(*args, **kwargs)

    return f


# ex 8 b

def multiply_output(function):
    def f(*args, **kwargs):
        return 2 * function(*args, **kwargs)

    return f


def multiply_by_three(x):
    return x * 3


# ex 8 c


def augment_function(function, decorators):
    def f(*args, **kwargs):
        result = function
        for deco in decorators:
            result = deco(result)
        return result(*args, **kwargs)

    return f


# ex 9
def ex_9(pairs) -> list:
    return [{"sum": pair[0] + pair[1],
             "prod": pair[0] * pair[1],
             "pow": pair[0] ** pair[1]} for pair in pairs]
