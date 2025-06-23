<p align="center">
  <img src="https://img.shields.io/badge/JavaScript-ES6-yellow" alt="Star Wars API">
  <img src="https://img.shields.io/badge/Status-Active-green" alt="Status">
  <img src="https://img.shields.io/badge/API-REST-blue" alt="API">
</p>

<div align="center">
  <h1>🌟 Star Wars API</h1>
  <p><em>API Integration and Asynchronous Data Processing</em></p>
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
This project integrates with the Star Wars API (SWAPI) to fetch and display character information for specific films. It demonstrates API consumption, asynchronous request handling, and data processing from external web services using JavaScript and modern async/await patterns.

## 🎯 Learning Objectives

- Master RESTful API integration and consumption
- Understand asynchronous programming with callbacks
- Practice HTTP request handling and JSON processing
- Develop external service integration skills

## Problem Description

Write a script that prints all characters of a Star Wars movie using the Star Wars API. The script takes a movie ID as an argument and displays all characters from that film in the same order as the "characters" list in the `/films/` endpoint.

### Usage:
```bash
./0-starwars_characters.js <Movie ID>
```

### Example:
```bash
./0-starwars_characters.js 3
# Output:
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
...
```

## Requirements

- **Language**: JavaScript (Node.js)
- **Module**: request module for HTTP requests
- **Input**: Movie ID as command line argument
- **Output**: Character names, one per line

## Files

- `0-starwars_characters.js`: Main implementation
- `README.md`: This file
- `ARCHITECTURE.md`: Technical architecture documentation
- `PROJECT-MANIFEST.md`: Project manifest and learning guide

## API Integration

### Star Wars API Endpoints:
- **Films**: `https://swapi-api.alx-tools.com/api/films/<id>/`
- **Characters**: Individual character URLs from film data

### Data Flow:
1. Fetch film data using movie ID
2. Extract character URLs from film response
3. Make individual requests for each character
4. Display character names in correct order

## Implementation Approach

The solution requires handling nested API calls while maintaining the correct order of characters as they appear in the film's character list.

## Complexity Considerations

- **Network Requests**: Multiple HTTP calls for character data
- **Asynchronous Handling**: Managing callback-based requests
- **Order Preservation**: Maintaining character sequence
- **Error Handling**: Network and API error management

---

*This project is part of the ALX Software Engineering interview preparation curriculum.*
