class BST:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

def arrayToTree(nums):
    if not nums:
        return None
    mid_num = len(nums) // 2
    node = BST(nums[mid_num])
    node.left = arrayToTree(nums[:mid_num])
    node.right = arrayToTree(nums[mid_num+1:])
    return node

def preOrder(node):
    if not node:
        return
    print(node.data)
    preOrder(node.left)
    preOrder(node.right)

nums = [-10,-3,0,5,9]
print("mid")
mid = len(nums)//2

print(nums[mid])

print("Original array")
print(nums)
result = arrayToTree(nums)
print("\nArray to Tree")
preOrder(result)
