# 求tree的每层的节点数，求哪一层具有最多节点数，节点数是多少
# input: root
# output: dic：key：每层序数，value：每层的node个数
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from copy import deepcopy
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:  # corner case
            return 0
        if not root.left and not root.right:  # corner case
            return 1

        queue = []
        queue.append([root, 0])  # index from 0 to i in every level
        res = []

        while queue:
            length = len(queue)  # use length to control the scan range, not scan lower level node
            res.append(deepcopy(queue))
            for i in range(length):  # length 是实际宽度
                node, index = queue.pop(0)
                if node.left:
                    queue.append([node.left, 2 * index])
                if node.right:
                    queue.append([node.right, 2 * index + 1])
        return res

from collections import deque
def constructTree(nodeList):  # input: list using bfs, output: root
    new_node = []
    for elem in nodeList:  # transfer list val to tree node
        if elem:
            new_node.append(TreeNode(elem))
        else:
            new_node.append(None)

    queue = deque()
    queue.append(new_node[0])

    resHead = queue[0]
    i = 1

    while i <= len(new_node) - 1:  # bfs method building
        head = queue.popleft()
        head.left = new_node[i]  # build left and push
        queue.append(head.left)
        if i + 1 == len(new_node):  # if no i + 1 in new_node
            break
        head.right = new_node[i + 1]  # build right and push
        queue.append(head.right)
        i = i + 2
    return resHead


root = constructTree([1,2,3,4,None,5])
x = Solution()
print(x.widthOfBinaryTree(root))