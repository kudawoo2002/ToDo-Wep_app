file_name = "todo.txt"


def get_todos(filepath=file_name):
    with open(filepath, 'r') as file:
        todos = file.readlines()
        return todos


def write_todo(todo_arg, filepath=file_name):
    with open(filepath, "w") as file:
        file.writelines(todo_arg)