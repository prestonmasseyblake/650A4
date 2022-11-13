import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_node("q0")
G.add_node("q1")
G.add_node("q2")
G.add_node("q3")
G.add_node("q4")
G.add_edge("q0", "q1", weight="1")
G.add_edge("q1", "q2")
G.add_edge("q2", "q3")
G.add_edge("q3", "q4")
G.add_edge("q0", "q4")
G.add_edge("q1", "q1")
G.add_edge("q4", "q4")
G.add_edge("q2", "q1")
G.add_edge("q2", "q1")
G.add_edge("q3", "q2")
G.add_edge("q3", "q1")

nx.draw_networkx(G)
plt.show()

