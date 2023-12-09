def parse(infile):
    lines = []
    with open(infile) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            lines.append([int(x) for x in line.split()])
    return lines


def process_line(nums):
    seqs = [nums]
    while not all(x == 0 for x in seqs[-1]):
        cur = seqs[-1]
        next_nums = []
        for i in range(len(cur) - 1):
            next_nums.append(cur[i + 1] - cur[i])
        seqs.append(next_nums)

    seqs.pop()
    for i in range(len(seqs) - 1):
        cur = seqs[-i - 1]
        cur_diff = cur[-1]
        cur_diff2 = cur[0]
        # print(cur_diff)
        seqs[-i - 2].append(seqs[-i - 2][-1] + cur_diff)
        seqs[-i - 2].insert(0, seqs[-i - 2][0] - cur_diff2)
        print(seqs)


def solve(infile):
    lines = parse(infile)
    print(lines)
    ans1 = 0
    ans2 = 0
    for line in lines:
        process_line(line)
        ans1 += line[-1]
        ans2 += line[0]

    return ans1, ans2


def main():
    print(solve('9_test.in'))
    print(solve('9.in'))


if __name__ == '__main__':
    main()
