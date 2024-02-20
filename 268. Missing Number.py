class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n1=sum(nums)
        a=(len(nums)*(len(nums)+1))//2
        return abs(a-n1)        