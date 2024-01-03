import random
from collections import defaultdict


def get_input(infile):
    with open(infile) as f:
        content = f.read()
    lines = content.splitlines()
    v = defaultdict(set)
    for line in lines:
        src, dsts = line.split(":", 1)
        for dst in dsts.split():
            v[src].add(dst)
            v[dst].add(src)
    return v


# https://en.wikipedia.org/wiki/Karger%27s_algorithm
def kargers(graph):
    while True:
        V = {name: (list(v), {name}) for name, v in graph.items()}

        while len(V.keys()) > 2:
            e = random.choice(list(V.keys()))
            f = random.choice(V[e][0])

            u, v = V[e], V[f]

            for edge in v[0]:
                if edge != e and edge != f:
                    u[0].append(edge)
                    V[edge][0].remove(f)
                    V[edge][0].append(e)
            V[e] = ([d for d in u[0] if d != f], u[1] | v[1])

            del V[f]

        if len(list(V.values())[0][0]) == 3:
            parts = list(v[1] for v in V.values())
            assert len(parts) == 2
            return parts[0], parts[1]


def solve(infile):
    g = get_input(infile)
    print(g)
    cut = kargers(g)
    print(cut)
    ans = len(cut[0]) * len(cut[1])
    return ans


def main():
    print(solve('25.in'))


if __name__ == '__main__':
    main()
