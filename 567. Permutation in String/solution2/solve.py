def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    s1_counts = [0] * 26
    s2_counts = [0] * 26
    
    # Initial setup for the first window
    for i in range(len(s1)):
        s1_counts[ord(s1[i]) - ord('a')] += 1
        s2_counts[ord(s2[i]) - ord('a')] += 1

    # Initialize matches count (0 to 26)
    matches = 0
    for i in range(26):
        if s1_counts[i] == s2_counts[i]:
            matches += 1

    # Sliding the window
    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True
        
        # 1. Update character entering from the RIGHT
        idx = ord(s2[r]) - ord('a')
        s2_counts[idx] += 1
        if s2_counts[idx] == s1_counts[idx]:
            matches += 1
        elif s2_counts[idx] == s1_counts[idx] + 1:
            matches -= 1
            
        # 2. Update character leaving from the LEFT
        idx = ord(s2[l]) - ord('a')
        s2_counts[idx] -= 1
        if s2_counts[idx] == s1_counts[idx]:
            matches += 1
        elif s2_counts[idx] == s1_counts[idx] - 1:
            matches -= 1
            
        l += 1
        
    return matches == 26
