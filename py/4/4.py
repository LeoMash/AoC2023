from collections import defaultdict


def get_card(line):
    _, nums = line.split(':')
    win, nums = nums.split('|')
    win = win.strip()
    win = list(map(int, filter(None, win.split(' '))))
    nums = nums.strip()
    nums = list(map(int, filter(None, nums.split(' '))))
    return win, nums


def get_card_cost(line):
    win, nums = get_card(line)
    win = set(win)

    cost = 0
    for num in nums:
        if num in win:
            cost += 1
    return cost


def solve1(infile):
    ans = 0
    with open(infile) as f:
        for line in f:
            cost = get_card_cost(line)
            if cost > 0:
                ans += pow(2, cost - 1)

    return ans


def solve2(infile):
    ans = 0
    cnt = defaultdict(int)
    with open(infile) as f:
        for i, line in enumerate(f):
            cost = get_card_cost(line)
            cnt[i] += 1
            ans += cnt[i]
            for j in range(cost):
                cnt[i + j + 1] += cnt[i]

    return ans


def main():
    print(solve1('4_test.in'))
    print(solve1('4.in'))
    print(solve2('4_test.in'))
    print(solve2('4.in'))


if __name__ == '__main__':
    main()
