import numpy as np
import matplotlib.pyplot as plt
import sympy


# noinspection PyPep8
# def nthtermofu(theta, n, i1, i2, i3, i4, beta, phi=0.14):
#     s1 = 2.0 * i1 * np.sin(n * phi / 2.0)
#     s2 = i2 * (np.sin(n * np.pi / 2.0 + n * phi / 2.0) - np.sin(n * np.pi / 2.0 - n * phi / 2.0))
#     s3 = i3 * (np.sin(n * np.pi + n * phi / 2.0) - np.sin(n * np.pi - n * phi / 2.0))
#     s4 = i4 * (np.sin(3.0 * n * np.pi / 2.0 + n * phi / 2.0) - np.sin(3.0 * n * np.pi / 2.0 - n * phi / 2.0))
#
#     t2 = i2 * (np.cos(n * np.pi / 2 - n * phi / 2.0) - np.cos(n * np.pi / 2.0 + n * phi / 2.0))
#     t4 = i4 * (np.cos(3.0 * n * np.pi / 2.0 - n * phi / 2.0) - np.cos(3.0 * n * np.pi / 2.0 + n * phi / 2.0))
#
#     nextsum1 = 1.0 / phi * 1.0 / (n ** 2.0) * (s1 * np.cos(n * theta) + beta * s1 * np.sin(n * theta))
#     nextsum2 = 1.0 / phi * 1.0 / (n ** 2.0) * ((s2 - beta * t2) * np.cos(n * theta) + (t2 + beta * s2) * np.sin(n * theta))
#     nextsum3 = 1.0 / phi * 1.0 / (n ** 2.0) * (s3 * np.cos(n * theta) + beta * s3 * np.sin(n * theta))
#     nextsum4 = 1.0 / phi * 1.0 / (n ** 2.0) * ((s4 - beta * t4) * np.cos(n * theta) + (t4 + beta * s4) * np.sin(n * theta))
#
#     totalsum = nextsum1 + nextsum2 + nextsum3 + nextsum4
#
#     return np.array([nextsum1, nextsum2, nextsum3, nextsum4, totalsum])
#
#
# for phival in [0.001, 0.14, 0.5, 15.0 * np.pi / 64.0]:
#     V1 = np.zeros(5, dtype=object)
#     V2 = np.zeros(5, dtype=object)
#     V3 = np.zeros(5, dtype=object)
#     V4 = np.zeros(5, dtype=object)
#
#     I1, I2, I3, I4 = sympy.symbols('I1 I2 I3 I4')
#     Beta = sympy.symbols('B')
#
#     ConstantTermEvo = []
#     BetaTermEvo = []
#     Labels = ['V1I1', 'V1I2', 'V1I3', 'V1I4', 'V2I1', 'V2I2', 'V2I3', 'V2I4', 'V3I1', 'V3I2', 'V3I3', 'V3I4', 'V4I1',
#               'V4I2', 'V4I3', 'V4I4']
#
#     for nth in range(1000):
#         V1 += nthtermofu(0, nth+1, I1, I2, I3, I4, Beta, phi=phival)
#         V2 += nthtermofu(np.pi / 2.0, nth+1, I1, I2, I3, I4, Beta, phi=phival)
#         V3 += nthtermofu(np.pi, nth+1, I1, I2, I3, I4, Beta, phi=phival)
#         V4 += nthtermofu(3.0 * np.pi / 2.0, nth+1, I1, I2, I3, I4, Beta, phi=phival)
#
#         V1I1 = sympy.expand((V2[0] - V1[0]) / I1)
#         V1I2 = sympy.expand((V2[1] - V1[1]) / I2)
#         V1I3 = sympy.expand((V2[2] - V1[2]) / I3)
#         V1I4 = sympy.expand((V2[3] - V1[3]) / I4)
#
#         V2I1 = sympy.expand((V3[0] - V2[0]) / I1)
#         V2I2 = sympy.expand((V3[1] - V2[1]) / I2)
#         V2I3 = sympy.expand((V3[2] - V2[2]) / I3)
#         V2I4 = sympy.expand((V3[3] - V2[3]) / I4)
#
#         V3I1 = sympy.expand((V4[0] - V3[0]) / I1)
#         V3I2 = sympy.expand((V4[1] - V3[1]) / I2)
#         V3I3 = sympy.expand((V4[2] - V3[2]) / I3)
#         V3I4 = sympy.expand((V4[3] - V3[3]) / I4)
#
#         V4I1 = sympy.expand((V1[0] - V4[0]) / I1)
#         V4I2 = sympy.expand((V1[1] - V4[1]) / I2)
#         V4I3 = sympy.expand((V1[2] - V4[2]) / I3)
#         V4I4 = sympy.expand((V1[3] - V4[3]) / I4)
#
#         Vals = [V1I1, V1I2, V1I3, V1I4, V2I1, V2I2, V2I3, V2I4, V3I1, V3I2, V3I3, V3I4, V4I1, V4I2, V4I3, V4I4]
#         Xs = np.array([value.subs(Beta, 0) for value in Vals])
#         Ys = np.array([(Vals[index] - Xs[index]).subs(Beta, 1) for index in range(len(Vals))])
#
#         ConstantTermEvo.append(Xs)
#         BetaTermEvo.append(Ys)
#
#         # plt.scatter(Xs, Ys, c=[(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0),
#         #                        (1, 0, 1), (0, 1, 1), (1, 1, 1), (1, 0.5, 0),
#         #                        (1, 0, 0.5), (0.5, 1, 0), (0, 1, 0.5), (0.5, 0, 1),
#         #                        (0, 0.5, 1), (1, 0.5, 0.5), (0.5, 1, 0.5), (0.5, 0.5, 1)])
#
#     a = (-1, np.pi / 4.0)
#     b = (1, np.pi / 4.0)
#     c = (0.35, -1 * np.pi / 4.0)
#     d = (-0.35, -1 * np.pi / 4.0)
#     PLPoints = [a, b, c, d]
#
#     ConstantTermEvo = np.array(ConstantTermEvo).T
#     BetaTermEvo = np.array(BetaTermEvo).T
#     colors = ['c', 'g', 'r', 'k']
#     for vindex in range(4):
#         for iindex in range(4):
#             plt.plot(ConstantTermEvo[iindex + vindex * 4], BetaTermEvo[iindex + vindex * 4], c=colors[iindex],
#                      label='{} Term'.format(Labels[iindex + vindex * 4]))
#             plt.scatter(ConstantTermEvo[iindex + vindex * 4][0], BetaTermEvo[iindex + vindex * 4][0],
#                         c=[colors[iindex]])
#             if np.abs(PLPoints[iindex][0]) == 1:
#                 plt.hlines(PLPoints[iindex][1], PLPoints[iindex][0] * 5, 0, colors=colors[iindex])
#             else:
#                 plt.scatter(PLPoints[iindex][0], PLPoints[iindex][1], c=[colors[iindex]])
#         plt.legend(loc='best')
#         plt.title('{} to {} Evolution for Phi of {} rad'.format(Labels[vindex * 4], Labels[vindex * 4 + 3], phival))
#         plt.xlabel('Constant Term')
#         plt.ylabel('Beta Term')
#         plt.savefig("/home/andreec/Desktop/Ryan's Shits on Andree's Computer/EP3/Parish-Littlewood Model/Propogation {}"
#                     " to {} at {} rad.png".format(Labels[vindex * 4], Labels[vindex * 4 + 3], phival))
#         plt.clf()
#         plt.cla()
#
#         PLPoints = np.roll(PLPoints, 1, axis=0)
#
#     print('Phi value of {}:'.format(phival))
#     print('\nTerm by Term for Voltage 1:')
#     print(V2[0] - V1[0])
#     print(V2[1] - V1[1])
#     print(V2[2] - V1[2])
#     print(V2[3] - V1[3])
#     print('\nTotal for Voltage 1:')
#     print(V2[4] - V1[4])
#
#     print('\nTerm by Term for Voltage 2:')
#     print(V3[0] - V2[0])
#     print(V3[1] - V2[1])
#     print(V3[2] - V2[2])
#     print(V3[3] - V2[3])
#     print('\nTotal for Voltage 2:')
#     print(V3[4] - V2[4])
#
#     print('\nTerm by Term for Voltage 3:')
#     print(V4[0] - V3[0])
#     print(V4[1] - V3[1])
#     print(V4[2] - V3[2])
#     print(V4[3] - V3[3])
#     print('\nTotal for Voltage 3:')
#     print(V4[4] - V3[4])
#
#     print('\nTerm by Term for Voltage 4:')
#     print(V1[0] - V4[0])
#     print(V1[1] - V4[1])
#     print(V1[2] - V4[2])
#     print(V1[3] - V4[3])
#     print('\nTotal for Voltage 4:')
#     print(V1[4] - V4[4])
#     print()

V = 0

# directedgraph = {1: [2],
#                  2: [3],
#                  3: [],
#                  4: [1]}
#
# undirectedgraph = {1: [2, 4],
#                    2: [1, 3],
#                    3: [2],
#                    4: [1]}
#
#
# def generate_edges(graph):
#     edges = []
#     for node in graph:
#         for neighbor in graph[node]:
#             edges.append((node, neighbor))
#     return edges
#
#
# print(generate_edges(directedgraph))
# print(generate_edges(undirectedgraph))
# print()

A = 0

########################################################################################################################
#  Part 1: Graph Class Definition
########################################################################################################################


class SemiDirectedGraph(object):
    def __init__(self, graph_dict=None, directed_dict=None):
        """
        Initializes a Graph object.
        If no graph or None is given, an empty graph will be used.
        Likewise with directed graph.
        """
        if graph_dict is None:
            graph_dict = {}
        if directed_dict is None:
            directed_dict = {}
        self.__graph_dict = graph_dict
        self.__directed_dict = directed_dict

    def vertices(self):
        """Returns the vertices of a graph"""
        return list(self.__graph_dict.keys())

    def edges_undirected(self):
        """ Returns the edges of the graph """
        return self.__generate_edges_undirected()

    def edges_directed(self):
        """ Returns the edges of the directed graph """
        return self.__generate_edges_directed()

    def add_vertex(self, vertex):
        """
        If the vertex "vertex" is not in self.__graph_dict,
        a key "vertex" with an empty list as a value is added to both dictionaries.
        Otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []
            self.__directed_dict[vertex] = []

    def add_edge_undirected(self, edge):
        """
        Assumes that edge is of type set, tuple or list.
        Note: Between two vertices can be multiple edges!
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        direction = (vertex1 > vertex2)

        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
            if direction:
                self.__directed_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]
            if direction:
                self.__directed_dict[vertex1] = vertex2

        if vertex2 in self.__graph_dict:
            self.__graph_dict[vertex2].append(vertex1)
            if not direction:
                self.__directed_dict[vertex2].append(vertex1)
        else:
            self.__graph_dict[vertex2] = [vertex1]
            if not direction:
                self.__directed_dict[vertex2] = vertex1

    def add_edge_directed(self, start_vertex, end_vertex):
        """
        Note: Between two vertices can be multiple edges!
        """
        if start_vertex in self.__graph_dict:
            self.__graph_dict[start_vertex].append(end_vertex)
            self.__directed_dict[start_vertex].append(end_vertex)
        else:
            self.__graph_dict[start_vertex] = [end_vertex]
            self.__directed_dict[start_vertex] = end_vertex

    def __generate_edges_undirected(self):
        """
        A static method generating the edges of the graph "graph".
        Edges are represented as sets with one (a loop back to the vertex) or two vertices.
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                edges.append({vertex, neighbour})
        return edges

    def __generate_edges_directed(self):
        """
        A static method generating the edges of the graph "graph".
        Edges are represented as sets with one (a loop back to the vertex) or two vertices.
        Order is important here, so use tuples instead of sets
        """
        edges = []
        for vertex in self.__directed_dict:
            for neighbour in self.__directed_dict[vertex]:
                edges.append((vertex, neighbour))
        return edges

    def get_graph_dict(self):
        return self.__graph_dict

    def get_directed_dict(self):
        return self.__directed_dict

    def find_path(self, start_vertex, end_vertex, path=None):
        """
        find a path from start_vertex to end_vertex in graph
        """
        if path is None:
            path = []
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex,
                                               end_vertex,
                                               path)
                if extended_path:
                    return extended_path
        return None


########################################################################################################################
# Generate all voltage drops used in the 1 by 1 system
########################################################################################################################

a, b, c, d = sympy.symbols('a b c d')
IL2, IH1, IL1, IH2 = sympy.symbols('Ig IH1 IL1 IH-1')

Voltages = np.matmul(np.array([[a, b, c, d], [d, a, b, c], [b, c, d, a]]), np.array([[IL2], [IH1], [IL1], [IH2]]))
Voltages[0][0] = sympy.collect(sympy.expand(Voltages[0][0].subs(IL2, -1 * (IH1 + IL1 + IH2))), [IH1, IL1, IH2])
Voltages[1][0] = sympy.collect(sympy.expand(Voltages[1][0].subs(IL2, -1 * (IH1 + IL1 + IH2))), [IH1, IL1, IH2])
Voltages[2][0] = sympy.collect(sympy.expand(Voltages[2][0].subs(IL2, -1 * (IH1 + IL1 + IH2))), [IH1, IL1, IH2])

########################################################################################################################
# Construction for 1 by 1 System
########################################################################################################################

print('For 1x1 System:')

# Construct both the graph and the directed graph for the system
One_by_one = {1: [2, 4],
              2: [1, 3],
              3: [2],
              4: [1]}
One_by_one_d = {1: [2],
                2: [3],
                3: [],
                4: [1]}

# Instantiate the Graph object using the graph and directed graph created above
One_by_one_graph = SemiDirectedGraph(One_by_one, One_by_one_d)

# Generate all voltage paths
Path_List = []
Voltage_Vertices = [2, 3, 4]
for Vertex in Voltage_Vertices:
    Path_List.append(One_by_one_graph.find_path(Vertex, 1))

# Generate all the directed graphs paths and associate each with a voltage drop
Directed_Edges = One_by_one_graph.edges_directed()
Cell_Voltage_Drops = {Directed_Edges[0]: Voltages[0],
                      Directed_Edges[1]: Voltages[1],
                      Directed_Edges[2]: Voltages[2]}

# Walk through each voltage path and calculate the voltage of each
Final_Voltages = []
for Path in Path_List:
    Path_Voltage = 0
    for Segment in range(len(Path)-1):
        # If the path is in the direction of the directed path, add the voltage
        if (Path[Segment], Path[Segment+1]) in Directed_Edges:
            Path_Voltage = Path_Voltage + Cell_Voltage_Drops[(Path[Segment], Path[Segment+1])][0]
        # If the path is in the opposite direction of the directed path, subtract the voltage
        elif (Path[Segment+1], Path[Segment]) in Directed_Edges:
            Path_Voltage = Path_Voltage - Cell_Voltage_Drops[(Path[Segment+1], Path[Segment])][0]
    Final_Voltages.append(Path_Voltage)

# Collect all like terms in the final voltages
Final_Voltages[0] = sympy.collect(sympy.expand(Final_Voltages[0]), [IH1, IL1, IH2])
Final_Voltages[1] = sympy.collect(sympy.expand(Final_Voltages[1]), [IH1, IL1, IH2])
Final_Voltages[2] = sympy.collect(sympy.expand(Final_Voltages[2]), [IH1, IL1, IH2])

# Print the voltages in a coherent manner
Voltage_List = ['VH1:\t', 'VL1:\t', 'VH-1:\t']
for Index in range(len(Final_Voltages)):
    print(Voltage_List[Index] + str(Final_Voltages[Index]))

# Rewrite all the voltage equations using an impedance matrix
ZMatrx = np.array([[Final_Voltages[0].coeff(IH1, 1), Final_Voltages[0].coeff(IH2, 1), Final_Voltages[0].coeff(IL1, 1)],
                   [Final_Voltages[2].coeff(IH1, 1), Final_Voltages[2].coeff(IH2, 1), Final_Voltages[2].coeff(IL1, 1)],
                   [Final_Voltages[1].coeff(IH1, 1), Final_Voltages[1].coeff(IH2, 1), Final_Voltages[1].coeff(IL1, 1)]])

# Print the impedance matrix
print()
print(np.array2string(ZMatrx, separator=','))
# noinspection PyTypeChecker
# np.savetxt("/home/andreec/Desktop/Ryan's Shits on Andree's Computer/EP3/Impedance1by1.txt", ZMatrx, fmt='%-25s',
#            delimiter='\t')

########################################################################################################################

a, b, c, d = sympy.symbols('a b c d')
IL2, IH1, IH2, IL1, IH4, IH3, IA = sympy.symbols('Ig IH1 IH2 IL1 IH-2 IH-1 Ia')

Voltages1 = np.matmul(np.array([[a, b, c, d], [d, a, b, c], [b, c, d, a]]), np.array([[IL2], [IH1], [IA], [IH3]]))
Voltages1[0][0] = sympy.collect(sympy.expand(Voltages1[0][0].subs(IL2, -1 * (IH1 + IA + IH3))), [IH1, IA, IH3])
Voltages1[1][0] = sympy.collect(sympy.expand(Voltages1[1][0].subs(IL2, -1 * (IH1 + IA + IH3))), [IH1, IA, IH3])
Voltages1[2][0] = sympy.collect(sympy.expand(Voltages1[2][0].subs(IL2, -1 * (IH1 + IA + IH3))), [IH1, IA, IH3])
Voltages1[0][0] = sympy.collect(sympy.expand(Voltages1[0][0].subs(IA, (IH2 + IL1 + IH4))), [IH1, IH2, IH3, IH4, IL1])
Voltages1[1][0] = sympy.collect(sympy.expand(Voltages1[1][0].subs(IA, (IH2 + IL1 + IH4))), [IH1, IH2, IH3, IH4, IL1])
Voltages1[2][0] = sympy.collect(sympy.expand(Voltages1[2][0].subs(IA, (IH2 + IL1 + IH4))), [IH1, IH2, IH3, IH4, IL1])

Voltages2 = np.matmul(np.array([[a, b, c, d], [d, a, b, c], [b, c, d, a]]), np.array([[-1 * IA], [IH2], [IL1], [IH4]]))
Voltages2[0][0] = sympy.collect(sympy.expand(Voltages2[0][0].subs(IA, (IH2 + IL1 + IH4))), [IH2, IH4, IL1])
Voltages2[1][0] = sympy.collect(sympy.expand(Voltages2[1][0].subs(IA, (IH2 + IL1 + IH4))), [IH2, IH4, IL1])
Voltages2[2][0] = sympy.collect(sympy.expand(Voltages2[2][0].subs(IA, (IH2 + IL1 + IH4))), [IH2, IH4, IL1])

########################################################################################################################

print('\n\nFor 1x2 System:')

One_by_Two = {1: [2, 7],
              2: [1, 3],
              3: [2, 4, 6],
              4: [3, 5],
              5: [4],
              6: [3],
              7: [1]}
One_by_Two_D = {1: [2],
                2: [3],
                3: [4],
                4: [5],
                5: [],
                6: [3],
                7: [1]}

One_by_Two_Graph = SemiDirectedGraph(One_by_Two, One_by_Two_D)
One_by_Two_Vertices = One_by_Two_Graph.vertices()

Path_List = []
Voltage_Vertices = [2, 4, 5, 6, 7]
for Vertex in Voltage_Vertices:
    Path_List.append(One_by_Two_Graph.find_path(Vertex, 1))

Directed_Edges = One_by_Two_Graph.edges_directed()
Cell_Voltage_Drops = {Directed_Edges[0]: Voltages1[0],
                      Directed_Edges[1]: Voltages1[1],
                      Directed_Edges[2]: Voltages2[0],
                      Directed_Edges[3]: Voltages2[1],
                      Directed_Edges[4]: Voltages2[2],
                      Directed_Edges[5]: Voltages1[2]}
Final_Voltages = []
for Path in Path_List:
    Path_Voltage = 0
    for Segment in range(len(Path)-1):
        if (Path[Segment], Path[Segment+1]) in Directed_Edges:
            Path_Voltage = Path_Voltage + Cell_Voltage_Drops[(Path[Segment], Path[Segment+1])][0]
        elif (Path[Segment+1], Path[Segment]) in Directed_Edges:
            Path_Voltage = Path_Voltage - Cell_Voltage_Drops[(Path[Segment+1], Path[Segment])][0]
    Final_Voltages.append(Path_Voltage)

Final_Voltages[0] = sympy.collect(sympy.expand(Final_Voltages[0]), [IH1, IH2, IH3, IH4, IL1])
Final_Voltages[1] = sympy.collect(sympy.expand(Final_Voltages[1]), [IH1, IH2, IH3, IH4, IL1])
Final_Voltages[2] = sympy.collect(sympy.expand(Final_Voltages[2]), [IH1, IH2, IH3, IH4, IL1])
Final_Voltages[3] = sympy.collect(sympy.expand(Final_Voltages[3]), [IH1, IH2, IH3, IH4, IL1])
Final_Voltages[4] = sympy.collect(sympy.expand(Final_Voltages[4]), [IH1, IH2, IH3, IH4, IL1])

Voltage_List = ['VH1:\t', 'VH2:\t', 'VL1:\t', 'VH-2:\t', 'VH-1:\t']
for Index in range(len(Final_Voltages)):
    print(Voltage_List[Index] + str(Final_Voltages[Index]))

ZMatrx = np.array([[Final_Voltages[0].coeff(IH1, 1), Final_Voltages[0].coeff(IH2, 1), Final_Voltages[0].coeff(IH3, 1),
                    Final_Voltages[0].coeff(IH4, 1), Final_Voltages[0].coeff(IL1, 1)],
                   [Final_Voltages[1].coeff(IH1, 1), Final_Voltages[1].coeff(IH2, 1), Final_Voltages[1].coeff(IH3, 1),
                    Final_Voltages[1].coeff(IH4, 1), Final_Voltages[1].coeff(IL1, 1)],
                   [Final_Voltages[4].coeff(IH1, 1), Final_Voltages[4].coeff(IH2, 1), Final_Voltages[4].coeff(IH3, 1),
                    Final_Voltages[4].coeff(IH4, 1), Final_Voltages[4].coeff(IL1, 1)],
                   [Final_Voltages[3].coeff(IH1, 1), Final_Voltages[3].coeff(IH2, 1), Final_Voltages[3].coeff(IH3, 1),
                    Final_Voltages[3].coeff(IH4, 1), Final_Voltages[3].coeff(IL1, 1)],
                   [Final_Voltages[2].coeff(IH1, 1), Final_Voltages[2].coeff(IH2, 1), Final_Voltages[2].coeff(IH3, 1),
                    Final_Voltages[2].coeff(IH4, 1), Final_Voltages[2].coeff(IL1, 1)]])

print()
print(np.array2string(ZMatrx, separator=','))
# noinspection PyTypeChecker
# np.savetxt("/home/andreec/Desktop/Ryan's Shits on Andree's Computer/EP3/Impedance1by2.txt", ZMatrx, fmt='%-25s',
#            delimiter='\t')

########################################################################################################################

a, b, c, d = sympy.symbols('a b c d')
IH1, IH2, IH3, IH4, IL1, IL2, IL3, IL4, IA, IB = sympy.symbols('IH1 IH2 IH-1 IH-2 IL1 IL2 Ig IL-2 Ia Ib')

Voltages1 = np.matmul(np.array([[a, b, c, d], [d, a, b, c], [b, c, d, a]]), np.array([[IL3], [IH1], [IA], [IB]]))
Voltages2 = np.matmul(np.array([[a, b, c, d], [d, a, b, c], [b, c, d, a]]), np.array([[-1 * IA], [IH2], [IL1], [IL2]]))
Voltages3 = np.matmul(np.array([[a, b, c, d], [d, a, b, c], [b, c, d, a]]), np.array([[IL4], [-1 * IB], [IH4], [IH3]]))
Voltages4 = np.matmul(np.array([[d, a, b, c], [b, c, d, a]]), np.array([[-1 * IH4], [-1 * IL2], [IL2], [IH4]]))

Voltages3[0][0] = sympy.collect(sympy.expand(Voltages3[0][0].subs(IB, (IL4 + IH4 + IH3))), [IL4, IH4, IH3])
Voltages3[1][0] = sympy.collect(sympy.expand(Voltages3[1][0].subs(IB, (IL4 + IH4 + IH3))), [IL4, IH4, IH3])
Voltages3[2][0] = sympy.collect(sympy.expand(Voltages3[2][0].subs(IB, (IL4 + IH4 + IH3))), [IL4, IH4, IH3])

Voltages2[0][0] = sympy.collect(sympy.expand(Voltages2[0][0].subs(IA, (IH2 + IL1 + IL2))), [IH2, IL1, IL2])
Voltages2[1][0] = sympy.collect(sympy.expand(Voltages2[1][0].subs(IA, (IH2 + IL1 + IL2))), [IH2, IL1, IL2])
Voltages2[2][0] = sympy.collect(sympy.expand(Voltages2[2][0].subs(IA, (IH2 + IL1 + IL2))), [IH2, IL1, IL2])

Voltages1[0][0] = sympy.collect(sympy.expand(Voltages1[0][0].subs(IL3, -(IH1 + IA + IB))), [IH1, IA, IB])
Voltages1[1][0] = sympy.collect(sympy.expand(Voltages1[1][0].subs(IL3, -(IH1 + IA + IB))), [IH1, IA, IB])
Voltages1[2][0] = sympy.collect(sympy.expand(Voltages1[2][0].subs(IL3, -(IH1 + IA + IB))), [IH1, IA, IB])
Voltages1[0][0] = sympy.collect(sympy.expand(Voltages1[0][0].subs(IB, (IL4 + IH4 + IH3))), [IH1, IB, IL4, IH4, IH3])
Voltages1[1][0] = sympy.collect(sympy.expand(Voltages1[1][0].subs(IB, (IL4 + IH4 + IH3))), [IH1, IB, IL4, IH4, IH3])
Voltages1[2][0] = sympy.collect(sympy.expand(Voltages1[2][0].subs(IB, (IL4 + IH4 + IH3))), [IH1, IB, IL4, IH4, IH3])
Voltages1[0][0] = sympy.collect(sympy.expand(Voltages1[0][0].subs(IA, (IH2 + IL1 + IL2))),
                                [IH1, IL4, IH4, IH3, IH2, IL1, IL2])
Voltages1[1][0] = sympy.collect(sympy.expand(Voltages1[1][0].subs(IA, (IH2 + IL1 + IL2))),
                                [IH1, IL4, IH4, IH3, IH2, IL1, IL2])
Voltages1[2][0] = sympy.collect(sympy.expand(Voltages1[2][0].subs(IA, (IH2 + IL1 + IL2))),
                                [IH1, IL4, IH4, IH3, IH2, IL1, IL2])

########################################################################################################################

print('\n\nFor 2x2 System:')
Two_by_Two = {1: [2, 6],
              2: [1, 3],
              3: [2, 4, 7],
              4: [3, 5],
              5: [4],
              6: [1, 8, 9],
              7: [3, 10],
              8: [6, 11],
              9: [6, 12],
              10: [7],
              11: [8],
              12: [9]}
Two_by_Two_D = {1: [2],
                2: [3],
                3: [4],
                4: [5],
                5: [],
                6: [1, 9],
                7: [3, 10],
                8: [6],
                9: [],
                10: [],
                11: [8],
                12: [9]}

Two_by_Two_Graph = SemiDirectedGraph(Two_by_Two, Two_by_Two_D)

Path_List = []
Voltage_Vertices = [2, 4, 11, 12, 5, 10, 8]
for Vertex in Voltage_Vertices:
    Path_List.append(Two_by_Two_Graph.find_path(Vertex, 1))

Directed_Edges = Two_by_Two_Graph.edges_directed()
Cell_Voltage_Drops = {Directed_Edges[0]: Voltages1[0],
                      Directed_Edges[1]: Voltages1[1],
                      Directed_Edges[2]: Voltages2[0],
                      Directed_Edges[3]: Voltages2[1],
                      Directed_Edges[4]: Voltages1[2],
                      Directed_Edges[5]: Voltages3[1],
                      Directed_Edges[6]: Voltages2[2],
                      Directed_Edges[7]: Voltages4[0],
                      Directed_Edges[8]: Voltages3[0],
                      Directed_Edges[9]: Voltages3[2],
                      Directed_Edges[10]: Voltages4[1]}
Final_Voltages = []
for Path in Path_List:
    Path_Voltage = 0
    for Segment in range(len(Path)-1):
        if (Path[Segment], Path[Segment+1]) in Directed_Edges:
            Path_Voltage = Path_Voltage + Cell_Voltage_Drops[(Path[Segment], Path[Segment+1])][0]
        elif (Path[Segment+1], Path[Segment]) in Directed_Edges:
            Path_Voltage = Path_Voltage - Cell_Voltage_Drops[(Path[Segment+1], Path[Segment])][0]
    Final_Voltages.append(Path_Voltage)

for Index in range(len(Final_Voltages)):
    Final_Voltages[Index] = sympy.collect(sympy.expand(Final_Voltages[Index]), [IH1, IL4, IH4, IH3, IH2, IL1, IL2])

Voltage_List = ['VH1:\t', 'VH2:\t', 'VH-1:\t', 'VH-2:\t', 'VL1:\t', 'VL2:\t', 'VL-2:\t']
for Index in range(len(Final_Voltages)):
    print(Voltage_List[Index] + str(Final_Voltages[Index]))

ZMatrx = np.array([[Final_Voltages[0].coeff(IH1, 1), Final_Voltages[0].coeff(IH2, 1), Final_Voltages[0].coeff(IH3, 1),
                    Final_Voltages[0].coeff(IH4, 1), Final_Voltages[0].coeff(IL1, 1), Final_Voltages[0].coeff(IL2, 1),
                    Final_Voltages[0].coeff(IL4, 1)],
                   [Final_Voltages[1].coeff(IH1, 1), Final_Voltages[1].coeff(IH2, 1), Final_Voltages[1].coeff(IH3, 1),
                    Final_Voltages[1].coeff(IH4, 1), Final_Voltages[1].coeff(IL1, 1), Final_Voltages[1].coeff(IL2, 1),
                    Final_Voltages[1].coeff(IL4, 1)],
                   [Final_Voltages[2].coeff(IH1, 1), Final_Voltages[2].coeff(IH2, 1), Final_Voltages[2].coeff(IH3, 1),
                    Final_Voltages[2].coeff(IH4, 1), Final_Voltages[2].coeff(IL1, 1), Final_Voltages[2].coeff(IL2, 1),
                    Final_Voltages[2].coeff(IL4, 1)],
                   [Final_Voltages[3].coeff(IH1, 1), Final_Voltages[3].coeff(IH2, 1), Final_Voltages[3].coeff(IH3, 1),
                    Final_Voltages[3].coeff(IH4, 1), Final_Voltages[3].coeff(IL1, 1), Final_Voltages[3].coeff(IL2, 1),
                    Final_Voltages[3].coeff(IL4, 1)],
                   [Final_Voltages[4].coeff(IH1, 1), Final_Voltages[4].coeff(IH2, 1), Final_Voltages[4].coeff(IH3, 1),
                    Final_Voltages[4].coeff(IH4, 1), Final_Voltages[4].coeff(IL1, 1), Final_Voltages[4].coeff(IL2, 1),
                    Final_Voltages[4].coeff(IL4, 1)],
                   [Final_Voltages[5].coeff(IH1, 1), Final_Voltages[5].coeff(IH2, 1), Final_Voltages[5].coeff(IH3, 1),
                    Final_Voltages[5].coeff(IH4, 1), Final_Voltages[5].coeff(IL1, 1), Final_Voltages[5].coeff(IL2, 1),
                    Final_Voltages[5].coeff(IL4, 1)],
                   [Final_Voltages[6].coeff(IH1, 1), Final_Voltages[6].coeff(IH2, 1), Final_Voltages[6].coeff(IH3, 1),
                    Final_Voltages[6].coeff(IH4, 1), Final_Voltages[6].coeff(IL1, 1), Final_Voltages[6].coeff(IL2, 1),
                    Final_Voltages[6].coeff(IL4, 1)]])

print()
print(np.array2string(ZMatrx, separator=','))
# noinspection PyTypeChecker
# np.savetxt("/home/andreec/Desktop/Ryan's Shits on Andree's Computer/EP3/Impedance2by2.txt", ZMatrx, fmt='%-25s',
#            delimiter='\t')

########################################################################################################################


class Unit:
    def __init__(self, cell_type=2):
        if type(cell_type) is int:
            if cell_type in (1, 2):
                self.__cell_type = cell_type
        elif type(cell_type) is not int or cell_type not in (1, 2):
            print('Invalid value for cell type given.')
            print('Cell type defaulting to 2.')
            self.__cell_type = 2
        self.__currents = [0, 0, 0, 0]
        self.__voltage_drops = [0, 0, None, 0]

    def add_input_current(self, new_current=0, position=0):
        if type(position) is int:
            if self.__cell_type == 1 and position in [0, 1, 2, 3]:
                self.__currents[position] = new_current
                return True
            elif self.__cell_type == 2 and position in [2, 3]:
                self.__currents[position] = new_current
                return True
        print('Invalid values given.')
        print('Aborting operation.')
        return False

    def __find_remaining_currents(self):
        if self.__cell_type == 1:
            if self.__currents.count(0) == 1:
                self.__currents[self.__currents.index(0)] = -1 * sum(self.__currents)
                return True
            print('Missing an argument for the cell type.')
            return False
        elif self.__cell_type == 2:
            if self.__currents[0] == 0 and self.__currents[1] == 0 and self.__currents.count(0) == 2:
                self.__currents[0] = -1 * self.__currents[3]
                self.__currents[1] = -1 * self.__currents[2]
                return True
            print('Invalid number of current arguments given for cell type.')
            return False

    def calculate_voltages(self):
        if self.__cell_type == 1:
            if self.__find_remaining_currents():
                temp_voltages = np.matmul(np.array([[a, b, c, d], [d, a, b, c], [b, c, d, a]]),
                                          np.array(self.__currents))
                self.__voltage_drops[0] = temp_voltages[0]
                self.__voltage_drops[1] = temp_voltages[1]
                self.__voltage_drops[3] = temp_voltages[2]
                return True
            print('Trouble calculating the remaining currents.')
            print('Please check that all necessary currents have been inputted.')
            return False
        if self.__cell_type == 2:
            if self.__find_remaining_currents():
                temp_voltages = np.matmul(np.array([[d, a, b, c], [b, c, d, a]]),
                                          np.array(self.__currents))
                self.__voltage_drops[0] = None
                self.__voltage_drops[1] = temp_voltages[0]
                self.__voltage_drops[3] = temp_voltages[1]
                return True
            print('Trouble calculating the remaining currents.')
            print('Please check that all necessary currents have been inputted.')
            return False

    def get_v1(self):
        return self.__voltage_drops[0]

    def get_v2(self):
        return self.__voltage_drops[1]

    def get_v4(self):
        return self.__voltage_drops[3]

    def get_i1(self):
        return self.__currents[0]

    def get_i2(self):
        return self.__currents[1]

    def get_i3(self):
        return self.__currents[2]

    def get_i4(self):
        return self.__currents[3]

    def get_cell_type(self):
        return self.__cell_type


class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def find_path(self, start_vertex, end_vertex, path=None):
        """ find a path from start_vertex to end_vertex
            in graph """
        if path == None:
            path = []
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex,
                                               end_vertex,
                                               path)
                if extended_path:
                    return extended_path
        return None


########################################################################################################################

def Network_Analysis(Dimensions):
    Network = np.zeros(Dimensions).tolist()
    Network_Graph = {}
    # Network_Directed_Graph = {}

    for IndexR in range(Dimensions[0]):
        for IndexC in range(Dimensions[1]):
            if IndexR == 0 or IndexC == 0:
                Network[IndexR][IndexC] = Unit(cell_type=1)
                for Direction in range(4):
                    if (IndexR, IndexC, Direction) not in Network_Graph.keys():
                        if Direction == 0:
                            Network_Graph[(IndexR, IndexC, Direction)] = [(IndexR, IndexC, 1), (IndexR, IndexC, 3)]
                            if not IndexC == 0 and IndexR == 0:
                                Network_Graph[(IndexR, IndexC, Direction)].append((IndexR, IndexC - 1, 2))
                        elif Direction == 1:
                            Network_Graph[(IndexR, IndexC, Direction)] = [(IndexR, IndexC, 0), (IndexR, IndexC, 2)]
                            if IndexC == 0 and not IndexR == 0:
                                Network_Graph[(IndexR, IndexC, Direction)].append((IndexR - 1, IndexC, 3))
                        elif Direction == 2:
                            Network_Graph[(IndexR, IndexC, Direction)] = [(IndexR, IndexC, 1)]
                            if not IndexC == Dimensions[1] - 1:
                                Network_Graph[(IndexR, IndexC, Direction)].append((IndexR, IndexC + 1, 0))
                        elif Direction == 3:
                            Network_Graph[(IndexR, IndexC, Direction)] = [(IndexR, IndexC, 0)]
                            if not IndexR == Dimensions[0] - 1:
                                Network_Graph[(IndexR, IndexC, Direction)].append((IndexR + 1, IndexC, 1))
                    elif (IndexR, IndexC, Direction) in Network_Graph.keys():
                        if Direction == 0:
                            Network_Graph[(IndexR, IndexC, Direction)].append((IndexR, IndexC, 1))
                            Network_Graph[(IndexR, IndexC, Direction)].append((IndexR, IndexC, 2))
                            if not IndexC == 0 and IndexR == 0:
                                Network_Graph[(IndexR, IndexC, Direction)].append((IndexR, IndexC - 1, 2))
                        elif Direction == 1:
                            Network_Graph[(IndexR, IndexC, Direction)].append((IndexR, IndexC, 0))
                            Network_Graph[(IndexR, IndexC, Direction)].append((IndexR, IndexC, 2))
                            if IndexC == 0 and not IndexR == 0:
                                Network_Graph[(IndexR, IndexC, Direction)].append((IndexR - 1, IndexC, 3))
                        elif Direction == 2:
                            Network_Graph[(IndexR, IndexC, Direction)].append((IndexR, IndexC, 1))
                            if not IndexC == Dimensions[1] - 1:
                                Network_Graph[(IndexR, IndexC, Direction)].append((IndexR, IndexC + 1, 0))
                        elif Direction == 3:
                            Network_Graph[(IndexR, IndexC, Direction)].append((IndexR, IndexC, 0))
                            if not IndexR == Dimensions[0] - 1:
                                Network_Graph[(IndexR, IndexC, Direction)].append((IndexR + 1, IndexC, 1))
            else:
                Network[IndexR][IndexC] = Unit(cell_type=2)
                for Direction in range(4):
                    if (IndexR, IndexC, Direction) not in Network_Graph.keys():
                        if Direction == 0:
                            Network_Graph[(IndexR, IndexC, Direction)] = [(IndexR, IndexC, 3), (IndexR, IndexC - 1, 2)]
                        elif Direction == 1:
                            Network_Graph[(IndexR, IndexC, Direction)] = [(IndexR, IndexC, 2), (IndexR - 1, IndexC, 3)]
                        elif Direction == 2:
                            Network_Graph[(IndexR, IndexC, Direction)] = [(IndexR, IndexC, 1)]
                            if not IndexC == Dimensions[1] - 1:
                                Network_Graph[(IndexR, IndexC, Direction)].append((IndexR, IndexC + 1, 0))
                        elif Direction == 3:
                            Network_Graph[(IndexR, IndexC, Direction)] = [(IndexR, IndexC, 0)]
                            if not IndexR == Dimensions[0] - 1:
                                Network_Graph[(IndexR, IndexC, Direction)].append((IndexR + 1, IndexC, 1))
                    elif (IndexR, IndexC, Direction) in Network_Graph.keys():
                        if Direction == 0:
                            Network_Graph[(IndexR, IndexC, Direction)].append((IndexR, IndexC, 3))
                            Network_Graph[(IndexR, IndexC, Direction)].append((IndexR, IndexC - 1, 2))
                        elif Direction == 1:
                            Network_Graph[(IndexR, IndexC, Direction)].append((IndexR, IndexC, 2))
                            Network_Graph[(IndexR, IndexC, Direction)].append((IndexR - 1, IndexC, 3))
                        elif Direction == 2:
                            Network_Graph[(IndexR, IndexC, Direction)].append((IndexR, IndexC, 1))
                            if not IndexC == Dimensions[1] - 1:
                                Network_Graph[(IndexR, IndexC, Direction)].append((IndexR, IndexC + 1, 0))
                        elif Direction == 3:
                            Network_Graph[(IndexR, IndexC, Direction)].append((IndexR, IndexC, 0))
                            if not IndexR == Dimensions[0] - 1:
                                Network_Graph[(IndexR, IndexC, Direction)].append((IndexR + 1, IndexC, 1))

    HallCurrentList = []
    LongCurrentList = []

    for IndexR in range(Dimensions[0]):
        TempString = "IL" + str(IndexR + 1)
        LongCurrentList.append(sympy.symbols(TempString))
    for IndexR in range(1, Dimensions[0]):
        TempString = 'IL' + str(-1 * IndexR - 1)
        LongCurrentList.append(sympy.symbols(TempString))

    for IndexC in range(Dimensions[1]):
        TempString = 'IH' + str(IndexC + 1)
        HallCurrentList.append(sympy.symbols(TempString))
    for IndexC in range(Dimensions[1]):
        TempString = 'IH' + str(-1 * IndexC - 1)
        HallCurrentList.append(sympy.symbols(TempString))

    for IndexR in range(Dimensions[0]-1, -1, -1):
        for IndexC in range(Dimensions[1]-1, -1, -1):
            if IndexC == Dimensions[1] - 1 and IndexR == Dimensions[0] - 1 and not IndexC == 0 and not IndexR == 0:
                Network[IndexR][IndexC].add_input_current(LongCurrentList[IndexR], 2)
                Network[IndexR][IndexC].add_input_current(HallCurrentList[Dimensions[1] + IndexC], 3)
                if not Network[IndexR][IndexC].calculate_voltages():
                    print('(' + str(IndexR) + ', ' + str(IndexC) + ')')
                    print(1)
            elif IndexR == Dimensions[0] - 1 and not IndexR == 0 \
                    and not IndexC == Dimensions[1] - 1 and not IndexC == 0:
                Network[IndexR][IndexC].add_input_current(-1 * Network[IndexR][IndexC + 1].get_i1(), 2)
                Network[IndexR][IndexC].add_input_current(HallCurrentList[Dimensions[1] + IndexC], 3)
                if not Network[IndexR][IndexC].calculate_voltages():
                    print('(' + str(IndexR) + ', ' + str(IndexC) + ')')
                    print(2)
            elif not IndexR == Dimensions[0] - 1 and not IndexR == 0 \
                    and IndexC == Dimensions[1] - 1 and not IndexC == 0:
                Network[IndexR][IndexC].add_input_current(LongCurrentList[IndexR], 2)
                Network[IndexR][IndexC].add_input_current(-1 * Network[IndexR + 1][IndexC].get_i2(), 3)
                if not Network[IndexR][IndexC].calculate_voltages():
                    print('(' + str(IndexR) + ', ' + str(IndexC) + ')')
                    print(3)
            elif IndexC == 0 and IndexR == Dimensions[0] - 1 and not IndexR == 0:
                Network[IndexR][IndexC].add_input_current(LongCurrentList[-1], 0)
                try:
                    Network[IndexR][IndexC].add_input_current(-1 * Network[IndexR][IndexC + 1].get_i1(), 2)
                except IndexError:
                    Network[IndexR][IndexC].add_input_current(LongCurrentList[IndexR], 2)
                Network[IndexR][IndexC].add_input_current(HallCurrentList[Dimensions[1] + IndexC], 3)
                if not Network[IndexR][IndexC].calculate_voltages():
                    print('(' + str(IndexR) + ', ' + str(IndexC) + ')')
                    print(4)
            elif IndexC == 0 and not IndexR == 0 and not IndexR == Dimensions[0] - 1:
                Network[IndexR][IndexC].add_input_current(LongCurrentList[Dimensions[1] + IndexR - 1], 0)
                try:
                    Network[IndexR][IndexC].add_input_current(-1 * Network[IndexR][IndexC + 1].get_i1(), 2)
                except IndexError:
                    Network[IndexR][IndexC].add_input_current(LongCurrentList[IndexR], 2)
                Network[IndexR][IndexC].add_input_current(-1 * Network[IndexR + 1][IndexC].get_i2(), 3)
                if not Network[IndexR][IndexC].calculate_voltages():
                    print('(' + str(IndexR) + ', ' + str(IndexC) + ')')
                    print(5)
            elif IndexR == 0 and IndexC == Dimensions[1] - 1 and not IndexC == 0:
                Network[IndexR][IndexC].add_input_current(HallCurrentList[IndexC], 1)
                Network[IndexR][IndexC].add_input_current(LongCurrentList[IndexR], 2)
                try:
                    Network[IndexR][IndexC].add_input_current(-1 * Network[IndexR + 1][IndexC].get_i2(), 3)
                except IndexError:
                    Network[IndexR][IndexC].add_input_current(HallCurrentList[Dimensions[1] + IndexC], 3)
                if not Network[IndexR][IndexC].calculate_voltages():
                    print('(' + str(IndexR) + ', ' + str(IndexC) + ')')
                    print(6)
            elif IndexR == 0 and not IndexC == 0 and not IndexC == Dimensions[1] - 1:
                Network[IndexR][IndexC].add_input_current(HallCurrentList[IndexC], 1)
                Network[IndexR][IndexC].add_input_current(-1 * Network[IndexR][IndexC + 1].get_i1(), 2)
                try:
                    Network[IndexR][IndexC].add_input_current(-1 * Network[IndexR + 1][IndexC].get_i2(), 3)
                except IndexError:
                    Network[IndexR][IndexC].add_input_current(HallCurrentList[Dimensions[1] + IndexC], 3)
                if not Network[IndexR][IndexC].calculate_voltages():
                    print('(' + str(IndexR) + ', ' + str(IndexC) + ')')
                    print(7)
            elif IndexR == 0 and IndexC == 0:
                Network[IndexR][IndexC].add_input_current(HallCurrentList[0], 1)
                try:
                    Network[IndexR][IndexC].add_input_current(-1 * Network[0][1].get_i1(), 2)
                except IndexError:
                    Network[IndexR][IndexC].add_input_current(LongCurrentList[0], 2)
                try:
                    Network[IndexR][IndexC].add_input_current(-1 * Network[1][0].get_i2(), 3)
                except IndexError:
                    Network[IndexR][IndexC].add_input_current(HallCurrentList[Dimensions[1]], 3)
                if not Network[IndexR][IndexC].calculate_voltages():
                    print('(' + str(IndexR) + ', ' + str(IndexC) + ')')
                    print(8)
            else:
                Network[IndexR][IndexC].add_input_current(-1 * Network[IndexR][IndexC + 1].get_i1(), 2)
                Network[IndexR][IndexC].add_input_current(-1 * Network[IndexR + 1][IndexC].get_i2(), 3)
                if not Network[IndexR][IndexC].calculate_voltages():
                    print('(' + str(IndexR) + ', ' + str(IndexC) + ')')
                    print(9)

    Network_Graph_Object = Graph(Network_Graph)
    Contact_Points = [Key for Key in Network_Graph.keys() if (Key[0] == 0 and Key[2] == 1) or
                      (Key[1] == Dimensions[1] - 1 and Key[2] == 2) or (Key[0] == Dimensions[0] - 1 and Key[2] == 3) or
                      (Key[1] == 0 and Key[2] == 0 and not Key[0] == 0)]
    Temp_Contacts = []
    if Dimensions == (1, 1):
        Temp_Contacts.append(Contact_Points[0])
        Temp_Contacts.append(Contact_Points[2])
        Temp_Contacts.append(Contact_Points[1])
    elif Dimensions[0] == 1:
        for Index in range(Dimensions[1]):
            Temp_Contacts.append(Contact_Points[2 * Index])
        for Index in range(Dimensions[1] - 1):
            Temp_Contacts.append(Contact_Points[2 * Index + 1])
        Temp_Contacts.append(Contact_Points[-1])
        Temp_Contacts.append(Contact_Points[-2])
    elif Dimensions[1] == 1:
        Temp_Contacts.append(Contact_Points[0])
        Temp_Contacts.append(Contact_Points[-1])
        for Index in range(Dimensions[0]):
            Temp_Contacts.append(Contact_Points[2 * Index + 1])
        for Index in range(Dimensions[0] - 1):
            Temp_Contacts.append(Contact_Points[2 + 2 * Index])
    else:
        for Index in range(Dimensions[1]):
            Temp_Contacts.append(Contact_Points[Index])
        for Index in range(Dimensions[1] - 1):
            Temp_Contacts.append(Contact_Points[Dimensions[1] + 2 * (Dimensions[1] - 1) + Index])
        Temp_Contacts.append(Contact_Points[-1])
        for Index in range(Dimensions[0] - 1):
            Temp_Contacts.append(Contact_Points[Dimensions[1] + 2 * Index])
        Temp_Contacts.append(Contact_Points[-2])
        for Index in range(Dimensions[0] - 1):
            Temp_Contacts.append(Contact_Points[Dimensions[1] + 1 + 2 * Index])
    Contact_Points = Temp_Contacts
    del Temp_Contacts

    Path_List = []
    for Contact in Contact_Points:
        Path_List.append(Network_Graph_Object.find_path(Contact, (0, 0, 0)))

    Voltage_List = []
    for Path in Path_List:
        Voltage = 0
        for Index in range(len(Path) - 1):
            if not Path[Index][0:2] == Path[Index + 1][0:2]:
                Voltage += 0
            elif Path[Index][2] == 0 and Path[Index + 1][2] == 1:
                Voltage += Network[Path[Index][0]][Path[Index][1]].get_v1()
            elif Path[Index][2] == 1 and Path[Index + 1][2] == 2:
                Voltage += Network[Path[Index][0]][Path[Index][1]].get_v2()
            elif Path[Index][2] == 3 and Path[Index + 1][2] == 0:
                Voltage += Network[Path[Index][0]][Path[Index][1]].get_v4()
            elif Path[Index][2] == 0 and Path[Index + 1][2] == 3:
                Voltage -= Network[Path[Index][0]][Path[Index][1]].get_v4()
            elif Path[Index][2] == 1 and Path[Index + 1][2] == 0:
                Voltage -= Network[Path[Index][0]][Path[Index][1]].get_v1()
            elif Path[Index][2] == 2 and Path[Index + 1][2] == 1:
                Voltage -= Network[Path[Index][0]][Path[Index][1]].get_v2()
        Voltage_List.append(Voltage)

    CurrentList = HallCurrentList + LongCurrentList
    Impedance = np.zeros((2 * Dimensions[0] + 2 * Dimensions[1] - 1,
                          2 * Dimensions[0] + 2 * Dimensions[1] - 1)).tolist()

    for Voltage in range(2 * Dimensions[0] + 2 * Dimensions[1] - 1):
        Voltage_List[Voltage] = sympy.collect(sympy.expand(Voltage_List[Voltage]), CurrentList)
        for Current in range(2 * Dimensions[0] + 2 * Dimensions[1] - 1):
            Impedance[Voltage][Current] = Voltage_List[Voltage].coeff(CurrentList[Current], 1)

    # noinspection PyTypeChecker
    # np.savetxt("/home/andreec/Desktop/Ryan's Shits on Andree's Computer/EP3/GeneralTest.txt", Impedance, fmt='%-25s',
    #            delimiter='\t')

    return Impedance


print()
FourxOneImpedance = Network_Analysis((4, 1))
print("Four by one complete.")
print()
FourxTwoImpedance = Network_Analysis((4, 2))
print("Four by two complete.")
print()
OnexFourImpedance = Network_Analysis((1, 4))
print('One by four complete.')

# noinspection PyTypeChecker
np.savetxt("C:/Users/ryank/Desktop/Personal Files/Github/PythonCodes/EP3/Mobility and Carrier Density/4x1Impedance.txt",
           FourxOneImpedance, fmt='%-25s', delimiter='\t')
# noinspection PyTypeChecker
np.savetxt("C:/Users/ryank/Desktop/Personal Files/Github/PythonCodes/EP3/Mobility and Carrier Density/4x2Impedance.txt",
           FourxTwoImpedance, fmt='%-25s', delimiter='\t')
# noinspection PyTypeChecker
np.savetxt("C:/Users/ryank/Desktop/Personal Files/Github/PythonCodes/EP3/Mobility and Carrier Density/1x4Impedance.txt",
           OnexFourImpedance, fmt='%-25s', delimiter='\t')
