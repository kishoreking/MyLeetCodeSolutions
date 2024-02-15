class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        sval=0
        ans=-1
        for num  in nums:
            if num<sval:
                ans=num+sval
            sval=sval+num
        return ans