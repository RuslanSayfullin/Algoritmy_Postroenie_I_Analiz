# Учитывая корень двоичного дерева, постройте строковую матрицу res с индексом 0 размером m x n, которая представляет собой форматированную раскладку дерева.
# Форматированная матрица должна быть построена по следующим правилам: 
#   высота дерева равна height, количество строк m должно быть равно height + 1.
#   Количество столбцов n должно быть равно 2height+1 - 1.
# Поместите корневой узел в середину верхней строки (более формально, в позицию res[0][(n-1)/2]).
# Для каждого узла, который был помещен в матрицу в позицию res[r][c], поместите его левого ребенка в res[r+1][c-2height-r-1], а правого - в res[r+1][c+2height-r-1].
# Продолжайте этот процесс, пока не будут размещены все узлы дерева. Любые пустые ячейки должны содержать пустую строку "". 
# Верните построенную матрицу res.

"""
Input: root = [1,2]
Output: 
[["","1",""],
 ["2","",""]]
 """

 class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findHeight(root):
    if not root:
        return -1
    return 1 + max(findHeight(root.left), findHeight(root.right))

def fill(res, root, r, c, height):
    if not root:
        return
    res[r][c] = str(root.val)
    if root.left:
        fill(res, root.left, r + 1, c - (1 << (height - r - 1)), height)
    if root.right:
        fill(res, root.right, r + 1, c + (1 << (height - r - 1)), height)

def printTree(root):
    height = findHeight(root)
    m = height + 1
    n = (1 << (height + 1)) - 1
    res = [["" for _ in range(n)] for _ in range(m)]
    fill(res, root, 0, (n - 1) // 2, height)
    return res