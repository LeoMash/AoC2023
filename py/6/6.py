def parse1(infile):
    with open(infile) as f:
        times = f.readline().split(':')[1].strip().split()
        times = list(map(int, times))
        distances = f.readline().split(':')[1].strip().split()
        distances = list(map(int, distances))
        return times, distances


def parse2(infile):
    with open(infile) as f:
        times = f.readline().split(':')[1].strip().split()
        time = int(''.join(times))
        distances = f.readline().split(':')[1].strip().split()
        distance = int(''.join(distances))
        return time, distance


def get_num_wins(t, win_d):
    num_win = 0
    for j in range(t + 1):
        if j * (t - j) > win_d:
            num_win += 1
    return num_win


def solve1(infile):
    times, distances = parse1(infile)
    ans = 1
    for t, d in zip(times, distances):
        ans *= get_num_wins(t, d)
    return ans


def solve2(infile):
    t, d = parse2(infile)
    return get_num_wins(t, d)


def main():
    print(solve1('6_test.in'))
    print(solve1('6.in'))
    print(solve2('6_test.in'))
    print(solve2('6.in'))


if __name__ == '__main__':
    main()
