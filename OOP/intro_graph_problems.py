class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight = 1.0):
        """Assumes src and dest are nodes, weight a number"""
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return self.src.getName() + '->(' + str(self.weight) + ')'\
               + self.dest.getName()

# ..................................................................................................

class Digraph(object):
    #nodes is a list of the nodes in the graph
    #edges is a dict mapping each node to a list of its children
    def __init__(self):
        self.nodes = []
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                         + dest.getName() + '\n'
        return result[:-1] #omit final newline


class Graph(Digraph):
    # Graph is a subclass of Digraph
    # It inherits all of the methods of `Digraph` except `addEdge`, which it overrides.
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

# ..................................................................................................

def DFS(graph, start, end, path, shortest, toPrint = False):
    """
    DEPTH-FIRST SEARCH: FIND THE SHORTEST PATH FROM START TO END IN GRAPH
        graph is a Digraph object
        start and end are Node objects
        path is a list of nodes
    Returns: shortest, a list of nodes
    (note that it requires an initial "shortest" to be passed)
    """
    path = path + [start]
    
    if toPrint:
        print('Current DFS path:', printPath(path))
    
    if start == end:
        return path
    
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
    
    return shortest

# ..................................................................................................

def shortestPath(graph, start, end, toPrint = False):
    """
    shortestPath is a wrapper for the DFS function
        graph is a Digraph object
        start and end are Node objects
        toPrint is a boolean that says whether to print or not?
    """
    return DFS(graph, start, end, [], None, toPrint)

def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str( path[i] )
        if i != len(path) - 1:
            result = result + '->'
    return result 

# ..................................................................................................

#Figure 12.11 (with a bug fixed)
def BFS(graph, start, end, toPrint = False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""

    initPath = [start] # a list with a node object (start)
    pathQueue = [initPath] # a list with a list inside

    while len(pathQueue) != 0:
        
        #Get and remove oldest element in pathQueue
        # `pop([i])`: removes the item with the index i from the array and returns it
        tmpPath = pathQueue.pop(0)
        
        if toPrint:
            print('Current BFS path:', printPath(tmpPath))
        lastNode = tmpPath[-1]
        
        if lastNode == end:
            return tmpPath
        
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    
    return None

# ..................................................................................................
# Run a depth-first search

## `testSP` function for `DFS`


def testSP():
    
    nodes = [] # ..... (i) 
    for name in range(6):
        nodes.append( Node(str(name)) )
    
    g = Digraph() # ..... (ii)
    
    for n in nodes: # ..... (iii)
        g.addNode(n)
        
    g.addEdge( Edge(nodes[0],nodes[1]) ) # ..... (iv)
    g.addEdge( Edge(nodes[1],nodes[2]) )
    g.addEdge( Edge(nodes[2],nodes[3]) )
    g.addEdge( Edge(nodes[2],nodes[4]) )
    g.addEdge( Edge(nodes[3],nodes[4]) )
    g.addEdge( Edge(nodes[3],nodes[5]) )
    g.addEdge( Edge(nodes[0],nodes[2]) )
    g.addEdge( Edge(nodes[1],nodes[0]) )
    g.addEdge( Edge(nodes[3],nodes[1]) )
    g.addEdge( Edge(nodes[4],nodes[0]) )
    
    sp = shortestPath(g, nodes[0], nodes[5]) # ..... (v)
    
    print('Shortest path found by DFS:', printPath(sp)) # ..... (vi)


# ..................................................................................................
# Run for a breadth-first search
## `testSP` function for `BFS`

def testSP():
    
    nodes = [] 
    for name in range(6):
        nodes.append( Node(str(name)) )
    
    g = Digraph()
    for n in nodes:
        g.addNode(n)
        
    g.addEdge( Edge(nodes[0],nodes[1]) )
    g.addEdge( Edge(nodes[1],nodes[2]) )
    g.addEdge( Edge(nodes[2],nodes[3]) )
    g.addEdge( Edge(nodes[2],nodes[4]) )
    g.addEdge( Edge(nodes[3],nodes[4]) )
    g.addEdge( Edge(nodes[3],nodes[5]) )
    g.addEdge( Edge(nodes[0],nodes[2]) )
    g.addEdge( Edge(nodes[1],nodes[0]) )
    g.addEdge( Edge(nodes[3],nodes[1]) )
    g.addEdge( Edge(nodes[4],nodes[0]) )
    
    # these two lines were used for depth-first search
    # sp = shortestPath(g, nodes[0], nodes[5]) # DFS was called through shortestPath
    # print('Shortest path found by DFS:', printPath(sp))
    
    # these two lines are used for breadth-first search
    sp = BFS(g, nodes[0], nodes[5]) # BFS called directly
    print( 'Shortest path found by BFS:', printPath(sp) )


# ..................................................................................................
# Code taxonomy
## Types

# * `Node` is a type
#     - requires input `name` (a string)
# 
# * `Edge` is a type
#     - requires inputs `src` and `dest` (Node objects)
#     
# * `WeightedEdge` is a subtype of `Edge`
#     - class `WeightedEdge` adds a weight attribute to class `Edge`
#     - requires inputs `src`, `dest` (Node objects), and `weight` (a float from 0 to 1.0)
# 
# * `Digraph` is a type which requires (creates?)
#     - `nodes`, a list of Node objects
#     - `edges`, a dictionary mapping each node to a list of its children
#       
# * `Graph` is a subtype of `Digraph`
#     - class `Graph` inherits all the methods of `Digraph` except `addEdge`, which it overrides
#     - `addEdge` creates `rev` (an Edge object)
#     - requires input `edge` (Edge type objects)

## Functions
  
# * `graph` is a Digraph object
# * `start` and `end` are Node objects
# * `path` is a list of nodes
# * `toPrint` is a boolean (to decide whether to print or not?)
# * `shortest` is a list of nodes
# 
# 
# * `DFS` is a function
# * `BFS` is a function
# * `shortestPath` is a wrapper for the `DFS` function. It serves to get the recursion started
#   properly and provide appropriate abstraction. It does that by indicating that
#     - the current path being explored is empty (`path == []`)
#     - no path from `start` to `end` has yet been found (`shortest == None`)
# * `printPath` is a function used to convert the result of `sp`, a path, to a string that can be
#   printed. (Remember the `path` variable is defined as a list of nodes.)
