"""
Вам дан массив целых чисел nums и два целых числа indexDiff и valueDiff.
Найдите пару индексов (i, j) таких, что:
i != j,
abs(i - j) <= indexDiff,
abs(nums[i] - nums[j]) <= valueDiff.

Верните true, если такая пара существует, или false в противном случае.
"""

"""
Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
"""

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0: return False
        buckets = {}
        w = t + 1

        for i in range(len(nums)):
            bucket = nums[i] // w if nums[i] >= 0 else (nums[i] + 1) // w - 1
            if bucket in buckets: return True
            if bucket - 1 in buckets and abs(nums[i] - buckets[bucket - 1]) < w: return True
            if bucket + 1 in buckets and abs(nums[i] - buckets[bucket + 1]) < w: return True
            buckets[bucket] = nums[i]
            if i >= k:
                del buckets[nums[i - k] // w if nums[i - k] >= 0 else (nums[i - k] + 1) // w - 1]
        return False

if __name__ == "__main__":
    example = Solution()
    result = example.containsNearbyAlmostDuplicate(nums = [1,2,3,1], k = 3, t = 0)
    print(result)