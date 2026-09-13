import sqlite3


class Todo:
    def __init__(self):
        self.conn = sqlite3.connect("./sqlite3_/todo.db")
        self.c = self.conn.cursor()
        self.create_task_table()

    def create_task_table(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS tasks (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     priority INTEGER NOT NULL
                     );""")

    def add_task(self):
        name = input("Enter task name: ")
        if not name:
            raise RuntimeError("Task name can't be empty")

        priority = input("Enter priority: ")
        self._validate_task_priority(priority)

        task_exists = self._find_task(name)
        if task_exists:
            raise RuntimeError(f"Task named {name} already exists")

        self.c.execute(
            "INSERT INTO tasks (name, priority) VALUES (?,?)", (name, priority)
        )
        self.conn.commit()

    def show_tasks(self):
        self.c.execute("SELECT * FROM tasks")
        columns = [desc[0] for desc in self.c.description]

        for task in self.c:
            for column, value in zip(columns, task):
                print(f"{column}: {value}")

            print()

    def change_priority(self):
        task_id_to_update = input("Enter task id to change task priority: ")
        task_exists = self._find_task_by_id(task_id_to_update)

        if not task_exists:
            raise RuntimeError(f"A task with the id {task_id_to_update} doesn't exist")

        current_task_priority = task_exists[2]
        new_task_priority = input(
            f"Enter new task priority (current: {current_task_priority}): "
        )

        self._validate_task_priority(new_task_priority)

        if new_task_priority == current_task_priority:
            raise RuntimeError("New task priority can't be equal to the current one")

        self.c.execute(
            "UPDATE tasks SET priority = ? WHERE id = ?",
            (new_task_priority, task_id_to_update),
        )
        self.conn.commit()

    def delete_task(self):
        task_id_to_delete = input("Enter task id to delete: ")
        task_exists = self._find_task_by_id(task_id_to_delete)

        if not task_exists:
            raise RuntimeError(f"A task with the id {task_id_to_delete} doesn't exist")

        self.c.execute("DELETE FROM tasks WHERE id = ?", (task_id_to_delete,))
        self.conn.commit()

    def _validate_task_priority(self, priority):
        try:
            priority = int(priority)
        except ValueError:
            raise TypeError("Priority must be an integer")

        if priority < 1:
            raise RuntimeError("Priority can't be less than 1")

    def _find_task(self, task_name):
        self.c.execute("SELECT * FROM tasks WHERE name LIKE ?", (task_name,))
        task = self.c.fetchone()

        return task

    def _find_task_by_id(self, task_id):
        self.c.execute("SELECT * FROM tasks WHERE id LIKE ?", (task_id,))
        task = self.c.fetchone()

        return task


if __name__ == "__main__":
    app = Todo()

    while True:
        print("TODO")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Change Priority")
        print("4. Delete Task")
        print("5. Exit")

        print()
        option = input("Enter your option: ")
        print()

        try:
            match option:
                case "1":
                    print("1. Show Tasks")
                    print()
                    app.show_tasks()
                case "2":
                    print("2. Add Task")
                    print()

                    app.add_task()

                    print()
                    print("Task has been added")
                case "3":
                    print("3. Change Priority")
                    print()

                    app.change_priority()

                    print()
                    print("Task priority has been updated")
                case "4":
                    print("4. Delete Task")
                    print()

                    app.delete_task()

                    print()
                    print("Task has been deleted")
                case "5":
                    print("Exiting...")
                    exit()
                case _:
                    print("Invalid option, try again")
        except RuntimeError as e:
            print()
            print(f"Error: {e}")

        print()
        print("-" * 100)
        print()
