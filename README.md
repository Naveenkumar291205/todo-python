# ✅ Python To-Do List Application

> A feature-rich command-line To-Do List application built with Python, featuring task persistence, priorities, filtering, progress tracking, and a colorful interactive terminal interface.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![JSON](https://img.shields.io/badge/Storage-JSON-000000?style=for-the-badge&logo=json&logoColor=white)](#)
[![CLI](https://img.shields.io/badge/Application-CLI-success?style=for-the-badge)](#)
[![Colorama](https://img.shields.io/badge/Colorama-Terminal%20UI-ff69b4?style=for-the-badge)](https://pypi.org/project/colorama/)

---

## 📌 About the Project

This project is a **command-line task management application** developed using Python.

It provides an interactive terminal interface where users can create, view, complete, delete, filter, and summarize their tasks.

Unlike a basic To-Do application, this project also includes:

- Task priorities
- Completion tracking
- Persistent JSON storage
- Task filtering
- Progress visualization
- Priority statistics
- Automatic timestamps
- Color-coded terminal output
- Graceful error handling

The application is designed as a practical Python project for learning **functions, file handling, JSON, lists, dictionaries, exception handling, and CLI application design**.

---

# 🚀 Features

## ➕ Add Task

Users can create a task by entering:

- Task name
- Priority level

Available priorities:

```text
🔴 High
🟡 Medium
🟢 Low
```

Each new task automatically receives:

- Unique ID
- Current date
- Current time
- Pending status

Example task structure:

```json
{
  "id": 1,
  "task": "Complete Python project",
  "priority": "High",
  "done": false,
  "time": "09:30 PM",
  "date": "09 Jun 2026"
}
```

---

## 📋 View All Tasks

Tasks are displayed in a formatted terminal table showing:

```text
No. | Task | Priority | Status | Date
```

The interface uses colors to make priority and completion states easier to identify.

---

## ✅ Mark Task as Completed

Users can select any pending task and mark it as completed.

Example:

```text
⏳ Pending
      ↓
✅ Done
```

The updated task state is automatically saved to `tasks.json`.

---

## 🗑️ Delete Task

Users can delete individual tasks.

Before deletion, the application asks for confirmation:

```text
Delete 'Complete Python project'? (y/n)
```

This prevents accidental task removal.

---

## 🔍 Filter Tasks

The application supports multiple filtering modes:

```text
1. Show All Tasks
2. Show Pending Tasks Only
3. Show Completed Tasks Only
4. Filter by Priority
```

Priority filters include:

```text
High
Medium
Low
```

---

## 🧹 Clear Completed Tasks

Users can remove all completed tasks at once.

The application displays the number of completed tasks before asking for confirmation.

Example:

```text
Clear 3 completed task(s)? (y/n)
```

---

## 📊 Task Summary

The summary dashboard provides:

- Total tasks
- Completed tasks
- Pending tasks
- High-priority count
- Medium-priority count
- Low-priority count
- Completion percentage
- ASCII progress bar

Example:

```text
📊 TASK SUMMARY

Total Tasks:       10
Completed:         6
Pending:           4

High Priority:     2
Medium Priority:   5
Low Priority:      3

Progress:
████████████░░░░░░░░  60%  (6 of 10 done)
```

---

## 💾 Persistent Storage

Tasks are stored in:

```text
tasks.json
```

This means tasks remain available even after the program is closed.

The application automatically:

- Loads tasks when it starts
- Saves tasks after modifications
- Saves tasks before exiting
- Saves tasks when interrupted with `Ctrl+C`

---

# 🎨 Terminal Interface

The application uses **Colorama** to create a more readable command-line interface.

Different colors represent:

| Color | Meaning |
|---|---|
| 🔴 Red | High priority / error |
| 🟡 Yellow | Medium priority / warning |
| 🟢 Green | Low priority / success |
| 🔵 Cyan | Information / navigation |
| 🟣 Magenta | Summary section |

---

# 🧭 Application Menu

The main menu contains nine operations:

```text
╔══════════════════════════════════════╗
║      📋  MY TO-DO LIST               ║
╠══════════════════════════════════════╣
║  1.  ➕  Add Task                    ║
║  2.  📄  View All Tasks              ║
║  3.  ✅  Mark Task as Completed      ║
║  4.  🗑️  Delete a Task              ║
║  5.  🔍  Filter Tasks                ║
║  6.  🧹  Clear All Completed         ║
║  7.  📊  Show Summary                ║
║  8.  💾  Save Tasks                  ║
║  9.  🚪  Exit                        ║
╚══════════════════════════════════════╝
```

---

# 🏗️ Project Architecture

The project follows a simple functional architecture:

```text
User
 │
 ▼
Main Menu
 │
 ├── Add Task
 │      ↓
 │   Task Creation
 │      ↓
 │   JSON Storage
 │
 ├── View Tasks
 │
 ├── Complete Task
 │      ↓
 │   Update Status
 │
 ├── Delete Task
 │
 ├── Filter Tasks
 │
 ├── Clear Completed
 │
 ├── Show Summary
 │
 ├── Save Tasks
 │
 └── Exit
        ↓
    Save JSON
```

---

# 📂 Project Structure

```text
todo-python/
│
├── todo.py
│   └── Main Python application
│
└── tasks.json
    └── Persistent task storage
```

---

# 🧩 Main Functions

The application is divided into logical functions.

### Utility

```python
clear_screen()
get_priority_color()
progress_bar()
```

### Storage

```python
load_tasks()
save_tasks()
```

### Display

```python
show_menu()
view_tasks()
```

### Task Management

```python
add_task()
complete_task()
delete_task()
filter_tasks()
clear_completed()
show_summary()
```

### Application Entry Point

```python
main()
```

This functional structure keeps individual responsibilities separated and makes the code easier to understand and maintain.

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Core application logic |
| **JSON** | Persistent task storage |
| **Colorama** | Colored terminal output |
| **Datetime** | Task date and time tracking |
| **OS** | Terminal screen management |

---

# 📦 Requirements

The application requires:

```text
Python 3.x
Colorama
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/Naveenkumar291205/todo-python.git
```

## 2. Enter the project directory

```bash
cd todo-python
```

## 3. Install the dependency

```bash
pip install colorama
```

---

# ▶️ Run the Application

Execute:

```bash
python todo.py
```

The application will load existing tasks from `tasks.json` and open the interactive menu.

---

# 🔄 Data Flow

Task creation follows this flow:

```text
User Input
   ↓
Validation
   ↓
Task Dictionary
   ↓
Python List
   ↓
tasks.json
```

When the application starts:

```text
tasks.json
   ↓
JSON Parsing
   ↓
Python List
   ↓
CLI Display
```

---

# 🗃️ Task Data Model

Each task is represented using a Python dictionary.

```json
{
  "id": 2,
  "task": "Read Clean Code book",
  "priority": "Medium",
  "done": false,
  "time": "08:52 PM",
  "date": "09 Jun 2026"
}
```

### Fields

| Field | Description |
|---|---|
| `id` | Unique task identifier |
| `task` | Task description |
| `priority` | High, Medium, or Low |
| `done` | Completion status |
| `time` | Creation time |
| `date` | Creation date |

---

# 🛡️ Error Handling

The application includes exception handling for common runtime problems such as:

- Invalid numeric input
- Invalid priority selection
- Invalid menu selection
- Missing task file
- Corrupted JSON
- File I/O errors
- Unexpected runtime errors
- `Ctrl+C` interruption

For example, if `tasks.json` contains invalid JSON, the application safely starts with an empty task list rather than crashing immediately.

---

# 📈 Learning Outcomes

This project demonstrates practical usage of several core Python concepts:

```text
Variables
   ↓
Lists & Dictionaries
   ↓
Functions
   ↓
Conditional Logic
   ↓
Loops
   ↓
Exception Handling
   ↓
File Handling
   ↓
JSON Serialization
   ↓
CLI Application Design
```

It is particularly useful for practicing Python fundamentals before moving into frameworks such as Flask or FastAPI.

---

# 🔮 Future Improvements

Possible upgrades for a more advanced version:

- Task editing
- Due dates
- Task categories
- Search functionality
- Recurring tasks
- Sorting by priority/date
- Export to CSV
- SQLite database
- User authentication
- Desktop GUI using Tkinter
- Web version using Flask
- REST API using FastAPI
- Unit tests with Pytest
- Configuration file
- Multi-user task management

---

# 💡 Possible Next Version

The project can evolve into a full-stack task-management application:

```text
                 TODO PLATFORM
                      │
       ┌──────────────┼──────────────┐
       │              │              │
    Frontend        Backend        Database
       │              │              │
     React          Flask/FastAPI   PostgreSQL
       │              │              │
       └──────────────┼──────────────┘
                      ↓
              Authentication
                      ↓
              Task Management
                      ↓
               Analytics
```

---

# 👨‍💻 Author

**Naveen Kumar M**

GitHub:  
https://github.com/Naveenkumar291205

---

# 📜 Project Type

**Python CLI / Internship Project**

The source file identifies this project as a Python internship project associated with **SaiTech Solution**.

---

# ⭐ Project Highlights

- Beginner-friendly Python architecture
- Interactive command-line interface
- Persistent JSON storage
- Priority-based task management
- Task filtering
- Completion tracking
- Progress visualization
- Colored terminal experience
- Robust input and file error handling

---

## 🎯 Project Goal

> **Build a simple but practical task management system while strengthening Python programming fundamentals and application design skills.**

Made with **Python + JSON + Colorama**.
