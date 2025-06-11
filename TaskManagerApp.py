from TaskManager import TaskManager, Menu


def main():
    manager = TaskManager()
    while True:
        print(
            'TASK MANAGER:\n'
            '1. Add task \n'
            '2. Mark task as completed \n'
            '3. Show task list \n'
            '4. Remove task from list \n'
            '5. Show list of completed tasks \n'
            '6. Show list of uncompleted tasks \n'
            '7. Save list \n'
            '8. Load list \n'
            '9. End'
        )

        try:
            choice = Menu(int(input('What would you like to do? \n')))
        except ValueError:
            print('\nYou have chosen invalid option.\n')
            continue
        except Exception as e:
            print(f'Error: {e}')

        if choice == Menu.ADD_TASK:
            task = input('What task would you like to add? \n')
            manager.add_task(task)
        elif choice == Menu.COMPLETE_TASK:
            task = input('What task would you like to complete? \n')
            manager.complete_task(task)
        elif choice == Menu.SHOW_LIST:
            manager.show_list()
        elif choice == Menu.REMOVE_TASK:
            task = input('What task would you like to remove? \n')
            manager.remove_from_list(task)
        elif choice == Menu.SHOW_LIST_OF_COMPLETED_TASKS:
            manager.list_of_completed_tasks()
        elif choice == Menu.SHOW_LIST_OF_UNFINISHED_TASKS:
            manager.list_of_unfinished_tasks()
        elif choice == Menu.SAVE_LIST:
            manager.save_list()
        elif choice == Menu.LOAD_LIST:
            manager.load_list()
        elif choice == Menu.END:
            print('\nClosing...')
            break
        else:
            print('\nYou have chosen wrong option\n')
            continue


if __name__ == '__main__':
    main()
