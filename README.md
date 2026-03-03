# Task Tracker CLI

A simple command-line task management tool built with Python.

This application allows you to create, update, delete, and manage tasks directly from the terminal.

---

### Project URL: https://roadmap.sh/projects/task-tracker

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/task-tracker-cli.git
cd task-cli
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it (Windows):

```bash
venv\Scripts\activate
```

Install the project in editable mode:

```bash
pip install -e .
```

---

## Usage

After installation, you can use the `task-cli` command from your terminal.

### Add a Task

```bash
task-cli add "Task description"
```

### Update a Task

```bash
task-cli update 1 "New task description"
```

### List Tasks

```bash
task-cli list
```

### Filter Tasks by Status

```bash
task-cli list --filter todo
task-cli list --filter in-progress
task-cli list --filter done
```

### Delete a Task

```bash
task-cli delete 1
```

### Mark Task Status

```bash
task-cli mark 1 todo
task-cli mark 1 in-progress
task-cli mark 1 done
```

---

## Features

- Add tasks
- Update tasks
- Delete tasks
- Filter tasks by status
- Mark tasks as `todo`, `in-progress`, or `done`

---


## Author

Dany Fernandez