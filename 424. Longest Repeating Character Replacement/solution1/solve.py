def characterReplacement(s: str, k: int) -> int:
    # Mathematical State
    count = {} # Frequency Map: maps char -> frequency in current window
    max_freq = 0 # count_max from our formula
    l = 0 # Left pointer
    max_length = 0 # Our result (The Codomain)

    # Iterate through the Domain using the Right pointer
    for r in range(len(s)):
        # 1. Update State
        count[s[r]] = 1 + count.get(s[r], 0)
        max_freq = max(max_freq, count[s[r]])

        # 2. Check Invariant: Window Length - Max Frequency > k
        # Current Window Length = (r - l + 1)
        while (r - l + 1) - max_freq > k:
            # If invalid, shrink from the left
            count[s[l]] -= 1
            l += 1
        
        # 3. Update Global Maximum
        max_length = max(max_length, r - l + 1)

    return max_length
