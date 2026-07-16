class Solution:



    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crsToPre = { i : [] for i in range(numCourses) }
        for crs,pre in prerequisites:
            crsToPre[crs].append(pre)
        path = set()

        def dfs(course):
            if crsToPre[course] == []:
                return True
            if course in path:
                return False
            path.add(course)
            for nei in crsToPre[course]:
                if not dfs(nei):
                    return False
            path.pop()
            crsToPre[course] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True



        