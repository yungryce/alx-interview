<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue" alt="Minimum Operations">
  <img src="https://img.shields.io/badge/Status-Active-green" alt="Status">
  <img src="https://img.shields.io/badge/Algorithm-Prime_Factorization-orange" alt="Algorithm">
</p>

<div align="center">
  <h1>⚙️ Minimum Operations</h1>
  <p><em>Mathematical Optimization Using Prime Factorization</em></p>
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
This project solves a mathematical optimization problem: given a text file containing a single character 'H', find the minimum number of operations needed to result in exactly `n` 'H' characters using only two operations: "Copy All" and "Paste". The solution demonstrates prime factorization and mathematical reasoning in algorithm design.

## 🎯 Learning Objectives
- Understand mathematical optimization problems
- Master prime factorization algorithms  
- Practice recursive problem decomposition
- Develop mathematical reasoning for algorithm design
- Apply number theory to algorithmic solutions
- Optimize computational complexity

## 🛠️ Tech Stack

**Core Technologies:**
- Python 3.x
- Prime Factorization Algorithms
- Mathematical Optimization

**Development Tools:**
- Number Theory Concepts
- Algorithm Analysis
- Mathematical Reasoning

## 📁 Project Structure
```
0x02-minimum_operations/
├── 0-minoperations.py       # Main implementation
├── main_0.py                # Test cases
├── README.md                # Project documentation
├── ARCHITECTURE.md          # Technical architecture
└── PROJECT-MANIFEST.md      # Learning guide
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- Understanding of prime numbers
- Basic mathematical reasoning
- Knowledge of algorithmic optimization

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd alx-interview/0x02-minimum_operations

# Make files executable
chmod +x 0-minoperations.py main_0.py
```

### Running the Project
```python
# Import the function
from 0-minoperations import minOperations

# Calculate minimum operations
result = minOperations(9)
print(result)  # Output: 6
```

## 💡 Usage

In a text file, there is a single character 'H'. Your text editor can execute only two operations:

1. **Copy All**: Copy all the characters currently in the file
2. **Paste**: Paste the characters that were last copied

Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` 'H' characters in the file.

### Examples:

```
n = 1: No operations needed
Result: 0

n = 4: H -> Copy All, Paste -> HH -> Copy All, Paste -> HHHH
Operations: Copy(1) + Paste(1) + Copy(1) + Paste(1) = 4
Result: 4

n = 9: H -> Copy, Paste, Paste -> HHH -> Copy, Paste, Paste -> HHHHHHHHH  
Operations: Copy(1) + Paste(2) + Copy(1) + Paste(2) = 6
Result: 6
```

## Mathematical Insight

The key insight is that this problem reduces to **prime factorization**:

- To reach `n` characters optimally, we need to factor `n` into its prime components
- For each prime factor `p`, the optimal strategy is:
  - Reach `n/p` characters first
  - Copy All (1 operation)  
  - Paste `p-1` times (`p-1` operations)
  - Total: `p` operations
- **Minimum operations = sum of all prime factors of n**

### Mathematical Proof:
- Any sequence of Copy All + Paste operations can be viewed as multiplication
- To reach `n` efficiently, we need the smallest sum of factors that multiply to `n`
- This is achieved by the sum of prime factors (fundamental theorem of arithmetic)

## Requirements

- **Language**: Python 3.x
- **Function**: `minOperations(n)`
- **Return**: Integer (minimum operations needed)
- **Prototype**: `def minOperations(n):`

## Files

- `0-minoperations.py`: Main implementation
- `0-main.py`: Test cases
- `README.md`: This file
- `ARCHITECTURE.md`: Technical architecture documentation
- `PROJECT-MANIFEST.md`: Project manifest and learning guide

## Algorithm Implementation

### Recursive Prime Factorization
```python
def minOperations(n):
    if n <= 1:
        return 0
    
    # Find smallest prime factor
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(n // i) + i
```

### Iterative Prime Factorization
```python
def minOperations(n):
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    if n > 1:
        operations += n
    
    return operations
```

### Dynamic Programming Approach
```python
def minOperations(n):
    if n <= 1:
        return 0
    
    dp = [float('inf')] * (n + 1)
    dp[1] = 0
    
    for i in range(2, n + 1):
        for j in range(2, i + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[i // j] + j)
    
    return dp[n]
```

## Complexity Analysis

- **Time Complexity**: O(√n) for finding prime factors
- **Space Complexity**: O(log n) for recursion depth (recursive approach)

## Test Cases

```python
print(minOperations(1))   # 0
print(minOperations(4))   # 4 (2 + 2)
print(minOperations(9))   # 6 (3 + 3) 
print(minOperations(12))  # 7 (2 + 2 + 3)
print(minOperations(13))  # 13 (prime number)
```

## Mathematical Examples

```
n = 12 = 2² × 3
Prime factors: 2, 2, 3
Operations: 2 + 2 + 3 = 7

Sequence:
H → Copy, Paste → HH (2 ops)
HH → Copy, Paste → HHHH (2 more ops, total 4)
HHHH → Copy, Paste, Paste → HHHHHHHHHHHH (3 more ops, total 7)
```

## Interview Focus Points

- Recognize this as a mathematical optimization problem
- Understand the connection to prime factorization
- Explain why the greedy approach works
- Discuss time complexity optimization
- Handle edge cases (n ≤ 1, prime numbers)

---

*This project is part of the ALX Software Engineering interview preparation curriculum.*
