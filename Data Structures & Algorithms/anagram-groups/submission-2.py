class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #initialize new keys with empty lists as values 

        for s in strs: 
            sortedString = ''.join(sorted(s)) 
            res[sortedString].append(s)
        
        return list(res.values()) 