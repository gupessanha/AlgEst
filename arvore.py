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
        
class BinaryTree:
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


a = Node(15)  
arvore = BinaryTree()
arvore.root = Node(10)
arvore.insert(5, arvore.root)
arvore.insert(11, arvore.root)
arvore.insert(20, arvore.root)
arvore.insert(25, arvore.root)

print("Nós:")
printNode(arvore.root)
print("Árvore:")
arvore.printTree()
print("Pré Ordem:")
arvore.preOrdem(arvore.root)
print("Em Ordem:")
arvore.emOrdem(arvore.root)
print("Pós Ordem:")
arvore.posOrdem(arvore.root)