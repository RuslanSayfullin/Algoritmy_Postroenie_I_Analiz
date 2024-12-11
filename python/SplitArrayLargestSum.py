# Учитывая целочисленный массив nums и целое число k, разбейте nums на k непустых подмассивов так, чтобы наибольшая сумма любого подмассива была минимальна. 
# Верните минимизированную наибольшую сумму разбиения. Подмассив - это смежная часть массива.

"""
Input: nums = [7,2,5,10,8], k = 2
Output: 18
"""

def splitArray(nums, k):
    def canSplit(nums, k, maxSum):
        currentSum = 0
        subarrays = 1
        for num in nums:
            if currentSum + num > maxSum:
                currentSum = num
                subarrays += 1
                if subarrays > k:
                    return False
            else:
                currentSum += num
        return True
    
    left, right = max(nums), sum(nums)
    while left < right:
        mid = (left + right) // 2
        if canSplit(nums, k, mid):
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == "__main__":
    result = splitArray(nums = [7,2,5,10,8], k = 2)
    print(result)