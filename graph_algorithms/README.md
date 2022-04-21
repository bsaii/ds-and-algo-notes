# Graph

A graph is a data structure that consists of the following two components:

1. A finite set of vertices also called as nodes.
2. A finite set of ordered pair of the form (u, v) called as edge. The pair is ordered because (u, v) is not the same as (v, u) in case of a directed graph(di-graph). The pair of the form (u, v) indicates that there is an edge from vertex u to vertex v. The edges may contain weight/value/cost.

Graphs are used to represent many real-life applications: Graphs are used to represent networks. The networks may include paths in a city or telephone network or circuit network. Graphs are also used in social networks like linkedIn, Facebook. For example, in Facebook, each person is represented with a vertex(or node). Each node is a structure and contains information like person id, name, gender, and locale.

The following is an example of an undirected graph with 5 vertices.

![Undirected Graph](https://i.imgur.com/xkgMnwx.png)

**The following two are the most commonly used representations of a graph**.

1. Adjacency Matrix
2. Adjacency List

There are other representations also like, Incidence Matrix and Incidence List. The choice of graph representation is situation-specific. It totally depends on the type of operations to be performed and ease of use.

## 1. Adjacency Matrix

Adjacency Matrix is a 2D array of size V x V where V is the number of vertices in a graph. Let the 2D array be `adj[][]`, a slot `adj[i][j] = 1` indicates that there is an edge from vertex i to vertex j. Adjacency matrix for undirected graph is always symmetric. Adjacency Matrix is also used to represent weighted graphs. If `adj[i][j] = w`, then there is an edge from vertex i to vertex j with weight w.

The adjacency matrix for the above example graph is:

![Adjency Matrix](https://i.imgur.com/oswYKTW.png)

_Pros_: Representation is easier to implement and follow. Removing an edge takes O(1) time. Queries like whether there is an edge from vertex ‘u’ to vertex ‘v’ are efficient and can be done O(1).

_Cons_: Consumes more space O(V^2). Even if the graph is sparse(contains less number of edges), it consumes the same space. Adding a vertex is O(V^2) time.

### Implementation of taking input for adjacency matrix

```python
#A simple representation of graph using Adjacency Matrix
class Graph:
    def __init__(self,numvertex):
        self.adjMatrix = [[-1]*numvertex for x in range(numvertex)]
        self.numvertex = numvertex
        self.vertices = {}
        self.verticeslist =[0]*numvertex

    def set_vertex(self,vtx,id):
        if 0<=vtx<=self.numvertex:
            self.vertices[id] = vtx
            self.verticeslist[vtx] = id

    def set_edge(self,frm,to,cost=0):
        frm = self.vertices[frm]
        to = self.vertices[to]
        self.adjMatrix[frm][to] = cost
        #for directed graph do not add this
        self.adjMatrix[to][frm] = cost

    def get_vertex(self):
        return self.verticeslist

    def get_edges(self):
        edges=[]
        for i in range (self.numvertex):
            for j in range (self.numvertex):
                if (self.adjMatrix[i][j]!=-1):
                    edges.append((self.verticeslist[i],self.verticeslist[j],self.adjMatrix[i][j]))
        return edges
        
    def get_matrix(self):
        return self.adjMatrix

G =Graph(6)
G.set_vertex(0,'a')
G.set_vertex(1,'b')
G.set_vertex(2,'c')
G.set_vertex(3,'d')
G.set_vertex(4,'e')
G.set_vertex(5,'f')
G.set_edge('a','e',10)
G.set_edge('a','c',20)
G.set_edge('c','b',30)
G.set_edge('b','e',40)
G.set_edge('e','d',50)
G.set_edge('f','e',60)
print("Vertices of Graph")
print(G.get_vertex())
print("Edges of Graph")
print(G.get_edges())
print("Adjacency Matrix of Graph")
print(G.get_matrix())
```

**Output**:

  ```txt
  Vertices of Graph
  ['a', 'b', 'c', 'd', 'e', 'f']
  Edges of Graph
  [('a', 'c', 20), ('a', 'e', 10), ('b', 'c', 30), ('b', 'e', 40), ('c', 'a', 20), ('c', 'b', 30), ('d', 'e', 50), ('e', 'a', 10), ('e', 'b', 40), ('e', 'd', 50), ('e', 'f', 60), ('f', 'e', 60)]
  Adjacency Matrix of Graph
  [[-1, -1, 20, -1, 10, -1], [-1, -1, 30, -1, 40, -1], [20, 30, -1, -1, -1, -1], [-1, -1, -1, -1, 50, -1], [10, 40, -1, 50, -1, 60], [-1, -1, -1, -1, 60, -1]]
  ```

## 2. Adjacency List

An array of lists is used. The size of the array is equal to the number of vertices. Let the array be an array[]. An entry array[i] represents the list of vertices adjacent to the ith vertex. This representation can also be used to represent a weighted graph. The weights of edges can be represented as lists of pairs.

Following is the adjacency list representation of the above graph.

![Adjacency List](https://i.imgur.com/rgMwkIW.png)

### Implementation of taking input for adjacency list (using linked list)

```python
"""
A Python program to demonstrate the adjacency
list representation of the graph
"""

# A class to represent the adjacency list of the node (The linked List)

class AdjNode:
 def __init__(self, data):
  self.vertex = data
  self.next = None


# A class to represent a graph. A graph is the list of the adjacency lists.
# Size of the array will be the number of the vertices "V"

class Graph:
 def __init__(self, vertices):
  self.V = vertices
  self.graph = [None] * self.V

 # Function to add an edge in an undirected graph
 def add_edge(self, src, dest):
  # Adding the node to the source node
  node = AdjNode(dest)
  node.next = self.graph[src]
  self.graph[src] = node

  # Adding the source node to the destination as
  # it is the undirected graph
  node = AdjNode(src)
  node.next = self.graph[dest]
  self.graph[dest] = node

 # Function to print the graph
 def print_graph(self):
  for i in range(self.V):
   print("Adjacency list of vertex {}\n head".format(i), end="")
   temp = self.graph[i]
   while temp:
    print(" -> {}".format(temp.vertex), end="")
    temp = temp.next
   print(" \n")


# Driver program to the above graph class
if __name__ == "__main__":
 V = 5
 graph = Graph(V)
 graph.add_edge(0, 1)
 graph.add_edge(0, 4)
 graph.add_edge(1, 2)
 graph.add_edge(1, 3)
 graph.add_edge(1, 4)
 graph.add_edge(2, 3)
 graph.add_edge(3, 4)

 graph.print_graph()

```

**Output**:

  ```txt
  Adjacency list of vertex 0
  head -> 1-> 4

  Adjacency list of vertex 1
  head -> 0-> 2-> 3-> 4

  Adjacency list of vertex 2
  head -> 1-> 3

  Adjacency list of vertex 3
  head -> 1-> 2-> 4

  Adjacency list of vertex 4
  head -> 0-> 1-> 3
  ```

### Simple representation of graph using adjacency list

```python
# Number of nodes
num_nodes = 5

# Edges represents the connection between the nodes
edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]


# class for the graph
class Graph:
  def __init__(self, num_nodes, edges):
    self.num_nodes =  num_nodes
    self.data = [[] for _ in range(num_nodes)] # created a list of empty list

    for n1, n2 in edges:
      # insert into the list of empty list
      self.data[n1].append(n2)
      self.data[n2].append(n1)
      
  
  """ A function to write the code as the diagram above """
  def __repr__(self):
    return "\n".join(["{}: {}".format(n, neighbors) for n, neighbors in enumerate(self.data)])
    # enumerate returns the index and value

  # to return the string format
  def __str__(self):
    return self.__repr__()


# Calling the class
graph1 = Graph(num_nodes, edges)

print(graph1.data)

# the representation of the diagram in code
print(graph1)
```

**Output**:

  ```txt

  From graph.data
  [[1, 4], [0, 2, 3, 4], [1, 3], [1, 2, 4], [0, 1, 3]]

  The representation of the graph in code
  0: [1, 4]
  1: [0, 2, 3, 4]
  2: [1, 3]
  3: [1, 2, 4]
  4: [0, 1, 3]
  ```

_Pros_: Saves space O(|V|+|E|) . In the worst case, there can be C(V, 2) number of edges in a graph thus consuming O(V^2) space. Adding a vertex is easier.

_Cons_: Queries like whether there is an edge from vertex u to vertex v are not efficient and can be done O(V).

## Breadth First Search or BFS for a Graph

Breadth-first search (BFS) is an algorithm for searching a tree data structure for a node that satisfies a given property. It starts at the tree root and explores all nodes at the present depth prior to moving on to the nodes at the next depth level. Extra memory, usually a queue, is needed to keep track of the child nodes that were encountered but not yet explored.

For example, in the following graph, we start traversal from vertex 2. When we come to vertex 0, we look for all adjacent vertices of it. 2 is also an adjacent vertex of 0. If we don’t mark visited vertices, then 2 will be processed again and it will become a non-terminating process.

**BFS pseudocode (Wikipedia)**:
_Input_: A graph G, and starting vertex root of G

_Output_: Goal state. The parent links trace the shortest path back to root

```txt
 1  procedure BFS(G, root) is
 2      let Q be a queue
 3      label root as discovered
 4      Q.enqueue(root)
 5      while Q is not empty do
 6          v := Q.dequeue()
 7           if v is the goal then
 8              return v
 9          for all edges from v to w in G.adjacentEdges(v) do
10              if w is not labeled as discovered then
11                  label w as discovered
12                  Q.enqueue(w)
```

**[Read More about Breadth First Search](https://en.wikipedia.org/wiki/Breadth-first_search)**

![BFS](https://i.imgur.com/E2Up1Pk.png)

### Implementation of Breadth-First Search

Following are the implementations of simple Breadth-First Traversal from a given source.
The implementation uses an adjacency list representation of graphs.

```python
def bfs(graph, root):
  queue = []

  # all data not discovered
  discovered = [False] * len(graph.data)

  # Enqueue root
  queue.append(root)

  # label root as discovered
  discovered[root] = True

  # Dequeue discovered
  idx = 0
  while idx < len(queue):
    current = queue[idx]
    idx += 1

    # check all edges of current
    for node in graph.data[current]:
      if not discovered[node]:
        discovered[node] = True # label as discovered
        queue.append(node)

  return queue
```

**Input**:

  ```python
  """
  The adjacency list representation of the graph1
  0: [1, 4]
  1: [0, 2, 3, 4]
  2: [1, 3]
  3: [1, 2, 4]
  4: [0, 1, 3]
  """

  bfs(graph1, 3)
  ```

**Output**:

  ```txt
  Following is Breadth First Traversal (starting from vertex/node 3)

  [3, 1, 2, 4, 0]
  ```

**Complexity Analysis**:

>**Time Complexity**: _O(V+E)_ where V is a number of vertices in the graph and E is a number of edges in the graph.
>**Space Complexity**: _O(V)_

## Depth First Search or DFS for a Graph

Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.

**DFS pseudocode (Wikipedia)**:

1. A recursive implementation of DFS:
  
  ```txt
  procedure DFS(G, v) is
    label v as discovered
    for all directed edges from v to w that are in G.adjacentEdges(v) do
        if vertex w is not labeled as discovered then
            recursively call DFS(G, w)
    ```

2. A non-recursive implementation of DFS with worst-case space complexity {\displaystyle O(|E|)}O(|E|), with the possibility of duplicate vertices on the stack:

  ```txt
  procedure DFS_iterative(G, v) is
    let S be a stack
    S.push(v)
    while S is not empty do
        v = S.pop()
        if v is not labeled as discovered then
            label v as discovered
            for all edges from v to w in G.adjacentEdges(v) do 
                S.push(w)
  ```

**[Read More about Depth First Search](https://en.wikipedia.org/wiki/Depth-first_search)**

### Implementation of Depth First Search

```python
def dfs(graph, root):
  stack = []

  # all nodes are false
  discovered = [False] * len(graph.data)

  result = []

  stack.append(root)

  while len(stack) > 0:
    current = stack.pop()
    if not discovered[current]:
      discovered[current] = True
      result.append(current)
      for node in graph.data[current]:
        if not discovered[node]:
          stack.append(node)

  return result
```

**Input**:
  
  ```python
  dfs(graph1, 3)
  ```

**Output**:

  ```txt
  The Depth First Traversal (starting from vertex/node 3)

  [3, 4, 1, 2, 0]
  ```

**Complexity Analysis**:

>**Time Complexity**: _O(V+E)_ where V is a number of vertices in the graph and E is a number of edges in the graph.
>**Space Complexity**: _O(V)_, since an extra visited array of size V is required.

#### More Info

- [GeeksforGeeks](https://www.geeksforgeeks.org/graph-and-its-representations/?ref=lbp)
