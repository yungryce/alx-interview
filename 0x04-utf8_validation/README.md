<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue" alt="UTF-8 Validation">
  <img src="https://img.shields.io/badge/Status-Active-green" alt="Status">
  <img src="https://img.shields.io/badge/Algorithm-Bit_Manipulation-orange" alt="Algorithm">
</p>

<div align="center">
  <h1>🔤 UTF-8 Validation</h1>
  <p><em>Character Encoding Validation Using Bit Manipulation</em></p>
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
This project implements UTF-8 character encoding validation using bit manipulation techniques. Given a list of integers, determine if it represents a valid UTF-8 encoding sequence according to the UTF-8 standard, demonstrating advanced bitwise operations and character encoding principles.

## 🎯 Learning Objectives

- Understand UTF-8 character encoding principles
- Master bit manipulation and bitwise operations
- Practice pattern recognition in binary data
- Develop text processing and validation skills

## Problem Description

UTF-8 is a variable-width character encoding that uses 1-4 bytes per character. Write a method that determines if a given data set represents a valid UTF-8 encoding.

### UTF-8 Encoding Rules:

**1-byte characters (ASCII):**
```
0xxxxxxx
```

**2-byte characters:**
```
110xxxxx 10xxxxxx
```

**3-byte characters:**
```
1110xxxx 10xxxxxx 10xxxxxx
```

**4-byte characters:**
```
11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
```

### Key Rules:
- Each integer represents 1 byte (only least significant 8 bits)
- Continuation bytes must start with `10`
- Leading bytes indicate the number of bytes in the character
- Invalid sequences should return False

## Requirements

- **Language**: Python 3.x
- **Function**: `validUTF8(data)`
- **Return**: Boolean (True if valid UTF-8)
- **Prototype**: `def validUTF8(data):`

## Files

- `0-validate_utf8.py`: Main implementation
- `README.md`: This file
- `ARCHITECTURE.md`: Technical architecture documentation
- `PROJECT-MANIFEST.md`: Project manifest and learning guide

## Algorithm Implementation

```python
def validUTF8(data):
    """
    Validates UTF-8 encoding
    
    Args:
        data: List of integers representing bytes
        
    Returns:
        bool: True if valid UTF-8, False otherwise
    """
    n_bytes = 0
    
    for byte in data:
        # Get only the 8 least significant bits
        byte = byte & 0xFF
        
        if n_bytes == 0:
            # Determine number of bytes in UTF-8 character
            if byte >> 7 == 0:          # 0xxxxxxx
                continue
            elif byte >> 5 == 0b110:    # 110xxxxx
                n_bytes = 1
            elif byte >> 4 == 0b1110:   # 1110xxxx
                n_bytes = 2
            elif byte >> 3 == 0b11110:  # 11110xxx
                n_bytes = 3
            else:
                return False
        else:
            # Check continuation byte: 10xxxxxx
            if byte >> 6 != 0b10:
                return False
            n_bytes -= 1
    
    return n_bytes == 0
```

## Bit Manipulation Techniques

### Extracting Bit Patterns:
```python
# Check if byte starts with 0
if byte >> 7 == 0:          # 0xxxxxxx

# Check if byte starts with 110
if byte >> 5 == 0b110:      # 110xxxxx

# Check if byte starts with 1110  
if byte >> 4 == 0b1110:     # 1110xxxx

# Check if byte starts with 11110
if byte >> 3 == 0b11110:    # 11110xxx

# Check if byte starts with 10
if byte >> 6 == 0b10:       # 10xxxxxx
```

### Masking Lower 8 Bits:
```python
byte = byte & 0xFF  # Keep only least significant 8 bits
```

## Test Cases

```python
# Valid UTF-8 sequences
print(validUTF8([65]))                    # True: 'A' (ASCII)
print(validUTF8([80, 121, 116, 104, 111, 110]))  # True: 'Python'
print(validUTF8([229, 165, 189]))        # True: 3-byte character
print(validUTF8([240, 159, 152, 128]))   # True: 4-byte character (emoji)

# Invalid UTF-8 sequences  
print(validUTF8([229, 65, 189]))         # False: invalid continuation
print(validUTF8([250, 145, 145, 145, 145])) # False: invalid start byte
print(validUTF8([229, 145]))             # False: incomplete sequence
```

## UTF-8 Examples

### ASCII Character 'A' (65):
```
Binary: 01000001
UTF-8:  01000001 (1 byte)
Valid:  True
```

### 2-byte Character (é):
```
Unicode: U+00E9
Binary:  11000011 10101001
UTF-8:   110xxxxx 10xxxxxx pattern
Valid:   True
```

### 3-byte Character (好):
```
Unicode: U+597D
Binary:  11100101 10100101 10111101  
UTF-8:   1110xxxx 10xxxxxx 10xxxxxx pattern
Valid:   True
```

### 4-byte Character (😀):
```
Unicode: U+1F600
Binary:  11110000 10011111 10011000 10000000
UTF-8:   11110xxx 10xxxxxx 10xxxxxx 10xxxxxx pattern  
Valid:   True
```

## Edge Cases

- **Empty data**: `[]` → True
- **Invalid start bytes**: `[250]` → False  
- **Missing continuation bytes**: `[229, 145]` → False
- **Extra continuation bytes**: `[65, 145]` → False
- **Large integers**: `[512]` → Use only lower 8 bits

## Complexity Analysis

- **Time Complexity**: O(n) where n is length of data
- **Space Complexity**: O(1) constant space

## Interview Tips

- Understand UTF-8 encoding principles thoroughly
- Master bit manipulation operations (>>, &, |)
- Handle state tracking for multi-byte sequences
- Consider edge cases and invalid inputs
- Explain the binary patterns clearly

---

*This project is part of the ALX Software Engineering interview preparation curriculum.*
