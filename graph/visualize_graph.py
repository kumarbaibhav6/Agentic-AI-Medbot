import matplotlib.pyplot as plt
import networkx as nx
from graph.build_graph import build_medical_graph

# Compile the graph
compiled_graph = build_medical_graph()

# Access internal graph
internal_graph = compiled_graph.get_graph()

# Extract nodes
nodes = list(internal_graph.nodes)

# Extract edges, including conditional info
edges = []
for edge in internal_graph.edges:
    source = edge.source
    target = edge.target
    label = "conditional" if edge.conditional else "regular"
    edges.append((source, target, {"label": label}))

# Create and populate a directed graph
G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Layout for visualization
pos = nx.spring_layout(G, seed=42)

# Draw nodes and edges
plt.figure(figsize=(12, 8))
nx.draw(
    G, pos,
    with_labels=True,
    node_color="skyblue",
    node_size=3000,
    font_size=10,
    font_weight='bold',
    arrows=True
)

# Draw edge labels (conditional or regular)
edge_labels = nx.get_edge_attributes(G, "label")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")

# Title and save
plt.title("LangGraph Medical Agent Workflow with Conditional Branching")
plt.savefig("langgraph_visualization_fixed.png")
plt.close()

print("✅ Graph saved as 'langgraph_visualization_fixed.png'")
