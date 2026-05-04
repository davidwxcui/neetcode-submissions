# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt=0
        ret=0
        def dfs(node,k):
            nonlocal cnt
            nonlocal ret
            if not node:
                return None
            
            dfs(node.left,k)
            cnt+=1
            if cnt==k:
                ret=node.val

            dfs(node.right,k)
        dfs(root,k)
        return ret