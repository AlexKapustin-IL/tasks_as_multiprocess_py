import os
from time import sleep

from task_worker import TaskWorker


class TaskWorkerTask1(TaskWorker):
    def __init__(self, task_id):
        super().__init__(task_id)
        pass

    def do_task(self):
        SLEEP = 1
        print(f"Process number {self.task_id} started.PID=[{os.getpid()}].ClassHash={hash(self)}.")
        sleep(SLEEP)
        return f"Process {self.task_id} finished after sleeping for {SLEEP} second."




