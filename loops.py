def double_numbers(nums: list) -> list:
    print(f"{'=' * 60}")
    print(f"{'*' * 19}Double Numbers in list{'*' * 19}")
    print(f"{'=' * 60}")
    """Takes a list of numbers and returns a list with each number doubled."""
    double_nums = []

    for num in nums:
        """Check num is a number before doubling."""
        if type(num) is int or type(num) is float:
            double = num * 2
        else:
            print(f"ERROR! {num} is not a number. The code will leave this unchanged.")
            double = num

        double_nums.append(double)

    return double_nums


def print_nested(nums_lists: list) -> None:
    print(f"\n{'=' * 60}")
    print(f"{'*' * 15}Flatten nested lists and print{'*' * 15}")
    print(f"{'=' * 60}")
    """Takes nested lists of numbers and prints each value."""
    num_list = nums_lists

    # Keep running the code while there is a nested list in num_list.
    # Use a generator function for iterate through num_list, combine with any to check types.
    while any(isinstance(list_val, list) for list_val in num_list):
        temp_list = []

        # Loop though num_list, check current value is list and add, otherwise append.
        for nested in num_list:
            if type(nested) is list:
                temp_list += nested
            else:
                temp_list.append(nested)

        num_list = temp_list

    print(num_list)
    for value in num_list:
        print(value)


def print_values_nested_dict(my_dict: dict) -> None:
    """Demonstrate printing values in nested dictionaries."""
    print(f"\n{'=' * 60}")
    print(f"{'*' * 11}Print values inside nested dictionaries{'*' * 10}")
    print(f"{'=' * 60}")

    print(f"{'-' * 10}Top level keys{'-' * 10}")
    for val in my_dict:
        print(val)

    print(f"\n{'-' * 10}Values inside each nested dict{'-' * 10}")
    vals_list = []
    for val in my_dict:
        nested_dict_values = my_dict[val].values()
        vals_list += nested_dict_values
        print(nested_dict_values)

    print(f"\n{'-' * 10}Print values 1 by 1{'-' * 10}")
    for val in vals_list:
        print(val)

    print(f"\n{'-' * 10}Print money values only{'-' * 10}")
    for val in vals_list:
        if val[0] == "$":
            print(val)


def while_loop_demo(x: int = 0) -> None:
    """Function to demo how while loops work."""
    print(f"\n{'=' * 60}")
    print(f"{'*' * 16}Demo while loop functionality{'*' * 15}")
    print(f"{'=' * 60}")
    while x < 10:
        print(f"print x -> {x}")
        x += 1
        if x > 4:
            break


def get_user_age() -> int:
    """Asks a user to enter their age, check it can be cast as int and then return."""
    print(f"\n{'=' * 60}")
    print(f"{'*' * 16}Get and validate a users age{'*' * 16}")
    print(f"{'=' * 60}")

    age_str = input("Please enter your age: ")

    # Input validation
    valid_input = False
    age_int = None
    while not valid_input:
        if age_str.isdigit():
            print(f"age_str {age_str}")
            # happy path
            age_int = int(age_str)
            if age_int <= 117:
                valid_input = True
            else:
                print(f"ERROR! {age_str} is too large.")
                age_str = input("Please enter your age: ")
        # sad path
        else:
            print(f"ERROR! {age_str} is not a number.")
            age_str = input("Please enter your age: ")

    return age_int


def main() -> None:
    """Main app functionality"""
    list_data = [1, 2, 3, 4, 5]
    embedded_lists = [[1, 2, 3], [4, 5, 6], [7, [8]]]
    dict_data = {1: {"name": "Bronson", "money": "$0.05"},
                 2: {"name": "Masha", "money": "$3.66"},
                 3: {"name": "Roscoe", "money": "$1.14"}}

    double_list = double_numbers(list_data)
    print(double_list)

    print_nested(embedded_lists)

    print_values_nested_dict(dict_data)

    while_loop_demo()

    age = get_user_age()
    print(age)


if __name__ == "__main__":
    main()
