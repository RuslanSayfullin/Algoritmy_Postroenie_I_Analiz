# Дан корень бинарного дерева, верните вертикальный порядок обхода значений его узлов (т.е. сверху вниз, столбец за столбцом).
# Если два узла находятся в одной строке и столбце, порядок должен быть слева направо.


"""
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
"""

from collections import defaultdict

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        columnTable = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)
                
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))
                        
        return [columnTable[x] for x in sorted(columnTable.keys())]

if __name__ == "__main__":
    example = Solution()
    result = example.verticalOrder(root = [3,9,20,null,null,15,7])
    print(result)