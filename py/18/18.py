def get_input(infile):
    with open(infile) as f:
        content = f.read()
    lines = content.split('\n')
    return [line.split() for line in lines]


RIGHT, DOWN, LEFT, UP = range(4)
DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]

DIRS = list(zip(DX, DY))

DIR_MAP = {
    'R': RIGHT,
    'D': DOWN,
    'L': LEFT,
    'U': UP,
}


def solve(infile, flag2=False):
    cmdline = get_input(infile)
    p = [(0, 0)]
    e = 0
    for d, l, col in cmdline:
        if not flag2:
            l = int(l)
            d = DIR_MAP[d]
        else:
            col = col[2:-1]
            d = int(col[-1])
            l = int(col[:-1], 16)
        print(d, l)
        e += l
        dx, dy = DIRS[d]
        x, y = p[-1]
        p.append((x + dx * l, y + dy * l))

    print(p)
    area = 0
    for i in range(len(p)):
        p1 = p[i]
        p2 = p[(i + 1) % len(p)]
        area += p1[0] * p2[1] - p1[1] * p2[0]

    area = abs(area) // 2 + e // 2 + 1
    return area


def main():
    # print(solve('18_test.in'))
    # print(solve('18.in'))
    # print(solve('18_test.in', True))
    print(solve('18.in', True))


if __name__ == '__main__':
    main()
