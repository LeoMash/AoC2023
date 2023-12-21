from collections import deque


def get_input(infile):
    with open(infile) as f:
        content = f.read()
    lines = content.split('\n')
    lines = [[x for x in line] for line in lines]
    return lines


def find_start(lines):
    n = len(lines)
    m = len(lines[0])
    for i in range(n):
        for j in range(m):
            if lines[i][j] == 'S':
                return i, j
    return -1, -1


RIGHT, DOWN, LEFT, UP = range(4)
DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]
DIRS = list(zip(DX, DY))


def bfs(lines, sx, sy, limit):
    n = len(lines)
    m = len(lines[0])
    q = set()
    q.add((sx, sy))
    steps = 0
    while steps < limit:
        # print(f'step {steps}, q {l}')
        # print(q)
        next_q = set()
        for x, y in q:
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    c = lines[nx][ny]
                    if c == '.':
                        next_q.add((nx, ny))
        q = next_q
        steps += 1
    return len(q)


def solve1(infile, limit):
    lines = get_input(infile)
    for line in lines:
        print(''.join(line))
    sx, sy = find_start(lines)
    lines[sx][sy] = '.'
    print(sx, sy)
    ans = bfs(lines, sx, sy, limit)
    return ans


def bfs2(lines, sx, sy, limit):
    n = len(lines)
    m = len(lines[0])
    odd = set()
    even = set()
    q = set()
    q.add((sx, sy))
    steps = 0
    while steps <= limit:
        # print(q)
        if steps % 2 == 0:
            s = even
            next_s = odd
        else:
            s = odd
            next_s = even

        next_q = set()
        for x, y in q:
            s.add((x, y))
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if (nx, ny) in next_s:
                    continue
                nxn, nyn = nx % n, ny % m
                c = lines[nxn][nyn]
                if c == '.':
                    next_q.add((nx, ny))
        q = next_q
        print(f'step {steps} : {len(s)}')
        # print(s)
        steps += 1

    if steps % 2 == 0:
        s = odd
    else:
        s = even

    return len(s)


def solve2(infile, limit):
    lines = get_input(infile)
    sx, sy = find_start(lines)
    lines[sx][sy] = '.'
    ans = bfs2(lines, sx, sy, limit)
    return ans


def main():
    # print(solve1('21_test.in', 6))
    # print(solve1('21.in', 64))
    # print(solve2('21_test.in', 6))
    # print(solve2('21_test.in', 10))
    # print(solve2('21_test.in', 50))
    # print(solve2('21_test.in', 100))
    # print(solve2('21_test.in', 500))
    print(solve2('21_test.in', 1000))
    print(solve2('21_test.in', 5000))
    # print(solve2('21.in', 26501365))


if __name__ == '__main__':
    main()
