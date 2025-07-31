import csv
from datetime import datetime

def edit_homework_due_date(teacher_data):
    teach_id,teach_classes,teac_sub=teacher_data  # assuming this is a comma-separated list in CSV

    # Load all homework
    with open('homework.csv', newline='') as file:
        reader = csv.reader(file)
        homeworks = list(reader)

    
    data = homeworks[1:]

    # Filter homeworks assigned by this teacher
    my_homeworks = [[i] + hw for i, hw in enumerate(data,start=1) if any(hw) and hw[3] == teach_id]

    if not my_homeworks:
        print("You haven't assigned any homework yet.")
        return

    print("\n Your Assigned Homework:")
    for i,row in enumerate(my_homeworks):
        print(f"SR No: {i+1} | Topic: {row[1]} | Subject: {row[2]} | Class: {row[3]} | Due: {row[5]}")

    # Loop until valid sr no
    while True:
        try:
            srno = int(input("\nEnter SR No of homework to edit: "))
            valid_srnos = [i+1 for i in range(len(my_homeworks))]
            if srno in valid_srnos:
                break
            else:
                print("SR No doesn't match your homework. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
    # Ask for due date until it's valid
        while True:
            new_due = input("Enter due date (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(new_due, "%Y-%m-%d")
                break
            except:
                print("Invalid format. Please enter in YYYY-MM-DD format.")
    
        with open('homework.csv', newline='') as file:
            reader = csv.reader(file)
            homeworks = list(reader)
    
        # Check for date clash
        clash = [hw for hw in homeworks if any(hw) and  hw[2] == my_homeworks[srno-1][3] and hw[4] == new_due]
        if len(clash) != 0:
            print("A homework already exists for this class on that date.")
        else: break
    # Update and write back
    row_no=my_homeworks[srno-1][0]
    homeworks[row_no][4] = new_due  
    with open('homework.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(homeworks)

    print("Homework due date updated successfully.")
