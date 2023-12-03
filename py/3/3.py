import re
from collections import defaultdict


def around(i, s, e, n, m):
    # ......
    # .4567.
    # ......
    check_locs = []
    if i > 0:
        check_locs += [(i - 1, j) for j in range(max(s - 1, 0), min(e + 1, m))]
    if s > 0:
        check_locs += [(i, s - 1)]
    if e < m - 1:
        check_locs += [(i, e)]
    if i < n - 1:
        check_locs += [(i + 1, j) for j in range(max(s - 1, 0), min(e + 1, m))]
    return check_locs


def solve1(infile):
    ans = 0
    with open(infile) as f:
        lines = f.read().splitlines()
        n = len(lines)
        m = len(lines[0])

        for i, line in enumerate(lines):
            for match in re.finditer(r'\d+', line):
                val = int(match.group())
                s = match.start()
                e = match.end()
                check_locs = around(i, s, e, n, m)
                for x, y in check_locs:
                    if lines[x][y] != '.':
                        ans += val
                        break
    return ans


def solve2(infile):
    ans = 0
    with open(infile) as f:
        lines = f.read().splitlines()
        n = len(lines)
        m = len(lines[0])
        adj = defaultdict(list)

        for i, line in enumerate(lines):
            for match in re.finditer(r'\d+', line):
                # ......
                # .4567.
                # ......
                val = int(match.group())
                s = match.start()
                e = match.end()
                check_locs = around(i, s, e, n, m)
                for x, y in check_locs:
                    if lines[x][y] == '*':
                        adj[x, y].append(val)
                        break

        for p in adj.values():
            if len(p) != 2:
                continue
            ans += p[0] * p[1]
    return ans


def main():
    print(solve1('3_test.in'))
    print(solve1('3.in'))
    print(solve2('3_test.in'))
    print(solve2('3.in'))

    pass


if __name__ == '__main__':
    main()
