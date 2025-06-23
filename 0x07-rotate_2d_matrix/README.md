<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue" alt="Rotate 2D Matrix">
  <img src="https://img.shields.io/badge/Status-Active-green" alt="Status">
  <img src="https://img.shields.io/badge/Algorithm-Matrix_Manipulation-orange" alt="Algorithm">
</p>

<div align="center">
  <h1>🔄 Rotate 2D Matrix</h1>
  <p><em>In-place Matrix Rotation Using Advanced Algorithms</em></p>
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
This project implements in-place 90-degree clockwise rotation of a 2D matrix without using additional memory. It demonstrates advanced matrix manipulation algorithms and space-efficient transformations essential for image processing and geometric operations.

## 🎯 Learning Objectives

- Master in-place matrix manipulation algorithms
- Understand geometric transformations and rotations
- Practice space-efficient algorithm design
- Develop matrix processing optimization skills

## Problem Description

Given an n × n 2D matrix, rotate it 90 degrees clockwise **in-place**. The rotation must be performed without using additional memory for another matrix.

### Requirements:
- Rotate matrix 90 degrees clockwise
- Must be done in-place (no extra matrix)
- Original matrix is modified directly
- Function: `rotate_2d_matrix(matrix)`

### Example:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]
]

# After rotation:
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

## Requirements

- **Language**: Python 3.x
- **Function**: `rotate_2d_matrix(matrix)`
- **Constraint**: In-place rotation (O(1) extra space)
- **Input**: n × n matrix (assume n ≥ 2)

## Files

- `0-rotate_2d_matrix.py`: Main implementation
- `README.md`: This file
- `ARCHITECTURE.md`: Technical architecture documentation
- `PROJECT-MANIFEST.md`: Project manifest and learning guide

## Algorithm Approaches

### Layer-by-Layer Rotation:
1. Process matrix in concentric layers
2. For each layer, rotate 4 corners at a time
3. Move elements in groups of 4

### Transpose + Reverse:
1. Transpose the matrix (swap rows/columns)
2. Reverse each row

## Complexity Analysis

- **Time Complexity**: O(n²) - must touch every element
- **Space Complexity**: O(1) - in-place transformation
- **Optimal**: Cannot do better than O(n²) time

## Implementation Strategy

The rotation maps element at position (i,j) to position (j, n-1-i) in a 90-degree clockwise rotation.

---

*This project is part of the ALX Software Engineering interview preparation curriculum.* 
