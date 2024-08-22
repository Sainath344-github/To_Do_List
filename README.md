1. Task Storage

Explanation: 
  - The `tasks` list is initialized as an empty list to store the tasks. Each task is represented as a sublist with two elements: the task description (a string) and its completion status (a boolean). This structure allows the program to track both the content of the task and whether it has been completed.

2. Display Tasks
Explanation: 
  - The `display_tasks()` function is responsible for showing all tasks to the user. It first checks if the `tasks` list is empty. If it is, a message "No tasks in the list." is displayed. If there are tasks, it loops through each task in the `tasks` list, displaying the task number, description, and whether it is marked as completed. Completed tasks are indicated by the text "(Completed)" next to the task description.

3. Add Task
Explanation: 
  - The `add_task()` function allows the user to add a new task to the list. It prompts the user to enter a task description, then creates a sublist containing this description and a `False` value (indicating the task is not yet completed). This sublist is appended to the `tasks` list. A confirmation message is printed to indicate that the task has been added.

4. Update Task
Explanation: 
  - The `update_task()` function allows the user to modify the description of an existing task. First, it displays the current list of tasks so the user can see the task numbers. The user is then prompted to enter the number of the task they want to update. If the number is valid, the user is asked to enter the new task description, which replaces the old description. If the number is invalid (outside the range of existing tasks), an error message is displayed.

5. Delete Task
Explanation: 
  - The `delete_task()` function enables the user to remove a task from the list. It displays the current tasks, allowing the user to see the task numbers. The user is then prompted to enter the number of the task they wish to delete. If the number is valid, the corresponding task is removed from the `tasks` list. If the number is invalid, an error message is shown.

6. Mark Task as Completed
Explanation: 
  - The `mark_completed()` function lets the user mark a task as completed. It first shows the list of tasks with their current status. The user selects a task by entering its number. If the input is valid, the completion status of that task is updated to `True`, and a confirmation message is printed. If the input is invalid, an error message is shown.

7. Main Loop
- Explanation: 
  - The main loop runs the program, continuously displaying a menu with options for the user. The user can choose to view tasks, add a new task, update an existing task, delete a task, mark a task as completed, or exit the program. Depending on the user's choice, the corresponding function is called. If the user chooses to exit, the loop ends, and the program terminates. If an invalid option is chosen, an error message prompts the user to try again.

8. Exiting the Program
Explanation:
  - The option to exit the program (`choice == '6'`) stops the loop, prints a goodbye message, and ends the program. This allows the user to close the to-do list application cleanly.
