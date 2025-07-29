# stud_mark_done.py

import csv

def mark_homework_done(st_data):
    """
    Allows a student to select a pending assignment and mark it as complete.
    """
    st_id, st_class = st_data

    try:
        with open('homework.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader) # Skip header
            all_homework = list(reader)

        with open('completion_status.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader) # Skip header
            completed_hw_ids = {row[0].strip() for row in reader if row and row[1].strip() == st_id}
                    
    except FileNotFoundError as e:
        print(f"Error: The file {e.filename} was not found.")
        return

    # Filter using the CORRECT column index for class (3)
    pending_hw = [
        hw for hw in all_homework
        if any(hw) and hw[3].strip() == st_class and hw[0].strip() not in completed_hw_ids
    ]

    if not pending_hw:
        print("\n🎉 You have no pending homework to mark as done!")
        return

    print("\n📝 Select a homework to mark as complete:\n")
    # CSV structure: [0:ID, 1:Topic, 2:Subject, 3:Class, 4:Teacher, 5:Due]
    for i, hw in enumerate(pending_hw):
        print(f"  {i + 1}. Subject: {hw[2]} | Topic: {hw[1]} (Due: {hw[5]})")

    while True:
        try:
            choice = int(input("\nEnter the number of the homework you completed: "))
            if 1 <= choice <= len(pending_hw):
                hw_to_mark_id = pending_hw[choice - 1][0]
                
                with open('completion_status.csv', mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([hw_to_mark_id, st_id])

                print("\n✅ Homework marked as complete. Well done!")
                break
            else:
                print("Invalid number. Please choose a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")
