import networkx as nx
import matplotlib.pyplot as plt


def get_input(infile):
    with open(infile) as f:
        content = f.read()
    lines = content.splitlines()
    g = nx.Graph()
    for line in lines:
        src, dsts = line.split(":", 1)
        for dst in dsts.split():
            g.add_edge(src, dst)
            g.add_edge(dst, src)
    return g


def draw_graph(graph: nx.Graph) -> None:
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(64, 64))
    nx.draw(graph, pos, with_labels=True, font_weight='bold', node_size=700)
    plt.show()


def solve(infile):
    g = get_input(infile)
    # draw_graph(g)

    # remove 3 edges
    # vnm - qpp
    # vff - rhk
    # kfr - vkp
    cut_edges = {('vnm', 'qpp'), ('rhk', 'bff'), ('vkp', 'kfr')}
    print(cut_edges)
    g.remove_edges_from(cut_edges)
    # draw_graph(g)

    comps = list(nx.connected_components(g))
    print(len(comps))
    a = len(comps[0])
    print(a)
    b = len(comps[1])
    print(b)
    return a * b


def main():
    print(solve('25.in'))


if __name__ == '__main__':
    main()
