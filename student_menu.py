# student_menu.py

# --- Import the student functions you created ---
# Make sure your files are named correctly (e.g., stud_view.py, stud_mark_done.py)
from stud_view import view_hw
from stud_mark_done import mark_homework_done

def student_menu(st_data):
    """
    Displays the menu for the student and handles their choices.
    The 'st_data' variable is passed directly from the login system.
    """
    while True:
        print("\n--- Student Menu ---")
        print(f"Logged in as: {st_data[0]} | Class: {st_data[1]}")
        print("1. View My Pending Homework")
        print("2. Mark a Homework as Done")
        print("3. Logout")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            # We pass the st_data tuple directly to the function
            view_hw(st_data)
        elif choice == '2':
            # We pass the st_data tuple directly to the function
            mark_homework_done(st_data)
        elif choice == '3':
            print("\nLogging out...")
            return # This exits the student_menu and goes back to the main login screen
        else:
            print("Invalid choice. Please try again.")

