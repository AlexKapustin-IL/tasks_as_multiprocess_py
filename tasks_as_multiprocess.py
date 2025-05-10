import time
from tasks_manager import TasksManager

if __name__ == '__main__':
    print(f"Start PY script.")
    tasks = TasksManager()

    start = time.perf_counter()
    tasks.run_tasks()
    end = time.perf_counter()

    duration = (end - start) * 1000
    print(f"_____________________\nAll took {duration:.2f} ms")

    print(f"All {tasks.tasks_number} tasks have completed.")
