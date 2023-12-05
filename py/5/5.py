
types = [
    'seed',
    'soil',
    'fertilizer',
    'water',
    'light',
    'temperature',
    'humidity',
]
total_modes = len(types)


def parse(infile):
    maps = []
    for i in range(total_modes):
        maps.append([])

    seeds = []
    with open(infile) as f:
        _, seedsline = f.readline().split(':')
        seeds = seedsline.strip().split(' ')
        seeds = list(map(int, seeds))

        cur_mode = -1
        for line in f:
            line = line.strip()
            if not line:
                continue
            for i, t in enumerate(types):
                if line.startswith(t):
                    cur_mode = i
                    break
            else:
                to, fr, num = line.split(' ')
                to = int(to)
                fr = int(fr)
                num = int(num)
                maps[cur_mode].append((fr, fr + num, to))
                maps[cur_mode].sort(key=lambda x: x[0])

    return seeds, maps


def transform(val, cur_map):
    for s, e, dst in cur_map:
        if s <= val < e:
            return dst + val - s
    return val


def is_valid_range(r):
    return r[1] > r[0]


def transform_range(r, cur_map):
    parts = [r]
    transformed_parts = []
    for s, e, dst in cur_map:
        new_parts = []
        while parts:
            st, ed = parts.pop()
            cut_before = (st, min(ed, s))
            if is_valid_range(cut_before):
                new_parts.append(cut_before)
            cur_intersected = (max(st, s), min(e, ed))
            if is_valid_range(cur_intersected):
                transformed_parts.append((cur_intersected[0] - s + dst, cur_intersected[1] - s + dst))
            cut_after = (max(e, st), ed)
            if is_valid_range(cut_after):
                new_parts.append(cut_after)
        parts = new_parts
    return transformed_parts + parts


def solve1(infile):
    seeds, maps = parse(infile)
    vals = seeds
    for mode in range(total_modes):
        print(vals)
        cur_map = maps[mode]
        new_vals = []
        for val in vals:
            val = transform(val, cur_map)
            new_vals.append(val)
        vals = new_vals

    print(vals)
    ans = min(vals)
    return ans


def solve2(infile):
    ans = 0
    seeds, maps = parse(infile)
    seed_ranges_ = list(zip(seeds[::2], seeds[1::2]))
    seed_ranges = []
    for r in seed_ranges_:
        seed_ranges.append((r[0], r[0] + r[1]))
    ranges = seed_ranges
    for mode in range(total_modes):
        print(ranges)
        cur_map = maps[mode]
        new_ranges = []
        for r in ranges:
            rs = transform_range(r, cur_map)
            new_ranges.extend(rs)
        ranges = new_ranges

    print(ranges)
    ranges_starts = [r[0] for r in ranges]
    ans = min(ranges_starts)

    return ans


def main():
    # print(solve1('5_test.in'))
    # print(solve1('5.in'))
    # print(solve2('5_test.in'))
    print(solve2('5.in'))


if __name__ == '__main__':
    main()
