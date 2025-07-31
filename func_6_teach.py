import csv 


def view_stu_w_comp_hw(teacher_data):
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
            srno = int(input("\nEnter SR No of homework to edit: "))
            valid_srnos = [row[0] for row in my_homeworks]
            if srno in valid_srnos:
                break
            else:
                print("SR No doesn't match your homework. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    target_class=my_homeworks[srno][3]    
    with open('student.csv','r',newline='') as f:
        reader = csv.reader(f)
        students = list(reader)
    
    
    data=students[1:]
    comp_stu=[row for row in data if row[4]== target_class and srno in row[-1]]
    print(f'Students who have completed {data[srno-1]}:')
    for i,row in enumerate(comp_stu):
            print(f'Sr. no.: {i} | Student Name: {row[2]} | Student Class: {row[3]} |')
    
    
    
    
    
                
    