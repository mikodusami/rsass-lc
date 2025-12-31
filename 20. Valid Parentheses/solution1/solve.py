"""
// ---------------------------------------------------------
// 1. TRANSLATION & CONSTRAINTS
//    Input:  String s
//    Output: Boolean (True if valid)
//    Parity: If len(s) % 2 != 0, return False (immediately).
//
// 2. BUDGET & BOUNDARIES
//    N = 10^4 -> O(N) Time.
//    Edge Cases: "]", "((", "([)]"
//
// 3. STRATEGY & BOTTLENECK
//    Tool: Stack (LIFO) to track the most recent opening bracket.
//    Logic: Map closers to openers for O(1) matching.
//
// 4. THE STATE MACHINE
//    - Opener: Push to stack.
//    - Closer: If stack empty OR top doesn't match mapping -> False.
//    - End: Return True if stack is empty.
// ---------------------------------------------------------
"""

def isValid_Stack(s: str) -> bool:
    if len(s) % 2 != 0: return False # Parity Check
    
    mapping = {")": "(", "}": "{", "]": "["}
    stack = []
    
    for char in s:
        if char in mapping:
            # Pop top if exists, else use dummy '#' to force mismatch
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
            
    return not stack
