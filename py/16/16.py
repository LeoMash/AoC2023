def get_input(infile):
    with open(infile) as f:
        content = f.read()
    return content.split('\n')


RIGHT, DOWN, LEFT, UP = range(4)


def get_dir(d, c):
    if c == '.':
        return [d]
    if c == '\\':
        if d == RIGHT:
            return [DOWN]
        if d == DOWN:
            return [RIGHT]
        if d == LEFT:
            return [UP]
        if d == UP:
            return [LEFT]
    if c == '/':
        if d == RIGHT:
            return [UP]
        if d == DOWN:
            return [LEFT]
        if d == LEFT:
            return [DOWN]
        if d == UP:
            return [RIGHT]
    if c == '|':
        if d == RIGHT:
            return [UP, DOWN]
        if d == DOWN:
            return [DOWN]
        if d == LEFT:
            return [UP, DOWN]
        if d == UP:
            return [UP]
    if c == '-':
        if d == RIGHT:
            return [RIGHT]
        if d == DOWN:
            return [LEFT, RIGHT]
        if d == LEFT:
            return [LEFT]
        if d == UP:
            return [LEFT, RIGHT]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(mirr, sx, sy, sdir, e):
    n = len(mirr)
    m = len(mirr[0])

    q = [(sx, sy, sdir)]

    while q:
        x, y, dir = q.pop(0)

        ev, edirs = e[x][y]
        if ev == '#' and dir in edirs:
            # already were here from this direction
            continue

        # update info about current cell
        edirs.add(dir)
        e[x][y] = ('#', edirs)

        # split ray to new directions
        new_dirs = get_dir(dir, mirr[x][y])
        for new_d in new_dirs:
            nx, ny = x + dx[new_d], y + dy[new_d]

            if nx < 0 or nx >= n:
                continue
            if ny < 0 or ny >= m:
                continue

            q.append((nx, ny, new_d))


def get_e_value(e, n, m):
    ans = 0
    for i in range(n):
        for j in range(m):
            v = e[i][j][0]
            if v == '#':
                ans += 1
    return ans


def solve(mirr, x, y, d):
    n = len(mirr)
    m = len(mirr[0])
    e = [[('.', set()) for _ in range(m)] for _ in range(n)]
    bfs(mirr, x, y, d, e)

    # print(e)
    val = get_e_value(e, n, m)
    # print(f'{x} {y} {d} = {val}')
    return val


def solve1(infile):
    mirr = get_input(infile)
    ans = solve(mirr, 0, 0, 0)
    return ans


def solve2(infile):
    mirr = get_input(infile)
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
    print(solve1('16_test.in'))
    print(solve1('16.in'))
    print(solve2('16_test.in'))
    print(solve2('16.in'))


if __name__ == '__main__':
    main()
