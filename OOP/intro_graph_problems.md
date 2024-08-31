# Graph Optimization Problems

Graphs are typically used to represent situations in which there are interesting relations among the
parts. Many practical problems can be treated as graph optimization problems.

## Definitions

A **graph** is a set of objects called **nodes** (or vertices) connected by a set of **edges**
(or *arcs*). If the edges are unidirectional, the graph is called a **directed graph**
(or **digraph**).

In a directed graph, if there is an edge from `n1` to `n2`, we refer to `n1` as the **source**
or **parent** node and `n2` as the **destination** or **child** node.

A graph (or a digraph) is said to contain a **path** between two nodes, `n1` and `n2`, if there is a
sequence of edges  
`< e0, … , en >` such that:

  * the source of `e0` is `n1`
  * the destination of `en` is `n2`
  * for all edges `e1` to `en` in the sequence, the source of `ei` is the destination of `ei−1`

A path from a node to itself is called a **cycle**. A graph containing a cycle is called *cyclic*,
and a graph that contains no cycles is called *acyclic*.

If a weight is associated with each edge in a graph (or digraph), it is called a **weighted graph**.

<!-- should move this? -->
One important decision is the choice of data structure used to represent a digraph. One common
representation is an `n × n` **adjacency matrix**, where `n` is the number of nodes in the graph.
Each cell of the matrix contains information (weights) about the edges connecting the pair of nodes
`<i, j>`. 

If the edges are unweighted, for a cell located at s, d:

* If there is an edge from `s` to `d`: `cell[s, d] = 1`
* Otherwise, `cell[s, d] = 0`

Another common representation is an **adjacency list**, which is what we use here [in the code
below].


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈***≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## Some Classic Graph-Theoretic Problems

One of the nice things about formulating a problem using graph theory is that there are well-known
algorithms for solving many optimization problems on graphs. 

Some of the best-known graph optimization problems are:

**Shortest path**. For some pair of nodes, `n1` and `n2`, find the shortest sequence of edges 
  `<sn, dn>` (source node and destination node), such that

* The source node in the first edge is `n1`
* The destination node of the last edge is `n2`
* For all edges `e1` and `e2` in the sequence, if `e2` follows `e1` in the sequence, the source node
  of `e2` is the destination node of `e1`

**Shortest weighted path**. This is like the shortest path, except instead of choosing the shortest
  sequence of edges that connects two nodes, we define some function on the weights of the edges in
  the sequence (e.g. their sum) and minimize that value. This is the kind of problem solved by a
  GPS app when asked to compute driving directions between two points.

**Min cut**. Given two sets of nodes in a graph, a **cut** is a set of edges whose removal
  eliminates all paths *from* each node in one set *to* each node in the other set.

**Maximum clique**. A **clique** is a set of nodes such that there is an edge between each pair of
  nodes in the set. A maximum clique is a clique of the largest size in a graph. (The minimum cut
  is the smallest set of edges whose removal accomplishes this—similarly to the notion of a social
  clique, i.e. a group of people who feel closely connected to each other and are inclined to
  exclude those not in the clique.)
  
### Shortest path: *depth-first* search
<!-- page 316 -->

**Depth-first search** (**DFS**) is usually **implemented recursively**. In general, a
depth-first-search algorithm begins by choosing one child of the start node. It then chooses one
child of that node and so on, going deeper and deeper until it either reaches the goal node or a
node with no children. The search then **backtracks**, returning to the most recent node with
children that it has not yet visited. When all paths have been explored, it chooses the shortest
path (assuming that there is one) from the start to the goal.

The code is more complicated than the algorithm we just described because it has to deal with the
possibility of the graph containing cycles, and it also avoids exploring paths longer than the
shortest path that it has already found.

Social networks are made up of individuals and relationships between individuals. These are
typically modeled as graphs in which the individuals are nodes and the edges relationships. If the
relationships are symmetric, the edges are undirected; if the relationships are asymmetric, the
edges are directed. Some social networks model multiple kinds of relationships, in which case
labels on the edges indicate the kind of relationship.

Think of the distance between pairs of people on Facebook, using the "friends" relation. For
example, you might wonder if you have a friend who has a friend who has a friend who is a friend of
Lady Gaga. Let's think about designing a program to answer such questions: the friend relation
(at least on Facebook) is symmetric, e.g. if Sam is a friend of Andrea, Andrea is a friend of Sam.
We will, therefore, implement the social network using type `Graph`. 

We can then define **the problem of finding the shortest connection between two members** as:

> Let `G` be the graph representing the friend relation. For `G`, find the shortest sequence of
  nodes, such that, if `n_i` and `n_i+1` are consecutive nodes in the sequence, there is an edge in
  `G` connecting `n_i` and `ni+1`.

### Shortest path: *breadth-first* search
<!-- page 321 -->

Of course, there are other ways to traverse a graph than depth-first. Another common approach is
**breadth-first search** (**BFS**), which is usually **implemented iteratively**. A breadth-first
traversal first visits all children of the start node; if none of those is the end node, it visits
all children of each of those nodes, and so on. 

BFS explores many paths simultaneously, adding one node to each path on each iteration. Since it
generates the paths in ascending order of length, the first path found with the goal as its last
node is guaranteed to have a minimum number of edges.


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈***≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## Code

[There is a "Code taxonomy" section below this one which has a list of objects used in this code; it
might be useful to understand what's going on here (more efficient than moving up and down the page
trying to find where objects came from and how they were defined).]

### Classes `Node`, `Edge`, `WeightedEdge`

The figure below contains classes implementing abstract types corresponding to nodes, weighted
edges, and edges. (None of the methods in class `Node` perform any interesting computation; but
having the class gives us the flexibility of deciding, at some later point, to introduce a subclass
of `Node` with additional properties.)

```Python

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

```

### Classes `Digraph` and `Graph`

The figure below contains implementations of the classes `Digraph` and `Graph`.

```Python

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

```

Class `Digraph` has two instance variables: `nodes` and `edges` (seen in `self.nodes` and
`self.edges`). 

* The variable `nodes` is a Python list containing the names of the nodes in the digraph. The
  connectivity of the nodes is represented using an adjacency list implemented as a dictionary. 

* The variable `edges` is a dictionary that maps each node in the digraph to a list of the children
  of that Node.

Class `Graph` is a subclass of `Digraph`. It inherits all of the methods of `Digraph` except
`addEdge`, which it overrides. (This is not the most space-efficient way to implement `Graph`,
since it stores each edge twice—once for each direction in the digraph. But it has the virtue of
simplicity.)

##### Subtypes and Supertypes

You might want to stop for a minute and think about why `Graph` is a subclass of `Digraph`, rather
than the other way around. 

In many of the examples of subclassing we have looked at, the subclass adds attributes to the
superclass (e.g. class `WeightedEdge` added a weight attribute to class `Edge`).

Here, `Digraph` and `Graph` have the same attributes but the `addEdge` method is implemented
differently in `Digraph` than in `Graph`. Either version of the `addEdge` method could have been
easily implemented by inheriting methods from the other, but the choice of which to make the
superclass was not arbitrary.

In Chapter 10, we stressed the importance of obeying the **substitution principle**: 
<!-- pdf 291 -->

> If client code works correctly using an instance of the supertype, you should make sure it also
  works correctly when an instance of the subtype is substituted for the instance of the
  supertype.

We have determined that if client code works correctly using an instance of `Digraph`, it will work
correctly if an instance of `Graph` is substituted for the instance of `Digraph`. The converse is
not true; thus `Graph` cannot be the superclass. 

[I wrote the lines above, including the "you should make sure it also works correctly ..." trying to
interpret what they meant—it wasn't clear, at all. I believe they are alluding to a process of
trial and error to determine which can be the superclass.]

### Function `DFS`

The `DFS` code is more complicated than the algorithm described earlier because it has to deal with
the possibility of the graph containing cycles, and it also avoids exploring paths longer than the
shortest path that it has already found.

`DFS` chooses one child of `start`, it then chooses one child of that node and keeps on choosing
children nodes until either it reaches the node end or a node with no unvisited children.

```Python

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

```

* The check `if node not in path` prevents the program from getting caught in a cycle.
<!-- how does it know if it's in path or not (notation, flag)? -->

* The check `if shortest == None or len(path) < len(shortest)` is used to decide if it is
  possible that continuing to search this path might yield a shorter path than the best path
  found so far.

* If so, `DFS` is called recursively: 
  `newPath = DFS(graph, node, end, path, shortest, toPrint) `. 
  If it finds a path to `end` that is no longer than the best found so far, `shortest` is 
  updated.

* When the last node on `path` has no children left to visit, the program backtracks to the
  previously visited node and visits the next child of that node.

* The function returns when all possible shortest paths from `start` to `end` have been
  explored.

### Functions `shortestPath`, `printPath`

`shortestPath` is a wrapper for the `DFS` function. It serves to get the recursion started properly
and provide appropriate abstraction. It does that by indicating that

* the current path being explored is empty (with `path == []`)
* no path from `start` to `end` has yet been found (with `shortest == None`)

```Python

def shortestPath(graph, start, end, toPrint = False):
    """
    shortestPath is a wrapper for the DFS function
        graph is a Digraph object
        start and end are Node objects
        toPrint is a boolean that says whether to print or not?
    """
    return DFS(graph, start, end, [], None, toPrint)

```

The `printPath` function is used to convert the result of `sp`, a path, to a string that can be
printed. (Remember the `path` variable is defined as a list of nodes.)

```Python

def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str( path[i] )
        if i != len(path) - 1:
            result = result + '->'
    return result 

```

### Function `BFS`

The `BFS` function uses a breadth-first search to find the shortest path in a directed graph.

```Python

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

```

The variable `pathQueue` is used to store all of the paths currently being explored. 

Each iteration of `while` starts with `pathQueue.pop(0)` which removes the first path from
`pathQueue`; this path is assigned to `tmpPath`. (Note that `pathQueue` is a list of lists and a
path is, itself, a list.)

If the last node in `tmpPath` is the same as the node called `end` (`if lastNode == end:` ), we
determine that `tmpPath` is *a* shortest path (return `tmpPath`).

Otherwise, a set of new paths is created, each of which extends `tmpPath` by adding one of its
children. Each of these new paths is then added to `pathQueue`.


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈***≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## Code taxonomy

### Types

* `Node` is a type
    - requires input `name` (a string)

* `Edge` is a type
    - requires inputs `src` and `dest` (Node objects)
    
* `WeightedEdge` is a subtype of `Edge`
    - class `WeightedEdge` adds a weight attribute to class `Edge`
    - requires inputs `src`, `dest` (Node objects), and `weight` (a float from 0 to 1.0)

* `Digraph` is a type which requires (creates?)
    - `nodes`, a list of Node objects
    - `edges`, a dictionary mapping each node to a list of its children
      
* `Graph` is a subtype of `Digraph`
    - class `Graph` inherits all the methods of `Digraph` except `addEdge`, which it overrides
    - `addEdge` creates `rev` (an Edge object)
    - requires input `edge` (Edge type objects)

### Functions
  
* `graph` is a Digraph object
* `start` and `end` are Node objects
* `path` is a list of nodes
* `toPrint` is a boolean (to decide whether to print or not?)
* `shortest` is a list of nodes

————————————

* `DFS` is a function
* `BFS` is a function
* `shortestPath` is a wrapper for the `DFS` function. It serves to get the recursion started
  properly and provide appropriate abstraction. It does that by indicating that
    - the current path being explored is empty (`path == []`)
    - no path from `start` to `end` has yet been found (`shortest == None`)
* `printPath` is a function used to convert the result of `sp`, a path, to a string that can be
  printed. (Remember the `path` variable is defined as a list of nodes.)


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈***≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## Run a depth-first search

### `testSP` function for `DFS`

The function `testSP` (test shortest path) runs all the definitions made so far to, first, build a
directed graph(see image) and then search for a shortest path between node 0 and node 5.

![](https://github.com/juanantonio284/my_python_notes/blob/main/OOP/testSP_sample_graph.png)

```Python

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

```

**(i) create a list with Node objects**

This is a common list that's been named "nodes".  
The `for` loop creates 6 objects of the `Node` type, i.e. 6 nodes, using calls to the `Node` class
(called inside the parentheses).  
The name given to each node comes from the iteration of the loop (0, 1, 2, 3, 4, 5).  
These nodes are appended to the list using the `.append` method from the `list` class.
 
**(ii) create an object `g` of type Digraph**

**(iii) add nodes to digraph `g`**

Use the `addNode` method from the `Digraph` class to take the `Node` objects from the "nodes" list,
i.e. the nodes, and add them to `g`.
 
**(iv) add edges to digraph `g`**

First, the edges are created with calls like `Edge(nodes[0],nodes[1])`.  
Then the `addEdge` method from the `Digraph` class is used to add edges to `g`.  

Note that when calling `Edge`, you pass actual node objects as values for the source (`src`) and
destination (`dest`) arguments (these are not just the name of the nodes or some label). 

My thought: In a cognitive sense, this is different than mathematics. In mathematics, an abstraction
is made: it's irrelevant what a node is supposed to represent and a node—despite being an element
with relationships and characteristics—is reduced to just a name, e.g. `1`. (At least that's how
it's handled in the work, we write "1" and the node is used for the proof or whatever). In this
code, it's as if a node is a digital object that has to be created, stored, and passed. 

**(v) find the shortest path**

The `shortestPath` function is called and its return is bound to the name `sp`.  

**(vi) show the result** 

The `printPath` function is used to convert the result of `sp`, a path (really, a list), to a string
that can be printed. 

Then the `print` function is called, this call is within the function definition (not sure why), and
the user sees something like `Shortest path found by DFS: 0->2->3->5`.

#### Output

When executed as above, `testSP` produces the output:

```
Current DFS path: 0
Current DFS path: 0->1
Current DFS path: 0->1->2
Current DFS path: 0->1->2->3
Current DFS path: 0->1->2->3->4
Current DFS path: 0->1->2->3->5
Current DFS path: 0->1->2->4


Current DFS path: 0->2
Current DFS path: 0->2->3
Current DFS path: 0->2->3->4
Current DFS path: 0->2->3->5
Current DFS path: 0->2->3->1
Current DFS path: 0->2->4
Shortest path found by DFS: 0->2->3->5
```

Notice that after exploring the path `0->1->2->3->4`, it backs up to node 3 and explores the path
`0->1->2->3->5`. After saving that as the shortest successful path so far, it backs up to node 2
and explores the `path 0->1->2->4`. When it reaches the end of that path (node 4), it backs up all
the way to node 0 and investigates the path starting with the edge from 0 to 2. And so on.

<!-- #### Exercise -->
<!-- Page 321 "Finger exercise" -->
<!-- The `DFS` algorithm implemented in finds the path with the minimum number of edges. If the
     edges have weights, it will not necessarily find the path that minimizes the sum of the
     weights of the edges. However, it is easily modified to do so. Modify the DFS algorithm to
     find a path that minimizes the sum of the weights. Assume that all weights are positive
     integers. -->


<!-- ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈***≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ -->
## Run for a breadth-first search

### `testSP` function for `BFS`

```Python

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

```

#### Output

When executed as above, `testSP` produces the output:

```

Current BFS path: 0
Current BFS path: 0->1
Current BFS path: 0->2
Current BFS path: 0->1->2
Current BFS path: 0->2->3
Current BFS path: 0->2->4
Current BFS path: 0->1->2->3
Current BFS path: 0->1->2->4
Current BFS path: 0->2->3->4
Current BFS path: 0->2->3->5
Shortest path found by BFS: 0->2->3->5

```

In this case `DFS` and `BFS` found the same *shortest path* (`0->2->3->5`). However, if a graph
contains more than one *shortest path* between a pair of nodes, `DFS` and `BFS` will not
necessarily find the same one. As mentioned above, breadth-first search is a convenient way to
search for a path with the fewest edges because the first time a path is found, it is guaranteed to
be such a path.

<!-- #### Exercise -->
<!-- Page 323 "Finger exercise" -->
<!-- Consider a digraph with weighted edges. Is the first path found by BFS guaranteed to minimize
     the sum of the weights of the edges? -->
