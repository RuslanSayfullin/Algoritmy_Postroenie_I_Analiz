"""
Дана строка, содержащая значения, разделенные запятыми, представляющие предварительный обход дерева (preorder). 
Верните true, если это правильная сериализация предварительного обхода бинарного дерева.
"""

# Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Output: true

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        nodes = preorder.split(',')
        
        for node in nodes:
            slots -= 1
            if slots < 0:
                return False
            if node != '#':
                slots += 2
        
        return slots == 0
    
if __name__ == "__main__":
    example = Solution()
    res = example.isValidSerialization(preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#")
    print(res)