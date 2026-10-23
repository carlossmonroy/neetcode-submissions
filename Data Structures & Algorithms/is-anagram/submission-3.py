class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if len(s) != len(t):
            return False
        
        s_Dict, t_Dict = {} , {}

        for i in range(len(s)):
            s_Dict[s[i]] = 1 + s_Dict.get(s[i] , 0)
            t_Dict[t[i]] = 1 + t_Dict.get(t[i] , 0)
        print(s_Dict)
        print(t_Dict)
        return (s_Dict == t_Dict)


