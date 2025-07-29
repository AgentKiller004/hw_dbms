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
            all_homework = list(reader)

        completed_hw_ids = set()
        with open('completion_status.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[1] == st_id:
                    completed_hw_ids.add(row[0])
                    
    except FileNotFoundError as e:
        print(f"Error: The file {e.filename} was not found.")
        return

    # Find homework for the student's class that is NOT yet done
    pending_hw = [
        hw for hw in all_homework
        if any(hw) and hw[2] == st_class and hw[0] not in completed_hw_ids
    ]

    if not pending_hw:
        print("\n🎉 You have no pending homework to mark as done!")
        return

    # Display the pending homework with numbers for selection
    print("\n📝 Select a homework to mark as complete:\n")
    for i, hw in enumerate(pending_hw):
        # hw[0]=ID, hw[1]=Topic, hw[2]=Subject, hw[5]=Due
        print(f"  {i + 1}. Subject: {hw[2]} | Topic: {hw[1]} (Due: {hw[5]})")

    # Get the user's choice
    while True:
        try:
            choice = int(input("\nEnter the number of the homework you completed: "))
            if 1 <= choice <= len(pending_hw):
                # Get the HomeworkID of the selected assignment
                hw_to_mark_id = pending_hw[choice - 1][0]
                
                # Append the new completion record to the status file
                with open('completion_status.csv', mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([hw_to_mark_id, st_id])

                print("\n✅ Homework marked as complete. Well done!")
                break
            else:
                print("Invalid number. Please choose a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")