import argparse
from multiprocessing import Event, Process, cpu_count, Pool

from task_worker import TaskWorker
from task_worker_calculate_pi import TaskWorkerCalculatePI
from task_worker_task1 import TaskWorkerTask1


class TasksManager:
    def __init__(self):
        # command line parser
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--tasks_num", type=int)
        self.parser.add_argument("--use_pickle", action="store_true")
        self.parser.add_argument("--task_type", choices=TaskWorker.VALID_TASK_TYPES, type=str.upper)
        self.args = self.parser.parse_args()
        self.tasks_num = self.args.tasks_num
        self.use_pickle = self.args.use_pickle
        self.task_type = self.args.task_type
        # other parameters
        self.num_cores = cpu_count()

    @property
    def tasks_number(self):
        return self.tasks_num

    @staticmethod
    def task_wrapper(task_type, task_id):
        return TasksManager.create_object(task_type, task_id).do_task()

    @staticmethod
    def create_object(task_type, task_id):
        if task_type == TaskWorker.TASK_TYPE_PI:
            return TaskWorkerCalculatePI(task_id)
        elif task_type == TaskWorker.TASK_TYPE_1:
            return TaskWorkerTask1(task_id)
        else:
            raise ValueError(f"Unknown task type: {task_type}")

    def create_task(self, pool: Pool, task_id: int):
        if self.use_pickle:
            # These lines of code trigger the pickle mechanism.
            task_worker = TasksManager.create_object(self.task_type, task_id+1)
            pool.apply_async(task_worker.do_task, callback=TasksManager.callback_res)
        else:
            # use the TasksManager.task_wrapper function to avoid Python’s pickle mechanism
            pool.apply_async(TasksManager.task_wrapper, args=(self.task_type, task_id + 1), callback=TasksManager.callback_res)

    def run_tasks(self):
        print(f"_____________________\nCPU cores: {self.num_cores}")

        try:
            with Pool(cpu_count()) as pool:
                for i in range(self.tasks_num):
                    self.create_task(pool, i)
                pool.close()
                pool.join()
        except Exception as e:
            print(f"apply_async failed due to: {e}")

    @staticmethod
    def callback_res(result) -> None:
        print(f"Callback with result: {result}")



