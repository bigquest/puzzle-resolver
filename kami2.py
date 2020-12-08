from datetime import datetime

class Graph:
    def __init__(self, nodes=dict(), edges=[], left_steps=0, depth=0):
        self.nodes = nodes
        self.edges = edges
        self.colors = len(set(nodes.values()))
        self.left_steps = left_steps
        self.depth = depth

    def connected(self, node):
        for edge in self.edges:
            if edge[0] == node:
                yield edge[1]
            elif edge[1] == node:
                yield edge[0]

    def step_colors(self, node):
        colors = {}
        for n in self.connected(node):
            color = self.nodes[n]
            if color in colors:
                colors[color] += 1
            else:
                colors[color] = 1

        return list(map(lambda x: x[0], sorted(colors.items(), key=lambda x: x[1], reverse=True)))

    def step_nodes(self):
        nodes = {}
        for n in self.nodes:
            connected_node_num = len(list(self.connected(n)))
            if self.left_steps >= self.colors and connected_node_num == 1:
                #print('skipping node {}'.format(n))
                continue
            nodes[n] = connected_node_num
        return list(map(lambda x: x[0], sorted(nodes.items(), key=lambda x: x[1], reverse=True)))[0:9]

    def color(self, node, color):
        to_merge = [node]
        to_merge += [n for n in self.connected(node) if self.nodes[n] == color]
        new_n = min(to_merge)

        new_nodes = { new_n: color }
        for node in self.nodes:
            if node not in to_merge:
                new_nodes[node] = self.nodes[node]

        new_edges = set()
        for edge in self.edges:
            if edge[0] in to_merge and edge[1] in to_merge:
                continue
            elif edge[0] in to_merge:
                new_edges.add(tuple(sorted((new_n, edge[1]))))
            elif edge[1] in to_merge:
                new_edges.add(tuple(sorted((edge[0], new_n))))
            else:
                new_edges.add(edge)

        return Graph(new_nodes, new_edges, left_steps=self.left_steps-1, depth=self.depth+1)


def solve(graph, steps, verbose=False):
    n = graph.left_steps
    #if verbose and graph.depth < 3:
    #    print('{}{}: solve graph {}'.format('\t'*graph.depth, datetime.now(), n))
    if len(graph.nodes) == 1:
        return steps

    if n == 0:
        return None

    if graph.colors > n + 1:
        return None

    for node in graph.step_nodes():
        colors = graph.step_colors(node)
        if verbose and graph.depth < 2:
            print('{}{}: solve graph node {}, {}'.format('\t'*graph.depth, datetime.now(), node, n))
        for color in colors:
            g = graph.color(node, color)
            r =  solve(g, steps + [(node, color)], verbose=verbose)
            if r:
                return r


colors = {
    "B": "Black",
    "W": "White",
    "R": "Red",
    "Y": "Yellow",
    "T": "Teal"
}

g_test = Graph(
        nodes = {
            1: "Purple",
            2: "Yellow",
            3: "Red",
            4: "Yellow",
            5: "White",
            6: "Purple",
            7: "Yellow",
            8: "Purple",
            9: "Yellow",
            10: "Red",
            11: "Purple",
            12: "White",
            13: "Purple",
            14: "Purple",
            15: "White",
            16: "Yellow",
            17: "Red",
            18: "Purple",
        },
        edges = [
            (1, 2),
            (1, 4),
            (2, 3),
            (2, 5),
            (2, 6),
            (3, 6),
            (3, 7),
            (4, 5),
            (4, 8),
            (5, 6),
            (5, 8),
            (6, 7),
            (6, 9),
            (7, 9),
            (7, 12),
            (8, 9),
            (8, 10),
            (9, 11),
            (9, 12),
            (10, 11),
            (10, 13),
            (10, 15),
            (12, 13),
            (12, 14),
            (12, 16),
            (13, 15),
            (13, 16),
            (13, 18),
            (15, 18),
            (16, 17),
            (16, 18),
            (17, 18),
        ],
        left_steps=5)

steps = solve(g_test, [])
print(steps)
assert steps == [(10, 'Purple'), (8, 'White'), (5, 'Yellow'), (2, 'Purple'), (1, 'Red')]



g = Graph(
        nodes = {
            1: "T",
            2: "Y",
            3: "Y",
            4: "Y",
            5: "Y",
            6: "Y",
            7: "Y",
            8: "Y",
            9: "B",
            10: "W",
            11: "B",
            12: "R",
            13: "R",
            14: "R",
            15: "Y",
            16: "R",
            17: "Y",
            18: "B",
            19: "Y",
            20: "R",
            21: "W",
            22: "B",
            23: "B",
            24: "Y",
            25: "B",
            26: "R",
            27: "Y",
            28: "R",
            29: "B",
            30: "R",
            31: "Y",
            32: "B",
            33: "W",
            34: "B",
            35: "B",
            36: "Y",
            37: "Y",
            38: "R",
            39: "B",
            40: "Y",
            41: "Y",
            42: "B",
            43: "B",
            44: "R",
            45: "Y",
            46: "B",
            47: "R",
            48: "Y",
            49: "R",
            50: "Y",
            51: "B",
            52: "Y",
            53: "B",
            54: "R",
            55: "R",
            56: "R",
            57: "Y",
            58: "Y",
            59: "R",
            60: "R",
        },
        edges = [
            (1, 2),
            (1, 3),
            (1, 4),
            (1, 5),
            (1, 6),
            (1, 7),
            (1, 8),
            (1, 10),
            (1, 11),
            (9, 12), (9, 13), (9, 14),
            (10, 11),
            (11, 12),
            (11, 13),
            (11, 15),
            (11, 17),
            (11, 60),
            (11, 59),
            (11, 57),
            (11, 36),
            (11, 55),
            (11, 54),
            (11, 56),
            (11, 52),
            (11, 50),
            (11, 48),
            (11, 49),
            (14, 15),
            (14, 18),
            (15, 16),
            (16, 17),
            (16, 18),
            (17, 25),
            (18, 20),
            (18, 19),
            (19, 21),
            (19, 22),
            (20, 24),
            (20, 21),
            (23, 26),
            (24, 25),
            (24, 26),
            (25, 28),
            (26, 27),
            (27, 28),
            (27, 29),
            (28, 31),
            (28, 32),
            (28, 58),
            (29, 30),
            (30, 31),
            (31, 33),
            (32, 36),
            (32, 57),
            (32, 58),
            (33, 34),
            (33, 35),
            (34, 37),
            (35, 37),
            (35, 36),
            (35, 38),
            (35, 55),
            (37, 39),
            (38, 39),
            (38, 52),
            (39, 40),
            (39, 41),
            (40, 42),
            (41, 42), (41, 43), (41, 51),
            (42, 45),
            (43, 44), (43, 47),
            (44, 45),
            (45, 46),
            (47, 48), (47, 51),
            (50, 51),
            (51, 52),
            (52, 53),
            (53, 54), (53, 55),
            (58, 59),

        ],
        left_steps=9)

steps = solve(g, [], verbose=True)
print(steps)

g = Graph(
        nodes = {
            1: "W",
            9: "B",
            11: "B",
            12: "R",
            13: "R",
            14: "R",
            15: "Y",
            16: "R",
            17: "Y",
            18: "B",
            19: "Y",
            20: "R",
            21: "W",
            22: "B",
            23: "B",
            24: "Y",
            25: "B",
            26: "R",
            27: "Y",
            28: "R",
            29: "B",
            30: "R",
            31: "Y",
            32: "B",
            33: "W",
            34: "B",
            35: "B",
            36: "Y",
            37: "Y",
            38: "R",
            39: "B",
            40: "Y",
            41: "Y",
            42: "B",
            43: "B",
            44: "R",
            45: "Y",
            46: "B",
            47: "R",
            48: "Y",
            49: "R",
            50: "Y",
            51: "B",
            52: "Y",
            53: "B",
            54: "R",
            55: "R",
            56: "R",
            57: "Y",
            58: "Y",
            59: "R",
            60: "R",
        },
        edges = [
            (1, 11),
            (9, 12), (9, 13), (9, 14),
            (11, 12),
            (11, 13),
            (11, 15),
            (11, 17),
            (11, 60),
            (11, 59),
            (11, 57),
            (11, 36),
            (11, 55),
            (11, 54),
            (11, 56),
            (11, 52),
            (11, 50),
            (11, 48),
            (11, 49),
            (14, 15),
            (14, 18),
            (15, 16),
            (16, 17),
            (16, 18),
            (17, 25),
            (18, 20),
            (18, 19),
            (19, 21),
            (19, 22),
            (20, 24),
            (20, 21),
            (23, 26),
            (24, 25),
            (24, 26),
            (25, 28),
            (26, 27),
            (27, 28),
            (27, 29),
            (28, 31),
            (28, 32),
            (28, 58),
            (29, 30),
            (30, 31),
            (31, 33),
            (32, 36),
            (32, 57),
            (32, 58),
            (33, 34),
            (33, 35),
            (34, 37),
            (35, 37),
            (35, 36),
            (35, 38),
            (35, 55),
            (37, 39),
            (38, 39),
            (38, 52),
            (39, 40),
            (39, 41),
            (40, 42),
            (41, 42), (41, 43), (41, 51),
            (42, 45),
            (43, 44), (43, 47),
            (44, 45),
            (45, 46),
            (47, 48), (47, 51),
            (50, 51),
            (51, 52),
            (52, 53),
            (53, 54), (53, 55),
            (58, 59),

        ],
        left_steps=8)

#steps = solve(g, [], verbose=True)
#print(steps)