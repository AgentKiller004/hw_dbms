import csv

def delete_homework(teacher_data):
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
    for row in my_homeworks:
        print(f"SR No: {row[0]} | Topic: {row[1]} | Subject: {row[2]} | Class: {row[3]} | Due: {row[4]}")

    # Loop until valid sr no
    while True:
        try:
            srno = int(input("\nEnter SR No of homework to delete: "))
            valid_srnos = [row[0] for row in my_homeworks]
            if srno in valid_srnos:
                break
            else:
                print("SR No doesn't match your homework. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    homeworks[srno]=["" for _ in homeworks]
    with open('homework.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(homeworks)

    print("Homework deleted successfully.")

    