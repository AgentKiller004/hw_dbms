import csv 
from datetime import datetime




def assign_homework(teach_data):
    teach_id,teach_classes,teach_sub=teach_data
    #print(type(teach_classes))
    
    print("\nSelect a class to assign homework to:")
    for i, cls in enumerate(teach_classes):
        print(f"{i+1}. {cls}")
    # Ask for class until it's valid
    while True:
        cl_choice = int(input("Enter serial number of class: "))
        
        try:
            target_class = teach_classes[cl_choice - 1]
            break
        except:
            print("Invalid choice. Try Again.")
        
    while True:
    # Ask for due date until it's valid
        while True:
            due_date = input("Enter due date (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
                break
            except:
                print("Invalid format. Please enter in YYYY-MM-DD format.")
    
        with open('homework.csv', newline='') as file:
            reader = csv.reader(file)
            homeworks = list(reader)
    
        # Check for date clash
        clash = [hw for hw in homeworks if any(hw) and hw[2] == target_class and hw[4] == due_date]
        if len(clash) != 0:
            print("A homework already exists for this class on that date.")
        else: break
            

    topic = input("Enter homework topic: ").strip().title()
    new_hw = [topic, teach_sub, target_class, teach_id, due_date, 0]
    homeworks.append(new_hw)

    with open('homework.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(homeworks)

    print("Homework assigned successfully.")
