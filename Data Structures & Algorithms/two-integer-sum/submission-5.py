class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, n in enumerate(nums): 
            indices[n] = i # the key is the number, value is index

        for i, n in enumerate(nums): 
            complement = target - n
            if complement in indices and indices[complement] != i: 
                return [i, indices[complement]]

        return []