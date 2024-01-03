from collections import deque, defaultdict


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
    step2cnt = defaultdict(int)
    visited = defaultdict(set)
    visited[0] = {(sx, sy)}
    q = deque()
    q.append(((sx, sy), 0))
    while q:
        (x, y), steps = q.popleft()
        if steps == limit:
            break
        step2cnt[steps] += 1
        steps += 1
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if lines[nx % n][ny % m] == '#':
                continue

            if steps not in step2cnt:
                step2cnt[steps] = step2cnt[steps - 2]
                visited[steps] = visited[steps - 2]

            if (nx, ny) not in visited[steps]:
                q.append(((nx, ny), steps))
                visited[steps].add((nx, ny))
    return step2cnt


def solve2(infile, limit):
    lines = get_input(infile)
    sx, sy = find_start(lines)
    lines[sx][sy] = '.'
    w = len(lines)
    h = len(lines[0])
    assert w == h
    print(w, h, sx, sy)
    limit_ovr = limit % w
    limit_upd = (limit_ovr + 2 * w) + 1
    print(limit_ovr, limit_upd)

    reachable = bfs2(lines, sx, sy, limit_upd)
    p = reachable[limit_ovr], reachable[limit_ovr + w], reachable[limit_ovr + 2 * w]
    print(p)

    n = limit // w
    a = (p[2] - 2 * p[1] + p[0]) // 2
    b = p[1] - p[0] - a
    c = p[0]
    ans = a * (n * n) + b * n + c
    return ans


def main():
    # print(solve1('21_test.in', 6))
    # print(solve1('21.in', 64))
    print(solve2('21.in', 26501365))


if __name__ == '__main__':
    main()
