
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    def insert(self,value):
        # Pass if the value is already in the tree
        if value == self.data:
            pass
        else:
            # If value is less than the node, check
            # left
            if value < self.data:
                # If empty, it becomes left node
                if self.left == None:
                    self.left = Node(value)
                # Otherwise, look in that node
                else:
                    self.left.insert(value)
            # Similar to less then check
            if value > self.data:
                if self.right == None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)

    def check(self, value):
        if value == self.data:
            return True
        else:
            # If value is less than the node, check
            # left
            if value < self.data:
                # If empty, it becomes left node
                if self.left == None:
                    return False
                # Otherwise, look in that node
                else:
                    return self.left.check(value)
            # Similar to less then check
            if value > self.data:
                if self.right == None:
                    return False
                else:
                    return self.right.check(value)

tree = Node(53)
numbers = [26,20,44,88,67,94,55,80]
for num in numbers:
    tree.insert(num)

print(tree.check(26))
print(tree.check(80))
print(tree.check(91))

