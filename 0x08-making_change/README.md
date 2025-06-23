<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue" alt="Making Change">
  <img src="https://img.shields.io/badge/Status-Active-green" alt="Status">
  <img src="https://img.shields.io/badge/Algorithm-Dynamic_Programming-orange" alt="Algorithm">
</p>

<div align="center">
  <h1>🪙 Making Change</h1>
  <p><em>Classic Coin Change Problem Using Dynamic Programming</em></p>
</div>

---

## 📋 Table of Contents
- [📖 Overview](#-overview)
- [🎯 Learning Objectives](#-learning-objectives)
- [🛠️ Tech Stack](#️-tech-stack)
- [📁 Project Structure](#-project-structure)
- [🚀 Getting Started](#-getting-started)
- [💡 Usage](#-usage)
- [🏆 Key Features](#-key-features)
- [📚 Resources](#-resources)
- [👥 Contributors](#-contributors)

## 📖 Overview
This project solves the classic coin change problem using dynamic programming. Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total, demonstrating optimal substructure and overlapping subproblems principles.

## 🎯 Learning Objectives
- Master dynamic programming algorithms and optimization
- Understand the coin change problem and its variations  
- Practice bottom-up problem solving approaches
- Develop skills in algorithmic optimization
- Apply optimal substructure principles
- Implement efficient memoization techniques

## Problem Description

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

### Requirements:
- Function: `makeChange(coins, total)`
- Return: Fewest number of coins needed
- Return -1 if total cannot be met
- Assume infinite supply of each coin denomination

### Example:
```python
makeChange([1, 2, 25], 37)
# Result: 7 coins (25 + 25 + 2 + 2 + 2 + 1 = 37)

makeChange([1256, 54, 48, 16, 102], 1453)  
# Result: -1 (cannot make exact amount)
```

## Requirements

- **Language**: Python 3.x
- **Function**: `makeChange(coins, total)`
- **Return**: Integer (minimum coins needed, -1 if impossible)
- **Constraint**: Assume infinite supply of each coin

## Files

- `0-making_change.py`: Main implementation
- `README.md`: This file
- `ARCHITECTURE.md`: Technical architecture documentation
- `PROJECT-MANIFEST.md`: Project manifest and learning guide

## Dynamic Programming Approach

### Algorithm:
1. Create DP table where dp[i] = minimum coins for amount i
2. Initialize dp[0] = 0, others = infinity
3. For each amount from 1 to total:
   - Try each coin denomination
   - Update dp[amount] = min(dp[amount], dp[amount-coin] + 1)
4. Return dp[total] or -1 if impossible

### Recurrence Relation:
```
dp[amount] = min(dp[amount-coin] + 1) for all valid coins
```

## Complexity Analysis

- **Time Complexity**: O(amount × coins)
- **Space Complexity**: O(amount) for DP table
- **Optimal**: This is the standard optimal solution

## Edge Cases

- total = 0: Return 0
- total < 0: Return -1  
- Empty coins list: Return -1
- No valid combination: Return -1

---

*This project is part of the ALX Software Engineering interview preparation curriculum.* 
