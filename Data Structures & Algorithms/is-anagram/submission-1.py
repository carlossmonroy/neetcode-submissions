class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_Dict, t_Dict = {} , {}
    
        if len(s) != len(t):
            return False
        else:

            for characters in s:
                if characters not in s_Dict:
                    s_Dict[characters] = 1
                else:
                    s_Dict[characters] += 1
            for characters in t:
                if characters not in t_Dict:
                    t_Dict[characters] = 1
                else:
                    t_Dict[characters] += 1       

            for keys in s_Dict:
                if keys not in t_Dict:
                    return False
                elif s_Dict[keys] != t_Dict[keys]:
                    return False
        return True
