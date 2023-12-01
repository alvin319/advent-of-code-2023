INPUT_PATH = "input.txt"
DIGIT_MAPPING = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def parse_sliding_window(buffer):
    digit_buffer = ""
    found_num = False

    while len(buffer) > 0:
        for key in DIGIT_MAPPING:
            if key in buffer:
                digit_buffer += DIGIT_MAPPING[key]
                new_buffer_index = buffer.index(key) + len(key) - 1
                buffer = buffer[new_buffer_index:]
                found_num = True

        if not found_num:
            break
        else:
            found_num = False

    return digit_buffer, buffer


def main():
    total = 0

    with open(INPUT_PATH) as r:
        lines = r.read().split("\n")

    for line in lines:
        nums = ""
        buffer = ""

        for c in line:
            if c.isdigit():
                nums += c

                if buffer in DIGIT_MAPPING:
                    nums += DIGIT_MAPPING[buffer]
                else:
                    digits, _ = parse_sliding_window(buffer)
                    nums += digits

                buffer = ""
            else:
                if buffer in DIGIT_MAPPING:
                    nums += DIGIT_MAPPING[buffer]
                    buffer = c
                else:
                    buffer += c
                    digits, buffer = parse_sliding_window(buffer)
                    nums += digits

        if len(nums) > 0:
            total += int(f"{nums[0]}{nums[-1]}")

    print(total)


if __name__ == "__main__":
    main()
