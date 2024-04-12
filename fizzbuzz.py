
def main(count: int = 100) -> None:
    print(f"\n{'=' * 60}")
    print(f"{'*' * 26}fizzbuzz{'*' * 26}")
    print(f"{'=' * 60}")
    for i in range(1, count):
        if i % 3 == 0 and i % 5 == 0:
            print(f"num {i} -> fizzbuzz")
        elif i % 3 == 0:
            print(f"num {i} -> fizz")
        elif i % 5 == 0:
            print(f"num {i} -> buzz")


if __name__ == "__main__":
    main()
