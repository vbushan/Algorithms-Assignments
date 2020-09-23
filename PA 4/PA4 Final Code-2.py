# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:02:34 2020

@author: Vamsi
"""

from __future__ import annotations

from typing import Optional, List

import unittest

class Node:
    def __init__(self, data):
        """
        Creates a node without children or parent
        :param data: the value stored in the node
        """
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.parent: Optional[Node] = None
        self.size = 1

    @staticmethod
    def get_size(node: Optional[Node]):
        """
        :param node: (possibly None) node
        :return: Size of the node. When the node is None, returns 0.
        """
        return 0 if node is None else node.size

    def fix_size(self):
        """
        Fixes node size based on sizes of its children
        """
        self.size = 1 + Node.get_size(self.left) + Node.get_size(self.right)
"""
Running Times of functions in TreeArray class:

1) size()- constant time, as the size of the tree is updated/stored in the root node after every operation. Asymptotic representation, O(1)
2) find(i)- depends on the configuration of the binary tree. Worst case is O(h), where h is the height of the tree. Worst case length of tree=O(n).
3) get(i)- depends on the configuration of the binary tree. Worst case is O(h), where h is the height of the tree. Worst case length of tree=O(n).
4) set(i,x)- depends on the configuration of the binary tree. Worst case is O(h), where h is the height of the tree. Worst case length of tree=O(n).
5) remove(i)- depends on the configuration of the binary tree. Worst case is O(h), where h is the height of the tree. Worst case length of tree=O(n).
6) insert(i,key)- depends on the configuration of the binary tree. Worst case is O(h), where h is the height of the tree. Worst case length of tree=O(n).
7) fix_sizes()- depends on the configuration of the binary tree. Worst case is O(h), where h is the height of the tree. Worst case length of tree=O(n).

"""



class TreeArray:
    """
    Efficient variable-size arrays implemented using tree
    """
    def __init__(self):
        self.root: Optional[Node] = None

    def size(self):
        """
        :return: The total number of elements
        """
        return Node.get_size(self.root)

    def find(self, i: int) -> Node:
        """
        :param i: An index of a node to find
        :return: A node in the the tree with index i
        :raises IndexError if index is out of bounds
        """
        if i>=Node.get_size(self.root):
            return -1
        node=self.root
        while True:
            pointer=Node.get_size(node.left)
            if i<pointer:
                node=node.left
                continue
            if i==pointer:
                return node
            if i>pointer:
                i=i-node.left.size-1
                node=node.right
                continue
        return -1

    def get(self, i: int):
        """
        :param i: Index where the element is inserted
        :return: A value at index i
        :raises IndexError if index is out of bounds
        """
        result=self.find(i)
        return -1 if result==-1 else result.data

    def set(self, i: int, x):
        """
        Changes value at index i to x
        :param i: Index of the modified value
        :param x: The new value
        :raises IndexError if index is out of bounds
        """
        node=self.find(i)
        if node==-1:
            return -1
        else:
            node.data=x

    def fix_sizes(self, node: Node):
        """
        Fixes sizes of all nodes on the path between this node and the root of the tree
        :param node: Starting node
        """
        if node!=None:
            while node.parent!=None:
                node=node.parent
                node.fix_size()
        

    def insert(self, i: int, x):
        """
        Insert value x into position i
        :param i: Index where the element is inserted
        :param x: The inserted value
        :raises IndexError if index is out of bounds
        """

        if i<0:
            return -1
        if i==0:
            
            y=None
            node=self.root
            visited_nodes=[]
            while node!=None:
                y=node
                visited_nodes.append(y)
                node=node.left
            if y==None:
                self.root=Node(x)
                y=self.root
            else:
                y.left=Node(x)
                y.left.parent=y
            
            
            self.fix_sizes(y.left)
            
        else:
            Tree_size=0 if self.root==None else self.root.size
            if i>Tree_size:
                return -1
          
            prev_node=self.find(i-1)
            if prev_node.right==None:
                prev_node.right=Node(x)
                prev_node.right.parent=prev_node
                
                self.fix_sizes(prev_node.right)
            else:
                curr_node=prev_node.right
                while curr_node!=None:
                    parent=curr_node
                    curr_node=curr_node.left
                parent.left=Node(x)
                parent.left.parent=parent
                
                self.fix_sizes(parent.left)
    
    def transplant(self,u,v):
        """
        Reference: Lecture Slides
        Used this function to replace node u with node v. 
        """
        
        if u.parent==None:
            self.root=v
        elif u==u.parent.left:
            u.parent.left=v
        else:
            u.parent.right=v
        if v!=None:
            v.parent=u.parent
    
    def minimum(self,node):
        """
        Reference: Lecture Slides
        Used this function to find the left-most node in a sub-tree.
        """
        while node.left!=None:
            node=node.left
        return node
    def successor(self,node):
        """
        Reference: Lecture Slides
        Used this function to find the successive node in a binary tree while traversing inorder.
        """
        
        if node.right!=None:
            return self.minimum(node)
        y=node.parent
        while y!=None and node==y.right:
            node=y
            y=y.parent
        return y
    def remove(self, i: int):
        """
        Removes an element at index i
        :param i: Index of the removed element
        :raises IndexError if index is out of bounds
        """
        ...
        
        if i>=Node.get_size(self.root):
            return -1
        
        node=self.find(i)
        if node.left==None and node.right==None:
            self.transplant(node,None)
            self.fix_sizes(node.parent)
        elif node.left==None and node.right!=None:
            self.transplant(node,node.right)
            self.fix_sizes(node.parent)
        elif node.right==None and node.left!=None:
            self.transplant(node,node.left)
            self.fix_sizes(node.parent)
        else:
            successor=self.successor(node)
            if successor==node.right or successor==node.left:
                self.transplant(node,successor)
                self.fix_sizes(node.parent)
            elif successor!=node.right or successor!=node.left:
                y=successor
                self.transplant(node,successor)
                self.transplant(y,y.right)
                self.fix_sizes(y.parent)
    def inorder(self) -> List:
        """
        :return: Elements in inorder. Should return an array represented by the tree
        """
        
        if self.root==None:
            return []
        root=self.root
        result=[]
        stack=[]
        while True:
            if root:
                stack.append(root)
                root=root.left
            else:
                if len(stack)==0:
                    break
                root=stack.pop()
                result.append(root.data)
                root=root.right
        
        return result
        
    
            
import random
class Test(unittest.TestCase):
        
    def setUp(self)->None:
        
        self.sorted_array=list(range(50))
        self.sorted_tree=TreeArray()
        
        for i in self.sorted_array[::-1]:
            self.sorted_tree.insert(0,i)
        
        
        
        self.random_array=list(range(50))
        random.shuffle(self.random_array)
        self.random_tree=TreeArray()
        
        for i in self.random_array[::-1]:
            self.random_tree.insert(0,i)
        
        
        self.empty_array=[]
        self.empty_tree=TreeArray()
        for i in self.empty_array[::-1]:
            self.empty_tree.insert(0,i)
            
    def test_size(self):
        
            
        self.assertEqual(len(self.sorted_array),self.sorted_tree.size())
        
        self.assertEqual(len(self.random_array),self.random_tree.size())
        
        self.assertEqual(len(self.empty_array),self.empty_tree.size())
    def test_find(self):
        #Valid Checks
        for i in range(len(self.sorted_array)):
            self.assertEqual(self.sorted_array[i],self.sorted_tree.find(i).data)
        
        for i in range(len(self.random_array)):
            self.assertEqual(self.random_array[i],self.random_tree.find(i).data)
        
        for i in range(len(self.empty_array)):
            self.assertEqual(self.empty_array[i],self.empty_tree.find(i).data)
        
        #Invalid Index
        
        self.assertEqual(-1,self.sorted_tree.find(100))
        self.assertEqual(-1,self.random_tree.find(100))
        self.assertEqual(-1,self.empty_tree.find(100))
        
        
        
        
    def test_get(self):
        #Valid Checks
        for i in range(len(self.sorted_array)):
            self.assertEqual(self.sorted_array[i],self.sorted_tree.get(i))
        
        for i in range(len(self.random_array)):
            self.assertEqual(self.random_array[i],self.random_tree.get(i))
        
        for i in range(len(self.empty_array)):
            self.assertEqual(self.empty_array[i],self.empty_tree.get(i))
            
        #Invalid Index
        
        self.assertEqual(-1,self.sorted_tree.get(100))
        self.assertEqual(-1,self.random_tree.get(100))
        self.assertEqual(-1,self.empty_tree.get(100))
        
    def test_set(self):
        #Valid Checks
        for i in range(len(self.sorted_array)):
            self.sorted_array[i]*=10
            
            self.sorted_tree.set(i,self.sorted_array[i])
            self.assertEqual(self.sorted_array[i],self.sorted_tree.get(i))
        
        for i in range(len(self.random_array)):
            self.random_array[i]*=10
            
            self.random_tree.set(i,self.random_array[i])
            self.assertEqual(self.random_array[i],self.random_tree.get(i))
        
        for i in range(len(self.empty_array)):
            self.empty_array[i]*=10
            
            self.empty_tree.set(i,self.empty_array[i])
            self.assertEqual(self.empty_array[i],self.empty_tree.get(i))
            
        #Invalid Index
        
        self.assertEqual(-1,self.sorted_tree.set(100,100))
        self.assertEqual(-1,self.random_tree.set(100,100))
        self.assertEqual(-1,self.empty_tree.set(100,100))
        
        
    def test_remove(self):
        #Valid
        self.sorted_array.pop(10)
        self.sorted_tree.remove(10)
        self.assertEqual(self.sorted_array,self.sorted_tree.inorder())
        
        self.random_array.pop(20)
        self.random_tree.remove(20)
        self.assertEqual(self.random_array,self.random_tree.inorder())
        
        
        
        #Invalid
        self.assertEqual(-1,self.sorted_tree.remove(1000))
        self.assertEqual(-1,self.random_tree.remove(1000))
        self.assertEqual(-1,self.empty_tree.remove(10))
    def test_insert(self):
        #Valid
        self.sorted_array.insert(10,245)
        self.sorted_tree.insert(10,245)
        self.assertEqual(self.sorted_array,self.sorted_tree.inorder())
        
        self.sorted_array.insert(10,2450)
        self.sorted_tree.insert(10,2450)
        self.assertEqual(self.random_array,self.random_tree.inorder())
        
        
        #Invalid
        self.assertEqual(-1,self.sorted_tree.insert(1000,1000))
        self.assertEqual(-1,self.random_tree.insert(1000,100))
        self.assertEqual(-1,self.empty_tree.insert(1000,1000))
    def test_fix_sizes(self):
        
        #Insert
        prev_size=self.sorted_tree.size
        self.sorted_tree.insert(10,245)
        new_size=self.sorted_tree.size
        self.assertEqual(prev_size,new_size)
        
        
        
        #Remove
        prev_size=self.sorted_tree.size
        self.sorted_tree.remove(10)
        new_size=self.sorted_tree.size
        self.assertEqual(prev_size,new_size)
        
        
    def test_inorder(self):
        self.assertEqual(self.sorted_array,self.sorted_tree.inorder())
        self.assertEqual(self.random_array,self.random_tree.inorder())
        self.assertEqual(self.empty_tree.inorder(),self.empty_array)
    
    
if __name__ == '__main__':
    unittest.main()
