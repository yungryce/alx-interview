<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue" alt="Pascal Triangle">
  <img src="https://img.shields.io/badge/Status-Active-green" alt="Status">
  <img src="https://img.shields.io/badge/Algorithm-Dynamic_Programming-orange" alt="Algorithm">
</p>

<div align="center">
  <h1>🔺 Pascal's Triangle</h1>
  <p><em>Dynamic Programming Implementation of the Classic Mathematical Pattern</em></p>
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
This project implements the classic Pascal's Triangle generation algorithm using dynamic programming principles. Pascal's Triangle is a triangular array of binomial coefficients where each number is the sum of the two numbers directly above it, demonstrating fundamental mathematical patterns and algorithmic optimization techniques.

## 🎯 Learning Objectives
- Understand mathematical patterns and combinatorics
- Implement dynamic programming solutions
- Practice efficient algorithm design
- Master list manipulation in Python
- Apply binomial coefficient concepts
- Develop algorithmic thinking skills

## 🛠️ Tech Stack

**Core Technologies:**
- Python 3.x
- Dynamic Programming Algorithms

**Development Tools:**
- PEP 8 Style Guide
- Algorithm Analysis

## 📁 Project Structure
```
0x00-pascal_triangle/
├── 0-pascal_triangle.py       # Main implementation
├── README.md                  # Project documentation
├── ARCHITECTURE.md            # Technical architecture
└── PROJECT-MANIFEST.md        # Learning guide
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- Basic understanding of lists and loops
- Knowledge of mathematical patterns

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd alx-interview/0x00-pascal_triangle

# Make the file executable (if needed)
chmod +x 0-pascal_triangle.py
```

### Running the Project
```python
# Import the function
from 0-pascal_triangle import pascal_triangle

# Generate Pascal's Triangle
triangle = pascal_triangle(5)
print(triangle)
```

## 💡 Usage

Given a non-negative integer `n`, return the first `n` rows of Pascal's Triangle.

### Pascal's Triangle Properties:
- Each row starts and ends with 1
- Each interior element is the sum of the two elements above it
- Row `i` has `i+1` elements
- Element at position `j` in row `i` represents the binomial coefficient C(i,j)

### Example:
```python
Input: n = 5
Output: [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]

# Visual representation:
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
```

**Algorithm Implementation:**
```python
from 0-pascal_triangle import pascal_triangle

# Generate first 5 rows
triangle = pascal_triangle(5)
print(triangle)
# Output: [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]

# Edge case
empty = pascal_triangle(0)
print(empty)  # Output: []
```

## 🏆 Key Features
- **Dynamic Programming**: Efficient O(n²) time complexity
- **Mathematical Accuracy**: Precise binomial coefficient generation
- **Edge Case Handling**: Proper handling of n ≤ 0
- **Memory Optimization**: Space-efficient triangle construction
- **PEP 8 Compliance**: Clean, readable Python code
- **Combinatorial Applications**: Ready for mathematical computations

## 📚 Resources
- [Pascal's Triangle - Wikipedia](https://en.wikipedia.org/wiki/Pascal%27s_triangle)
- [Dynamic Programming Concepts](https://en.wikipedia.org/wiki/Dynamic_programming)
- [Binomial Coefficients](https://en.wikipedia.org/wiki/Binomial_coefficient)
- [Python Lists Documentation](https://docs.python.org/3/tutorial/datastructures.html)

## 👥 Contributors
- **ALX Software Engineering Program**
- Interview Preparation Curriculum