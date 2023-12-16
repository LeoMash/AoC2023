import time
from collections import deque


def get_input(infile):
    with open(infile) as f:
        content = f.read()
    return content.split('\n')


CNV = {
    '.': 0,
    '\\': 1,
    '/': 2,
    '|': 3,
    '-': 4,
}


def conv(mirr):
    n = len(mirr)
    m = len(mirr[0])
    res = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            res[i][j] = CNV[mirr[i][j]]
    return res


RIGHT, DOWN, LEFT, UP = range(4)
MASK = [1, 2, 4, 8]

DSP = [
    [[RIGHT], [DOWN], [LEFT], [UP]],                    # '.'
    [[DOWN], [RIGHT], [UP], [LEFT]],                    # '\\'
    [[UP], [LEFT], [DOWN], [RIGHT]],                    # '/'
    [[UP, DOWN], [DOWN], [UP, DOWN], [UP]],             # '|'
    [[RIGHT], [LEFT, RIGHT], [LEFT], [LEFT, RIGHT]],    # '-'
]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(mirr, sx, sy, sdir, e):
    n = len(mirr)
    m = len(mirr[0])

    q = deque([(sx, sy, sdir)])

    while q:
        x, y, d = q.popleft()

        edirs = e[x][y]
        if (edirs & MASK[d]) == MASK[d]:
            # already were here from this direction
            continue

        # update info about current cell
        e[x][y] = edirs | MASK[d]

        # split ray to new directions
        for nd in DSP[mirr[x][y]][d]:
            nx, ny = x + dx[nd], y + dy[nd]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            q.append((nx, ny, nd))


def get_e_value(e, n, m):
    ans = 0
    for i in range(n):
        for j in range(m):
            if e[i][j]:
                ans += 1
    return ans


def solve(mirr, x, y, d):
    n = len(mirr)
    m = len(mirr[0])
    e = [[0 for _ in range(m)] for _ in range(n)]
    bfs(mirr, x, y, d, e)

    # print(e)
    val = get_e_value(e, n, m)
    # print(f'{x} {y} {d} = {val}')
    return val


def solve1(infile):
    mirr = get_input(infile)
    mirr = conv(mirr)
    ans = solve(mirr, 0, 0, 0)
    return ans


def solve2(infile):
    mirr = get_input(infile)
    mirr = conv(mirr)
    n = len(mirr)
    m = len(mirr[0])

    ans = 0
    for i in range(n):
        ans = max(ans, solve(mirr, i, 0, 0))
        ans = max(ans, solve(mirr, i, m - 1, 2))
    for j in range(m):
        ans = max(ans, solve(mirr, 0, j, 1))
        ans = max(ans, solve(mirr, n - 1, j, 3))
    return ans


def main():
    # print(solve1('16_test.in'))
    # print(solve1('16.in'))
    # print(solve2('16_test.in'))
    tm = time.time()
    print(solve2('16.in'))
    print(time.time() - tm)


if __name__ == '__main__':
    main()
