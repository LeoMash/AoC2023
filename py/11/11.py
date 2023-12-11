def parse(infile):
    lines = []
    with open(infile) as f:
        for line in f:
            line = line.strip()
            lines.append(list(line))
    return lines


def expand_h(lines):
    # expand rows
    n = len(lines)
    m = len(lines[0])
    cols_to_copy = []
    for j in range(m):
        col_has_galaxy = False
        for i in range(n):
            if lines[i][j] == '#':
                col_has_galaxy = True
                break
        if col_has_galaxy:
            continue
        cols_to_copy.append(j)

    return cols_to_copy


def expand_v(lines):
    # expand columns
    n = len(lines)
    m = len(lines[0])
    rows_to_copy = []
    for i in range(n):
        row_has_galaxy = False
        for j in range(m):
            if lines[i][j] == '#':
                row_has_galaxy = True
                break
        if row_has_galaxy:
            continue
        rows_to_copy.append(i)

    return rows_to_copy


def expand(lines):
    cols = expand_h(lines)
    rows = expand_v(lines)
    return cols, rows


def solve(infile, expand_factor):
    lines = parse(infile)
    exp_cols, exp_rows = expand(lines)
    n = len(lines)
    m = len(lines[0])
    galaxies = []
    for i in range(n):
        for j in range(m):
            if lines[i][j] == '#':
                galaxies.append((i, j))

    n = len(galaxies)
    dist = [[0 for i in range(n)] for j in range(n)]
    ans = 0
    for i in range(n):
        gix, giy = galaxies[i]
        for j in range(i + 1, n):
            gjx, gjy = galaxies[j]

            exp_dist = 0
            for r in exp_rows:
                if gix < r < gjx:
                    exp_dist += expand_factor - 1
            for c in exp_cols:
                if giy < gjy:
                    if giy < c < gjy:
                        exp_dist += expand_factor - 1
                else:
                    if gjy < c < giy:
                        exp_dist += expand_factor - 1

            dist[i][j] = exp_dist + abs(gix - gjx) + abs(giy - gjy)
            ans += dist[i][j]
    return ans


def main():
    print(solve('11_test.in', 2))
    print(solve('11_test.in', 10))
    print(solve('11_test.in', 100))
    print(solve('11.in', 2))
    print(solve('11.in', 1e6))


if __name__ == '__main__':
    main()
