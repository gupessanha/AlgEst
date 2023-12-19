class RB_node:
    def __init__(self, key, value, color, left, right):
        self.key = key
        self.value = value
        self.color = color
        self.left = left
        self.right = right
    
class RB_tree:
    def __init__(self):
        self.nil = RB_node(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

def insert(self, val):
    new_node = RB_node(val)
    new_node.parent = None
    new_node.left = self.nil
    new_node.right = self.nil
    new_node.red = True  
    parent = None
    current = self.root
    
    while current != self.nil:
        parent = current
        if new_node.val < current.val:
            current = current.left
        elif new_node.val > current.val:
            current = current.right
        else:
            return new_node.parent = parent
    
    if parent == None:
        self.root = new_node
    
    elif new_node.val < parent.val:
        parent.left = new_node
    
    else:
        parent.right = new_node
    self.fix_insert(new_node)
