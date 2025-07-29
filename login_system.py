# login_system.py

import csv

def student_login():
    """Handles the login process for a student without verification."""
    st_id = input("Enter your Student ID: ").strip()
    st_name = input("Enter your full name: ").strip().title()
    st_class = input("Enter your class (e.g., 10A): ").strip().upper()

    # No verification needed, just welcome the user and return the data.
    print(f"\nWelcome, {st_name}!")
    # Return the role and the student's data (ID, Class)
    return 'student', (st_id, st_class)

def teacher_login():
    """Handles the login process for a teacher without verification."""
    teach_id = input("Enter your Teacher ID: ").strip()
    teach_name = input("Enter your full name: ").strip().title()
    classes_str = input("Enter the classes you teach (separated by semicolon, e.g., 10A;11B): ").strip()
    subject = input("Enter the subject you teach: ").strip().title()

    # Parse the classes string into a list
    classes = [c.strip().upper() for c in classes_str.split(';')]
    
    print(f"\nWelcome, {teach_name}!")
    # Return the role and teacher's data (ID, Classes list, Subject)
    return 'teacher', (teach_id, classes, subject)

def admin_login():
    """Handles the login process for an admin without verification."""
    admin_id = input("Enter your Admin ID: ").strip()

    # No verification needed.
    print(f"\nWelcome, Admin {admin_id}!")
    # Return the role and the admin's data (ID)
    return 'admin', (admin_id,)

def main_login():
    """The main entry point for the application login."""
    while True:
        print("\n--- Homework Management System ---")
        print("1. Login as a Student")
        print("2. Login as a Teacher")
        print("3. Login as an Admin")
        print("4. Exit")
        
        choice = input("Select your role (1-4): ").strip()

        if choice == '1':
            return student_login()
        elif choice == '2':
            return teacher_login()
        elif choice == '3':
            return admin_login()
        elif choice == '4':
            print("👋 Goodbye!")
            return 'exit', None
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

