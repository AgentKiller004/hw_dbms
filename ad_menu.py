import csv

def add_user(file_name):
    """Adds a new student or teacher to the respective CSV file."""
    print(f"\n📥 Adding new user to {file_name}")

    try:
        user_id = int(input("Enter ID (admission/employment no.): ").strip())
    except ValueError:
        print("❌ Invalid ID. Please enter a number.")
        return

    password = input("Enter password: ").strip()
    name = input("Enter full name: ").strip().title()

    if file_name == 'student.csv':
        class_info = input("Enter class (format: Class-Sec like 11-A): ").strip().upper()
        new_row = [user_id, password, name, class_info, '[]']  # empty list for completions

    elif file_name == 'teacher.csv':
        classes = input("Enter classes you teach (comma-separated, e.g., 9-A,10-B): ").strip()
        subject = input("Enter subject: ").strip().title()
        new_row = [user_id, password, classes, subject]

    # FIX: Read all data, append the new row, and write it all back to prevent formatting errors.
    try:
        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
    except FileNotFoundError:
        # If the file doesn't exist, create it with a header
        if file_name == 'student.csv':
            rows = [['student_id', 'student_pass', 'stu_name', 'class', 'list_comp']]
        elif file_name == 'teacher.csv':
            rows = [['teach_id', 'teach_pass', 'teach_class', 'subject']]
        else:
            rows = [] # Should not happen with current logic

    rows.append(new_row)

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print(f"✅ User '{name}' with ID {user_id} added successfully.")

def change_pass(file_name):
    """Changes the password for a user in the specified file."""
    try:
        user_id = int(input("Enter your ID: ").strip())
    except ValueError:
        print("❌ Invalid ID. Please enter a number.")
        return

    current_pass = input("Enter current password: ").strip()

    try:
        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
    except FileNotFoundError:
        print(f"❌ {file_name} not found.")
        return

    header = data[0]
    rows = data[1:]

    found = False
    for i, row in enumerate(rows):
        if row and row[0] == str(user_id) and row[1] == current_pass:
            new_pass = input("Enter new password: ").strip()
            rows[i][1] = new_pass
            found = True
            break

    if found:
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)
        print("✅ Password changed successfully.")
    else:
        print("❌ Incorrect ID or password.")

def ad_menu():
    """Displays the admin menu and handles admin actions."""
    while True:
        print("\n===== 🛠️ ADMIN MENU =====")
        print("1. ➕ Add Student")
        print("2. ➕ Add Teacher")
        print("3. 🔐 Change Student Password")
        print("4. 🔐 Change Teacher Password")
        print("5. 🚪 Exit")

        choice = input("Enter your choice (1–5): ").strip()

        if choice == '1':
            add_user('student.csv')
        elif choice == '2':
            add_user('teacher.csv')
        elif choice == '3':
            change_pass('student.csv')
        elif choice == '4':
            change_pass('teacher.csv')
        elif choice == '5':
            print("👋 Exiting admin menu.")
            break
        else:
            print("❌ Invalid choice. Try again.")
        
        input('\nPress Enter to continue...')