class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
       adjList = { i : [] for i in range(n) }
       for n1, n2 in edges:
              adjList[n1].append(n2)
              adjList[n2].append(n1)
       
       visited = set()

       def dfs(parentNode, currentNode):
              if currentNode in visited:
                     return False
              visited.add(currentNode)
              for nei in adjList[currentNode]:
                     if nei == parentNode:
                            continue
                     if not dfs(currentNode, nei):
                            return False
              return True

       return dfs(-1, 0) and len(visited) == n
       