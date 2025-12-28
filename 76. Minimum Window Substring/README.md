# Problem Solving: 76. Minimum Window Substring

### Phase 1: Formalization

**1. Define the Domain ($X$) and Codomain ($Y$)**
* **Input ($X$):** Two strings $s$ (length $m$) and $t$ (length $n$).
* **Output ($Y$):** A substring $s[i:j]$ or an empty string $""$.

**2. Define the Objective Function ($f(x)$)**
Minimize the length $(j - i + 1)$ such that the following condition is satisfied:
$$\forall c \in \text{unique}(t) : \text{count}(s[i:j], c) \ge \text{count}(t, c)$$

**3. Identify Invariants**
* The search space is contiguous: if a window is valid, expanding it further will always keep it valid (monotonicity of inclusion).
* To find the *minimum*, we must shrink a valid window from the left until it becomes invalid.

---

### Phase 2: Constraint Analysis

* **Constraints:** $m, n \le 10^5$.
* **Allowable Complexity:** According to the $10^8$ operations rule, $N = 10^5$ requires $O(N)$ or $O(N \log N)$.
* **Verdict:** $O(N^2)$ or $O(N^3)$ brute force is mathematically eliminated. We need a linear time complexity solution.

---

### Phase 3: Dimensionality Reduction

**1. The Brute Force Formula**
Checking all possible pairs $(i, j)$ results in $\approx \frac{m^2}{2}$ substrings. Validating each takes $O(n)$. Total: $O(m^2 \cdot n)$.

**2. Optimization via Data Structures**
We need $O(1)$ frequency tracking.
* **Choice:** Hash Maps or Integer Arrays of size 52 (to cover 'A-Z' and 'a-z').

**3. Optimization via Recurrence**
The problem exhibits a sliding property: once a valid window $[L, R]$ is found, the next potential minimum can only be found by moving $L$ forward or $R$ forward. We never need to "reset" the pointers to the beginning.



---

### Phase 4: Implementation (The Template)

```python
def minWindow(s: str, t: str) -> str:
    # 1. INPUT/OUTPUT:
    #    Input: Strings s (length m), t (length n) where m, n <= 10^5.
    #    Output: Minimum window substring or "".

    # 2. FORMULA:
    #    Minimize (R - L + 1) such that:
    #    For all c in t, window_counts[c] >= target_counts[c].

    # 3. CONSTRAINTS & COMPLEXITY:
    #    N = 10^5, therefore max Time Complexity = O(N).
    #    The two-pointer approach ensures each character is visited 
    #    at most twice, resulting in O(m + n).

    # 4. STRATEGY:
    #    Brute force is O(m^2 * n).
    #    Bottleneck is re-scanning substrings to check character counts.
    #    Optimize bottleneck using a sliding window and a frequency 
    #    Hash Map to achieve O(m + n).

    if not s or not t:
        return ""

    # Mathematical Setup: Frequency Requirements
    target_counts = {}
    for char in t:
        target_counts[char] = target_counts.get(char, 0) + 1

    required_unique = len(target_counts)
    window_counts = {}
    formed_unique = 0
    
    # ans: (window_length, left_idx, right_idx)
    ans = (float("inf"), 0, 0)
    L = 0

    for R in range(len(s)):
        char = s[R]
        window_counts[char] = window_counts.get(char, 0) + 1

        # Check if the current character satisfies the frequency requirement
        if char in target_counts and window_counts[char] == target_counts[char]:
            formed_unique += 1

        # Shrink the window from the left as long as it remains "valid"
        while L <= R and formed_unique == required_unique:
            char_at_l = s[L]

            # Update the global minimum
            if (R - L + 1) < ans[0]:
                ans = (R - L + 1, L, R)

            # Dimensionality Reduction: Remove the leftmost character
            window_counts[char_at_l] -= 1
            if char_at_l in target_counts and window_counts[char_at_l] < target_counts[char_at_l]:
                formed_unique -= 1
            
            L += 1

    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]