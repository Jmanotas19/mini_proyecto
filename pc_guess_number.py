import random


def pc_guess_number(number):
    print("Welcome pc, guess the number".center(40, "="))

    print(f"Select a number between 1 and {number}")

    lower_bound = 1
    upper_bound = number
    my_number = ""
    attempts = 0

    while my_number != "c":
        if lower_bound != upper_bound:
            unknown_number = random.randint(lower_bound, upper_bound)
        else:
            unknown_number = lower_bound

        my_number = input(
            f"My number is: {unknown_number}\nIf it's higher, enter (a). If it's lower, enter (b). If it's correct, enter (c): "
        ).lower()
        attempts += 1

        if my_number == "a":
            upper_bound = unknown_number - 1
        elif my_number == "b":
            lower_bound = unknown_number + 1

    print(f"Congrats! The PC guessed your number: ({unknown_number})")
    print(f"It took the PC {attempts} attempts to guess your number.")


pc_guess_number(100)
# Mi número = 10
