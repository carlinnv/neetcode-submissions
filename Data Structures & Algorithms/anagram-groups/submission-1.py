class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for string in strs: 
            sortedStr = ''.join(sorted(string))
            if sortedStr in res: 
                res[sortedStr].append(string) 
            else: 
                res[sortedStr] = [string] 
            
        return list(res.values())