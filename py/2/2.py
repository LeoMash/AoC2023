LIMITS = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def solve1(infile):
    ans = 0
    with open(infile) as f:
        for line in f:
            line = line.strip()
            game, sets = line.split(':')
            game = game.strip()
            _, game = game.split(' ')
            game = int(game)
            sets = sets.split(';')
            sets_are_invalid = False
            for s in sets:
                if sets_are_invalid:
                    break
                vals = s.split(',')
                for val in vals:
                    val = val.strip()
                    val, color = val.split(' ')
                    val = int(val)
                    limit_value = LIMITS[color]
                    if val > limit_value:
                        sets_are_invalid = True
                        break
            if not sets_are_invalid:
                ans += game
    return ans


COL_2_IDX = {
    'red': 0,
    'green': 1,
    'blue': 2,
}


def solve2(infile):
    ans = 0
    with open(infile) as f:
        for line in f:
            line = line.strip()
            game, sets = line.split(':')
            sets = sets.split(';')
            min_set = [0, 0, 0]
            for s in sets:
                vals = s.split(',')
                for val in vals:
                    val = val.strip()
                    val, color = val.split(' ')
                    val = int(val)
                    idx = COL_2_IDX[color]
                    min_set[idx] = max(min_set[idx], val)
            power = min_set[0] * min_set[1] * min_set[2]
            ans += power

    return ans


def main():
    # print(solve1('2_test.in'))
    # print(solve1('2.in'))
    # print(solve2('2_test.in'))
    print(solve2('2.in'))

    pass


if __name__ == '__main__':
    main()
