"""
The interact command opens up an interactive console inside the debugger. The console's global namespace includes all names in the current scope. Allowing the console to interact with a snapshot of the application at the time the interactive console was opened.
"""


class Task:
    ''' A task that can be completed by setting the completed attribute to True. '''

    def __init__(self, task_name, completed, urgency=0.5):
        self.task_name = task_name
        self.completed = completed
        self.urgency = urgency

    def __repr__(self) -> str:
        return f'{self.task_name}: completed: {"Yes" if self.completed else "No"}'


def tasks_by_urgency(all_tasks):
    ''' Implement the body of this function so it returns a list of tasks sorted by urgency.
        Urgency ranges between 0 and 1 (lowest to highest).

        Args:
            all_tasks   | A list of Task objects.
    '''
    breakpoint()
    return []


if __name__ == '__main__':
    tasks = [
        ('Feed the cat', True, 1.0),
        ('Learn Python', True, 0.75),
        ('Break gravity', False, 0.25),
        ('Disprove time', False, 0.35),
    ]
    tasks = [Task(name, completed, urgency) for (name, completed, urgency) in tasks]

    print("Today's TODO list:")
    print(*tasks_by_urgency(tasks), sep='\n')