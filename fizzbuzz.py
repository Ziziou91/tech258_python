
def main(count: int = 100) -> None:
    print(f"\n{'=' * 60}")
    print(f"{'*' * 26}fizzbuzz{'*' * 26}")
    print(f"{'=' * 60}")
    for i in range(count):
        fb_str = ""
        if i % 3 == 0:
            fb_str += "fizz"
        if i % 5 == 0:
            fb_str += "buzz"
        print(f"num {i} -> {fb_str}")


if __name__ == "__main__":
    main()