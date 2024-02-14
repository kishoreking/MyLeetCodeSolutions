class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a1,a2,ans=[],[],[]
        for num in nums:
            if num>=0:
                a1.append(num)
            else:
                a2.append(num)
        i1,i2=0,0
        while i1< len(nums)//2:
            ans.append(a1[i1])
            i1=i1+1
            ans.append(a2[i2])
            i2=i2+1
        return ans