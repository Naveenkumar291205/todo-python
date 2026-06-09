# ─────────────────────────────────────────────────────────────
# To-Do List Application
# Python Internship Project — SaiTech Solution
# Author: Your Name Here
# ─────────────────────────────────────────────────────────────
# Requirements: pip install colorama
# Run with:     python todo.py
# ─────────────────────────────────────────────────────────────

import os
import json
import datetime
from colorama import Fore, Back, Style, init

# Initialize colorama with autoreset enabled (colors reset after each print)
init(autoreset=True)

# Global list to store all tasks in memory
tasks = []

# ═════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ═════════════════════════════════════════════════════════════

def clear_screen():
    """Clear the terminal screen (works on Windows and Unix/Mac)."""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_priority_color(priority):
    """
    Return colorama Fore color based on priority string.
    
    Args:
        priority (str): Priority level - "High", "Medium", or "Low"
    
    Returns:
        str: Colorama Fore color code
    """
    if priority == "High":
        return Fore.RED + Style.BRIGHT
    elif priority == "Medium":
        return Fore.YELLOW + Style.BRIGHT
    elif priority == "Low":
        return Fore.GREEN + Style.BRIGHT
    else:
        return Fore.WHITE


def progress_bar(done, total):
    """
    Generate an ASCII progress bar showing completion percentage.
    
    Args:
        done (int): Number of completed tasks
        total (int): Total number of tasks
    
    Returns:
        str: Formatted progress bar string with percentage (e.g., "████████░░░░░░░░░░░░  40%")
    """
    if total == 0:
        return f"{Fore.CYAN}░░░░░░░░░░░░░░░░░░░░  0% (0 of 0 done)"
    
    # Calculate percentage and bar length
    percentage = int((done / total) * 100)
    filled = int((done / total) * 20)  # 20 character bar
    empty = 20 - filled
    
    # Build the bar with filled (█) and empty (░) characters
    bar = f"{Fore.CYAN}{'█' * filled}{'░' * empty}  {percentage}%  ({done} of {total} done)"
    return bar


# ═════════════════════════════════════════════════════════════
# FILE PERSISTENCE FUNCTIONS
# ═════════════════════════════════════════════════════════════

def load_tasks():
    """
    Load tasks from tasks.json file.
    If file doesn't exist, return empty list.
    
    Returns:
        list: List of task dictionaries loaded from JSON file
    """
    global tasks
    try:
        # Check if tasks.json exists in the current directory
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
                print(f"{Fore.GREEN}✓ Tasks loaded from tasks.json")
                return tasks
        else:
            # File doesn't exist yet (first run)
            tasks = []
            return tasks
    except json.JSONDecodeError:
        # File is corrupted, start fresh
        print(f"{Fore.YELLOW}⚠ tasks.json is corrupted. Starting with empty task list.")
        tasks = []
        return tasks
    except Exception as e:
        # Catch any other unexpected errors
        print(f"{Fore.RED}✗ Error loading tasks: {e}")
        tasks = []
        return tasks


def save_tasks():
    """
    Save all tasks to tasks.json file.
    Creates the file if it doesn't exist.
    """
    try:
        # Write tasks list as formatted JSON
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=2)
        print(f"{Fore.GREEN}💾 Tasks saved to tasks.json")
    except Exception as e:
        # Catch any file I/O errors
        print(f"{Fore.RED}✗ Error saving tasks: {e}")


# ═════════════════════════════════════════════════════════════
# MENU AND DISPLAY FUNCTIONS
# ═════════════════════════════════════════════════════════════

def show_menu():
    """
    Display the main menu with current date/time and all options.
    Clears screen and shows formatted menu box.
    """
    clear_screen()
    
    # Get current date and time for display
    now = datetime.datetime.now()
    date_str = now.strftime("%A, %d %B %Y")
    time_str = now.strftime("%I:%M %p")
    
    # Display menu header with current date/time
    print(f"\n{Fore.CYAN}╔══════════════════════════════════════╗")
    print(f"{Fore.CYAN}║      📋  MY TO-DO LIST               ║")
    print(f"{Fore.CYAN}║      {date_str}  {time_str}  ║")
    print(f"{Fore.CYAN}╠══════════════════════════════════════╣")
    print(f"{Fore.CYAN}║  1.  ➕  Add Task                    ║")
    print(f"{Fore.CYAN}║  2.  📄  View All Tasks              ║")
    print(f"{Fore.CYAN}║  3.  ✅  Mark Task as Completed      ║")
    print(f"{Fore.CYAN}║  4.  🗑️   Delete a Task              ║")
    print(f"{Fore.CYAN}║  5.  🔍  Filter Tasks                ║")
    print(f"{Fore.CYAN}║  6.  🧹  Clear All Completed         ║")
    print(f"{Fore.CYAN}║  7.  📊  Show Summary                ║")
    print(f"{Fore.CYAN}║  8.  💾  Save Tasks                  ║")
    print(f"{Fore.CYAN}║  9.  🚪  Exit                        ║")
    print(f"{Fore.CYAN}╚══════════════════════════════════════╝\n")


def view_tasks(task_list=None):
    """
    Display all tasks in a formatted table with columns: No. | Task | Priority | Status | Date | Time
    Supports optional filtered task list parameter.
    
    Args:
        task_list (list, optional): List of tasks to display. If None, uses global tasks list.
    """
    # Use provided list or default to global tasks
    display_list = task_list if task_list is not None else tasks
    
    # Handle empty list
    if len(display_list) == 0:
        print(f"\n{Fore.YELLOW}No tasks found. Add one to get started!\n")
        return
    
    # Print table header
    print(f"\n{Fore.CYAN}─────────────────────────────────────────────────────────────────────")
    header = " No. | Task                      | Priority   | Status       | Date"
    print(f"{Fore.CYAN}{header}")
    print(f"{Fore.CYAN}─────────────────────────────────────────────────────────────────────")
    
    # Print each task as a formatted row
    for idx, task in enumerate(display_list, 1):
        task_name = task["task"].ljust(25)  # Left-align task name, pad to 25 chars
        priority = task["priority"].ljust(10)  # Left-align priority, pad to 10 chars
        
        # Apply color to priority based on level
        priority_colored = f"{get_priority_color(task['priority'])}{priority}{Style.RESET_ALL}"
        
        # Set status display based on completion
        if task["done"]:
            status = f"{Style.DIM}{Fore.WHITE}✅ Done{Style.RESET_ALL}".ljust(15)
        else:
            status = f"{Fore.CYAN}⏳ Pending{Style.RESET_ALL}".ljust(15)
        
        date_display = task["date"].ljust(15)  # Left-align date, pad to 15 chars
        
        # Print the formatted row
        print(f" {idx}. | {task_name} | {priority_colored} | {status} | {date_display}")
    
    # Print table footer
    print(f"{Fore.CYAN}─────────────────────────────────────────────────────────────────────\n")


# ═════════════════════════════════════════════════════════════
# TASK MANAGEMENT FUNCTIONS
# ═════════════════════════════════════════════════════════════

def add_task():
    """
    Add a new task to the list.
    Prompts user for task name and priority level.
    Auto-assigns id, timestamp, and completion status.
    """
    try:
        # Get task name from user and validate
        task_name = input(f"{Fore.CYAN}Enter task name: {Style.RESET_ALL}").strip()
        if not task_name:
            print(f"{Fore.RED}✗ Task name cannot be empty!")
            return
        
        # Display priority options and get user choice
        print(f"{Fore.CYAN}Priority levels:")
        print(f"  1. {Fore.RED}High{Style.RESET_ALL}")
        print(f"  2. {Fore.YELLOW}Medium{Style.RESET_ALL}")
        print(f"  3. {Fore.GREEN}Low{Style.RESET_ALL}")
        
        # Get and validate priority choice
        priority_choice = int(input(f"{Fore.CYAN}Select priority (1-3): {Style.RESET_ALL}"))
        
        # Map choice to priority string
        priority_map = {1: "High", 2: "Medium", 3: "Low"}
        if priority_choice not in priority_map:
            print(f"{Fore.RED}✗ Invalid priority! Please enter 1, 2, or 3.")
            return
        
        priority = priority_map[priority_choice]
        
        # Get current date and time for timestamp
        now = datetime.datetime.now()
        task_time = now.strftime("%I:%M %p")  # Format: 09:30 AM
        task_date = now.strftime("%d %b %Y")  # Format: 09 Jun 2026
        
        # Calculate next task ID (max existing + 1, or 1 if no tasks)
        next_id = max([t["id"] for t in tasks], default=0) + 1
        
        # Create task dictionary with all required fields
        new_task = {
            "id": next_id,
            "task": task_name,
            "priority": priority,
            "done": False,
            "time": task_time,
            "date": task_date
        }
        
        # Add task to global list
        tasks.append(new_task)
        
        # Persist to file
        save_tasks()
        
        # Confirm to user
        print(f"{Fore.GREEN}✓ Task added successfully!\n")
        
    except ValueError:
        # Handle non-integer input for priority
        print(f"{Fore.RED}✗ Invalid input! Please enter a valid number.\n")
    except Exception as e:
        # Catch any unexpected errors
        print(f"{Fore.RED}✗ Error adding task: {e}\n")


def complete_task():
    """
    Mark a task as completed.
    Shows list of pending tasks and prompts user to select one.
    """
    try:
        # Filter only pending (incomplete) tasks
        pending_tasks = [t for t in tasks if not t["done"]]
        
        # Handle case where all tasks are already completed
        if len(pending_tasks) == 0:
            print(f"\n{Fore.YELLOW}No pending tasks!\n")
            return
        
        # Display pending tasks
        print(f"\n{Fore.CYAN}Pending Tasks:")
        view_tasks(pending_tasks)
        
        # Get task number from user
        task_num = int(input(f"{Fore.CYAN}Enter task number to mark complete: {Style.RESET_ALL}"))
        
        # Validate task number is in range
        if task_num < 1 or task_num > len(pending_tasks):
            print(f"{Fore.RED}✗ Invalid task number!\n")
            return
        
        # Mark the selected task as done (convert 1-indexed to 0-indexed)
        selected_task = pending_tasks[task_num - 1]
        
        # Find and update the task in the global list
        for task in tasks:
            if task["id"] == selected_task["id"]:
                task["done"] = True
                break
        
        # Persist to file
        save_tasks()
        
        # Confirm to user
        print(f"{Fore.GREEN}✅ Task marked as completed!\n")
        
    except ValueError:
        # Handle non-integer input
        print(f"{Fore.RED}✗ Invalid input! Please enter a valid number.\n")
    except Exception as e:
        # Catch any unexpected errors
        print(f"{Fore.RED}✗ Error completing task: {e}\n")


def delete_task():
    """
    Delete a task from the list.
    Displays all tasks, asks user to select one, then asks for confirmation.
    """
    try:
        # Handle case where no tasks exist
        if len(tasks) == 0:
            print(f"\n{Fore.YELLOW}No tasks to delete!\n")
            return
        
        # Display all tasks
        print(f"\n{Fore.CYAN}All Tasks:")
        view_tasks()
        
        # Get task number from user
        task_num = int(input(f"{Fore.CYAN}Enter task number to delete: {Style.RESET_ALL}"))
        
        # Validate task number is in range
        if task_num < 1 or task_num > len(tasks):
            print(f"{Fore.RED}✗ Invalid task number!\n")
            return
        
        # Get the selected task for confirmation
        selected_task = tasks[task_num - 1]
        
        # Ask for confirmation before deleting
        confirm = input(f"{Fore.YELLOW}Delete '{selected_task['task']}'? (y/n): {Style.RESET_ALL}").lower()
        
        if confirm == 'y':
            # Remove task from list
            tasks.pop(task_num - 1)
            
            # Persist to file
            save_tasks()
            
            # Confirm to user
            print(f"{Fore.GREEN}🗑️  Task deleted.\n")
        else:
            print(f"{Fore.YELLOW}Deletion cancelled.\n")
        
    except ValueError:
        # Handle non-integer input
        print(f"{Fore.RED}✗ Invalid input! Please enter a valid number.\n")
    except Exception as e:
        # Catch any unexpected errors
        print(f"{Fore.RED}✗ Error deleting task: {e}\n")


def filter_tasks():
    """
    Display a submenu to filter tasks by status or priority.
    Options: All / Pending / Completed / By Priority
    """
    try:
        # Display filter submenu
        print(f"\n{Fore.CYAN}Filter Options:")
        print(f"  1. Show All Tasks")
        print(f"  2. Show Pending Tasks Only")
        print(f"  3. Show Completed Tasks Only")
        print(f"  4. Filter by Priority\n")
        
        # Get filter choice from user
        filter_choice = int(input(f"{Fore.CYAN}Select filter (1-4): {Style.RESET_ALL}"))
        
        if filter_choice == 1:
            # Show all tasks
            print()
            view_tasks(tasks)
            
        elif filter_choice == 2:
            # Show pending (not done) tasks
            pending = [t for t in tasks if not t["done"]]
            print()
            view_tasks(pending)
            
        elif filter_choice == 3:
            # Show completed (done) tasks
            completed = [t for t in tasks if t["done"]]
            print()
            view_tasks(completed)
            
        elif filter_choice == 4:
            # Filter by priority
            print(f"\n{Fore.CYAN}Priority levels:")
            print(f"  1. {Fore.RED}High{Style.RESET_ALL}")
            print(f"  2. {Fore.YELLOW}Medium{Style.RESET_ALL}")
            print(f"  3. {Fore.GREEN}Low{Style.RESET_ALL}\n")
            
            priority_choice = int(input(f"{Fore.CYAN}Select priority (1-3): {Style.RESET_ALL}"))
            
            # Map choice to priority string
            priority_map = {1: "High", 2: "Medium", 3: "Low"}
            if priority_choice not in priority_map:
                print(f"{Fore.RED}✗ Invalid priority!\n")
                return
            
            # Filter tasks by selected priority
            priority = priority_map[priority_choice]
            filtered = [t for t in tasks if t["priority"] == priority]
            
            print()
            view_tasks(filtered)
        else:
            # Invalid filter choice
            print(f"{Fore.RED}✗ Invalid filter option!\n")
            
    except ValueError:
        # Handle non-integer input
        print(f"{Fore.RED}✗ Invalid input! Please enter a valid number.\n")
    except Exception as e:
        # Catch any unexpected errors
        print(f"{Fore.RED}✗ Error filtering tasks: {e}\n")


def clear_completed():
    """
    Clear all completed tasks at once.
    Asks for confirmation and displays count before removing.
    """
    try:
        # Count completed tasks
        completed_count = len([t for t in tasks if t["done"]])
        
        # Handle case where no completed tasks exist
        if completed_count == 0:
            print(f"\n{Fore.YELLOW}No completed tasks to clear.\n")
            return
        
        # Ask for confirmation
        confirm = input(f"{Fore.YELLOW}Clear {completed_count} completed task(s)? (y/n): {Style.RESET_ALL}").lower()
        
        if confirm == 'y':
            # Remove all completed tasks using list comprehension
            tasks[:] = [t for t in tasks if not t["done"]]
            
            # Persist to file
            save_tasks()
            
            # Confirm to user
            print(f"{Fore.GREEN}🧹 Cleared {completed_count} completed task(s).\n")
        else:
            print(f"{Fore.YELLOW}Clear operation cancelled.\n")
            
    except Exception as e:
        # Catch any unexpected errors
        print(f"{Fore.RED}✗ Error clearing tasks: {e}\n")


def show_summary():
    """
    Display a summary of task statistics including:
    - Total tasks, completed, and pending counts
    - Breakdown by priority (High/Medium/Low)
    - Progress bar showing completion percentage
    """
    # Handle case where no tasks exist
    if len(tasks) == 0:
        print(f"\n{Fore.MAGENTA}{Style.BRIGHT}{'=' * 50}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}📊 TASK SUMMARY")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}{'=' * 50}")
        print(f"\n{Fore.YELLOW}No tasks yet! Add one to get started.\n")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}{'=' * 50}\n")
        return
    
    # Calculate statistics
    total = len(tasks)
    completed = len([t for t in tasks if t["done"]])
    pending = total - completed
    
    # Count tasks by priority
    high_count = len([t for t in tasks if t["priority"] == "High"])
    medium_count = len([t for t in tasks if t["priority"] == "Medium"])
    low_count = len([t for t in tasks if t["priority"] == "Low"])
    
    # Display summary header
    print(f"\n{Fore.MAGENTA}{Style.BRIGHT}{'=' * 50}")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}📊 TASK SUMMARY")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}{'=' * 50}\n")
    
    # Display task counts
    print(f"{Fore.CYAN}Total Tasks:       {total}")
    print(f"{Fore.GREEN}Completed:         {completed}")
    print(f"{Fore.YELLOW}Pending:           {pending}")
    
    # Display priority breakdown
    print(f"\n{Fore.RED}High Priority:     {high_count}")
    print(f"{Fore.YELLOW}Medium Priority:   {medium_count}")
    print(f"{Fore.GREEN}Low Priority:      {low_count}")
    
    # Display progress bar
    print(f"\n{Fore.CYAN}Progress: {progress_bar(completed, total)}\n")
    
    # Display summary footer
    print(f"{Fore.MAGENTA}{Style.BRIGHT}{'=' * 50}\n")


# ═════════════════════════════════════════════════════════════
# MAIN EVENT LOOP
# ═════════════════════════════════════════════════════════════

def main():
    """
    Main event loop for the To-Do List application.
    Loads tasks on startup, displays menu in continuous loop,
    routes user input to appropriate functions, and handles exit.
    """
    # Load tasks from file on startup
    load_tasks()
    
    # Add small delay after loading
    print()
    input("Press Enter to continue...")
    
    # Main loop - runs until user chooses to exit
    while True:
        # Display menu with current date/time
        show_menu()
        
        try:
            # Get user's menu choice
            choice = int(input(f"{Fore.CYAN}Enter your choice (1-9): {Style.RESET_ALL}"))
            
            # Route to appropriate function based on choice
            if choice == 1:
                add_task()
            elif choice == 2:
                print()
                view_tasks()
            elif choice == 3:
                complete_task()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                filter_tasks()
            elif choice == 6:
                clear_completed()
            elif choice == 7:
                show_summary()
            elif choice == 8:
                print()
                save_tasks()
                print()
            elif choice == 9:
                # Exit: save and close
                save_tasks()
                print(f"{Fore.GREEN}👋 Goodbye! Your tasks have been saved.")
                print(f"{Fore.GREEN}See you next time!\n")
                break
            else:
                # Invalid menu choice
                print(f"{Fore.RED}✗ Invalid choice! Please enter a number between 1 and 9.\n")
            
            # Add pause before next menu loop
            input(f"{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")
            
        except ValueError:
            # Handle non-integer input for menu choice
            print(f"{Fore.RED}✗ Invalid input! Please enter a valid number.\n")
            input(f"{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print(f"\n{Fore.YELLOW}Application interrupted.")
            save_tasks()
            print(f"{Fore.GREEN}Tasks saved. Goodbye!\n")
            break
        except Exception as e:
            # Catch any unexpected errors
            print(f"{Fore.RED}✗ Unexpected error: {e}\n")
            input(f"{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")


# ═════════════════════════════════════════════════════════════
# ENTRY POINT
# ═════════════════════════════════════════════════════════════

if __name__ == "__main__":
    main()
