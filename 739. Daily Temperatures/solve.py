# ---------------------------------------------------------
# 1. TRANSLATION & CONSTRAINTS
#    Input:  List[int] (Temperatures)
#    Output: List[int] (Days until a warmer temperature)
#    Goal:   For each index i, find the distance to the first j > i where T[j] > T[i].
#    Parity: If no warmer day exists, the result for that index is 0.
#
# 2. BUDGET & BOUNDARIES
#    N = 10^5
#    Time: O(N) required. No nested loops allowed (unless it's an amortized O(N) stack).
#    Space: O(N) to store the result and the stack history.
#    Edge Cases: 
#       - Temperatures consistently decreasing (Stack will just grow, results stay 0).
#       - Temperatures consistently increasing (Stack will pop immediately every time).
#
# 3. STRATEGY & BOTTLENECK
#    Naive: For every day, scan all future days. O(N^2). Too slow for 10^5.
#    Pivot: We need to "pause" the search for a day's answer and move on, but 
#           "resume" it as soon as we find a warmer day. 
#    Tool:  Monotonic Stack (Decreasing). It keeps track of indices waiting for a warmer day.
#
# 4. THE STATE MACHINE (The "Human" logic)
#    - WHILE [current temp > temp at stack top]:
#        1. We found the warmer day! Pop the index from the stack.
#        2. Calculate distance: current_index - popped_index.
#        3. Store distance in result array at [popped_index].
#    - ALWAYS: 
#        1. Push current_index to the stack.
# ---------------------------------------------------------



from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize result array with 0s (covers the "no warmer day" case)
        n = len(temperatures)
        answer = [0] * n
        stack = [] # Stores indices: [i1, i2, ...]
        
        for curr_idx, curr_temp in enumerate(temperatures):
            # Check if current temperature is warmer than the 'pending' days in stack
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_idx = stack.pop()
                # The 'wait time' is the difference between indices
                answer[prev_idx] = curr_idx - prev_idx
            
            # We always add the current day to the stack to find its future warmer day
            stack.append(curr_idx)
            
        return answer

# Time: O(N) - Each index is pushed and popped exactly once.
# Space: O(N) - In the worst case (decreasing temps), the stack holds all indices.
