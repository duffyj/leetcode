"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

#Recursive function that looks up node in cache and returns it. If it not there it creates a copy and adds it to the cache and copies all the depended by calling the function recursively.

class Solution:
    def cloneGraph(self, node):
        nodeRefs = {}

        def copyNode(srcNode):
            if srcNode.val in nodeRefs:
                return nodeRefs[srcNode.val]
    
            destNode = Node()
            destNode.val = srcNode.val
            nodeRefs[srcNode.val] = destNode
            for adjNode in srcNode.neighbors:
                destNode.neighbors.append(copyNode(adjNode))

            return destNode
        return copyNode(node) if node else None
        
class Solution2:
    def cloneGraph(self, node):
        if node:
            nodeRefs = {}
            copiedNodes = set()

            def createNode(val):
                if val in nodeRefs:
                    destNode = nodeRefs[val]
                else:
                    destNode = Node()
                    destNode.val = val
                    nodeRefs[val] = destNode
                return destNode

            def copyNode(srcNode,destNode=None):
                if not destNode:
                    destNode = createNode(srcNode.val)
                
                if srcNode.val not in copiedNodes:
                    copiedNodes.add(srcNode.val)
                    for adjNode in srcNode.neighbors:
                        destNode.neighbors.append(copyNode(adjNode))
                return destNode

            #setup
            res = copyNode(node,createNode(node.val))
            return res





            