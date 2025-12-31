# The First Principles Framework: A Beginner’s Guide to Algorithms

This guide deconstructs algorithmic problem solving. Instead of memorizing code, we focus on translating a human "story" into computer logic using four distinct phases.

---

## Phase 1: The Translation (Formalization)
**Goal:** Stop reading the problem as a story. Start reading it as data inputs and outputs.

The first principle is that **Code is just a translation machine**. You feed it raw ingredients (Input), and it cooks a specific dish (Output).

### Step 1: Define "What I Have" (The Input Domain $X$)
Don't just say "an array." Be specific.
* **Data Type:** Is it a list of numbers? A string of characters? A grid (matrix)?
* **Properties:** Are the numbers sorted? Can they be negative? Are there duplicates?
* **Mathematical Notation:** $A = [a_1, a_2, ... a_n]$

### Step 2: Define "What I Want" (The Output Codomain $Y$)
What exactly does the function return?
* **Decision:** True/False? (Boolean)
* **Value:** A single number? (Integer/Float)
* **Structure:** A list of items? (Array/List)
* **Location:** An index or coordinate?

### Step 3: The "One Sentence" Goal (The Objective Function)
Strip away the flavor text. Write one sentence that describes the relationship between Input and Output.
* *Example Story:* "Help the thief steal the most money from houses without alerting police."
* *Mathematical Sentence:* "Find the subset of non-adjacent numbers with the maximum sum."

---

## Phase 2: The Budget (Constraint Analysis)
**Goal:** Determine how "expensive" your solution is allowed to be before you write a single line of code.

Computers have a speed limit (approx. $10^8$ operations per second). The size of the input ($N$) dictates which algorithms fit in your "budget."

| Input Size ($N$) | Your Time Budget | Allowable Complexity | The "Vibe" of the Solution |
| :--- | :--- | :--- | :--- |
| **Small** ($N \le 20$) | Unlimited | $O(2^N)$ or $O(N!)$ | You can try every combination (Recursion). |
| **Medium** ($N \le 1,000$) | Generous | $O(N^2)$ | Nested loops (compare every item to every other item). |
| **Large** ($N \le 10^5$) | Tight | $O(N)$ or $O(N \log N)$ | You can touch every item once, or sort them. **No nested loops.** |
| **Huge** ($N > 10^9$) | Instant | $O(\log N)$ or $O(1)$ | You cannot even look at all inputs. Use Math or Binary Search. |

** Beginner Tip:** If $N = 100,000$, and you write a double for-loop (`for i in arr: for j in arr:`), you have already failed. Stop and rethink.

---

## Phase 3: The Strategy (Dimensionality Reduction)
**Goal:** Avoid checking every possibility (Brute Force). Find a shortcut.

### Step 1: The Naive Approach (Brute Force)
First, admit how you would solve it if you had infinite time.
* *Thought:* "I'll check every single subarray to see which is largest."
* *Cost:* $O(N^2)$ or $O(N^3)$.
* *Check:* Does this fit the Phase 2 Budget? If yes, code it! If no, proceed to Step 2.

### Step 2: Identify the Bottleneck
Why is the Brute Force slow?
* Are we re-calculating the same sum over and over?
* Are we searching the whole list just to find one number?

### Step 3: Choose the Optimization Tool
Match your bottleneck to a specific Data Structure tool.

| The Bottleneck Problem | The Mathematical Solution | The Code Tool |
| :--- | :--- | :--- |
| "I need to find if Item X exists quickly." | Membership Check $O(1)$ | **Hash Set / Hash Map** |
| "I need the biggest/smallest item constantly." | Ordering $O(1)$ | **Heap (Priority Queue)** |
| "I need to access recent history in order." | LIFO / FIFO | **Stack / Queue** |
| "I need the sum of a specific range repeatedly." | Range Algebra | **Prefix Sum Array** |
| "The answer for N depends on N-1." | Recurrence Relation | **Dynamic Programming** |

---

## Phase 4: The Algorithm Selection (The Solver)
**Goal:** Select the standard coding pattern that fits the data structure.

### A. Is the input Sorted or Monotonic?
* *Does the data go up/down consistently?*
* **Technique:** Binary Search.
* **Why:** We can ignore half the data at every step.

### B. Do we need Combinations or Permutations?
* *Does the problem ask for "all subsets" or "all ways to arrange"?*
* **Technique:** Backtracking (Recursion).

### C. Are we looking for a contiguous sub-part?
* *Are we looking for a slice of an array or string?*
* **Technique:** Sliding Window or Two Pointers.
* **Why:** We use pointers ($Left$ and $Right$) to slide over the data once ($O(N)$) instead of looping repeatedly.

### D. Is it a connection problem?
* *Are items connected like cities on a map or friends in a network?*
* **Technique:** BFS / DFS (Graph Theory).

---

## Example Walkthrough: Two Sum
**Problem:** Given array `nums` and target `T`, find indices `i` and `j` where `nums[i] + nums[j] = T`.

1.  **Translation:**
    * Input: Array of Ints.
    * Goal: Find $i, j$ such that $A[i] = T - A[j]$.
2.  **Budget:**
    * $N = 10,000$.
    * Budget is $O(N)$ or $O(N \log N)$. **We cannot use nested loops ($O(N^2)$).**
3.  **Strategy:**
    * *Naive:* Loop `i`, then Loop `j`. Too slow.
    * *Bottleneck:* Finding the partner number ($T - A[i]$) takes too long ($O(N)$) inside the loop.
    * *Tool:* We need fast lookups. **Use a Hash Map.**
4.  **Algorithm:**
    * Loop through array once.
    * Calculate `needed_value = Target - current_value`.
    * Ask Map: "Have we seen `needed_value`?"
        * Yes: Return indices.
        * No: Add `current_value` to Map and continue.

---

## The "New Solver" Comment Template
Copy and paste this into your code editor at the start of every problem. Fill it out *before* writing code.

```text
// ---------------------------------------------------------
// 1. TRANSLATION & CONSTRAINTS
//    Input:  (e.g., String s)
//    Output: (e.g., Boolean)
//    Goal:   (e.g., Match nested pairs in LIFO order)
//    Parity: (Are there math shortcuts? e.g., if len(s) % 2 != 0, return False)
//
// 2. BUDGET & BOUNDARIES
//    N = ... 
//    Time: O(...) | Space: O(...)
//    Edge Cases to Check: 
//       - Empty input ("")
//       - Single element ("(")
//       - Maximum constraints (N=10^4)
//       - "Heavy" start (all openers) vs "Heavy" end (all closers)
//
// 3. STRATEGY & BOTTLENECK
//    Naive:   (e.g., Search for every matching pair. O(N^2))
//    Pivot:   (Why is Naive bad? e.g., We lose track of nesting order)
//    Tool:    (e.g., Stack for LIFO, Hash Map for O(1) matching)
//
// 4. THE STATE MACHINE (The "Human" logic)
//    - If [Condition A]: Push to stack/Update pointer
//    - If [Condition B]: Pop/Compare/Calculate
//    - Final Check: (e.g., Is stack empty? Is pointer at N?)
// ---------------------------------------------------------
