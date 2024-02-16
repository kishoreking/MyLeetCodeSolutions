class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        distinct_nums = len(set(arr))
        frequencies = {}

        for num in arr:
            frequencies[num] = frequencies.get(num, 0) + 1
        
        for value in sorted(frequencies.values()):
            if value <= k:
                distinct_nums -= 1
                k = k - value

        return distinct_nums   