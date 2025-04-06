"""
Вам даны заголовки двух отсортированных связанных списков list1 и list2. 
Объедините два списка в один отсортированный список. 
Список должен быть составлен путем сращивания узлов первых двух списков. 
Возвращает заголовок объединенного связанного списка.  
"""

# Input: list1 = [1,2,4], list2 = [1,3,4]  
# Output: [1,1,2,3,4,4]  

class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        cur.next = l1 or l2
        return dummy.next
    

if __name__ == "__main__":
    example = Solution
    result = Solution.mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4] )
    print(result)