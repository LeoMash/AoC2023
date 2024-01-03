import z3


def get_input(infile):
    with open(infile) as f:
        content = f.read()
    stones = []
    for line in content.split('\n'):
        line = line.replace('@', ', ')
        stone = [int(x) for x in line.split(', ')]
        stones.append(stone)
    return stones


def isect2d(s1, s2):
    s1x, s1y, _, s1dx, s1dy, _ = s1
    s2x, s2y, _, s2dx, s2dy, _ = s2

    div = (s1dx * s2dy - s1dy * s2dx)
    if div == 0:
        return None
    n1 = (-s1x * s2dy + s1y * s2dx - s2dx * s2y + s2dy * s2x) / div
    n2 = (s1dx * s1y - s1dx * s2y - s1dy * s1x + s1dy * s2x) / div
    ix = s1x + n1 * s1dx
    iy = s1y + n1 * s1dy
    return ix, iy, n1, n2


def solve1(infile, lim):
    stones = get_input(infile)
    print(stones)
    n = len(stones)
    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            print(i, j)
            res = isect2d(stones[i], stones[j])
            print(res)
            if res is None:
                continue
            ix, iy, d1, d2 = res
            if not (lim[0] <= ix <= lim[1] and lim[0] <= iy <= lim[1]):
                continue
            if not (d1 > 0 and d2 > 0):
                continue
            ans += 1

    return ans


def solve2(infile):
    stones = get_input(infile)
    print(stones)

    sx, sy, sz, dx, dy, dz = z3.Real('sx'), z3.Real('sy'), z3.Real('sz'), z3.Real('dx'), z3.Real('dy'), z3.Real('dz')
    t = [z3.Real('t0'), z3.Real('t1'), z3.Real('t2')]
    solver = z3.Solver()
    for i in range(3):
        solver.add(sx + t[i] * dx - stones[i][0] - t[i] * stones[i][3] == 0)
        solver.add(sy + t[i] * dy - stones[i][1] - t[i] * stones[i][4] == 0)
        solver.add(sz + t[i] * dz - stones[i][2] - t[i] * stones[i][5] == 0)
    assert solver.check()
    model = solver.model()
    x = model.eval(sx)
    y = model.eval(sy)
    z = model.eval(sz)
    print(x, y, z)
    ans = model.eval(x + y + z)
    return ans


def main():
    # print(solve1('24_test.in', [7, 27]))
    # print(solve1('24.in', [200000000000000, 400000000000000]))
    # print(solve2('24_test.in'))
    print(solve2('24.in'))


if __name__ == '__main__':
    main()
