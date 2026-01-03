import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        // ---------------------------------------------------------
        // 1. TRANSLATION & CONSTRAINTS
        //    Input:  A list of strings (tokens).
        //    Output: An integer result of the RPN expression.
        //    Goal:   Evaluate RPN using a stack-based approach for O(N) efficiency.
        //
        // 2. BUDGET & BOUNDARIES
        //    N = 10^4 = tokens.length 
        //    Time: O(n) | Space: O(n)
        //    Edge Cases: 
        //       - Single number: ["18"] should return 18.
        //       - Negative results: Truncate division toward zero (6 / -132 = 0).
        //
        // 3. STRATEGY & BOTTLENECK
        //    Pivot:   Store numbers in a stack. When an operator is hit, pop 2, 
        //             calculate, and push result back.
        //    Bottleneck: Python's `//` operator rounds toward negative infinity. 
        //                RPN requires truncation toward zero.
        //
        // 4. THE STATE MACHINE
        //    - If [number]: stack.append(int(token))
        //    - If [operator]:
        //        popFirst (Right Operand)
        //        popSecond (Left Operand)
        //        Calculate: Left [op] Right
        //    - Final Check: return stack[0]
        // ---------------------------------------------------------
        """
        stack = []
        
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                # Corrected: Must cast string to int before pushing
                stack.append(int(token))
            else:
                # Corrected: The order of popping matters for - and /
                r = stack.pop()
                l = stack.pop()
                
                if token == "+":
                    stack.append(l + r)
                elif token == "-":
                    stack.append(l - r)
                elif token == "*":
                    stack.append(l * r)
                elif token == "/":
                    # Corrected: Truncation toward zero logic
                    # int(l / r) is the most concise Architect approach in Python
                    stack.append(int(l / r))
                    
        return stack[0]
