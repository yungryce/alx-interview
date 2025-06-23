<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue" alt="Log Parsing">
  <img src="https://img.shields.io/badge/Status-Active-green" alt="Status">
  <img src="https://img.shields.io/badge/Algorithm-Stream_Processing-orange" alt="Algorithm">
</p>

<div align="center">
  <h1>📊 Log Parsing</h1>
  <p><em>Real-time Stream Processing and Statistical Analysis</em></p>
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
This project implements a real-time log parsing system that reads HTTP access logs from stdin, validates the format, and computes statistics on-the-fly. It demonstrates stream processing, signal handling, and statistical analysis of incoming data in a production-like environment.

## 🎯 Learning Objectives
- Master real-time data stream processing
- Understand signal handling in Python
- Practice regular expressions and pattern matching
- Develop system monitoring and analysis skills
- Implement statistical analysis algorithms
- Handle system interrupts gracefully

## Problem Description

Write a script that reads stdin line by line and computes metrics from HTTP access logs.

### Input Format:
```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

### Requirements:
- Read from stdin line by line
- Print statistics every 10 lines or when interrupted (SIGINT)
- Track total file size and count of status codes
- Handle invalid log format gracefully

### Output Format:
```
File size: <total size>
<status code>: <number>
<status code>: <number>
...
```

### Valid Status Codes:
200, 301, 400, 401, 403, 404, 405, 500

## Files

- `0-stats.py`: Main log parser implementation
- `0-generator.py`: Log generator for testing
- `README.md`: This file
- `ARCHITECTURE.md`: Technical architecture documentation
- `PROJECT-MANIFEST.md`: Project manifest and learning guide

## Algorithm Implementation

```python
#!/usr/bin/python3
import sys
import signal
import re

# Global variables for statistics
total_size = 0
status_counts = {}
line_count = 0
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

def print_stats():
    """Print current statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def signal_handler(signum, frame):
    """Handle SIGINT signal"""
    print_stats()
    sys.exit(0)

def parse_line(line):
    """Parse a single log line"""
    pattern = r'^(\S+) - \[(.*?)\] "GET (\S+) HTTP/1.1" (\d+) (\d+)$'
    match = re.match(pattern, line.strip())
    
    if match:
        ip, date, path, status, size = match.groups()
        return status, int(size)
    return None, None

# Set up signal handler
signal.signal(signal.SIGINT, signal_handler)

# Initialize status code counters
for code in valid_codes:
    status_counts[code] = 0

try:
    for line in sys.stdin:
        line_count += 1
        status, size = parse_line(line)
        
        if status and size is not None:
            total_size += size
            if status in valid_codes:
                status_counts[status] += 1
        
        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
finally:
    print_stats()
```

## Usage

### Testing with Generator:
```bash
# Generate logs and parse them
./0-generator.py | ./0-stats.py

# Manual testing
echo '127.0.0.1 - [2023-01-01 00:00:00.000000] "GET /projects/260 HTTP/1.1" 200 5024' | ./0-stats.py
```

### Expected Output:
```
File size: 5024
200: 1
```

## Signal Handling

The script properly handles SIGINT (Ctrl+C):
- Prints current statistics before exiting
- Ensures data integrity during interruption
- Graceful shutdown without data loss

## Pattern Matching

Uses regular expressions to validate log format:
- Extracts IP address, timestamp, path, status code, and file size
- Validates complete log line structure  
- Ignores malformed lines gracefully

## Performance Considerations

- **Stream Processing**: Processes data in real-time without buffering
- **Memory Efficiency**: Constant space complexity O(1)
- **Signal Safety**: Thread-safe signal handling
- **Error Tolerance**: Continues processing despite invalid lines

## Edge Cases

- Invalid log format lines (ignored)
- Non-standard status codes (ignored) 
- Missing file size (ignored)
- Empty input (prints zeros)
- Large file sizes (handles integer overflow)

## Testing

```bash
# Test with sample data
echo '127.0.0.1 - [2023-01-01] "GET /test HTTP/1.1" 200 1024' | ./0-stats.py
echo '127.0.0.1 - [2023-01-01] "GET /test HTTP/1.1" 404 512' | ./0-stats.py  
```

---

*This project is part of the ALX Software Engineering interview preparation curriculum.*
