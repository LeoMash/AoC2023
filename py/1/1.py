def extract_code1(line):
    digits = list(filter(lambda c: c.isnumeric(), line))
    code = (ord(digits[0]) - 48) * 10 + ord(digits[-1]) - 48
    return code


MAP = [
    ("one", 1),
    ("two", 2),
    ("three", 3),
    ("four", 4),
    ("five", 5),
    ("six", 6),
    ("seven", 7),
    ("eight", 8),
    ("nine", 9),
]


def extract_code2(line):
    digits = []
    n = len(line)
    for idx in range(n):
        if line[idx].isnumeric():
            digits.append(ord(line[idx]) - 48)
            continue

        for mapping in MAP:
            if line[idx:].startswith(mapping[0]):
                digits.append(mapping[1])
                break

    code = digits[0] * 10 + digits[-1]
    return code


def solve1(infile):
    ans = 0
    with open(infile) as f:
        for line in f:
            line = line.strip()
            ans += extract_code1(line)
    return ans


def solve2(infile):
    ans = 0
    with open(infile) as f:
        for line in f:
            line = line.strip()
            ans += extract_code2(line)
    return ans


def main():
    # print(solve1('1_1_test.in'))
    # print(solve1('1_1.in'))
    # print(solve2('1_2_test.in'))
    print(solve2('1_2.in'))

    pass


if __name__ == '__main__':
    main()
