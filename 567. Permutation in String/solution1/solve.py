def checkInclusion(s1: str, s2: str) -> bool:
    n1, n2 = len(s1), len(s2)
    if n1 > n2:
        return False

    # 1. Define the target frequency vector (The Math Core)
    s1_counts = [0] * 26
    s2_counts = [0] * 26
    
    # Fill initial window and target
    for i in range(n1):
        # ord(char) - ord('a') maps 'a'-'z' to 0-25
        s1_counts[ord(s1[i]) - ord('a')] += 1
        s2_counts[ord(s2[i]) - ord('a')] += 1

    # 2. Check the initial state
    if s1_counts == s2_counts:
        return True

    # 3. Slide the window (Inductive Step)
    # Start from index n1 and move to the end of s2
    for i in range(n1, n2):
        # Add the character entering the window
        s2_counts[ord(s2[i]) - ord('a')] += 1
        # Remove the character leaving the window
        s2_counts[ord(s2[i - n1]) - ord('a')] -= 1
        
        # Check equality of the frequency vectors
        if s1_counts == s2_counts:
            return True

    return False
