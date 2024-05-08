import random


def play():
    while True:
        user = input("choose one option: (r) rock, (p) paper, (s) scissor:\n").lower()
        if user in ["r", "p", "s"]:
            break
        else:
            print("Invalid option. Please choose again.")

    pc = random.choice(["r", "p", "s"])

    if user == pc:
        return "draw"
    if player_win(user, pc):
        return "you win"
    return "you lose"


def player_win(player, opponent):
    if (
        (player == "r" and opponent == "s")
        or (player == "s" and opponent == "p")
        or (player == "p" and opponent == "r")
    ):
        return True
    else:
        return False


def main():
    while True:
        result = play()
        print(result)
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            break


main()
