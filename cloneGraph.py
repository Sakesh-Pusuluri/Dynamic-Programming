"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.visited={}
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        if node in self.visited:
            return self.visited[node]
        clonedNode = Node(node.val,[])
        self.visited[node]=clonedNode
        if node.neighbors:
            clonedNode.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return clonedNode
