import os
from abc import abstractmethod


class TaskWorker:
    TASK_TYPE_PI = "PI"
    TASK_TYPE_1 = "TYPE1"
    VALID_TASK_TYPES = [TASK_TYPE_PI, TASK_TYPE_1]
    def __init__(self, task_id):
        self.task_id = task_id  # Shared instance variable

    # you can detect exactly when Python’s pickle mechanism is triggered
    def __getstate__(self):
        print(f"Pickle: start in the process [{os.getpid()}]")
        return self.__dict__

    def __setstate__(self, state):
        print(f"Pickle: load in the process [{os.getpid()}]")
        self.__dict__.update(state)

    @abstractmethod
    def do_task(self):
        pass


