

def add_node(v):
    nodes.append(v)
    for n in graph:
        n.append(0)
    temp = []
    for i in range(len(nodes)):
        temp.append(0)
    graph.append(temp)

nodes = []
graph = []


add_node("A")

print(graph)

