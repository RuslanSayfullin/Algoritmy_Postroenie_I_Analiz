# Вам даны два бинарных дерева root1 и root2. 
# Представьте, что при наложении одного из них на другое некоторые узлы двух деревьев перекрываются, а другие - нет. 

"""
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
"""

from TreeNode import TreeNode

def mergeTrees(root1, root2):
    if not root1:
        return root2
    if not root2:
        return root1
    
    mergedNode = TreeNode(root1.val + root2.val)
    mergedNode.left = mergeTrees(root1.left, root2.left)
    mergedNode.right = mergeTrees(root1.right, root2.right)
    
    return mergedNode


if __name__ == "__main__":
    result = mergeTrees(root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7])
    print(result)