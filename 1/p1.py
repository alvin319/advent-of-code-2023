INPUT_PATH = "input.txt"
DIGITS = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}


def main():
    total = 0

    with open(INPUT_PATH) as r:
        lines = r.read().split("\n")

    for line in lines:
        nums = "".join([c for c in line if c in DIGITS])

        if len(nums) == 0:
            continue
        else:
            total += int(f"{nums[0]}{nums[-1]}")

    print(total)


if __name__ == "__main__":
    main()
