import csv

def add_user(file_name):
    print(f"\n📥 Adding new user ")

    user_id = int(input("Enter ID (admission/employment no.): ").strip())
    password = input("Enter password: ").strip()
    name = input("Enter full name: ").strip().title()

    if file_name == 'student.csv':
        class_info = input("Enter class (format: Class-Sec like 11-A): ").strip().upper()
        row = [user_id, password, name, class_info, '[]']  # empty list for completions

    elif file_name == 'teacher.csv':
        classes = input("Enter classes you teach (comma-separated, e.g., 9-A,10-B): ").strip()
        subject = input("Enter subject: ").strip().title()
        row = [user_id, password, classes, subject]

    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)

    print("✅ User added successfully.")

def change_pass(file_name):
    user_id = int(input("Enter your ID: ")).strip()
    current_pass = input("Enter current password: ").strip()

    with open(file_name, newline='') as file:
        reader = csv.reader(file)
        data = list(reader)

    header = data[0]
    rows = data[1:]

    found = False
    for i, row in enumerate(rows):
        if row and row[0] == user_id and row[1] == current_pass:
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
