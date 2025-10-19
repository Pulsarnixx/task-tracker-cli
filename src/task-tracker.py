#!/usr/bin/python3

import task

def add_task():
    pass

def update_task():
    pass

def list_task():
    pass

def delete_task():
    pass

def mark_task_as_done():
    pass

def mark_task_as_in_progress():
    pass

def main() -> None:
    while True:
        option: str = input("task-cli: ")

        match option:
            case 'add':
                add_task()
            case 'update':
                update_task()
            case 'list':
                list_task()
            case 'delete':
                delete_task()
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