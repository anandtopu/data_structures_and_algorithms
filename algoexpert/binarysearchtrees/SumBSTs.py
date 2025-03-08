'''
You're given a Binary Tree. As with any Binary Tree, this tree may contain
one or more Binary Search Trees (BSTs), and it may even be a BST itself.
Write a function that returns the sum of all the values of nodes in this
tree which are part of a BST containing at least 3 nodes.
Each BinaryTree node has an integer value, a
left child node, and a right child node. Children
nodes can either be BinaryTree nodes themselves or
None / null.
A BST is a special type of Binary Tree whose nodes all satisfy the BST
property. A node satisfies the BST property if its value is
strictly greater than the values of every node to its left; its
value is less than or equal to the values of every node to its
right; and its children nodes are either valid BST nodes
themselves or None / null.
Sample Input #1
tree =     8
/    \
2       9
/   \       \
1     10       5
Sample Output #1
13 // 1, 2, and 10 form the only BST containing at least 3 nodes.
Sample Input #2
tree =            20
/                \
7                 10
/   \             /     \
0     8           5      15
/   \       /   \   /   \
7     9     2     5 13   22
/           \
1             14
Sample Output #2
118 // The subtrees rooted at 7 and 10 are both BSTs, and their node values add up to 118.
Sample Input #3
tree =            20
/                \
9                 10
/   \             /     \
0     8           6      15
/           /   \   /   \
7           2     5 17   22
/           \
1             14
Sample Output #3
0 // The subtrees rooted at 8 and 2 are both BSTs, but they only contain 2 nodes each.

'''
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def sumBsts(tree):
    return getTreeInfo(tree).totalSumBstNodes

def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(
            True,
            float("-inf"),
            float("inf"),
            0,
            0,
            0,
        )
    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)
    satisfiesBstProp = tree.value > leftTreeInfo.maxValue and tree.value <= rightTreeInfo.minValue
    isBst = satisfiesBstProp and leftTreeInfo.isBst and rightTreeInfo.isBst
    maxValue = max(tree.value, max(leftTreeInfo.maxValue, rightTreeInfo.maxValue))
    minValue = min(tree.value, min(leftTreeInfo.minValue, rightTreeInfo.minValue))
    bstSum = 0
    bstSize = 0
    totalSumBstNodes = leftTreeInfo.totalSumBstNodes + rightTreeInfo.totalSumBstNodes
    if isBst:
        bstSum = tree.value + leftTreeInfo.bstSum + rightTreeInfo.bstSum
        bstSize = 1 + leftTreeInfo.bstSize + rightTreeInfo.bstSize
        if bstSize >= 3:
            totalSumBstNodes = bstSum
    return TreeInfo(
        isBst,
        maxValue,
        minValue,
        bstSum,
        bstSize,
        totalSumBstNodes,
    )

class TreeInfo:
    def __init__(self, isBst, maxValue, minValue, bstSum, bstSize, totalSumBstNodes):
        self.isBst = isBst
        self.maxValue = maxValue
        self.minValue = minValue
        self.bstSum = bstSum
        self.bstSize = bstSize
        self.totalSumBstNodes = totalSumBstNodes