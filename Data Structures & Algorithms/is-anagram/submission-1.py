class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 
        
        s_string = sorted(list(s))
        t_string = sorted(list(t))

        if s_string != t_string: 
            return False

        return True 