import os

from task_worker import TaskWorker


class TaskWorkerCalculatePI(TaskWorker):
    def __init__(self, task_id):
        super().__init__(task_id)
        self._TERMS = 1_000_000
        self.task_id = task_id
        #Important! When code contains system resources (e.g., files, locks)
        # like this: self.file = open("log.txt", "w")
        # it cause errors during pickling (serialization/deserialization).
        #otherwise you need to avoid pickling (see TasksManager.create_task)

    def _compute_pi_leibniz(self):
        pi_approx = 0
        for k in range(self._TERMS):
            pi_approx += (-1) ** k / (2 * k + 1)

        return 4 * pi_approx

    def do_task(self):
        print(f"Process number {self.task_id} started.PID=[{os.getpid()}].ClassHash={hash(self)}.")
        pi_val = self._compute_pi_leibniz()
        return f"Process number {self.task_id} finished with the result {pi_val}."




