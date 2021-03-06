import collections

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        value_list = collections.deque([(beginWord, 1)])
        value_dict = set(wordList)
        visit_value_dict = set()
        res = 0
        
        while value_list:
            temp_value = len(value_list)
            
            for _ in range(temp_value):
                word, cost = value_list.popleft()
                
                if word == endWord:
                    res = cost
                    
                    return res
                
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + char + word[i + 1:]
                        
                        if not new_word in visit_value_dict and new_word in value_dict:
                            value_list.append((new_word, cost + 1))
                            visit_value_dict.add(new_word)
                            
        return res