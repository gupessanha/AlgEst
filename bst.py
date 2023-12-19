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
    
    def insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert(data, node.right)
        else:
            print("Valor já existe na árvore")

    def printTree(self):
        if self.root is not None:
            printNode(self.root)
        else:
            print("Árvore vazia")
            
    def preOrdem(self, node):
        if node is not None:
            print(node.data)
            self.preOrdem(node.left)
            self.preOrdem(node.right)
            
    def emOrdem(self, node):
        if node is not None:
            self.emOrdem(node.left)
            print(node.data)
            self.emOrdem(node.right)
            
    def posOrdem(self, node):
        if node is not None:
            self.posOrdem(node.left)
            self.posOrdem(node.right)
            print(node.data)
            
    def search(self, data, node):
        if node is None:
            return None
        elif data < node.data:
            return self.search(data, node.left)
        elif data > node.data:
            return self.search(data, node.right)
        else:
            return node
        
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
        
    def delete(self, data, node):
        if node is None:
            return node
        elif data < node.data:
            node.left = self.delete(data, node.left)
        elif data > node.data:
            node.right = self.delete(data, node.right)
        else:
            if node.left is None and node.right is None:
                node = None
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                aux = self.findMin(node)
                node.data = aux.data
                node.right = self.delete(aux.data, node.right)
        return node
    
arvore = BinarySearchTree()
arvore.root = Node(10)
arvore.insert(5, arvore.root)
arvore.insert(11, arvore.root)
arvore.insert(12, arvore.root)
arvore.insert(13, arvore.root)
arvore.insert(14, arvore.root)
arvore.insert(15, arvore.root)
arvore.insert(16, arvore.root)
arvore.insert(17, arvore.root)
arvore.insert(18, arvore.root)
arvore.insert(19, arvore.root)
arvore.insert(20, arvore.root)
arvore.insert(1, arvore.root)
arvore.insert(2, arvore.root)
arvore.insert(3, arvore.root)

arvore.printTree()

printNode(arvore.search(12, arvore.root))