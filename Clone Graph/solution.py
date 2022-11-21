"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            newNode = None
            return newNode
        newNode = Node(node.val, None)
        nodesSeen = {}
        nodesSeen[newNode.val] = newNode
        self.helper(node, newNode, nodesSeen)
        return newNode
    
    def helper(self, node, newNode, nodesSeen):
        for neighbor in node.neighbors:
            newNeighbor = None
            if neighbor.val in nodesSeen:
                newNeighbor = nodesSeen[neighbor.val]
                newNode.neighbors.append(newNeighbor)
            else:
                newNeighbor = Node(neighbor.val, None)
                newNode.neighbors.append(newNeighbor)
                nodesSeen[newNeighbor.val] = newNeighbor
                self.helper(neighbor, newNeighbor, nodesSeen)
