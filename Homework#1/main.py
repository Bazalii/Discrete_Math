# import dwave_networkx as dnx
import networkx as nx
from networkx.algorithms import approximation
from networkx.algorithms import planarity
from networkx.algorithms import planar_drawing
import matplotlib.pyplot as plt
import graphviz as gv
import dwave_networkx as dnx
colors = ['green', 'red', 'orange', 'yellow', 'pink', 'blue', 'purple', 'olive', 'magenta']

def color_the_edges(inp_graph, type_of_coloring):
    buffer = []
    for i in type_of_coloring:
        if i not in buffer and (i[1], i[0]) not in buffer:
            inp_graph.edge(i[0], i[1], color='red')
            buffer.append(i)
    for i in Main_graph.nodes:
        inp_graph.node(i)
    for i in Main_graph.edges:
        if i not in buffer and (i[1], i[0]) not in buffer:
            inp_graph.edge(i[0], i[1])

def color_the_vertexes(inp_graph, type_of_coloring):
    buffer = []
    for i in type_of_coloring:
        inp_graph.node(i, style='filled', fillcolor=colors[0])
        buffer.append(i)
    for i in Main_graph.nodes:
        if i not in buffer:
            inp_graph.node(i)
    for i in Main_graph.edges:
        inp_graph.edge(i[0], i[1])

countries = []
edges = []
nw_edges = []
fout = open('list_of_enumerate_vertexes.txt', 'w')
with open('input.txt') as file:
    for line in file:
        input_data = line.replace('\n', '')
        input_data = input_data.split(',')
        if input_data[0] not in countries:
            countries.append(input_data[0])
        if input_data[1] not in countries:
            countries.append(input_data[1])
        if input_data[1] == 'VA':
            edges.append((input_data[0], input_data[1], int(input_data[2])))
            nw_edges.append((input_data[0], input_data[1]))
        if int(input_data[2]) != 0:
            edges.append((input_data[0], input_data[1], int(input_data[2])))
            nw_edges.append((input_data[0], input_data[1]))
print(len(countries))
Full_graph = nx.Graph()
nw_Full = nx.Graph()
Full_graph.add_nodes_from(countries)
nw_Full.add_nodes_from(countries)
print(edges)
Full_graph.add_weighted_edges_from(edges, weight="weight")
nw_Full.add_edges_from(nw_edges)
print(Full_graph.edges)
nx.draw_planar(Full_graph, with_labels=True, font_weight='bold')
plt.show()
Main_graph = Full_graph.subgraph(max(nx.connected_components(Full_graph)))
nw_Main = nw_Full.subgraph(max(nx.connected_components(Full_graph)))
print("b")
print("Number of nodes:", Full_graph.number_of_nodes())
print("Number of edges:", Full_graph.number_of_edges())
print("Diameter:", nx.algorithms.distance_measures.diameter(Main_graph))
print("Radius", nx.algorithms.distance_measures.radius(Main_graph))
print("Center:", nx.center(Main_graph))
print("Girth:", min(nx.algorithms.minimum_cycle_basis(Main_graph)),
      len(min(nx.algorithms.minimum_cycle_basis(Main_graph))))
maximum_degree = 0
minimum_degree = 100
for i in Main_graph.nodes:
    if Main_graph.degree[i] > maximum_degree:
        maximum_degree = Main_graph.degree[i]
    if Main_graph.degree[i] < minimum_degree:
        minimum_degree = Main_graph.degree[i]
print("Maximum degree:", maximum_degree)
print("Minimum degree:", minimum_degree)
print("c")
vertex_coloring = nx.greedy_color(Main_graph)
print(vertex_coloring)
vertex_colored_graph = gv.Graph()
for i in Main_graph.edges:
    vertex_colored_graph.edge(i[0], i[1])
for i in vertex_coloring:
    vertex_colored_graph.node(i, style='filled', fillcolor=colors[vertex_coloring.get(i)])
# vertex_colored_graph.view(filename='vertex_colored_graph', quiet_view=True)
print("d")
edge_coloring = nx.greedy_color(nx.line_graph(Main_graph))
print(edge_coloring)
edge_colored_graph = gv.Graph()
for i in edge_coloring:
    edge_colored_graph.edge(i[0], i[1], color=colors[edge_coloring.get(i)])
for i in Main_graph.nodes:
    edge_colored_graph.node(i)
# edge_colored_graph.view(filename='edge_colored_graph')
a = nx.find_cliques(Main_graph)
print("e")
maximum_clique = approximation.max_clique(Main_graph)
print(maximum_clique)
maximum_clique_list = []
for i in maximum_clique:
    maximum_clique_list.append(i)
maximum_clique_subgraph = gv.Graph()
for i in range(0, len(maximum_clique_list)):
    maximum_clique_subgraph.node(maximum_clique_list[i])
    for j in range(i + 1, len(maximum_clique_list)):
        if i != j:
            maximum_clique_subgraph.edge(maximum_clique_list[i], maximum_clique_list[j])
# maximum_clique_subgraph.view(filename='maximum_clique_subgraph')
print("f")
independent_set = approximation.maximum_independent_set(Main_graph)
independent_set_graph = gv.Graph()
print("Independent set:", independent_set)
color_the_vertexes(independent_set_graph, independent_set)
# independent_set_graph.view(filename='independent_set')
print(len(approximation.maximum_independent_set(Main_graph)))
print("g")
maximum_matching = nx.max_weight_matching(Main_graph)
maximum_matching_graph = gv.Graph()
print("Maximum matching:", maximum_matching)
print(len(maximum_matching))
print("nwMaximum matching:", nx.max_weight_matching(nw_Main))
print(len(nx.max_weight_matching(nw_Main)))
for i in range (20):
    print(nx.maximal_matching(Main_graph))
    print(len(nx.maximal_matching(Main_graph)))

print(nx.is_maximal_matching(Main_graph, maximum_matching))
color_the_edges(maximum_matching_graph, maximum_matching)
# maximum_matching_graph.view(filename='maximum_matching')
print("h")
for a in Main_graph.nodes:
    for b in Main_graph.nodes:
        for c in Main_graph.nodes:
            for d in Main_graph.nodes:
                for e in Main_graph.nodes:
                    for f in Main_graph.nodes:
                        for g in Main_graph.nodes:
                            for h in Main_graph.nodes:
                                for i in Main_graph.nodes:
                                    for j in Main_graph.nodes:
                                        for k in Main_graph.nodes:
                                            for l in Main_graph.nodes:
                                                for m in Main_graph.nodes:
                                                    for n in Main_graph.nodes:
                                                        for o in Main_graph.nodes:
                                                            for p in Main_graph.nodes:
                                                                for q in Main_graph.nodes:
                                                                    for r in Main_graph.nodes:
                                                                        for s in Main_graph.nodes:
                                                                            for t in Main_graph.nodes:
                                                                                for u in Main_graph.nodes:
                                                                                    for v in Main_graph.nodes:
                                                                                        for w in Main_graph.nodes:
                                                                                            vertex_cover1 = {a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w}
                                                                                            vertex_cover2 = {a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v}
                                                                                            vertex_cover3 = {a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u}
                                                                                            vertex_cover4 = {a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t}
                                                                                            if dnx.is_vertex_cover(Main_graph, vertex_cover1):
                                                                                                print(vertex_cover1)
                                                                                            if dnx.is_vertex_cover(Main_graph, vertex_cover2):
                                                                                                print(vertex_cover1)
                                                                                            if dnx.is_vertex_cover(Main_graph, vertex_cover3):
                                                                                                print(vertex_cover1)
                                                                                            if dnx.is_vertex_cover(Main_graph, vertex_cover4):
                                                                                                print(vertex_cover1)

# minimum_vertex_cover = nx.algorithms.minimum_node_cut(Main_graph)
# minimum_vertex_cover_graph = gv.Graph()
# print("Minimum vertex cover:", minimum_vertex_cover)
# print(len(approximation.min_weighted_vertex_cover(Main_graph)))
# color_the_vertexes(minimum_vertex_cover_graph, minimum_vertex_cover)
# minimum_vertex_cover_graph.view(filename='minimum_vertex_cover_graph')
print("i")
minimum_edge_cover = nx.algorithms.min_edge_cover(Main_graph)
minimum_edge_cover_graph = gv.Graph()
print("Minimum edge cover:", minimum_edge_cover)
print(len(minimum_edge_cover))
color_the_edges(minimum_edge_cover_graph, minimum_edge_cover)
# minimum_edge_cover_graph.view(filename='minimum_edge_cover')
print("l")
block_cut_tree_graph = gv.Graph()
k = 0
for i in nx.algorithms.components.biconnected_components(Full_graph):
    for j in i:
        print(j, end=",")
    print()
for i in nx.algorithms.components.biconnected_components(Full_graph):
    for j in i:
        block_cut_tree_graph.node(j, style='filled', fillcolor=colors[k])
    k += 1
for edge in Full_graph.edges:
    block_cut_tree_graph.edge(edge[0], edge[1])
# block_cut_tree_graph.view(filename='block_cut_tree_graph')
block_cut_tree = gv.Graph()
block_cut_tree.node('2', style='filled', fillcolor=colors[0])
block_cut_tree.node('3', style='filled', fillcolor=colors[1])
block_cut_tree.node('8', style='filled', fillcolor=colors[2])
block_cut_tree.node('7', style='filled', fillcolor=colors[3])
block_cut_tree.node('4', style='filled', fillcolor=colors[5])
block_cut_tree.node('6', style='filled', fillcolor=colors[6])
block_cut_tree.node('1', style='filled', fillcolor=colors[7])
block_cut_tree.node('5', style='filled', fillcolor=colors[8])
block_cut_tree.node('Hinge 1')
block_cut_tree.node('Hinge 2')
block_cut_tree.node('Hinge 3')
block_cut_tree.node('Hinge 4')
block_cut_tree.node('Hinge 5')
block_cut_tree.node('Hinge 6')
block_cut_tree.edge('1', 'Hinge 1')
block_cut_tree.edge('1', 'Hinge 2')
block_cut_tree.edge('1', 'Hinge 3')
block_cut_tree.edge('1', 'Hinge 4')
block_cut_tree.edge('3', 'Hinge 2')
block_cut_tree.edge('2', 'Hinge 1')
block_cut_tree.edge('4', 'Hinge 3')
block_cut_tree.edge('5', 'Hinge 3')
block_cut_tree.edge('Hinge 5', 'Hinge 4')
block_cut_tree.edge('6', 'Hinge 5')
block_cut_tree.edge('7', 'Hinge 4')
block_cut_tree.edge('7', 'Hinge 6')
block_cut_tree.edge('8', 'Hinge 6')
# nx.algorithms.connectivity.all_pairs_node_connectivity()
# block_cut_tree.view(filename='block_cut_tree')
print("m")
for i in nx.algorithms.connectivity.k_edge_components(Full_graph, 2):
    for j in i:
        print(j, end=",")
    print()
print("n")
print("o")
minimum_spanning_tree = (nx.algorithms.tree.minimum_spanning_tree(Main_graph)).edges
minimum_spanning_tree_graph = gv.Graph()
print("Minimum spanning tree:", minimum_spanning_tree)
print(len(minimum_spanning_tree))
color_the_edges(minimum_spanning_tree_graph, minimum_spanning_tree)
# minimum_spanning_tree_graph.view(filename='minimum_spanning_tree')
print("p")
print(nx.barycenter(nx.algorithms.tree.minimum_spanning_tree(Main_graph)))
print("q")
prufer_minimum_spanning_tree = nx.algorithms.tree.minimum_spanning_tree(Main_graph)
Prufer_graph = nx.Graph()
prufer_graph_edges = []
for index, vertex in enumerate(Main_graph.nodes):
    print(vertex, ":", index, file=fout)
for edge in Main_graph.edges(data=True):
    for index, vertex in enumerate(Main_graph.nodes):
        if vertex == edge[0]:
            first_index = index
        if vertex == edge[1]:
            second_index = index
        if index not in Prufer_graph.nodes:
            Prufer_graph.add_node(index)
    prufer_graph_edges.append((first_index, second_index, edge[2].get('weight')))
Prufer_graph.add_weighted_edges_from(prufer_graph_edges)
print(nx.algorithms.to_prufer_sequence(nx.algorithms.tree.minimum_spanning_tree(Prufer_graph)))
proof1 = gv.Graph()
proof1.node('1')
proof1.node('2')
proof1.node('3')
proof1.edge('1', '2')
# proof1.view(filename='proof1')
proof2 = gv.Graph()
proof2.node('1')
proof2.node('2')
proof2.node('3')
proof2.edge('1', '2')
proof2.edge('1', '2')
proof2.edge('3', '2')
proof2.edge('1', '3')
# proof2.view(filename='proof2')
