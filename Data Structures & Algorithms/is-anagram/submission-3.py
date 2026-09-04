class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        HashS = {}
        HashT = {}
        lenS = len(s)
        lenT = len(t)

        if lenS != lenT:
            return False
        
        for i in range(lenS):
            HashS[s[i]] = 1 + HashS.get(s[i],0) 
            HashT[t[i]] = 1 + HashT.get(t[i],0)

        return HashS == HashT