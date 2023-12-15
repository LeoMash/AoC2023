def get_input(infile):
    with open(infile) as f:
        content = f.read()
    return content.split(',')


def my_hash(s):
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val = val % 256
    return val


def solve1(infile):
    strs = get_input(infile)
    ans = 0
    for s in strs:
        ans += my_hash(s)
    return ans


def solve2(infile):
    strs = get_input(infile)

    m = [[] for i in range(256)]
    for s in strs:
        if '-' in s:
            lbl, _ = s.split('-')
            h = my_hash(lbl)
            for i in range(len(m[h])):
                if m[h][i][0] == lbl:
                    del m[h][i]
                    break
        else:
            lbl, val = s.split('=')
            val = int(val)
            h = my_hash(lbl)
            for i in range(len(m[h])):
                if m[h][i][0] == lbl:
                    m[h][i][1] = val
                    break
            else:
                m[h].append([lbl, val])
        # print(m)

    ans = 0
    for i in range(256):
        for j, (lbl, val) in enumerate(m[i]):
            ans += (i + 1) * (j + 1) * val
    return ans


def main():
    # print(solve1('15_test.in'))
    # print(solve1('15.in'))
    # print(solve2('15_test.in'))
    print(solve2('15.in'))


if __name__ == '__main__':
    main()
