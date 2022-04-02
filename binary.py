
from cgi import print_arguments
from distutils.log import info
from unittest import result
    
class Info:
    def __init__(self): #gives the depth of each subtree and helps with calculate_time method
        self.leftDepth = 0
        self.rightDepth = 0
        self.contains = False
        self.time = -1
class BinaryTree:
    def __init__(self, root_obj, left=None, right=None):
        self.__key = root_obj
        self.left = left
        self.right = right
        result = 0
        self.left_list=[]
        self.right_list=[]
        self.info = Info()
        self.info.contains = True
        self.info.time = 0
        self.info.leftDepth = 0
        self.info.rightDepth = 0
        if self.left is not None:
            self.info.leftDepth = self.left.info.leftDepth + 1
        if self.right is not None:
            self.info.rightDepth = self.right.info.rightDepth + 1
        if self.left is not None and self.right is not None:
            self.info.leftDepth = self.left.info.leftDepth + 1
            self.info.rightDepth = self.right.info.rightDepth + 1
            if self.left.info.contains and self.right.info.contains:
                self.info.contains = True
                self.info.time = self.left.info.time + self.right.info.time
            else:
                self.info.contains = False
                self.info.time = -1
        elif self.left is not None:
            self.info.leftDepth = self.left.info.leftDepth + 1
            self.info.rightDepth = self.left.info.rightDepth
            if self.left.info.contains:
                self.info.contains = True
                self.info.time = self.left.info.time
            else:
                self.info.contains = False
                self.info.time = -1
    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(self.__key,end=" ")
    def sum_tree(self, root):
        if root is None:
            return 0
        else:
            return root.__key + self.sum_tree(root.left) + self.sum_tree(root.right)
    
        
    def check_leaf(self, root):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return True
        else:
            return False
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.__key,end=" ")
        if self.right is not None:
            self.right.inorder()
    def insetion(self, key):
        if self.__key == key:
            return False
        elif self.__key > key:
            if self.left is None:
                self.left = BinaryTree(key)
                return True
            else:
                return self.left.insetion(key)
        else:
            if self.right is None:
                self.right = BinaryTree(key)
                return True
            else:
                return self.right.insetion(key)
    
    
    def calculate_time(self, node, info, target):
        if node is None:
            return 0
        if node.__key == target:
            info.contains = True
            info.time = 0
            return 0
        if node.left is not None:
            info.leftDepth = node.left.info.leftDepth + 1
        if node.right is not None:
            info.rightDepth = node.right.info.rightDepth + 1
        if node.left is not None and node.right is not None:
            info.leftDepth = node.left.info.leftDepth + 1
            info.rightDepth = node.right.info.rightDepth + 1
            if node.left.info.contains and node.right.info.contains:
                info.contains = True
                info.time = node.left.info.time + node.right.info.time
            else:
                info.contains = False
                info.time = -1
        elif node.left is not None:
            info.leftDepth = node.left.info.leftDepth + 1
            info.rightDepth = node.left.info.rightDepth
            if node.left.info.contains:
                info.contains = True
                info.time = node.left.info.time
            else:
                info.contains = False
                info.time = -1
        else:
            info.leftDepth = node.right.info.leftDepth
            info.rightDepth = node.right.info.rightDepth + 1
            if node.right.info.contains:
                info.contains = True
                info.time = node.right.info.time
            else:
                info.contains = False
                info.time = -1
        if info.contains:
            return info.time
        else:
            return -1
    def solve(self, root, target):
        info = Info()
        return self.sum_tree(root) + self.calculate_time(root, info, target)
    def search(self, root, target):
        if root is None:
            return False
        if root.__key == target:
            if root.left is None and root.right is None:
                return True
           
        elif root.__key > target:
            return self.search(root.left, target)
        else:
            return self.search(root.right, target)
        
bst=BinaryTree(0)
class Solution():	
    result = 0
    
    def calculate_time(self, node, info, target):
        if bst.search(node, target):
            return bst.sum_tree(node)
        else:
            print("the node must be leaf")
            return -1
    def solve(self, root, target):
        info = Info()
        self.result=self.calculate_time(root, info, target)
        return self.result

if __name__ == '__main__':
    # print("This is a binary tree implementation")
    tree = BinaryTree(8)
    info = Info()
    tree.insetion(2)
    tree.insetion(4)
    tree.insetion(16)
    tree.insetion(32)
    tree.insetion(64)
    tree.insetion(128)
    tree.insetion(256)
    tree.insetion(512)
    tree.insetion(1024)
    tree.insetion(2048)
    # print("inorder:")
    # tree.inorder()
    # print("\npostorder:")
    # tree.postorder()
    # print("\n")
    slove_1=Solution()
    
    print(slove_1.solve(tree,2048),"sec")
    # x=tree.search(16)
    # print(x)
    # print(tree.left_list)
    # print(tree.right_list)
    # print(tree.sum_tree(tree))
    # print(tree.calculate_time(tree, info, 16))
    # # Code that builds the tree like in the binary.pdf example.
    
    #s = Solution()
    #print(s.solve(racine, target))
