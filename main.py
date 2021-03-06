from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    ### TODO
    def dijkstra(visited, frontier):
      if len(frontier) == 0:
        return visited
      else:
        distance, cnt, node = heappop(frontier)
        if node in visited:
          return dijkstra(visited, frontier)
        else:
          visited[node] = (distance, cnt)
          for neighbor, weight in graph[node]:
            heappush(frontier, (distance + weight, cnt + 1, neighbor))
          return dijkstra(visited, frontier)
    
    frontier = []
    heappush(frontier, (0, 0, source))
    visited = dict()
    return dijkstra(visited, frontier)
    
def test_shortest_shortest_path():

    graph = {
                's': {('a', 1), ('c', 4)},
                'a': {('b', 2)}, # 'a': {'b'},
                'b': {('c', 1), ('d', 4)}, 
                'c': {('d', 3)},
                'd': {},
                'e': {('d', 0)}
            }
    result = shortest_shortest_path(graph, 's')
    # result has both the weight and number of edges in the shortest shortest path
    assert result['s'] == (0,0)
    assert result['a'] == (1,1)
    assert result['b'] == (3,2)
    assert result['c'] == (4,1)
    assert result['d'] == (7,2)
    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO
    queue = []
    visited = {}
    for u in graph.keys():
      visited[u] = False
    visited[source] = True
    res = {}
    queue.append(source)
    while queue:
      u = queue.pop(0)
      for v in graph[u]:
        if visited[v] == False:
          queue.append(v)
          visited[v] = True
          res[v] = u
    return res

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }

def test_bfs_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert parents['a'] == 's'
    assert parents['b'] == 's'    
    assert parents['c'] == 'b'
    assert parents['d'] == 'c'
    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    res = ''
    while destination in parents:
      res += parents[destination]
      destination = parents[destination]
    return res[::-1]

def test_get_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert get_path(parents, 'd') == 'sbc'
