def get_lines(infile):
    with open(infile) as f:
        for line in f:
            line = line.strip()
            yield line


def go(row, data, ofs, ofs_part, cur_part, memo):
    if ofs == len(row):
        if ofs_part == len(data) and cur_part == 0:
            return 1
        if ofs_part == len(data) - 1 and data[ofs_part] == cur_part:
            return 1
        return 0

    k = (ofs, ofs_part, cur_part)
    if k in memo:
        return memo[k]

    def go_dot():
        if cur_part == 0:
            return go(row, data, ofs + 1, ofs_part, 0, memo)
        elif ofs_part < len(data) and data[ofs_part] == cur_part:
            # start new part if all prefix parts were valid
            return go(row, data, ofs + 1, ofs_part + 1, 0, memo)
        else:
            return 0  # invalid combination

    def go_hash():
        return go(row, data, ofs + 1, ofs_part, cur_part + 1, memo)

    ans = 0
    if row[ofs] == '.':
        ans += go_dot()
    elif row[ofs] == '#':
        ans += go_hash()
    else:  # row[ofs] == '?'
        ans += go_dot()
        ans += go_hash()
    memo[k] = ans
    return ans


def get_variants_count(line, flag2=False):
    row, data = line.split(' ')
    if flag2:
        row = '?'.join([row] * 5)
        data = ','.join([data] * 5)
    row = list(row)
    data = list(map(int, data.split(',')))
    print(row, data)
    memo = {}
    return go(row, data, 0, 0, 0, memo)


def solve(infile, flag2=False):
    ans = 0
    for line in get_lines(infile):
        num = get_variants_count(line, flag2)
        ans += num
    return ans


def main():
    for flag in [False, True]:
        # print(get_variants_count('???.### 1,1,3', flag))
        # print(get_variants_count('.??..??...?##. 1,1,3', flag))
        # print(get_variants_count('?#?#?#?#?#?#?#? 1,3,1,6', flag))
        # print(get_variants_count('????.#...#... 4,1,1', flag))
        # print(get_variants_count('????.######..#####. 1,6,5', flag))
        print(get_variants_count('?###???????? 3,2,1', flag))
        print(solve('12.in', flag))


if __name__ == '__main__':
    main()
