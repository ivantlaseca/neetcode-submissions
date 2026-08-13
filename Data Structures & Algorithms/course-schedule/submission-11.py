"""
crsToPre = 
{
0 -> 1
1 -> []
}

Algo:

Create adj list
DFS on each course, looking for cycles

DFS
Base: No prereq so true
If crs in seen, return False
DFS on this course's prereqs
Remove crs from set and set val of course in map to []
Return true

T: O(V + E), recursive algo on a adj list
S: O(V + E), stack will take that much space in the worst case

Tests:
in: nC = 2, pre = [[0,1]]
out: true

in: nC = 1, pre = []
out: true

in: nC = 2, pre = [[0,1],[1,0]]
out: false
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crsToPre = defaultdict(list)
        for crs, pre in prerequisites:
            crsToPre[crs].append(pre)

        seen = set()
        def dfs(course):
            if not crsToPre[course]:
                return True
            if course in seen:
                return False
            seen.add(course)
            for pre in crsToPre[course]:
                if not dfs(pre):
                    return False
            seen.remove(course)
            crsToPre[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True

