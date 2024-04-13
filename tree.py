class BinarySearchTree:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        
        if self.key > data:
            if self.leftChild:
                self.leftChild.insert(data)
            else:
                self.leftChild = BinarySearchTree(data)
        else:
            if self.rightChild:
                self.rightChild.insert(data)
            else:
                self.rightChild = BinarySearchTree(data)
    def search(self, data):
        if self.key == data:
            print("Data is found")
            return
        if data < self.key:
            if self.leftChild:
                self.leftChild.search(data)
            else:
                print("Data not found")

        else:
            if self.rightChild:
                self.rightChild.search(data)
            else:
                print("Data not found")

    #traversal
    def preorder(self):
        print(self.key, end=" ")
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()
    
    #inorder: left -> root -> right
    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key, end=" ")
        if self.rightChild:
            self.rightChild.inorder()

    #postorder: left -> right -> root
    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key, end= " ")

    def delete(self, data, curr):
        if self.key is None:
            print("Tree is empty")
            return
        if data< self.key:
            if self.leftChild:
                self.leftChild = self.leftChild.delete(data, curr)
            else:
                print("data is not present in the tree")
        elif data> self.key:
            if self.rightChild:
                self.rightChild = self.rightChild.delete(data, curr)
            else:
                print("data is present in the tree")
        else:
            if self.leftChild is None:
                temp = self.rightChild
                if data == curr:
                    self.key = temp.key
                    self.leftChild = temp.leftChild
                    self.rightChild = temp.rightChild
                    temp = None
                    return

                self = None
                return temp
            if self.rightChild is None:
                temp = self.leftChild
                if data == curr:
                    self.key = temp.key
                    self.leftChild = temp.leftChild
                    self.rightChild = temp.rightChild
                    temp = None
                    return
                self = None
                return temp
            node = self.rightChild
            while node.leftChild:
                node = node.leftChild
            self.key = node.key
            self.rightChild = self.rightChild.delete(node.key, curr)
        return self
    
    def Min(self):
        if self.leftChild:
            self.leftChild.Min()
        else:
            print("Minimam: ",self.key)
    def Max(self):
        if self.rightChild:
            self.rightChild.Max()
        else:
            print("Maximum: ", self.key)        

    

def count(node):
    if node is None:
        return 0
    
    return 1 + count(node.leftChild) + count(node.rightChild)


root  = BinarySearchTree(10)

list1 = [2,14, 7, 5, 3, 4, 9, 11, 12, 19, 23]

for i in list1:
    root.insert(i)

print("In order")
root.inorder()

print()
root.Min()
print()
root.Max()

# if count(root) > 1:
#     root.delete(10, root.key)
# else:
#     print("Can't delete the root node")
# print("after delete")
# root.inorder()


