"""
Task Manager Module

Manages available evaluation tasks for MAEF.
"""


TASKS = {
    "1": "Generic Image Evaluation",
    "2": "Infographic Evaluation",
    "3": "Product Advertisement Evaluation",
    "4": "Prompt Iteration Evaluation",
    "5": "Style Transfer Evaluation",
    "6": "Image Editing Evaluation",
    "0": "Exit",
}


def get_task_name(choice):
    """Return the task name for a selected menu choice."""

    return TASKS.get(choice)