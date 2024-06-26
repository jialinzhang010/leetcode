# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'None'
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val) + ',' + left + ',' + right

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        def traversal():
            nxt = vals.pop(0)
            if nxt == 'None':
                return None
            new = TreeNode(int(nxt))
            new.left = traversal()
            new.right = traversal()
            return new
        return traversal()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))