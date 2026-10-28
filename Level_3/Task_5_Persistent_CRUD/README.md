# Task 5: Persistent CRUD Application

## Internship
Cognifyz Technologies — Software Development Internship

## Description
A Python console application that manages tasks using CRUD operations and stores them in a JSON file so they remain available after restarting the program.

## Features
- Add, view, update, and delete tasks
- Save tasks to `tasks.json`
- Load saved tasks at startup
- Handle invalid menu choices and task numbers
- Handle missing or invalid JSON files
- Validate task input

## Technologies Used
- Python 3
- JSON
- pathlib

## How to Run
From the project root, execute:

`python Level_3/Task_5_Persistent_CRUD/main.py`

## Data Storage
Tasks are stored in `tasks.json` in the same folder as `main.py`.

## Concepts Learned
- File handling
- JSON serialization and deserialization
- Exception handling
- CRUD operations
- Persistent data storage

## Testing
Verified that tasks can be added, viewed, and retained after restarting the application.

## Learning Outcome
Learned to extend a console application with persistent storage using JSON and Python file operations.