"""
// ---------------------------------------------------------
// 1. TRANSLATION & CONSTRAINTS
//    Goal: Mimic a stack using a pointer on a pre-allocated array.
//
// 2. BUDGET & BOUNDARIES
//    Space: Trying to be as efficient as possible with pre-allocation.
//
// 3. STRATEGY
//    Tool: A list of size N and a 'top' integer pointer.
//
// 4. THE STATE MACHINE
//    - 'top' pointer starts at -1.
//    - If opener: move 'top' forward and write char to array[top].
//    - If closer: check array[top], then move 'top' backward.
// ---------------------------------------------------------

"""

def isValid_Pointer(s: str) -> bool:
    if len(s) % 2 != 0: return False
    
    # Pre-allocate array to avoid dynamic resizing overhead
    # Note: Still O(N) space, but often faster in low-level languages
    stack = [None] * len(s)
    top = -1 
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping:
            # If pointer is at start, we have a closer with no opener
            if top == -1 or stack[top] != mapping[char]:
                return False
            top -= 1 # "Pop" by moving pointer back
        else:
            top += 1 # "Push" by moving pointer forward
            stack[top] = char
            
    return top == -1
