import heapq
import time
from collections import deque


def get_input(infile):
    with open(infile) as f:
        content = f.read()
    lines = content.split('\n')
    return [[int(x) for x in line] for line in lines]


RIGHT, DOWN, LEFT, UP = range(4)
DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]

DIRS = list(zip(DX, DY))


def get_new_dir_len_1(new_dir, cur_dir, cur_dir_len):
    if (cur_dir + 2) % 4 == new_dir:
        # can't go reverse direction
        return None
    if cur_dir == new_dir:
        new_dir_len = cur_dir_len + 1
        if new_dir_len > 3:
            return None
        return new_dir_len
    else:
        new_dir_len = 1
        return new_dir_len


def get_new_dir_len_2(new_dir, cur_dir, cur_dir_len):
    if (cur_dir + 2) % 4 == new_dir:
        # can't go reverse direction
        return None
    if cur_dir == new_dir:
        new_dir_len = cur_dir_len + 1
        if new_dir_len > 10:
            return None
        return new_dir_len
    else:
        if cur_dir_len < 4 and cur_dir != -1:
            # can't rotate
            return None
        new_dir_len = 1
        return new_dir_len


def solve(infile, part2=False):
    a = get_input(infile)
    # print(a)
    n = len(a)
    m = len(a[0])

    q = []
    q.append((0, 0, 0, -1, -1))

    state = [[{} for j in range(m)] for i in range(n)]

    while q:
        dist, x, y, di, dl = heapq.heappop(q)
        if (di, dl) in state[x][y]:
            continue
        state[x][y][(di, dl)] = dist

        for ndi in range(4):
            dx, dy = DIRS[ndi]
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if not part2:
                ndl = get_new_dir_len_1(ndi, di, dl)
                if ndl is None:
                    continue
            else:
                ndl = get_new_dir_len_2(ndi, di, dl)
                if ndl is None:
                    continue
            new_dist = dist + a[nx][ny]
            heapq.heappush(q, (new_dist, nx, ny, ndi, ndl))

    # print(state)

    ans = 100000000
    for dist in state[n - 1][m - 1].values():
        ans = min(ans, dist)
    return ans


def main():
    # print(solve('17_test.in'))
    # print(solve('17.in'))
    # print(solve('17_test.in', True))
    print(solve('17.in', True))


if __name__ == '__main__':
    main()
