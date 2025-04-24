"""
Если задан целочисленный массив nums, верните максимально возможную сумму элементов массива, которая делится на три.
"""

# Input: nums = [3,6,5,1,8]
# Output: 18

def maxSumDivThree(nums):
    total_sum = sum(nums)
    if total_sum % 3 == 0:
        return total_sum
    
    mod1 = [x for x in nums if x % 3 == 1]
    mod2 = [x for x in nums if x % 3 == 2]
    
    mod1.sort()
    mod2.sort()
    
    if total_sum % 3 == 1:
        if len(mod1) >= 1 and len(mod2) >= 2:
            return max(total_sum - mod1[0], total_sum - sum(mod2[:2]))
        if len(mod1) >= 1:
            return total_sum - mod1[0]
        if len(mod2) >= 2:
            return total_sum - sum(mod2[:2])
    
    if total_sum % 3 == 2:
        if len(mod2) >= 1 and len(mod1) >= 2:
            return max(total_sum - mod2[0], total_sum - sum(mod1[:2]))
        if len(mod2) >= 1:
            return total_sum - mod2[0]
        if len(mod1) >= 2:
            return total_sum - sum(mod1[:2])
    
    return 0

if __name__ == "__main__":
    result = maxSumDivThree(nums = [3,6,5,1,8])
    print(result)