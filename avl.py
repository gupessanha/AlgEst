class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

def printNode(node):
    if node is not None:
        print(node.data)
        printNode(node.left)
        printNode(node.right)
        
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def printTree(self):
        if self.root is not None:
            printNode(self.root)
        else:
            print("Árvore vazia")
        
            
    def search(self, data, node):
        if node is None:
            return None
        elif data < node.data:
            return self.search(data, node.left)
        elif data > node.data:
            return self.search(data, node.right)
        else:
            return node
     
    def height(self, node):
        if node is None:
            return -1
        else:
            return max(self.height(node.left), self.height(node.right)) + 1
        
    def findMin(self, node):
        if node is None:
            return None
        elif node.left is None:
            return node
        else:
            return self.findMin(node.left)
        
    def findMax(self, node):
        if node is None:
            return None
        elif node.right is None:
            return node
        else:
            return self.findMax(node.right)
    
    def RightRotation(self, node):
        aux = node.left
        node.left = aux.right
        aux.right = node
        return aux
    
    def LeftRotation(self, node):
        aux = node.right
        node.right = aux.left
        aux.left = node
        return aux
    
    def RightLeftRotation(self, node):
        node.right = self.RightRotation(node.right)
        return self.LeftRotation(node)
    
    def LeftRightRotation(self, node):
        node.left = self.LeftRotation(node.left)
        return self.RightRotation(node)
    
    def insert(self, data, node):
        if node is None:
            node = Node(data)
        elif data < node.data:
            node.left = self.insert(data, node.left)
            if (self.height(node.left) - self.height(node.right)) == 2:
                if data < node.left.data:
                    node = self.RightRotation(node)
                else:
                    node = self.LeftRightRotation(node)
        elif data > node.data:
            node.right = self.insert(data, node.right)
            if (self.height(node.right) - self.height(node.left)) == 2:
                if data > node.right.data:
                    node = self.LeftRotation(node)
                else:
                    node = self.RightLeftRotation(node)
        else:
            print("Valor já existe na árvore")
        return node
    
    def remove(self, data, node):
        if node is None:
            print("Valor não encontrado")
        elif data < node.data:
            node.left = self.remove(data, node.left)
            if (self.height(node.right) - self.height(node.left)) == 2:
                if node.right.right is None:
                    node = self.RightLeftRotation(node)
                else:
                    node = self.LeftRotation(node)
        elif data > node.data:
            node.right = self.remove(data, node.right)
            if (self.height(node.left) - self.height(node.right)) == 2:
                if node.left.left is None:
                    node = self.LeftRightRotation(node)
                else:
                    node = self.RightRotation(node)
        elif node.left is not None and node.right is not None:
            node.data = self.findMin(node.right).data
            node.right = self.remove(node.data, node.right)
        else:
            if node.left is not None:
                node = node.left
            else:
                node = node.right
        return node