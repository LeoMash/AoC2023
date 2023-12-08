import math
import re

M = re.compile(r'(.*) = \((.*), (.*)\)')


def solve1(infile):
    ans = 0
    cur = 'AAA'
    tree = {}
    with open(infile) as f:
        cmd = f.readline().strip()
        for line in f:
            line = line.strip()
            if not line:
                continue
            m = M.match(line)
            assert m
            fr = m.group(1)
            l = m.group(2)
            r = m.group(3)
            tree[fr] = (l, r)
    print(tree)
    while cur != 'ZZZ':
        # print(cur)
        c = cmd[ans % len(cmd)]
        cur = tree[cur][0 if c == 'L' else 1]
        ans += 1
    return ans


def lcm(a, b):
    return (a * b) // math.gcd(a, b)


def solve2(infile):
    ans = 0
    cur = []
    tree = {}
    with open(infile) as f:
        cmd = f.readline().strip()
        for line in f:
            line = line.strip()
            if not line:
                continue
            m = M.match(line)
            assert m
            fr = m.group(1)
            l = m.group(2)
            r = m.group(3)
            if fr[2] == 'A':
                cur.append(fr)
            tree[fr] = (l, r)

    steps = []
    for node in cur:
        steps_node = 0
        while node[2] != 'Z':
            # print(cur)
            c = cmd[steps_node % len(cmd)]
            node = tree[node][0 if c == 'L' else 1]
            steps_node += 1
        steps.append(steps_node)
    print(steps)
    ans = 1
    for st in steps:
        ans = lcm(st, ans)
    return ans


def main():
    # print(solve1('8_test.in'))
    # print(solve1('8.in'))
    # print(solve2('8_test2.in'))
    print(solve2('8.in'))


if __name__ == '__main__':
    main()
