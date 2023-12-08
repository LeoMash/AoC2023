import math
import re

M = re.compile(r'(.*) = \((.*), (.*)\)')


def parse(infile):
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
    return cmd, tree


def num_steps(cmd, tree, start, check):
    cur = start
    ans = 0
    while not check(cur):
        c = cmd[ans % len(cmd)]
        cur = tree[cur][0 if c == 'L' else 1]
        ans += 1
    return ans


def solve1(infile):
    cmd, tree = parse(infile)
    ans = num_steps(cmd, tree, 'AAA', lambda x: x == 'ZZZ')
    return ans


def solve2(infile):
    cmd, tree = parse(infile)
    cur = []
    for node in tree.keys():
        if node[2] == 'A':
            cur.append(node)

    steps = []
    for node in cur:
        steps_node = num_steps(cmd, tree, node, lambda x: x[2] == 'Z')
        steps.append(steps_node)

    print(steps)
    ans = math.lcm(*steps)
    return ans


def main():
    print(solve1('8_test.in'))
    print(solve1('8.in'))
    print(solve2('8_test2.in'))
    print(solve2('8.in'))


if __name__ == '__main__':
    main()
