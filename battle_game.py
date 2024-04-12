from random import randint


def battle_round(fighter_1: dict, fighter_2: dict, round_count: int) -> None:
    print(f"{'='*40}")
    print(f"{'*'*17}round {round_count}{'*'*16}")
    print(f"{'=' * 40}")
    # Fighter 1 attack
    fighter_1_att = randint(0, fighter_1["att"])
    fighter_2_def = randint(0, fighter_2["def"])

    if fighter_1_att > fighter_2_def:
        fighter_2["hp"] -= 1
        print(f"{'-'*10}HIT{'-'*10}")
        print(f"{fighter_1["name"]} damages {fighter_2["name"]} for 1 hp.")
    else:
        print(f"{'-' * 10}BLOCK{'-' * 10}")
        print(f"{fighter_2["name"]} blocks {fighter_1["name"]}'s attack.")
    print(f"{fighter_2["name"]} has {fighter_2["hp"]} hp left.")

    # Fighter 2 attack
    fighter_2_att = randint(0, fighter_2["att"])
    fighter_1_def = randint(0, fighter_1["def"])

    if fighter_2_att > fighter_1_def:
        fighter_1["hp"] -= 1
        print(f"{'-' * 10}HIT{'-' * 10}")
        print(f"{fighter_2["name"]} damages {fighter_1["name"]} for 1 hp.")
    else:
        print(f"{'-' * 10}BLOCK{'-' * 10}")
        print(f"{fighter_1["name"]} blocks {fighter_2["name"]}'s attack.")
    print(f"{fighter_1["name"]} has {fighter_1["hp"]} hp left.")


def choose_fighter(characters: list, player: str) -> dict:
    """Asks the user to choose a fighter, checks their input is valid."""

    print(f"{player} choose your character.")
    for i, character in enumerate(characters):
        print(f"{i} - {character['name']}")
    char_select = input("Your input: ")

    fighter = None

    # Input validation.
    valid_input = False
    while not valid_input:
        # Check char_select is a number.
        if char_select.isdigit():
            num_char = int(char_select)
            # Check num_char corresponds to an index in characters list.
            try:
                fighter = characters[num_char]
            except IndexError:
                print(f"ERROR! {char_select} is not a valid input. Please try again")
                char_select = input("Your input: ")
            else:
                valid_input = True
        else:
            print(f"ERROR! {char_select} is not a number.")
            char_select = input("Your input: ")

    return fighter


def main() -> None:
    print(f"\n{'=' * 60}")
    print(f"{'*' * 25}battle game{'*' * 24}")
    print(f"{'=' * 60}")

    characters = [{
        "name": "robo-joe",
        "att": 6,
        "def": 6,
        "hp": 3
    },
        {
        "name": "1963 Ford Anglia",
        "att": 2,
        "def": 8,
        "hp": 4
    },
        {
        "name":  "Pernicious Python",
        "att": 7,
        "def": 4,
        "hp": 3
    }
    ]

    # Choose a character, then validate the input
    fighter1 = choose_fighter(characters, "Player 1")
    fighter2 = choose_fighter(characters, "Player 2")

    # Game is a series of rounds, taking turns to attack and defend
    round_count = 0
    while fighter1["hp"] > 0 and fighter2["hp"] > 0:
        battle_round(fighter1, fighter2, round_count)
        round_count += 1

    print(f"\n{'='*10}BATTLE END{'='*10}")

    if fighter1["hp"] > 0:
        print(f"{fighter1['name']} WINS!")
    else:
        print(f"{fighter2['name']} WINS!")


if __name__ == "__main__":
    main()
