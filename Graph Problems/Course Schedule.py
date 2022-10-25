class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # initializing the hashmap with each course mapping to an empty list
        preMap = { i:[] for i in range(numCourses) }
        
        # updating the hashmap with mapping the prereqs to courses
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        # marking all the visited course node
        visitSet = set()
        
        # creating the recursive dfs function, passing only the current node we are visiting
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs) # just like all other graph probs, remove the visited node
            preMap[crs] = [] # and set that to empty list if we come back to this node we'll know it is taken

            return True
        
        # now just calling the dfs on each node 
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
