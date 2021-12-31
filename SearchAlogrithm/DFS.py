
def DFS_graph(graph, start=None):

    stackNode=[]
    visited=[]
    # check path from start to target
    spaceSearch = {}
    path = []

    if start == None:
        start = 'A'

    stackNode.append(start)
    visited.append(start)

    while len(stackNode) != 0:
        
        node = stackNode.pop()
        print(node)
        if node == 'G':
            break
        for item in graph.get(node):
            if item not in visited:
                visited.append(item)
                stackNode.append(item)
                spaceSearch[item] = node

    # tracking path
    node = "G"
    while node != start:
        path.append(node)
        node = spaceSearch.get(node)
    path.append(start)
     
    path.reverse()
    print(path)

if __name__ == '__main__':
    # Adjacency List
    graph  = {'A':['B', 'C'],
            'B':['D','A'],
            'C':['E', 'F','A'],
            'D':['J', 'B'],
            'E':['G', 'C'],
            'F':['G', 'C'],
            'G':['I', 'E', 'F'],
            'J':['I', 'D'],
            'I':['G', 'J']}

    DFS_graph(graph)
