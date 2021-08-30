# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        cur_node = root
        cur_str = ''
        if cur_node:
            q = []
            q.append((cur_node, str(cur_node.val)))
            while q:
                cur_node, cur_str = q.pop(-1)
                if cur_node.left:
                    q.append((cur_node.left, cur_str + '->' + str(cur_node.left.val)))
                
                if cur_node.right:
                    q.append((cur_node.right, cur_str + '->' + str(cur_node.right.val)))
                
                if not cur_node.left and not cur_node.right:
                    result.append(cur_str)
        
        return result
