"""
[0,1]
nC = 2

0 -> [1]
1 -> []

Algo:
Create adj list
DFS on each course
DFS:
Base: No prereqs, return True
Searching for cycles on this course and it's prereqs

"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crsToPre = defaultdict(list)
        for crs, pre in prerequisites:
            crsToPre[crs].append(pre)

        seen = set()
        def isValid(course):
            if crsToPre[course] == []:
                return True
            if course in seen:
                return False
            seen.add(course)
            for pre in crsToPre[course]:
                if not isValid(pre):
                    return False
            seen.remove(course)
            crsToPre[course] = []
            return True
        
        for course in range(numCourses):
            if not isValid(course):
                return False
        
        return True

        