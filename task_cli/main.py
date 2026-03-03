
import argparse
import json 
from datetime import datetime
    
def load_tasks():  
    try:
        with open("tasks.json", "r") as file:

            data = json.load(file)
            return data 
    except FileNotFoundError:
        return {}

def save_tasks(data):
    with open("tasks.json", "w") as file:
        json.dump(data, file, indent = 4)



def add_task(args):
        all_task = load_tasks()
        todo_id = int(max(all_task.keys(), default = 0)) + 1
        time = datetime.now()

        task_properties = {
        "id":todo_id,
        "description":args.task,
        "status":"todo",
        "createdAt":time.strftime("%a-%d%b-%Y, %I:%M%p"),
        "UpdatedAt":None
       
        }

        all_task[todo_id] = task_properties
        save_tasks(all_task)

        print(f"'{args.task}' added to your tasks{time.strftime(" on %a-%d%b-%Y, at %I:%M%p")}, ID: {todo_id}") 
        return all_task
#List tasks       
def list_tasks(args):
    all_task = load_tasks()

    counter = 0
    for task in all_task.values():
        if args.filter is None:
            counter += 1
            print(task)

        elif task["status"] == args.filter:
            counter += 1
            print(task)
    if counter == 0:
        print(f"No tasks were found")
            


def delete_task(args):
    all_task = load_tasks()
    
    if args.id not in all_task:
        print('You provided a non existing task id')
    else:
        all_task.pop(args.id)

        print(f"task {args.id} has been deleted")

        save_tasks(all_task)

def mark_task(args):
    all_task = load_tasks()

    if args.id not in all_task:
         print('You provided a non existing task id')

    all_task[args.id]["status"] = args.status

    save_tasks()
    print(f"task status changed to {args.status}.")

def update_task(args):

    all_task = load_tasks()
    if args.id not in all_task:
         print('You provided a non existing task id')
    time = datetime.now()
    all_task[args.id]["description"] = args.description
    all_task[args.id]["UpdateAt"] = time

    save_tasks()
    print(f"task {args.id} updated{time.strftime(" on %a-%d%b-%Y, at %I:%M%p")}")

    
def main():

    #Main parser and subparser
    parser = argparse.ArgumentParser(prog = "TaskTracker", description = "This is CLI app to help you manage your tasks")
    subparser = parser.add_subparsers(dest = "command")

    #add command
    parser_add = subparser.add_parser("add", help = "Use this command to add a task")
    parser_add.add_argument("task", help = "short description")
    parser_add.set_defaults(func = add_task)

    #list command
    parser_list = subparser.add_parser("list", help = "Use this command to display your tasks")
    parser_list.add_argument('--filter', choices = ["todo", "done", "in-progress"])
    parser_list.set_defaults(func = list_tasks)

    #delete command
    parser_delete = subparser.add_parser("delete", help = "Use this command to delete a specified task")
    parser_delete.add_argument("id",help = "Enter a task ID")
    parser_delete.set_defaults(func = delete_task)

    #mark command 
    parser_mark = subparser.add_parser("mark", help = "Use this command to change your tasks' status.")
    parser_mark.add_argument("id")
    parser_mark.add_argument("status", choices = ["done", "todo", "in-progress"])
    parser_mark.set_defaults(func = mark_task)

    #update command
    parser_update = subparser.add_parser("update", help = "Update your tasks' description")
    parser_update.add_argument("id", help = "Enter a task ID")
    parser_update.add_argument("description", help = "Enter a new description")
    parser_update.set_defaults(func = update_task)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else: 
        parser.print_help()

if __name__=="__main__":
    main()

















