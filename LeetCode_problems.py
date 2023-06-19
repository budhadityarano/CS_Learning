#

## Two Sums 

# Brute force solution of two sum problem
class Solution:
    def twoSum_bruteforce(self, nums: List[int], target: int) -> List[int]:
        n - len(nums)
        for i in range(n -1):
            for j in range(i+1,n):
                if nums[i] + nums[j]==target
                    return [i,j]
        return [] #No solution found
      
      
    def twoSum_hash_1(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        # Creating the hash map
        for i in range(n):
            numMap[nums[i]] = i


        # Find the complement
        for i in range(n):
            complement = target - num[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []
