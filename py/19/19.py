
def get_input(infile):
    with open(infile) as f:
        content = f.read()
    rules_str, parts_str = content.split('\n\n')

    rules_str = rules_str.split('\n')
    rules = {}
    for rule_str in rules_str:
        rule_str = rule_str[:-1]
        name, rule_str = rule_str.split('{')
        rule_parts = rule_str.split(',')
        rules_seq = []
        for rule_part in rule_parts:
            if ':' not in rule_part:
                op = None
                n = None
                val = None
                next_rule_name = rule_part
            else:
                rule_cond, next_rule_name = rule_part.split(':')
                if '<' in rule_cond:
                    op = '<'
                    n, val = rule_cond.split('<')
                    val = int(val)
                elif '>' in rule_cond:
                    op = '>'
                    n, val = rule_cond.split('>')
                    val = int(val)
                else:
                    assert False
            rules_seq.append((op, n, val, next_rule_name))
        rules[name] = rules_seq
    print(rules)
    parts_str = parts_str.split('\n')
    parts = []
    for part_str in parts_str:
        part_str = part_str[1:-1]
        vals_str = part_str.split(',')
        part = {}
        for val_str in vals_str:
            n, val = val_str.split('=')
            part[n] = int(val)
        parts.append(part)
    print(parts)

    return rules, parts


def is_ok(part, rules):
    cur_rule = 'in'
    while cur_rule != 'A' and cur_rule != 'R':
        rule = rules[cur_rule]
        next_rule = None
        for rule_part in rule:
            op, n, val, nxt = rule_part
            if op is None:
                next_rule = nxt
                break
            v1 = part[n]
            if op == '<' and v1 < val:
                next_rule = nxt
                break
            if op == '>' and v1 > val:
                next_rule = nxt
                break

        cur_rule = next_rule
    return cur_rule == 'A'


def solve1(infile):
    rules, parts = get_input(infile)
    ans = 0
    for part in parts:
        if not is_ok(part, rules):
            continue
        ans += part['x'] + part['m'] + part['a'] + part['s']
    return ans


def count(path):
    parts = dict(
        x=[1, 4000],
        m=[1, 4000],
        a=[1, 4000],
        s=[1, 4000],
    )

    for op, n, val in path:
        if op == '<':
            parts[n][1] = min(parts[n][1], val - 1)
        else:  # op == '>'
            parts[n][0] = max(val + 1, parts[n][0])
        if parts[n][1] < parts[n][0]:
            return 0
    cnt = 1
    for k in parts.keys():
        range_len = (parts[k][1] - parts[k][0] + 1)
        print(f'{k}: {parts[k]} = {range_len}')
        cnt *= range_len
    return cnt


def dfs(rules, name, index, path):
    if name == 'R':
        return 0
    if name == 'A':
        print(path)
        total = count(path)
        return total
    total = 0
    r = rules[name][index]
    op, n, val, nxt = r
    if op is not None:
        path.append((op, n, val))
        total += dfs(rules, nxt, 0, path)
        path.pop()
        if op == '<':
            op = '>'
            val = val - 1
        else:
            op = '<'
            val = val + 1
        path.append((op, n, val))
        total += dfs(rules, name, index + 1, path)
        path.pop()
    else:
        total += dfs(rules, nxt, 0, path)
    return total


def solve2(infile):
    rules, _ = get_input(infile)
    ans = dfs(rules, 'in', 0, [])
    return ans


def main():
    # print(solve1('19_test.in'))
    # print(solve1('19.in'))
    # print(solve2('19_test.in'))
    print(solve2('19.in'))


if __name__ == '__main__':
    main()
