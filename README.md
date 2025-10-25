# Task Tracker CLI

A simple **Task Tracker** CLI tool written in Python.
The project was written with the aim of developing skills in Python and learning new tools.

---

## :toolbox: Tech stack
| **Tool / Library** | **Purpose** |
|:----------------:|:----------:|
| **Python 3.x** | Core programming language |
| **venv** | Virtual environment for dependency isolation |
| **pydoc** | Built-in documentation generator |
| **pdb** | Python Debugger |
| **mypy** | Static typing for Python |

## Requirements

- task saved in JSON file
- user can:
    - Add, Update, and Delete tasks
    - Mark a task as in progress or done
    - List all tasks
    - List all tasks that are done
    - List all tasks that are not done
    - List all tasks that are in progress

## Example

```bash
# Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress
```
