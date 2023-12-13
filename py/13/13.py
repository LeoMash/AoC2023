def get_blocks(infile):
    with open(infile) as f:
        content = f.read()
    blocks = content.split('\n\n')
    for block in blocks:
        lines = []
        for line in block.split('\n'):
            lines.append(line)
        yield lines


def conv_to_numbers(lines):
    hor_values = []
    for line in lines:
        val = 0
        for c in line:
            if c == '#':
                val += 1
            val *= 2
        hor_values.append(val)
    print(hor_values)
    ver_values = []
    n = len(lines)
    m = len(lines[0])
    for j in range(m):
        val = 0
        for i in range(n):
            c = lines[i][j]
            if c == '#':
                val += 1
            val *= 2
        ver_values.append(val)
    print(ver_values)
    return hor_values, ver_values


def check_sym(vals, i, non_sym_bits_limit=0):
    num_non_sym_bits = 0
    n = len(vals)
    k = min(i, n - i - 2)
    for j in range(k + 1):
        x, y = vals[i - j], vals[i + 1 + j]
        bit_diff = (x ^ y).bit_count()
        num_non_sym_bits += bit_diff
        if num_non_sym_bits > non_sym_bits_limit:
            return False
    return num_non_sym_bits == non_sym_bits_limit


def get_block_value(lines, flag):
    print(lines)
    limit = 1 if flag else 0
    hor_values, ver_values = conv_to_numbers(lines)
    for i in range(len(hor_values) - 1):
        # hor_line between i and i+1
        if check_sym(hor_values, i, limit):
            return (i + 1) * 100
    for i in range(len(ver_values) - 1):
        # ver_line between i and i+1
        if check_sym(ver_values, i, limit):
            return i + 1
    return 0


def solve(infile, flag2=False):
    ans = 0
    for block in get_blocks(infile):
        num = get_block_value(block, flag2)
        print(num)
        ans += num
    return ans


def main():
    # print(solve('13_test.in'))
    # print(solve('13_test.in', True))
    print(solve('13.in', False))
    print(solve('13.in', True))


if __name__ == '__main__':
    main()
