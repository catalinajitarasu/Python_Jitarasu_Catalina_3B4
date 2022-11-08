from utils import process_items

if __name__ == "__main__":
    while True:
        user_input = input("Enter number:\n")
        if user_input == "q":
            exit()

        try:
            x = int(user_input)
            print(process_items(x))
        except Exception as e:
            print("Other error", e)
