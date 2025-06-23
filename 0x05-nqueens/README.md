<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue" alt="N Queens">
  <img src="https://img.shields.io/badge/Status-Active-green" alt="Status">
  <img src="https://img.shields.io/badge/Algorithm-Backtracking-orange" alt="Algorithm">
</p>

<div align="center">
  <h1>♛ N Queens</h1>
  <p><em>Classic Backtracking Algorithm for Constraint Satisfaction</em></p>
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
This project solves the classic N-Queens problem using backtracking algorithms. The challenge is to place N chess queens on an N×N chessboard such that no two queens attack each other, demonstrating advanced recursive problem-solving and constraint satisfaction techniques.

## 🎯 Learning Objectives
- Master backtracking algorithms and recursion
- Understand constraint satisfaction problems
- Practice systematic search with pruning
- Develop complex problem-solving strategies
- Apply chess logic to algorithmic solutions
- Implement efficient search optimization

## 🛠️ Tech Stack

**Core Technologies:**
- Python 3.x
- Backtracking Algorithms
- Constraint Satisfaction

**Development Tools:**
- Recursive Problem Solving
- Chess Logic Implementation
- Algorithm Optimization

## 📁 Project Structure
```
0x05-nqueens/
├── 0-nqueens.py             # Main implementation
├── README.md                # Project documentation
├── ARCHITECTURE.md          # Technical architecture
└── PROJECT-MANIFEST.md      # Learning guide
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- Understanding of recursion and backtracking
- Basic chess rules knowledge
- Command-line interface familiarity

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd alx-interview/0x05-nqueens

# Make the script executable
chmod +x 0-nqueens.py
```

### Running the Project
```bash
# Run the N-Queens solver
./0-nqueens.py 4

# Or with Python
python3 0-nqueens.py 8
```

## 💡 Usage

The N-Queens problem requires placing N queens on an N×N chessboard so that no two queens can attack each other. Queens can attack horizontally, vertically, and diagonally.

### Rules:
- N queens on N×N board
- No two queens in same row, column, or diagonal
- Find all possible solutions
- Print each solution as list of queen positions

### Command Usage:
```bash
./nqueens.py N
```

Where N must be an integer ≥ 4.

### Output Format:
Each solution printed as: `[[row, col], [row, col], ...]`

## Requirements

- **Language**: Python 3.x
- **Usage**: `./nqueens.py N`
- **Input**: Integer N ≥ 4
- **Output**: All possible solutions

## Files

- `nqueens.py`: Main implementation
- `README.md`: This file
- `ARCHITECTURE.md`: Technical architecture documentation
- `PROJECT-MANIFEST.md`: Project manifest and learning guide

## Algorithm Implementation

The solution uses backtracking to systematically explore all possible queen placements while pruning invalid configurations early.

### Core Functions:

1. **is_safe()**: Check if queen placement conflicts with existing queens
2. **solve_nqueens()**: Recursive backtracking solver
3. **nqueens()**: Main driver function

## Complexity Analysis

- **Time Complexity**: O(N!) factorial time in worst case
- **Space Complexity**: O(N) for recursion stack and board
- **Solutions Count**: Varies by N (e.g., N=8 has 92 solutions)

## Example Solutions

### N = 4:
```
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

### N = 8:
92 different solutions exist for the classic 8×8 chessboard.

---

*This project is part of the ALX Software Engineering interview preparation curriculum.*
