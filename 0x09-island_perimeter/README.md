<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue" alt="Island Perimeter">
  <img src="https://img.shields.io/badge/Status-Active-green" alt="Status">
  <img src="https://img.shields.io/badge/Algorithm-Grid_Traversal-orange" alt="Algorithm">
</p>

<div align="center">
  <h1>🏝️ Island Perimeter</h1>
  <p><em>Grid Traversal and Boundary Detection Algorithm</em></p>
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
This project calculates the perimeter of an island represented in a 2D grid. It demonstrates grid traversal algorithms, boundary detection techniques, and computational geometry concepts essential for spatial analysis problems and geographic information systems.

## 🎯 Learning Objectives

- Master 2D grid traversal and analysis algorithms
- Understand boundary detection and perimeter calculation
- Practice computational geometry problem solving
- Develop spatial analysis and processing skills

## Problem Description

Create a function that returns the perimeter of the island described in a grid:

### Grid Rules:
- 0 represents water
- 1 represents land  
- Each cell is square with side length 1
- Cells are connected horizontally/vertically (not diagonally)
- Grid is completely surrounded by water
- There is only one island (or nothing)
- Island doesn't have "lakes" (water inside that isn't connected to surrounding water)

### Example:
```python
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0], 
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
# Perimeter = 16
```

## Requirements

- **Language**: Python 3.x
- **Function**: `island_perimeter(grid)`
- **Return**: Integer (perimeter of the island)
- **Grid**: List of lists of integers (0s and 1s)

## Files

- `0-island_perimeter.py`: Main implementation
- `README.md`: This file
- `ARCHITECTURE.md`: Technical architecture documentation
- `PROJECT-MANIFEST.md`: Project manifest and learning guide

## Algorithm Approach

### Perimeter Calculation:
1. Traverse each cell in the grid
2. For each land cell (1), check its 4 neighbors
3. Add 1 to perimeter for each water neighbor or grid boundary
4. Sum all contributions to get total perimeter

### Edge Counting:
Each land cell contributes edges where it borders:
- Water cells (0)
- Grid boundaries (outside the grid)

## Complexity Analysis

- **Time Complexity**: O(rows × cols) - visit each cell once
- **Space Complexity**: O(1) - constant extra space
- **Optimal**: Cannot do better than O(mn) for m×n grid

## Implementation Strategy

The key insight is that each land cell's contribution to the perimeter equals 4 minus the number of adjacent land cells.

---

*This project is part of the ALX Software Engineering interview preparation curriculum.*

Create a function def island_perimeter(grid): that returns the perimeter of the island described in grid:

- grid is a list of list of integers:
    - 0 represents water
    - 1 represents land
    - Each cell is square, with a side length of 1
    - Cells are connected horizontally/vertically (not diagonally).
    - grid is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).