import csv
import ast # Import the Abstract Syntax Tree module for safe parsing

def view_stu_w_comp_hw(teacher_data):
    """
    Shows a list of students who have completed a specific homework
    assigned by the logged-in teacher.
    """
    teach_id, teach_classes, teac_sub = teacher_data

    # --- Load homework and student data ---
    try:
        with open('homework.csv', 'r', newline='') as file:
            homeworks = list(csv.reader(file))
        with open('student.csv', 'r', newline='') as file:
            students = list(csv.reader(file))
    except FileNotFoundError as e:
        print(f"❌ Error: {e.filename} not found.")
        return

    # Store original index with homework data for the logged-in teacher
    my_homeworks = [
        [i, hw] for i, hw in enumerate(homeworks)
        if i > 0 and any(hw) and hw[3] == teach_id
    ]

    if not my_homeworks:
        print("\nℹ️ You haven't assigned any homework to view completions for.")
        return

    # --- Get homework selection from teacher ---
    print("\n--- View Student Completions ---")
    for display_srno, (original_index, hw) in enumerate(my_homeworks, 1):
        print(f"Sr No: {display_srno} | Topic: {hw[0]} | Class: {hw[2]} | Due: {hw[4]}")

    while True:
        try:
            choice = int(input("\nEnter the Sr No of the homework to see completions: "))
            if 1 <= choice <= len(my_homeworks):
                break
            else:
                print(f"❌ Invalid choice. Please enter a number between 1 and {len(my_homeworks)}.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
    
    # --- FIX: Correctly identify the target homework details and original index ---
    selected_hw_index, selected_hw_details = my_homeworks[choice - 1]
    target_class = selected_hw_details[2]

    # --- Find students who have completed this homework ---
    completed_students = []
    # Skip header row of students file
    for stu in students[1:]:
        if not any(stu): continue

        # Ensure student is in the correct class
        if stu[3] == target_class:
            try:
                # --- FIX: Safely parse the string representation of the list ---
                completed_list = ast.literal_eval(stu[4])
                if not isinstance(completed_list, list):
                    completed_list = []
            except (ValueError, SyntaxError):
                completed_list = [] # Treat malformed data as an empty list

            if selected_hw_index in completed_list:
                completed_students.append(stu)

    # --- FIX: Display the correct information ---
    print(f"\n--- Students who completed '{selected_hw_details[0]}' in class {target_class} ---")
    if not completed_students:
        print("No students have marked this homework as complete yet.")
    else:
        for i, row in enumerate(completed_students, 1):
            print(f'Sr. no.: {i} | Student Name: {row[2]} | Student ID: {row[0]}')