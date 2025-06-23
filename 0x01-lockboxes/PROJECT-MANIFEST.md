# Project Manifest

## Project Information
- **Project Name**: Lockboxes
- **Container**: 0x01-lockboxes
- **Category**: Graph Theory & Algorithms
- **Difficulty Level**: Intermediate
- **Topics**: Graph Traversal, Connectivity, Reachability Analysis

## Learning Objectives
- Master graph connectivity algorithms
- Understand reachability and traversal concepts
- Practice problem modeling and abstraction
- Develop efficient search strategies

## Files Structure
```
0x01-lockboxes/
├── 0-lockboxes.py               # Main implementation
├── main_0.py                    # Test cases
├── README.md                    # Project description
├── ARCHITECTURE.md              # Technical architecture
└── PROJECT-MANIFEST.md         # This file
```

## Implementation Requirements
- **Language**: Python 3.x
- **Function**: canUnlockAll(boxes)
- **Return Type**: Boolean (True if all boxes can be unlocked)
- **Constraints**: Box 0 is always unlocked initially
- **Performance**: O(n + k) time where n is boxes, k is total keys

## Key Concepts
1. **Graph Theory**
   - Boxes as nodes in a directed graph
   - Keys as edges pointing to other boxes
   - Connectivity and reachability problems
   - Graph traversal algorithms (DFS/BFS)

2. **Problem Modeling**
   - Abstract real-world problem to graph theory
   - Identify constraints and edge cases
   - Design efficient solution approach
   - Handle various input scenarios

3. **Algorithm Design**
   - Choose appropriate traversal method
   - Optimize for time and space complexity
   - Handle edge cases and invalid inputs
   - Implement robust error checking

## Test Cases
- **Basic Cases**: Simple connected graphs
- **Edge Cases**: Single box, empty boxes, unreachable boxes
- **Complex Cases**: Large graphs with multiple paths
- **Invalid Inputs**: Non-list inputs, malformed data

## Algorithm Approaches

### Depth-First Search (DFS)
```python
def canUnlockAll_dfs(boxes):
    visited = set([0])  # Box 0 is always unlocked
    stack = [0]
    
    while stack:
        current = stack.pop()
        for key in boxes[current]:
            if key not in visited and 0 <= key < len(boxes):
                visited.add(key)
                stack.append(key)
    
    return len(visited) == len(boxes)
```

### Breadth-First Search (BFS)
```python
def canUnlockAll_bfs(boxes):
    from collections import deque
    
    visited = set([0])
    queue = deque([0])
    
    while queue:
        current = queue.popleft()
        for key in boxes[current]:
            if key not in visited and 0 <= key < len(boxes):
                visited.add(key)
                queue.append(key)
    
    return len(visited) == len(boxes)
```

## Interview Focus Areas
- Problem analysis and modeling
- Graph theory concept application
- Algorithm selection and justification
- Complexity analysis and optimization
- Code implementation and testing

## Common Pitfalls
- Not handling self-referencing keys
- Missing input validation
- Inefficient duplicate key processing
- Incorrect boundary condition handling
- Poor time/space complexity analysis

## Success Criteria
- ✅ Correct connectivity determination
- ✅ Efficient traversal implementation
- ✅ Proper edge case handling
- ✅ Optimal time and space complexity
- ✅ Clean, maintainable code

## Extensions and Variations
- Find minimum keys needed to unlock all boxes
- Determine the unlocking sequence
- Handle weighted boxes or keys
- Solve for multiple starting points
- Implement parallel unlocking strategies

---

*This project builds essential graph theory skills and algorithmic thinking required for advanced technical interviews and system design challenges.*
