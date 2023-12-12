def get_lines(infile):
    with open(infile) as f:
        for line in f:
            line = line.strip()
            yield line


def check(row, data):
    row = ''.join(row)
    parts = list(map(list, filter(None, row.split('.'))))
    # print(parts)

    if len(parts) != len(data):
        return False
    for part, val in zip(parts, data):
        if len(part) != val:
            return False
    print(parts)
    return True


def go(row, data, ofs):
    for i in range(ofs, len(row)):
        if row[i] == '?':
            ans = 0
            row[i] = '.'
            ans += go(row, data, i + 1)
            row[i] = '#'
            ans += go(row, data, i + 1)
            row[i] = '?'
            return ans
    # no ? left after ofs
    return 1 if check(row, data) else 0


def get_variants_count(line):
    row, data = line.split(' ')
    row = list(row)
    data = list(map(int, data.split(',')))
    print(row, data)

    return go(row, data, 0)


def solve(infile):
    ans = 0
    for line in get_lines(infile):
        num = get_variants_count(line)
        ans += num
    return ans


def main():
    print(get_variants_count('???.### 1,1,3'))
    print(get_variants_count('.??..??...?##. 1,1,3'))
    print(get_variants_count('?#?#?#?#?#?#?#? 1,3,1,6'))
    print(get_variants_count('????.#...#... 4,1,1'))
    print(get_variants_count('????.######..#####. 1,6,5'))
    print(get_variants_count('?###???????? 3,2,1'))
    print(solve('12.in'))


if __name__ == '__main__':
    main()
