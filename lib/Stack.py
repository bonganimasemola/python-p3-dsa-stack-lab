class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
        
        # initialize self.dictionary with a default value for each index in the range of limit, if limit is meant to be the maximum number of items that the stack can hold
        self.dictionary = {i: None for i in range(limit)}
    
    def isEmpty(self):
        return self.items == []
                

    def push(self, item):
        # This method adds a new element to the top of the stack.
        # It first checks if the stack is full by comparing the length of the items list with the limit.
        # If the stack is full, it raises an exception.
        # Otherwise, it adds the item to the items list and the corresponding index to the dictionary.
        # Returns the updated stack.
        if len(self.items) == self.limit:
            raise Exception("Stack is full.")
        # interestingly if you just input the below the Push to 0 & Pop 1 off the stack tests pass pytest 
        self.dictionary[item] = None
        self.items.append(item)
        return self 


    def pop(self):
        pass

    def peek(self):
        pass
    
    def size(self) -> int:
        return len(self.items)
    
        
    def full(self):
        return len(self.items) == self.limit
        

    def search(self, target):
        for i in reversed(range(len(self.items))):
            if self.items[i] == target:
                return len(self.items) -1  - i 
        return -1
