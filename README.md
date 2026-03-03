Task Tracker CLI
A simple command-line task management tool built with Python.

This application allows you to create, update, delete, and manage tasks directly from the terminal.


Installation
Clone the repository:

git clone https://github.com/yourusername/task-tracker-cli.git
cd task-cli

Create and activate a virtual environment:
python -m venv venv

Activate it:
venv\Scripts\activate

Install the project in editable mode:

pip install -e .


Usage

After installation, you can use the task-cli command from your terminal.

Add a Task
task-cli add "Task description"

Update a Task
task-cli update <task_id> "New task description"

List Tasks
task-cli list


Filter tasks by status:
task-cli list --filter todo
task-cli list --filter in-progress
task-cli list --filter done

Delete a Task
task-cli delete <task_id>

Mark Task Status
task-cli mark <task_id> todo
task-cli mark <task_id> in-progress
task-cli mark <task_id> done

Features

Add tasks
Update tasks
Delete tasks
Filter tasks by status
Mark tasks as todo, in-progress, or done

Author
Dany Fernandez