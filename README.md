# First Principles Algorithmic Solving Framework

This guide outlines a **First Principles Framework** for solving algorithmic problems. Instead of memorizing solutions or "pattern matching" (e.g., "This looks like a dynamic programming problem"), a first principles approach requires you to deconstruct the problem into its fundamental mathematical truths: **Data**, **Constraints**, and **State Transitions**.

---

## Phase 1: Formalization (The Translation)

The first principle of algorithmic solving is that code is simply a function mapping an input set to an output set. You must translate the "story" of the problem into mathematical notation.

### 1. Define the Domain ($X$) and Codomain ($Y$)
Determine exactly what the input looks like and what the output must be.
* **Input ($X$):** Is it a set, a sequence, a graph, or a matrix?
* **Output ($Y$):** Are you returning a boolean, a scalar (max/min), or a subset?

### 2. Define the Objective Function ($f(x)$)
Express the problem as a function to be optimized or satisfied.

> **Example:** *Given an array of integers, find the contiguous subarray with the largest sum.*
> * **Input:** Sequence $A = \{a_1, a_2, ..., a_n\}$ where $a_i \in \mathbb{Z}$.
> * **Output:** A scalar $S_{max}$.
> * **Objective:** Maximize $\sum_{k=i}^{j} a_k$ for some $1 \le i \le j \le n$.

### 3. Identify Invariants
What properties must remain true throughout the execution? (e.g., "The array is sorted," or "We must visit every node once").

---

## Phase 2: Constraint Analysis (The Boundaries)

Before thinking about *how* to solve it, you must mathematically determine the *allowable complexity*. This is derived from the Input Size ($N$).

Standard competitive programming (and interview) environments allow roughly $10^8$ operations per second.



![](./time-complexity-image.jpeg)


* **If $N \le 20$:** You can use exponential time $O(2^N)$ or factorial $O(N!)$. (Likely Recursion/Backtracking).
* **If $N \le 1000$:** You can use quadratic time $O(N^2)$. (Nested loops are okay).
* **If $N \le 10^5$ or $10^6$:** You must use linear $O(N)$ or linearithmic $O(N \log N)$. (One pass or Sorting).
* **If $N > 10^9$:** You must use logarithmic $O(\log N)$ or constant $O(1)$. (Binary search or Math formula).

**Action:** Look at the constraints given in the problem. If $N = 10^5$, **mathematically prove to yourself** that a nested loop solution will fail (Time Limit Exceeded). This narrows your search space immediately.

---

## Phase 3: Dimensionality Reduction (The Search Space)

Most problems ask you to search for an answer within a "Search Space" (all possible valid outputs). A brute force approach checks every point in this space. Your goal is to use mathematical properties to ignore vast parts of that space.

### 1. The Brute Force Formula
Write down the naive mathematical solution.
For the "Max Subarray" example, the search space is all pairs $(i, j)$.
Total pairs $\approx \frac{N^2}{2}$. Summing each takes $O(N)$.
**Total Complexity:** $O(N^3)$.

### 2. Optimization via Data Structures
We optimize by choosing a data structure that minimizes the cost of specific operations required by your objective function.

| Operation Needed | Mathematical Cost | Data Structure Choice |
| :--- | :--- | :--- |
| **Membership ($x \in S$?)** | $O(1)$ vs $O(N)$ | Hash Map / Hash Set |
| **Ordering / Min-Max** | $O(1)$ vs $O(N)$ | Heap (Priority Queue) |
| **Sequential Dependency** | LIFO / FIFO | Stack / Queue |
| **Prefix/Suffix Algebra** | $O(1)$ Range Sum | Prefix Sum Array |

### 3. Optimization via Recurrence (Inductive)
If the problem asks for an optimal value, check if the problem has **Optimal Substructure**. Can the answer for input size $N$ be derived from the answer for input size $N-1$?

$$Solve(n) = f(Solve(n-1), ...)$$

* **Top-Down:** Recursion with Memoization.
* **Bottom-Up:** Dynamic Programming (Iteration).



---

## Phase 4: Algorithm Selection (The "Solver")

Based on the mathematical structure identified in Phase 3, select the algorithmic paradigm.

### A. If the Search Space is Monotonic:
If the function $f(x)$ is increasing or decreasing (sorted), you do not need to scan linearly.
* **Technique:** Binary Search.
* **Math:** Reduces search space by half each step: $N \to \frac{N}{2} \to \frac{N}{4}$.

### B. If the Search Space involves Combinations/Permutations:
If you need to explore all subsets.
* **Technique:** Backtracking (Depth First Search).

### C. If the Search Space is Linear/Sequential:
If you are processing a stream or array and need to maintain a "window" of state.
* **Technique:** Sliding Window or Two Pointers.
* **Math:** $Left$ and $Right$ pointers move monotonically (never move backward), ensuring $O(N)$ complexity.



### D. If the relationships are Pairwise/Connected:
If objects are connected to other objects.
* **Technique:** Graph Theory (BFS/DFS).
* **Math:** Model as $G = (V, E)$.

---

## Example Walkthrough: Two Sum

**Problem:** *Given array $A$ and target $T$, find indices $i, j$ such that $A[i] + A[j] = T$.*

1.  **Formalization:** Find $(i, j)$ such that $A[i] = T - A[j]$.
2.  **Constraints:** Assume $N = 10^5$. We need $O(N)$ or $O(N \log N)$. $O(N^2)$ is forbidden.
3.  **Search Space:** Naive approach checks all pairs $(i, j)$. Complexity $O(N^2)$.
4.  **Mathematical Reduction:** Fix index $i$. We are looking for a value $x = T - A[i]$ in the rest of the array. To check for existence in $O(1)$, we use a **Hash Map**.
5.  **Solution:** Iterate $i$ from $0 \to N$. Calculate required $diff = T - A[i]$. If $diff$ exists in Hash Map $\to$ Success. Else, store $A[i]$ in Hash Map.

---

## Summary Checklist for the Programmer

When you face a new problem, do not write code immediately. Write this comment block:

```text
// 1. INPUT/OUTPUT:
//    Input: [Type, Constraints]
//    Output: [Type, Value]

// 2. FORMULA:
//    Maximize/Find f(x) where...

// 3. CONSTRAINTS & COMPLEXITY:
//    N = [Size], therefore max Time Complexity = O(...)

// 4. STRATEGY:
//    Brute force is O(...).
//    Bottleneck is [Inner Loop / Lookup / Sorting].
//    Optimize bottleneck using [Hash Map / Two Pointers / DP] to achieve O(...).