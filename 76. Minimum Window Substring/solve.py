class Solution:
    def minWindow(s: str, t: str) -> str:
        # 1. INPUT/OUTPUT:
        #    Input: Strings s and t, lengths up to 10^5.
        #    Output: String (Minimum window substring or "").

        # 2. FORMULA:
        #    Minimize (R - L + 1) where for all c in t: 
        #    window_counts[c] >= target_counts[c].

        # 3. CONSTRAINTS & COMPLEXITY:
        #    N = 10^5, therefore max Time Complexity = O(N).
        #    A single pass with two pointers (L, R) ensures O(2N) = O(N).

        # 4. STRATEGY:
        #    Brute force is O(N^3).
        #    Bottleneck is re-calculating character counts for every substring.
        #    Optimize bottleneck using two pointers and a frequency Hash Map 
        #    to achieve O(N).

        if not t or not s:
            return ""

        # Frequency requirement map
        dict_t = {}
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        required = len(dict_t)
        l, r = 0, 0
        
        # formed is used to track how many unique characters in t 
        # have their frequency requirement met in the current window.
        formed = 0
        window_counts = {}

        # ans tuple of (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1    

            # Keep expanding the window once we've done contracting.
            r += 1    
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
        