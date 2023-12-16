def get_input(infile):
    with open(infile) as f:
        content = f.read()
    return content.split('\n')


def show(data):
    for line in data:
        print(line)


RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3


def get_dir(dir, c):
    if c == '.':
        return [dir]
    if c == '\\':
        if dir == RIGHT:
            return [DOWN]
        if dir == DOWN:
            return [RIGHT]
        if dir == LEFT:
            return [UP]
        if dir == UP:
            return [LEFT]
    if c == '/':
        if dir == RIGHT:
            return [UP]
        if dir == DOWN:
            return [LEFT]
        if dir == LEFT:
            return [DOWN]
        if dir == UP:
            return [RIGHT]
    if c == '|':
        if dir == RIGHT:
            return [UP, DOWN]
        if dir == DOWN:
            return [DOWN]
        if dir == LEFT:
            return [UP, DOWN]
        if dir == UP:
            return [UP]
    if c == '-':
        if dir == RIGHT:
            return [RIGHT]
        if dir == DOWN:
            return [LEFT, RIGHT]
        if dir == LEFT:
            return [LEFT]
        if dir == UP:
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
            nx = x + dx[new_d]
            ny = y + dy[new_d]

            if nx < 0 or nx >= n:
                continue
            if ny < 0 or ny >= m:
                continue

            q.append((nx, ny, new_d))


def get_e_value(e, n, m):
    ans = 0
    for i in range(n):
        for j in range(m):
            v, _ = e[i][j]
            if v == '#':
                ans += 1
    return ans


def solve1(infile):
    mirr = get_input(infile)
    show(mirr)
    n = len(mirr)
    m = len(mirr[0])
    e = [[('.', set()) for j in range(m)] for i in range(n)]

    bfs(mirr, 0, 0, 0, e)

    print(e)

    ans = get_e_value(e, n, m)
    return ans


def solve2(infile):
    mirr = get_input(infile)
    show(mirr)
    n = len(mirr)
    m = len(mirr[0])

    ans = 0
    for i in range(n):
        e = [[('.', set()) for j in range(m)] for i in range(n)]
        bfs(mirr, i, 0, 0, e)

        # print(e)
        val = get_e_value(e, n, m)
        print(f'{i} {0} = val')
        ans = max(ans, val)
    for j in range(m):
        e = [[('.', set()) for j in range(m)] for i in range(n)]
        bfs(mirr, 0, j, 1, e)

        # print(e)
        val = get_e_value(e, n, m)
        print(f'{0} {j} = val')
        ans = max(ans, val)
    for i in range(n):
        e = [[('.', set()) for j in range(m)] for i in range(n)]
        bfs(mirr, i, m - 1, 2, e)

        # print(e)
        val = get_e_value(e, n, m)
        print(f'{i} {m - 1} = val')
        ans = max(ans, val)
    for j in range(m):
        e = [[('.', set()) for j in range(m)] for i in range(n)]
        bfs(mirr, n - 1, j, 3, e)

        # print(e)
        val = get_e_value(e, n, m)
        print(f'{n - 1} {j} = val')
        ans = max(ans, val)
    return ans


def main():
    # print(solve1('16_test.in'))
    # print(solve1('16.in'))
    # print(solve2('16_test.in'))
    print(solve2('16.in'))


if __name__ == '__main__':
    main()
