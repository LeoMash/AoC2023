from collections import deque


def get_input(infile):
    with open(infile) as f:
        content = f.read()
    return content.split('\n')


DXS = [-1, 0, 1, 0]
DYS = [0, -1, 0, 1]
D = list(zip(DXS, DYS))

DIRS = {
    "^": [(-1, 0)],
    "v": [(1, 0)],
    "<": [(0, -1)],
    ">": [(0, 1)],
    ".": [(-1, 0), (1, 0), (0, -1), (0, 1)],
}


def solve(infile, part2=False):
    grid = get_input(infile)
    print('\n'.join(grid))

    n = len(grid)
    m = len(grid[0])

    sx, sy = 0, grid[0].index('.')
    ex, ey = n - 1, grid[n - 1].index('.')

    print(sx, sy)
    print(ex, ey)

    split_points = []
    for x in range(n):
        for y in range(m):
            c = grid[x][y]
            if c == '#':
                continue
            path_variants = 0
            for dx, dy in D:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#':
                    path_variants += 1
            if path_variants >= 3:
                split_points.append((x, y))

    points = [(sx, sy)]
    points.extend(split_points)
    points.append((ex, ey))
    print(points)

    # build graph with points as nodes
    g = {pt: {} for pt in points}

    for cx, cy in points:
        stack = [(0, cx, cy)]
        seen = {(cx, cy)}

        print(cx, cy)

        while stack:
            d, x, y = stack.pop()
            print(n, x, y)

            if d > 0 and (x, y) in points:
                print('edge found')
                g[(cx, cy)][(x, y)] = d
                continue

            c = grid[x][y]
            dirs = DIRS[c] if not part2 else DIRS['.']
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    nc = grid[nx][ny]
                    if nc != "#" and (nx, ny) not in seen:
                        stack.append((d + 1, nx, ny))
                        seen.add((nx, ny))

    print(g)

    visited = [[False for _ in range(m)] for _ in range(n)]

    def dfs(x, y):
        if x == ex and y == ey:
            return 0

        d = -1e9

        visited[x][y] = True
        for (nx, ny) in g[(x, y)]:
            if not visited[nx][ny]:
                d = max(d, dfs(nx, ny) + g[(x, y)][(nx, ny)])
        visited[x][y] = False

        return d

    return dfs(sx, sy)


def main():
    print(solve('23_test.in'))
    print(solve('23.in'))
    print(solve('23_test.in', True))
    print(solve('23.in', True))


if __name__ == '__main__':
    main()
