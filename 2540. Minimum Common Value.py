class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        z=(set(nums1)).intersection(set(nums2))
        return min(z) if len(z)>0 else -1 