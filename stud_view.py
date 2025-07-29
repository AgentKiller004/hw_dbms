# stud_view.py

import csv

def view_hw(st_data):
    """
    Displays homework for the student's class that they have not yet completed.
    """
    st_id, st_class = st_data

    try:
        with open('homework.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)
            all_homework = list(reader)

        with open('completion_status.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            completed_hw_ids = {row[0].strip() for row in reader if row and row[1].strip() == st_id}

    except FileNotFoundError as e:
        print(f"Error: The file {e.filename} was not found. Please create it.")
        return

    # Filter using the CORRECT column index for class (3)
    my_pending_hw = [
        hw for hw in all_homework
        if any(hw) and hw[3].strip() == st_class and hw[0].strip() not in completed_hw_ids
    ]

    if not my_pending_hw:
        print(f"\n🎉 No pending homework for Class {st_class}. You're all caught up!")
        return

    print(f"\n📚 Pending Homework for Class {st_class}:\n")
    print("-" * 60)
    # CSV structure: [0:ID, 1:Topic, 2:Subject, 3:Class, 4:Teacher, 5:Due]
    for hw in my_pending_hw:
        print(f"  📖 Subject: {hw[2]}")
        print(f"     Topic:   {hw[1]}")
        print(f"     Due:     {hw[5]}")
        print(f"     By:      Teacher {hw[4]}")
        print("-" * 60)
