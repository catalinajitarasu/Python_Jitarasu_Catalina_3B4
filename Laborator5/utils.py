def verification_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if int(n % 2) == 0:
        return False
    for i in range(3, int(n / 2)):
        if n % i == 0:
            return False
    return True


def process_items(x: int) -> int:
    while not verification_prime(x + 1):
        x += 1
    return x + 1


if __name__ == "__main__":
    try:
        x = int(input("Enter a number\n"))
        print(process_items(x))
    except TypeError as e:
        print("Input is not integer", e)
    except Exception as e:
        print("Other error", e)
