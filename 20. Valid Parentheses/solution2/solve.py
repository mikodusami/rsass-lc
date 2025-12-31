"""
// ---------------------------------------------------------
// 1. TRANSLATION & CONSTRAINTS
//    Goal: Shrink the string by removing full pairs "()", "[]", "{}" 
//          until no pairs are left.
//
// 2. BUDGET & BOUNDARIES
//    Small N: O(N^2) is acceptable.
//
// 3. STRATEGY
//    Naive: Keep scanning the string. If "()" exists, delete it.
//    Bottleneck: Scanning the string multiple times.
//
// 4. THE STATE MACHINE
//    - While any pair exists in string:
//        replace "()" with ""
//    - If string becomes empty -> True.
// ---------------------------------------------------------
"""

def isValid_Replacement(s: str) -> bool:
    if len(s) % 2 != 0: return False
    
    # We loop at most N/2 times
    old_len = -1
    while len(s) > 0 and len(s) != old_len:
        old_len = len(s)
        s = s.replace("()", "").replace("[]", "").replace("{}", "")
        
    return len(s) == 0
