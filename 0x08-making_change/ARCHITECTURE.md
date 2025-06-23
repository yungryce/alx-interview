# Architecture Documentation

## Project: Making Change

### Component Overview

This module solves the classic coin change problem using dynamic programming, determining the minimum number of coins needed to make a given amount. It demonstrates optimal substructure and overlapping subproblems patterns.

### Implementation Details

#### Core Algorithm
- **Dynamic Programming**: Bottom-up approach with memoization
- **Optimal Substructure**: Minimum coins for amount = 1 + min(coins for amount-coin)
- **Time Complexity**: O(amount × coins) 
- **Space Complexity**: O(amount) for DP table

---

*This implementation showcases fundamental dynamic programming concepts essential for optimization problems.*
