def get_input(infile):
    with open(infile) as f:
        content = f.read()
    return list(map(list, content.split('\n')))


def roll(data):
    n = len(data)
    m = len(data[0])
    for j in range(m):
        col = []
        for i in range(n):
            if data[i][j] == '#':
                col.append((i, 1))
            elif data[i][j] == 'O':
                col.append((i, 0))

        # print(j, col)
        cur_idx = -1
        for k in range(len(col)):
            i, o = col[k]
            if not o:
                data[i][j] = '.'
                cur_idx += 1
                data[cur_idx][j] = 'O'
            else:
                # rock found
                cur_idx = i


def print_data(data):
    for line in data:
        print(''.join(line))


def solve1(infile):
    data = get_input(infile)
    print_data(data)
    roll(data)
    print_data(data)
    line_cost = len(data)
    ans = 0
    for line in data:
        for c in line:
            if c == 'O':
                ans += line_cost
        line_cost -= 1
    return ans


def rotate(data):
    n = len(data)
    m = len(data[0])
    rdata = [['' for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            rdata[j][n - 1 - i] = data[i][j]
    return rdata


def solve2(infile, num_spins):
    data = get_input(infile)
    print_data(data)
    data_to_spin = {}
    data_cache = []
    data_idx = -1
    spin = 0
    while spin < num_spins:
        # print(spin)
        for rot in range(4):
            # print(spin, rot)
            roll(data)
            # print_data(data)
            # print('=' * 80)
            data = rotate(data)
            # print_data(data)

        imm_data = tuple(tuple(line) for line in data)
        h = hash(imm_data)
        if h in data_to_spin:
            idx_cycle_start = data_to_spin[h]
            cycle_len = spin - idx_cycle_start
            print(f'CYCLE FOUND: start {idx_cycle_start}, len {cycle_len}')
            spins_to_skip = (num_spins - spin) // cycle_len
            spin += spins_to_skip * cycle_len
            spins_left = num_spins - spin - 1
            print(f'SKIPPING to {spin}, spins_left {spins_left}')
            data_idx = idx_cycle_start + spins_left
            break

        data_to_spin[h] = spin
        data_cache.append(imm_data)
        spin += 1

    print(f'Use data from spin {data_idx}')
    data = data_cache[data_idx]
    print_data(data)

    line_cost = len(data)
    ans = 0
    for line in data:
        for c in line:
            if c == 'O':
                ans += line_cost
        line_cost -= 1
    return ans


def main():
    num_spins = 1000000000
    # print(solve1('14_test.in'))
    # print(solve2('14_test.in', num_spins))
    # print(solve1('14.in', False))
    print(solve2('14.in', num_spins))


if __name__ == '__main__':
    main()
