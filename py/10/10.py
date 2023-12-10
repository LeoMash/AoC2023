def parse(infile):
    lines = []
    with open(infile) as f:
        for line in f:
            line = line.strip()
            lines.append(line)
    return lines


def wrap(lines, param):
    m = len(lines[0])
    lines.insert(0, [param] * m)
    lines.append([param] * m)
    new_lines = []
    for line in lines:
        line = [param] + list(line) + [param]
        new_lines.append(line)
    return new_lines


dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]
D = list(zip(dxs, dys))
DIRS = {
    '.': [None, None, None, None],
    '|': [0, None, 2, None],
    '-': [None, 1, None, 3],
    'L': [None, 0, 3, None],
    'J': [None, None, 1, 0],
    '7': [1, None, None, 2],
    'F': [3, 2, None, None]
}


def solve(infile):
    lines = parse(infile)
    lines = wrap(lines, '.')
    print(lines)
    n = len(lines)
    m = len(lines[0])

    def find_start():
        for i in range(n):
            for j in range(m):
                if lines[i][j] == 'S':
                    return i, j
        return -1, -1

    sx, sy = find_start()
    print(sx, sy)
    q = []
    visited = [[False for i in range(m)] for j in range(n)]
    visited[sx][sy] = True
    for i in range(len(D)):
        dx, dy = D[i]
        x, y = (sx + dx, sy + dy)
        q.append((x, y, i, 1))

    def go(x, y, dfrom):
        c = lines[x][y]
        new_d = DIRS[c][dfrom]
        if new_d is None:
            return None
        dx, dy = D[new_d]
        return (x + dx, y + dy, new_d)

    # print(visited)
    ans = 0
    cx, cy = 0, 0
    while q:
        x, y, dfrom, steps = q.pop(0)
        p = go(x, y, dfrom)
        if not p:
            print(lines[x][y], (x, y, dfrom), steps, '-> None')
            continue
        visited[x][y] = True
        nx, ny, newd = p
        print(lines[x][y], (x, y, dfrom), steps, '->', lines[nx][ny], p)
        if visited[nx][ny]:
            print('VISITED!!!')
            ans = steps
            cx = x
            cy = y
            break
        q.append((nx, ny, newd, steps + 1))

    visited = [[False for i in range(m)] for j in range(n)]
    visited[cx][cy] = True
    path1 = [(cx, cy, 0)]
    while True:
        x, y, d = path1[-1]
        nx, ny, nd = go(x, y, d)
        visited[nx][ny] = True
        path1.append((nx, ny, nd))
        if lines[nx][ny] == 'S':
            break
    path2 = [(cx, cy, 2)]
    while True:
        x, y, d = path2[-1]
        nx, ny, nd = go(x, y, d)
        visited[nx][ny] = True
        path2.append((nx, ny, nd))
        if lines[nx][ny] == 'S':
            break

    area = 0
    for i in range(n):
        inside = False
        for j in range(m):
            c = lines[i][j]
            if visited[i][j] and c in ('|', '7', 'F'):
                inside = not inside
            if inside and not visited[i][j]:
                area += 1

    return ans, area


def main():
    # print(solve('10_test.in'))
    # print(solve('10_test2.in'))
    print(solve('10.in'))


if __name__ == '__main__':
    main()
