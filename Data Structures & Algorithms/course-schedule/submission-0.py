class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crsToPre = { i : [] for i in range(numCourses) }
        for crs, pre in prerequisites:
            crsToPre[crs].append(pre)
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if crsToPre[course] == []:
                return True
            visited.add(course)
            for pre in crsToPre[course]:
                if not dfs(pre): return False
            visited.remove(course)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True


"""
1. Map courses to prereqs
2. DFS on each course
    Check for loops (course visited already)
    Run dfs on prereqs for this course
3. return True


nC: 2
pre: [0,1]

crsToPre
0 -> 1
1 -> []
visited: ()


"""