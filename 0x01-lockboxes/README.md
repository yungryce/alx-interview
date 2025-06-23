<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue" alt="Lockboxes">
  <img src="https://img.shields.io/badge/Status-Active-green" alt="Status">
  <img src="https://img.shields.io/badge/Algorithm-Graph_Traversal-orange" alt="Algorithm">
</p>

<div align="center">
  <h1>🔐 Lockboxes</h1>
  <p><em>Graph Connectivity Challenge Using DFS/BFS Algorithms</em></p>
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
This project solves the lockboxes problem, a classic graph connectivity challenge. Given a set of locked boxes where each box contains keys to other boxes, determine if all boxes can be unlocked starting with box 0 being initially unlocked. The solution demonstrates fundamental graph traversal algorithms and connectivity analysis.

## 🎯 Learning Objectives
- Master graph traversal algorithms (DFS/BFS)
- Understand connectivity and reachability problems
- Practice problem modeling and abstraction
- Develop efficient search strategies
- Apply graph theory to practical problems
- Implement algorithmic solutions with optimal complexity

## 🛠️ Tech Stack

**Core Technologies:**
- Python 3.x
- Graph Algorithms (DFS/BFS)

**Development Tools:**
- Set Data Structures
- Algorithm Analysis
- Graph Theory Concepts

## 📁 Project Structure
```
0x01-lockboxes/
├── 0-lockboxes.py           # Main implementation
├── main_0.py                # Test cases
├── README.md                # Project documentation
├── ARCHITECTURE.md          # Technical architecture
└── PROJECT-MANIFEST.md      # Learning guide
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- Understanding of graph theory basics
- Knowledge of DFS/BFS algorithms
- Familiarity with Python sets and lists

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd alx-interview/0x01-lockboxes

# Make files executable
chmod +x 0-lockboxes.py main_0.py
```

### Running the Project
```python
# Import the function
from 0-lockboxes import canUnlockAll

# Test the algorithm
boxes = [[1], [2], [3], [4], []]
result = canUnlockAll(boxes)
print(result)  # True
```

## 💡 Usage

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

### Rules:
- Box 0 is always unlocked initially
- A key with the same number as a box opens that box
- All keys will be positive integers
- There can be keys that do not have boxes
- The first box `boxes[0]` is always unlocked

### Function Prototype:
```python
def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked
    Args: boxes - list of lists containing keys
    Returns: True if all boxes can be unlocked, False otherwise
    """
```

### Example Usage:
```python
from 0-lockboxes import canUnlockAll

# Example 1: All boxes can be unlocked
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # True

# Example 2: Complex connectivity
boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # True

# Example 3: Some boxes unreachable
boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # False
```

## 🏆 Key Features
- **Graph Traversal**: Efficient DFS/BFS implementation
- **Connectivity Analysis**: Determines reachability from starting node
- **Edge Case Handling**: Manages invalid keys and self-references
- **Optimal Complexity**: O(n + k) time complexity
- **Memory Efficient**: O(n) space complexity
- **Robust Algorithm**: Handles various input scenarios

## 📚 Resources
- [Graph Theory Introduction](https://en.wikipedia.org/wiki/Graph_theory)
- [Depth-First Search](https://en.wikipedia.org/wiki/Depth-first_search)
- [Breadth-First Search](https://en.wikipedia.org/wiki/Breadth-first_search)
- [Python Sets Documentation](https://docs.python.org/3/tutorial/datastructures.html#sets)

## 👥 Contributors
- **ALX Software Engineering Program**
- Interview Preparation Curriculum
