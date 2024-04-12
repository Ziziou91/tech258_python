def double_numbers(nums: list) -> list:
    print(f"{'='*60}")
    print(f"{'*'*19}Double Numbers in list{'*'*19}")
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
        

def main() -> None:
    """Main app functionality"""
    list_data = [1, 2, 3, 4, 5]
    embedded_lists = [[1,2,3],[4,5,6],[7,[8]]]
    dict_data = {1: {"name": "Bronson", "money": "$0.05"},
                2: {"name": "Masha", "money": "$3.66"},
                3: {"name": "Roscoe", "money": "$1.14"}}

    double_list = double_numbers(list_data)
    print(double_list)

    print_nested(embedded_lists)




if __name__ == "__main__":
    main()