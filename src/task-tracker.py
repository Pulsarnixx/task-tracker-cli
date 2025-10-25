#!/usr/bin/python3

from task import Task 

def add_task(task_list: list[Task], id: int, description: str) -> None:
    task_list.append(Task(id, description))
    
def update_task(task_list: list[Task], id: int, description: str) -> None:
    
    for task in task_list:
        if task.getId() == id:
            task.setDescription(description)
            break

def list_tasks(task_list: list[Task])-> None:
    for task in task_list:
        task.print()

def delete_task(task_list: list[Task], id: int):

    for task in task_list:
        if task.getId() == id:
            task_list.remove(task)
            break

def mark_task_as_done():
    pass

def mark_task_as_in_progress():
    pass

def main() -> None:

    global_id: int = 0
    task_list: list[Task] = []

    while True:
        option: str = input("task-cli ")

        match option:
            case 'add':
                add_task(task_list, global_id, "Zrobić zakupy")
                global_id += 1
                
            case 'update':
                update_task(task_list, 0, "Nie robić nic")
            case 'list':
                list_tasks(task_list)
            case 'delete':
                delete_task(task_list, 0)
            case 'mark-done':
                mark_task_as_done()
            case 'mark-in-progress':
                mark_task_as_in_progress()
            case 'exit':
                print("Exiting program...")
                break
            case _:
                print("Unsupported functionality.")

if __name__ == "__main__":
    main()