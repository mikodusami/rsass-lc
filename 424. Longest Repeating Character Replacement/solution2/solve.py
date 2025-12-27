def characterReplacement(s: str, k: int) -> int:
    n = len(s)
    
    # Mathematical Helper: Can we find a valid substring of length 'length'?
    def is_valid(length):
        count = {}
        max_f = 0
        # Initial window of size 'length'
        for i in range(length):
            count[s[i]] = count.get(s[i], 0) + 1
            max_f = max(max_f, count[s[i]])
        
        if length - max_f <= k:
            return True
            
        # Slide the fixed window across the rest of the string
        for i in range(length, n):
            # Add new character
            count[s[i]] = count.get(s[i], 0) + 1
            # Remove old character
            count[s[i - length]] -= 1
            
            # Recalculate max frequency (Only 26 letters, so O(26) is fine)
            max_f = max(count.values())
            
            if length - max_f <= k:
                return True
        return False

    # Binary Search on the Answer
    low, high = 1, n
    res = 0
    
    while low <= high:
        mid = (low + high) // 2
        if is_valid(mid):
            res = mid  # This length works, try to find a longer one
            low = mid + 1
        else:
            high = mid - 1 # Too long, try shorter
            
    return res
