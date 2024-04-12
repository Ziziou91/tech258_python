def check_rating(film_rating) -> None:
    # use an if statement to check for "universal" rating
    if film_rating == "universal":
        print("all age groups can watch this film")
    # check if film rating is "pg"
    elif film_rating == "pg":
        print("General viewing, but some scenes may be unsuitable for young children.")
    # check if film rating is "12" or "12a"
    elif film_rating == "12":
        print(
            """Films classified 12A and video works classified 12 contain material that is not generally suitable for
children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an 
adult.""")
    # check if film rating is "15"
    elif film_rating == "15":
        print("No one younger than 15 may see a 15 film in a cinema.")
    # check if film rating is "18"
    elif film_rating == "18":
        print("No one younger than 18 may see an 18 film in a cinema.")


def main() -> None:
    possible_film_rating = {"universal", "pg", "12", "12a", "15", "18"}

    print("please enter the rating of the film to see if it's suitable. Options are:")
    for rating in possible_film_rating:
        print(f"\t{rating}")

    film_rating = input("Enter your films rating here: ")

    valid_input = False
    while not valid_input:
        if film_rating not in possible_film_rating:
            print(f"ERROR! {film_rating} is not a valid input. Please try again.")
            film_rating = input("Enter your films rating here: ")
        else:
            valid_input = True

    check_rating(film_rating)


if __name__ == "__main__":
    main()
