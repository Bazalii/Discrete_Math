import networkx as nx
from networkx.algorithms import approximation
from networkx.algorithms import mis
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
fout = open('list_of_enumerate_vertexes.txt', 'w')
main = open('output.txt', 'w')
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
Full_graph = nx.Graph()
Full_graph.add_nodes_from(countries)
Full_graph.add_weighted_edges_from(edges, weight="weight")
nx.draw_planar(Full_graph, with_labels=True, font_weight='bold')
plt.show()
Main_graph = Full_graph.subgraph(max(nx.connected_components(Full_graph)))
print("b", file=main)
print("Number of nodes:", Full_graph.number_of_nodes(), file=main)
print("Number of edges:", Full_graph.number_of_edges(), file=main)
print("Diameter:", nx.algorithms.distance_measures.diameter(Main_graph), file=main)
print("Radius", nx.algorithms.distance_measures.radius(Main_graph), file=main)
print("Center:", nx.center(Main_graph), file=main)
print("Girth:", min(nx.algorithms.minimum_cycle_basis(Main_graph)), file=main)
maximum_degree = 0
minimum_degree = 100
for i in Main_graph.nodes:
    if Main_graph.degree[i] > maximum_degree:
        maximum_degree = Main_graph.degree[i]
    if Main_graph.degree[i] < minimum_degree:
        minimum_degree = Main_graph.degree[i]
print("Maximum degree:", maximum_degree, file=main)
print("Minimum degree:", minimum_degree, file=main)
print("c", file=main)
vertex_coloring = nx.greedy_color(Main_graph)
print(vertex_coloring, file=main)
vertex_colored_graph = gv.Graph()
for i in Main_graph.edges:
    vertex_colored_graph.edge(i[0], i[1])
for i in vertex_coloring:
    vertex_colored_graph.node(i, style='filled', fillcolor=colors[vertex_coloring.get(i)])
# vertex_colored_graph.view(filename='vertex_colored_graph', quiet_view=True)
print("d", file=main)
edge_coloring = nx.greedy_color(nx.line_graph(Main_graph))
print(edge_coloring, file=main)
edge_colored_graph = gv.Graph()
for i in edge_coloring:
    edge_colored_graph.edge(i[0], i[1], color=colors[edge_coloring.get(i)])
for i in Main_graph.nodes:
    edge_colored_graph.node(i)
# edge_colored_graph.view(filename='edge_colored_graph', quiet_view=True)
a = nx.find_cliques(Main_graph)
print("e", file=main)
maximum_clique = approximation.max_clique(Main_graph)
print(maximum_clique, file=main)
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
print("f", file=main)
independent_set_graph = gv.Graph()
maximum_independent_set = ['AD', 'CZ', 'EE', 'MK', 'HU', 'SM', 'NO', 'LU', 'MC', 'RO', 'LT', 'BA', 'DK', 'ME', 'NL', 'CH', 'PT', 'VA', 'TR']
print("Independent set:", maximum_independent_set, file=main)
print(dnx.is_independent_set(Main_graph, maximum_independent_set), file=main)
color_the_vertexes(independent_set_graph, maximum_independent_set)
# independent_set_graph.view(filename='independent_set')
print("maximum_independent_set.size =", len(maximum_independent_set), file=main)
print("g", file=main)
maximum_matching = nx.max_weight_matching(Main_graph)
maximum_matching_graph = gv.Graph()
print("Maximum matching:", maximum_matching, file=main)
print("maximum_matching.size =", len(maximum_matching), file=main)
color_the_edges(maximum_matching_graph, maximum_matching)
# maximum_matching_graph.view(filename='maximum_matching')
print("h", file=main)
part = []
minimum_vertex_cover_graph = gv.Graph()
min_vertex_cover = {'AL', 'KO', 'BG', 'GR', 'RS', 'HR', 'HU', 'RO', 'FI', 'NO', 'UA', 'RU', 'LV', 'BY', 'SP', 'FR', 'BE', 'DE', 'PL', 'IT', 'SK', 'AT', 'CH'}
print(min_vertex_cover, file=main)
print(dnx.is_vertex_cover(Main_graph, min_vertex_cover), file=main)
print("min_vertex_cover.size =", len(min_vertex_cover), file=main)
color_the_vertexes(minimum_vertex_cover_graph, min_vertex_cover)
# minimum_vertex_cover_graph.view(filename='minimum_vertex_cover')
print("i", file=main)
minimum_edge_cover = nx.algorithms.min_edge_cover(Main_graph)
minimum_edge_cover_graph = gv.Graph()
normalized_edge_cover = set((a, b) if a <= b else (b, a) for (a, b) in minimum_edge_cover)
print("Minimum edge cover:", normalized_edge_cover, file=main)
print("minimum_edge_cover.size =", len(normalized_edge_cover), file=main)
color_the_edges(minimum_edge_cover_graph, normalized_edge_cover)
# minimum_edge_cover_graph.view(filename='minimum_edge_cover')
print("l", file=main)
block_cut_tree_graph = gv.Graph()
k = 0
for i in nx.algorithms.components.biconnected_components(Full_graph):
    for j in i:
        print(j, end=",", file=main)
    print('', file=main)
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
# block_cut_tree.view(filename='block_cut_tree')
print("m", file=main)
for i in nx.algorithms.connectivity.k_edge_components(Full_graph, 2):
    for j in i:
        print(j, end=",", file=main)
    print('', file=main)
print("o", file=main)
minimum_spanning_tree = (nx.algorithms.tree.minimum_spanning_tree(Main_graph)).edges
minimum_spanning_tree_graph = gv.Graph()
print("Minimum spanning tree:", minimum_spanning_tree, file=main)
print("minimum_spanning_tree.size =", len(minimum_spanning_tree), file=main)
color_the_edges(minimum_spanning_tree_graph, minimum_spanning_tree)
# minimum_spanning_tree_graph.view(filename='minimum_spanning_tree')
print("p", file=main)
print(nx.barycenter(nx.algorithms.tree.minimum_spanning_tree(Main_graph)), file=main)
print("q", file=main)
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
print(nx.algorithms.to_prufer_sequence(nx.algorithms.tree.minimum_spanning_tree(Prufer_graph)), file=main)
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
