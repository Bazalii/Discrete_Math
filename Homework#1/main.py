from random import random
from random import randrange
import networkx as nx
from networkx.algorithms import approximation
from networkx.algorithms import planarity
from networkx.algorithms import planar_drawing
import matplotlib.pyplot as plt
import graphviz as gv
colors = ['green', 'red', 'orange', 'yellow', 'pink', 'blue', 'purple', 'black']

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
        if int(input_data[2]) != 0:
            edges.append((input_data[0], input_data[1], int(input_data[2])))
print(len(countries))
Full_graph = nx.Graph()
Full_graph.add_nodes_from(countries)
Full_graph.add_weighted_edges_from(edges)
print(nx.algorithms.check_planarity(Full_graph))
nx.draw_planar(Full_graph, with_labels=True, font_weight='bold')
plt.show()
Main_graph = Full_graph.subgraph(max(nx.connected_components(Full_graph)))
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
vertex_colored_graph.view(filename='vertex_colored_graph', quiet_view=True)
print("d")
edge_coloring = nx.greedy_color(nx.line_graph(Main_graph))
print(edge_coloring)
edge_colored_graph = gv.Graph()
for i in edge_coloring:
    edge_colored_graph.edge(i[0], i[1], color=colors[edge_coloring.get(i)])
for i in Main_graph.nodes:
    edge_colored_graph.node(i)
edge_colored_graph.view(filename='edge_colored_graph')
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
maximum_clique_subgraph.view(filename='maximum_clique_subgraph')
print("f")
independent_set = approximation.maximum_independent_set(Main_graph)
independent_set_graph = gv.Graph()
print("Independent set:", independent_set)
color_the_vertexes(independent_set_graph, independent_set)
independent_set_graph.view(filename='independent_set_graph')
print(len(approximation.maximum_independent_set(Main_graph)))
print("g")
maximum_matching = nx.max_weight_matching(Main_graph)
maximum_matching_graph = gv.Graph()
print("Maximum matching:", nx.max_weight_matching(Main_graph))
print(len(nx.max_weight_matching(Main_graph)))
color_the_edges(maximum_matching_graph, maximum_matching)
maximum_matching_graph.view(filename='maximum_matching_graph')
print("h")
minimum_vertex_cover = approximation.min_weighted_vertex_cover(Main_graph)
minimum_vertex_cover_graph = gv.Graph()
print("Minimum vertex cover:", minimum_vertex_cover)
print(len(approximation.min_weighted_vertex_cover(Main_graph)))
color_the_vertexes(minimum_vertex_cover_graph, minimum_vertex_cover)
minimum_vertex_cover_graph.view(filename='minimum_vertex_cover_graph')
print("i")
minimum_edge_cover = nx.algorithms.min_edge_cover(Main_graph)
minimum_edge_cover_graph = gv.Graph()
print("Minimum edge cover:", minimum_edge_cover)
print(len(minimum_edge_cover))
color_the_edges(minimum_edge_cover_graph, minimum_edge_cover)
minimum_edge_cover_graph.view(filename='minimum_edge_cover_graph')
print("l")
for i in nx.algorithms.components.biconnected_components(Full_graph):
    print(i)
print("m")
for i in nx.algorithms.connectivity.k_edge_components(Full_graph, 2):
    for j in i:
        print(j, end = ",")
    print()
print("n")
print("o")
minimum_spanning_tree = (nx.algorithms.tree.minimum_spanning_tree(Main_graph)).edges
minimum_spanning_tree_graph = gv.Graph()
print("Minimum spanning tree:", minimum_spanning_tree)
print(len(minimum_spanning_tree))
color_the_edges(minimum_spanning_tree_graph, minimum_spanning_tree)
minimum_spanning_tree_graph.view(filename='minimum_spanning_tree')
print("p")
print(nx.barycenter(nx.algorithms.tree.minimum_spanning_tree(Main_graph)))
print("q")
