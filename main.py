# main.py - The main script to run your application

# --- Import your functions ---
# From the login system
from login_system import main_login 

# From the teacher's menu (you already have this file)
from teach_menu import teacher_menu 

# From the new student menu (we will create this below)
from student_menu import student_menu

def main():
    """The main application loop."""
    while True:
        # First, call the login function. It returns the role and user data.
        role, user_data = main_login()

        # If the user chose to exit
        if role == 'exit':
            print("Exiting the application.")
            break
        
        # If the login was successful, user_data will not be None
        if user_data:
            if role == 'student':
                # Pass the student's data to the student menu
                student_menu(user_data)
            elif role == 'teacher':
                # Pass the teacher's data to the teacher menu
                teacher_menu(user_data)
            elif role == 'admin':
                print("\nAdmin menu is not yet implemented. Logging out.")
        
        # If login fails, the loop continues and shows the login screen again

if __name__ == "__main__":
    main()
