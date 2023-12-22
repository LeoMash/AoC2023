from collections import deque


def get_input(infile):
    with open(infile) as f:
        content = f.read()
    blocks = [block.replace('~', ',').split(',') for block in content.split('\n')]
    blocks = [[int(c) for c in block] for block in blocks]
    return blocks


def overlaps(b1, b2):
    b1x1, b1y1, b1z1, b1x2, b1y2, b1z2 = b1
    b2x1, b2y1, b2z1, b2x2, b2y2, b2z2 = b2
    return max(b1x1, b2x1) <= min(b1x2, b2x2) and max(b1y1, b2y1) <= min(b1y2, b2y2)


def solve1(infile):
    blocks = get_input(infile)
    print(blocks)

    # sort by z
    blocks.sort(key=lambda block: block[2])
    print(blocks)
    # fall blocks from lowest
    for index, block in enumerate(blocks):
        max_z = 1
        for prev_block in blocks[:index]:
            if overlaps(block, prev_block):
                max_z = max(max_z, prev_block[5] + 1)
        diff = block[2] - max_z
        block[5] -= diff
        block[2] -= diff

    print(blocks)

    me_supports = {i: set() for i in range(len(blocks))}
    me_supported_by = {i: set() for i in range(len(blocks))}
    for j, upper in enumerate(blocks):
        for i, lower in enumerate(blocks[:j]):
            if overlaps(lower, upper) and upper[2] == lower[5] + 1:
                me_supports[i].add(j)
                me_supported_by[j].add(i)

    print(me_supports)
    print(me_supported_by)

    ans = 0
    for i in range(len(blocks)):
        if all(len(me_supported_by[j]) >= 2 for j in me_supports[i]):
            ans += 1
    return ans


def solve2(infile):
    blocks = get_input(infile)
    print(blocks)

    # sort by z
    blocks.sort(key=lambda block: block[2])
    print(blocks)

    # fall blocks from lowest
    for index, block in enumerate(blocks):
        max_z = 1
        for prev_block in blocks[:index]:
            if overlaps(block, prev_block):
                max_z = max(max_z, prev_block[5] + 1)
        diff = block[2] - max_z
        block[5] -= diff
        block[2] -= diff

    print(blocks)

    me_supports = {i: set() for i in range(len(blocks))}
    me_supported_by = {i: set() for i in range(len(blocks))}
    for j, upper in enumerate(blocks):
        for i, lower in enumerate(blocks[:j]):
            if overlaps(lower, upper) and upper[2] == lower[5] + 1:
                me_supports[i].add(j)
                me_supported_by[j].add(i)

    print(me_supports)
    print(me_supported_by)

    ans = 0
    for i in range(len(blocks)):
        print(i)
        q = deque(j for j in me_supports[i] if len(me_supported_by[j]) == 1)
        falling = set(q) | {i}
        while q:
            print(q)
            print(falling)
            j = q.popleft()
            j_supports_left = me_supports[j] - falling
            for k in j_supports_left:
                if me_supported_by[k].issubset(falling):
                    q.append(k)
                    falling.add(k)

        ans += len(falling) - 1

    return ans


def main():
    # print(solve1('22_test.in'))
    # print(solve1('22.in'))
    # print(solve2('22_test.in'))
    print(solve2('22.in'))


if __name__ == '__main__':
    main()
