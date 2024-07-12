# Write a program to implement a given list of tasks with regards to their priority.

from collections import deque

def task_priority(tasks):
    result = []
    queue = deque()
    for task in tasks:
        queue.append(task)

    while queue:
        current = queue.popleft()
        if current[1] == "high":
            result.insert(0, current[0])
        else:
            result.append(current[0])

    return result

tasks = [("task1", "high"), ("task2", "low"), ("task3", "high"), ("task4", "low")]
print(task_priority(tasks))




