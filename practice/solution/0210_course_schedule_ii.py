import collections

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        value_graph = collections.defaultdict(list)
        degree_value_list = [0] * numCourses
        value_list = collections.deque()
        res = []
        
        for a, b in prerequisites:
            value_graph[b].append(a)
            degree_value_list[a] += 1
            
        for i in range(numCourses):
            if not degree_value_list[i]:
                value_list.append(i)
                
        while value_list:
            temp_value = len(value_list)
            
            for _ in range(temp_value):
                b = value_list.popleft()
                res.append(b)
                
                for a in value_graph[b]:
                    degree_value_list[a] -= 1

                    if not degree_value_list[a]:
                        value_list.append(a)

        if len(res) != numCourses:
            res = []
                    
        return res