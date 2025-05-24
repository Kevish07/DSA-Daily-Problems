class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        c=[]
        for i in range(len(words)):
            if x in words[i]:
                c.append(i)
        return c
    

# Optimized

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]