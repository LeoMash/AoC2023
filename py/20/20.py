import math
from collections import deque


def get_input(infile):
    with open(infile) as f:
        content = f.read()
    lines = content.split('\n')
    broadcast_targets = []
    modules = {}
    for line in lines:
        name, dst = line.split(' -> ')
        dst = dst.split(', ')
        if name == 'broadcaster':
            broadcast_targets = dst
        else:
            t = name[0]
            name = name[1:]
            modules[name] = (t, dst)
    print(broadcast_targets)
    print(modules)
    return broadcast_targets, modules


def solve1(infile):
    broadcast_targets, modules = get_input(infile)
    # fill memory state for conjunctions
    memo_conj = {nm: {} for nm, mod in modules.items() if mod[0] == '&'}
    for name, module in modules.items():
        for outp in module[1]:
            if outp in modules and modules[outp][0] == '&':
                memo_conj[outp][name] = 0
    memo_flip = {nm: 0 for nm, mod in modules.items() if mod[0] == '%'}
    print(memo_conj)
    print(memo_flip)

    num_lo = 0
    num_hi = 0

    for _ in range(1000):
        # print('#' * 80)
        # print(memo_conj)
        # print(memo_flip)
        num_lo += 1
        q = deque()
        for tgt in broadcast_targets:
            q.append(('broadcaster', tgt, 0))

        while q:
            name_from, name, pulse = q.popleft()
            # print(f'{name_from} {pulse} -> {name}')
            if pulse:
                num_hi += 1
            else:
                num_lo += 1

            if name not in modules:
                continue

            tt, dst = modules[name]
            if tt == '%':
                # flip-flop
                if pulse == 0:
                    memo_flip[name] = 1 - memo_flip[name]
                    next_pulse = memo_flip[name]
                    for tgt in dst:
                        q.append((name, tgt, next_pulse))
                else:
                    # ignore high pulses
                    pass
            else:  # tt == '&'
                # conjunction
                memo_conj[name][name_from] = pulse
                next_pulse = 0 if all(memo_conj[name].values()) else 1
                for tgt in dst:
                    q.append((name, tgt, next_pulse))

    print(num_lo)
    print(num_hi)
    return num_lo * num_hi


def solve2(infile):
    broadcast_targets, modules = get_input(infile)
    # fill memory state for conjunctions
    memo_conj = {nm: {} for nm, mod in modules.items() if mod[0] == '&'}
    for name, module in modules.items():
        for outp in module[1]:
            if outp in modules and modules[outp][0] == '&':
                memo_conj[outp][name] = 0
    memo_flip = {nm: 0 for nm, mod in modules.items() if mod[0] == '%'}
    print(memo_conj)
    print(memo_flip)

    rx_src = [name for name, module in modules.items() if 'rx' in module[1]]
    assert len(rx_src) == 1
    rx_src = rx_src[0]
    print(rx_src)

    cycle_lengths = {}
    num_seen = {name: 0 for name, module in modules.items() if rx_src in module[1]}

    num = 0

    while True:
        num += 1
        q = deque()
        for tgt in broadcast_targets:
            q.append(('broadcaster', tgt, 0))

        while q:
            name_from, name, pulse = q.popleft()
            # print(f'{name_from} {pulse} -> {name}')
            if name not in modules:
                continue

            if name == rx_src and pulse == 1:
                num_seen[name_from] += 1
                if name_from not in cycle_lengths:
                    cycle_lengths[name_from] = num

                if all(num_seen.values()):
                    return math.lcm(*cycle_lengths.values())

            tt, dst = modules[name]
            if tt == '%':
                # flip-flop
                if pulse == 0:
                    memo_flip[name] = 1 - memo_flip[name]
                    next_pulse = memo_flip[name]
                    for tgt in dst:
                        q.append((name, tgt, next_pulse))
                else:
                    # ignore high pulses
                    pass
            else:  # tt == '&'
                # conjunction
                memo_conj[name][name_from] = pulse
                next_pulse = 0 if all(memo_conj[name].values()) else 1
                for tgt in dst:
                    q.append((name, tgt, next_pulse))


def main():
    print(solve1('20_test.in'))
    print(solve1('20.in'))
    print(solve2('20.in'))


if __name__ == '__main__':
    main()
