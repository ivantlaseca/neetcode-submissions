"""
T: O(V + E)
S: O(V + E)

"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create adjacency list and set
        adjList = { i : [] for i in range(numCourses) }
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        visited = set()

        # DFS
        def dfs(course):
            if adjList[course] == []:
                return True
            if course in visited:
                return False
            visited.add(course)
            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            adjList[course] = []
            return True

        # Running the DFS
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
        
        