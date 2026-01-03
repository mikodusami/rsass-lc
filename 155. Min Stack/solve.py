class MinStack:
    """
    Goal: design a stack that always retrieves the miniumum element
    """

    def __init__(self):
        self.stack = []
        self.sstack = []

    def push(self, val: int) -> None:
        """
        Input: a integer number
        Output: None
        Goal: To push an element onto the stack
        Budegt: You must implement a solution with O(1) time complexity for each function
        Strategy:
        - Naive: to push elements to stack but when finding minimum, we traverse through the top of stack and find the minimum number and return it.
        - Pivot for O(1): add an addtional stack to keep only the current minimum value each time you push a number
        Tool: Stack (Two)

        THE STATE MACHINE (The "Human" logic)
        - IF [no elements in stack] : push both numbers to the stack
        - IF [element in stack]: get the lesser number between top of stack and val and store minimum in sstack
        """
        current_number = val if not self.sstack else min(val, self.sstack[-1])
        self.stack.append(val)
        self.sstack.append(current_number)


    def pop(self) -> None:
        self.stack.pop()
        self.sstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.sstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
