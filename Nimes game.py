import random

def smart_nim_game(piles):
    while True:
        print("Current piles:")
        for i, pile in enumerate(piles):
            if pile == 0:
                print(f"Pile {i+1}: empty")
            else:
                print(f"Pile {i+1}: {pile}")

        player_turn = input("Your turn. Enter the pile number (1-{}) to take from: ".format(len(piles)))
        pile = int(player_turn) - 1

        if pile < 0 or pile >= len(piles):
            print("Invalid pile number. Please choose a valid pile.")
            continue
        if(piles[pile]>1):     
            max_take = piles[pile] // 2
        else:
            max_take = 1
        take = int(input(f"How many to take from pile {pile+1} (1-{max_take}): "))

        if take < 1 or take > max_take:
            print("Invalid number of items to take. Please choose a valid number.")
            continue

        piles[pile] -= take

        if check_game_over(piles):
            print("Congratulations! You win!")
            break

        # Computer's turn
        pile, take = computer_move(piles)
        piles[pile] -= take

        print(f"Computer took {take} from pile {pile + 1}")

        if check_game_over(piles):
            print("Computer wins. You lose!")
            break

def check_game_over(piles):
    return all(pile == 0 for pile in piles)

def computer_move(piles):
    non_empty_piles = [i for i, pile in enumerate(piles) if pile > 0]

    if not non_empty_piles:
        return None, None  # No non-empty piles to choose from

    pile = random.choice(non_empty_piles)
    if (piles[pile] & (piles[pile] + 1)) == 0:
        # If the pile size is already 2^n - 1, take a random number of items
        max_take = max(1, random.randint(1, piles[pile]))
        take = random.randint(1, max_take)
    else:
        # Try to make the pile size 2^n - 1
        k = 1
        while (k & piles[pile]) > 0:
            k <<= 1
        max_take = max(1, (piles[pile] + 1) - k)
        take = random.randint(1, max_take)

    return pile, take


if __name__ == "__main__":
    piles = [1, 3, 5]  # You can change the initial pile sizes
    smart_nim_game(piles)
