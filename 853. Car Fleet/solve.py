from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Calculates the number of car fleets that will arrive at the destination.
        """
        
        # ---------------------------------------------------------
        # 1. TRANSLATION & CONSTRAINTS
        #    Input:  target (int), position (List[int]), speed (List[int])
        #    Output: Integer (Number of fleets)
        #    Goal:   Group cars based on arrival times. If a car behind is faster 
        #            than the car in front, it merges (doesn't add to count).
        #    Math:   Time to target = (target - position) / speed
        #
        # 2. BUDGET & BOUNDARIES
        #    N = 10^5
        #    Time: O(N log N) (due to sorting) | Space: O(N) (for storing pairs/stack)
        #    Edge Cases: 
        #       - Single car (N=1) -> Returns 1 fleet.
        #       - All cars start at same time? (Constraint says unique pos).
        #       - Car starts AT target? (pos < target).
        #       - Very large target (10^6).
        #
        # 3. STRATEGY & BOTTLENECK
        #    Naive:   Simulate movement step-by-step. Time complexity would be 
        #             dependent on distance/speed resolution. Too slow/inaccurate.
        #    Pivot:   We only care about *arrival time*. Physics doesn't change 
        #             until a collision happens. 
        #    Tool:    Sorting (to establish spatial order) + Stack (to track fleets).
        #             We process from the finish line BACKWARDS (Position Descending).
        #             The car closest to target sets the 'pace' for those behind.
        #
        # 4. THE STATE MACHINE
        #    - Pair (pos, speed) and SORT by pos descending.
        #    - Calculate 'time_to_finish' for the current car.
        #    - Push time to stack.
        #    - Check Stack:
        #         If len(stack) >= 2 and stack[-1] <= stack[-2]:
        #             (Current car is faster/equal to the one ahead).
        #             The current car catches up and merges.
        #             POP the current car (it is absorbed into the fleet ahead).
        #             The fleet ahead (stack[-2]) maintains its slower time.
        #    - Return len(stack).
        # ---------------------------------------------------------

        # Combine position and speed, then sort by position descending.
        # We want to look at the car closest to the target first.
        # Complexity: O(N log N)
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        
        stack = []  # To store the arrival time of each independent fleet leader

        for p, s in cars:
            # Calculate time to reach target (float)
            time = (target - p) / s
            
            # Push current car's theoretical arrival time to the stack
            stack.append(time)
            
            # CONSTRAINT CHECK (The Fleet Logic):
            # If the car we just added (stack[-1]) arrives SOONER (smaller time)
            # or at the same time as the car in front of it (stack[-2]),
            # it means it catches up.
            # Since it cannot pass, it merges into that fleet.
            # We pop it because it doesn't add a new "fleet count"; 
            # the fleet is represented by the slower car (stack[-2]).
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

# ---------------------------------------------------------
# ALTERNATIVE PERSPECTIVE (Variable Tracking)
# ---------------------------------------------------------
# While the Stack is great for visualization, we can technically optimize 
# Space to O(1) (ignoring the sorted input storage) by just tracking the 
# "current_slowest_time".
#
# Logic:
# 1. Iterate through sorted cars.
# 2. If a car's time > current_slowest_time: 
#       It's slower than the fleet ahead. It becomes the new bottleneck.
#       Increment fleet_count. Update current_slowest_time.
# 3. If a car's time <= current_slowest_time:
#       It catches up. Do nothing.
# ---------------------------------------------------------

if __name__ == "__main__":
    # Test Case 1
    target1 = 12
    pos1 = [10, 8, 0, 5, 3]
    speed1 = [2, 4, 1, 1, 3]
    sol = Solution()
    print(f"Test 1 Output: {sol.carFleet(target1, pos1, speed1)} (Expected: 3)")

    # Test Case 2
    target2 = 10
    pos2 = [3]
    speed2 = [3]
    print(f"Test 2 Output: {sol.carFleet(target2, pos2, speed2)} (Expected: 1)")

    # Test Case 3
    target3 = 100
    pos3 = [0, 2, 4]
    speed3 = [4, 2, 1]
    print(f"Test 3 Output: {sol.carFleet(target3, pos3, speed3)} (Expected: 1)")
