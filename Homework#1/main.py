from random import random
from random import randrange
import networkx as nx
from networkx.algorithms import approximation
from networkx.algorithms import planarity
from networkx.algorithms import planar_drawing
import matplotlib.pyplot as plt
countries = []
edges = []
fout = open("input.txt", "w")
with open('input.txt') as file:
    for line in file:
        input_data = line.replace('\n', '')
        input_data = input_data.split(',')
        if input_data[0] not in countries:
            countries.append(input_data[0])
        if input_data[1] not in countries:
            countries.append(input_data[1])
        if int(input_data[2]) != 0:
            edges.append((input_data[0], input_data[1], int(input_data[2])))
print(len(countries))
Full_graph = nx.Graph()
Full_graph.add_nodes_from(countries)
Full_graph.add_weighted_edges_from(edges)
print(planarity.check_planarity(Full_graph))
nx.draw_planar(Full_graph, with_labels=True, font_weight='bold')
plt.show()
# del countries
# del edges
Main_graph = Full_graph.subgraph(max(nx.connected_components(Full_graph)))
print("b")
print("Number of nodes:", Main_graph.number_of_nodes())
print("Number of edges:", Main_graph.number_of_edges())
print("Diameter:", nx.algorithms.distance_measures.diameter(Main_graph))
print("Radius", nx.algorithms.distance_measures.radius(Main_graph))
print("Center:", nx.center(Main_graph))
print("Girth:", min(nx.algorithms.minimum_cycle_basis(Main_graph)), len(min(nx.algorithms.minimum_cycle_basis(Main_graph))))
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
print(nx.greedy_color(Main_graph))
print("d")
print(nx.greedy_color(nx.line_graph(Main_graph)))
a = nx.find_cliques(Main_graph)
print("e")
print(approximation.max_clique(Main_graph))
current = 3
for element in a:
    if len(element) > current:
        print(element)
print("f")
print("Independent set:", approximation.maximum_independent_set(Main_graph))
print(len(approximation.maximum_independent_set(Main_graph)))
print("g")
print("Maximum matching:", nx.max_weight_matching(Main_graph))
print(len(nx.max_weight_matching(Main_graph)))
print("h")
print("Minimum vertex cover:", approximation.min_weighted_vertex_cover(Main_graph))
print(len(approximation.min_weighted_vertex_cover(Main_graph)))
print("i")
print("Minimum edge cover:", nx.algorithms.min_edge_cover(Main_graph))
print(len(nx.algorithms.min_edge_cover(Main_graph)))
print("l")
for i in nx.algorithms.components.biconnected_components(Main_graph):
    print(i)
print("m")
for i in nx.algorithms.connectivity.k_edge_components(Main_graph, 2):
    print(i)
print("n")
print("o")
print((nx.algorithms.tree.minimum_spanning_tree(Main_graph)).edges)
nx.draw_planar(nx.algorithms.tree.minimum_spanning_tree(Main_graph), with_labels=True, font_weight='bold')
plt.show()
print("p")
nx.barycenter(nx.algorithms.tree.minimum_spanning_tree(Main_graph))
print("q")
