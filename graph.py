def add_node(v):
    global node_count
    if v in nodes:
        print("Node is already in the list")
    else:
        node_count = node_count + 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

# def add_node(v):
#     if v in nodes:
#         print(v, "is in already there")
#         return
#     nodes.append(v)
#     graph.append([0]*len(nodes))
#     for row in graph:
#         row.append(0)

def add_edge(v1, v2, cost):
    if v1 not in nodes:
        print(v1, "is not present in the graph")
    elif v2 not in nodes:
        print(v2, "is not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)

        graph[index1][index2] = cost
        graph[index2][index1] = cost


def print_graph():
    for row in graph:
        print(" ".join(map(str, row)))


nodes = [] 
graph= []
node_count=0


print("Before adding nodes")
print(nodes)
print(graph)
print_graph()

add_node("A")
add_node("B")
add_node("C")
add_node("D")

print("After adding nodes")
print(nodes)
print(graph)
print_graph()

