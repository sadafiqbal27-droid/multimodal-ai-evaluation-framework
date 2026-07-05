"""
Multimodal AI Evaluation Framework (MAEF)
Main Entry Point

Author: Sadaf Iqbal
"""

from core.cli import (
    display_header,
    display_menu,
    get_user_choice,
)

from core.task_manager import get_task_name

def main():
    display_header()
    display_menu()

    while True:
        choice = get_user_choice()
        task_name = get_task_name(choice)

        if task_name is None:
            print("\nInvalid option. Please choose a number between 0 and 6.")
        else:
            print(f"\nSelected Task: {task_name}")
            break

    print("\nThank you for using MAEF.")


if __name__ == "__main__":
    main()