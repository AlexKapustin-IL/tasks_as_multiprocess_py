# tasks_as_multiprocess_py

A lightweight Python program for exploring and running configurable task classes in parallel using multiprocessing.
Tasks are dynamically created and assigned to multiple processes using Python's `multiprocessing` module, 
with optional control over serialization (pickling).

Purpose:
Explore pure heavy computations with and without Python's serialization (pickling) mechanism.

## 🚀 Features
- Parallel task execution using `multiprocessing.Pool`
- Configurable number of tasks via CLI:         --tasks_num 100 
- Optional avoidance of `pickle` serialization: is true with --use_pickle, otherwise false
- Easy extension with custom task classes:      --task_type pi/type1
- Predefined tasks:
  - `TaskWorkerCalculatePI`: computes π using the Leibniz series
  - `TaskWorkerTask1`: simulates a time-consuming task via sleep -> feel free to customize it for your own logic.
CMD examples:
python tasks_as_multiprocess.py --tasks_num 100 --task_type pi --use_pickle
python tasks_as_multiprocess.py --tasks_num 100 --task_type pi 
---

## 📁 Project Structure

tasks_as_multiprocess_py/
├── tasks_as_multiprocess.py          # Main entry point
├── task_worker.py                    # Abstract base class: TaskWorker
├── task_worker_calculate_pi.py       # Concrete class: TaskWorkerCalculatePI
├── task_worker_task1.py              # Concrete class: TaskWorkerTask1
└── README.md                         # This file
