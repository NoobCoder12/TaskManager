# Task Manager

A simple task manager in Python that allows you to add, mark as completed, remove, display, save, and load tasks from a file.
## Features

  Add new tasks

  Mark tasks as completed

  Remove tasks from the list

  Display the full task list

  Display lists of completed and unfinished tasks

  Save the task list to a file (task_list.txt)

  Load the task list from a file (task_list.txt)

  Simple console menu interface

## How to Use

Run the main script:

    python main.py

Choose an option from the menu by entering the corresponding number and pressing Enter.

## File Structure

  TaskManager.py – contains the Task and TaskManager classes responsible for task management logic

  main.py – user interface (console menu)

  test_task_manager.py – unit tests for the task manager functionality (uses pytest)

## Installation and Testing

   Make sure you have Python 3.6+ installed

  Install pytest if you want to run tests:

    pip install pytest

  To run the tests, execute the following command in the project directory:

    pytest

## Example Usage

TASK MANAGER:
1. Add task 
2. Mark task as completed 
3. Show task list 
4. Remove task from list 
5. Show list of completed tasks 
6. Show list of uncompleted tasks 
7. Save list 
8. Load list 
9. End

        What would you like to do? 
        > 1
        What task would you like to add? 
        > Clean the house
        Task was added to list.

## Notes

  The task list is saved to and loaded from a file named task_list.txt located in the same directory as the script.

  Tasks are stored in a text format where each line contains task|is_completed.

  The menu provides basic input validation.

## Author

NoobCoder12

## License

This project is licensed under the MIT License.
