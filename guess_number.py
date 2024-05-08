import random


def guess_number(number):
    print("welcome to guess number".center(40, "="))

    random_number = random.randint(1, number)

    my_number = 0

    while my_number != random_number:
        try:
            my_number = int(input(f"please, guess a number between 1 and {number}: "))
        except ValueError:
            print("please enter a valid number.")
            continue

        if my_number < random_number:
            print("try again, that number is smaller than the number")
        elif my_number > random_number:
            print("try again, that number is greater than the number")
    print(f"congrats! you guessed the number ({random_number})")


guess_number(100)
