# Project Manifest

## Project Information
- **Project Name**: Log Parsing
- **Container**: 0x03-log_parsing
- **Category**: Data Processing & System Programming
- **Difficulty Level**: Intermediate
- **Topics**: Stream Processing, Regular Expressions, Signal Handling

## Learning Objectives
- Master real-time data stream processing
- Understand signal handling in Python
- Practice pattern matching and data validation
- Develop system monitoring and analysis skills

## Files Structure
```
0x03-log_parsing/
├── 0-stats.py                  # Main log parser implementation
├── 0-generator.py              # Log generator for testing
├── README.md                   # Project description
├── ARCHITECTURE.md             # Technical architecture
└── PROJECT-MANIFEST.md        # This file
```

## Implementation Requirements
- **Language**: Python 3.x
- **Input**: stdin log lines in specific format
- **Output**: Statistics every 10 lines and on SIGINT
- **Format**: `<IP> - [<date>] "GET <file> HTTP/1.1" <status> <size>`
- **Performance**: Real-time processing capability

## Key Concepts
1. **Stream Processing**
   - Process data as it arrives
   - Handle continuous input streams
   - Maintain running statistics
   - Memory-efficient processing

2. **Signal Handling**
   - Graceful shutdown on SIGINT
   - Preserve data integrity
   - Clean termination procedures
   - System interrupt management

3. **Pattern Matching**
   - Regular expression validation
   - String parsing techniques
   - Data format compliance
   - Error handling for malformed input

## Success Criteria
- ✅ Correct log format parsing
- ✅ Real-time statistics computation
- ✅ Proper signal handling
- ✅ Efficient memory usage
- ✅ Accurate metric reporting

---

*This project builds essential skills in system programming and data processing, crucial for backend development and system administration roles.*
