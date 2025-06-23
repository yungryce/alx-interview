<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue" alt="Prime Game">
  <img src="https://img.shields.io/badge/Status-Active-green" alt="Status">
  <img src="https://img.shields.io/badge/Algorithm-Game_Theory-orange" alt="Algorithm">
</p>

<div align="center">
  <h1>🎮 Prime Game</h1>
  <p><em>Strategic Game Theory Using Prime Number Mathematics</em></p>
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
This project implements a strategic game theory problem involving prime numbers. Two players take turns removing prime numbers and their multiples from a set of consecutive integers, demonstrating game theory principles, prime number mathematics, and optimal strategy algorithms.

## 🎯 Learning Objectives
- Master game theory and optimal strategy algorithms
- Understand prime number theory and applications
- Practice competitive programming techniques
- Develop mathematical reasoning skills
- Implement efficient prime detection algorithms
- Apply strategic thinking to algorithmic problems

## 🛠️ Tech Stack

**Core Technologies:**
- Python 3.x
- Prime Number Algorithms
- Game Theory Mathematics

**Development Tools:**
- Mathematical Optimization
- Strategic Algorithm Design
- Competitive Programming

## 📁 Project Structure
```
0x0A-primegame/
├── 0-prime_game.py          # Main implementation
├── main_0.py                # Test cases
├── README.md                # Project documentation
├── ARCHITECTURE.md          # Technical architecture
└── PROJECT-MANIFEST.md      # Learning guide
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- Understanding of prime numbers
- Basic game theory knowledge
- Mathematical reasoning skills

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd alx-interview/0x0A-primegame

# Make files executable
chmod +x 0-prime_game.py main_0.py
```

### Running the Project
```python
# Import the function
from 0-prime_game import isWinner

# Test the game
rounds = [4, 5, 1]
result = isWinner(3, rounds)
print(result)  # Output: Winner name or None
```

## 💡 Usage

**Game Rules:**
- Maria and Ben play optimally
- Players take turns removing prime numbers and their multiples
- Player who cannot make a move loses
- Maria always goes first

**Function Prototype:**
```python
def isWinner(x, nums):
    """
    Determines the winner of prime game rounds
    Args: x - number of rounds, nums - array of n values
    Returns: Name of winner or None if tied
    """
```

## 🏆 Key Features
- **Game Theory Implementation**: Optimal strategy algorithms
- **Prime Number Mathematics**: Efficient prime detection
- **Strategic Analysis**: Winning condition evaluation
- **Multiple Rounds**: Tournament-style game management
- **Optimal Performance**: Efficient algorithm complexity
- **Mathematical Reasoning**: Game state analysis

## 📚 Resources
- [Game Theory Introduction](https://en.wikipedia.org/wiki/Game_theory)
- [Prime Numbers](https://en.wikipedia.org/wiki/Prime_number)
- [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
- [Competitive Programming](https://usaco.guide/)

## 👥 Contributors
- **ALX Software Engineering Program**
- Interview Preparation Curriculum