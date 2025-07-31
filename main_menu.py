from student_menu import *
from teach_menu import *
from login import *
from ad_menu import *
import csv
import os

def boot_files():
    files = {
        'student.csv': ['student_id', 'student_pass', 'stu_name', 'class', 'list_comp'],
        'teacher.csv': ['teach_id', 'teach_pass', 'teach_class', 'subject'],
        'homework.csv': ['homework_topic', 'subject', 'class', 'teacher', 'due_date', 'no_of_comp']
    }

    for filename, header in files.items():
        if not os.path.exists(filename):
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header)

def main_menu():
    #boot_files()
    while True:
        print("1. Admin login")
        print("2. Teacher login")
        print("3. Student login")
        print("4. Exit ")
        
        choice = input('Enter you choice (1-4):').strip()
        if choice == '1':
            ad_id = input('Enter Admin ID')
            ad_pass = input('Enter Admin Pass')
            if ad_id == '1413@@abc' and ad_pass == '1413@@abc':
                print("logged in succesfully as an Admin")
                ad_menu()
            else: 
                print('Invalid ID or Password')
        
        elif choice == '2':
            teach_dat = login('teacher.csv')
            if teach_dat:
                print('You are succesfully logged in as a teacher ')
                teach_dat = [teach_dat[0], teach_dat[2].split(","), teach_dat[3]]
                teach_menu(teach_dat)
        
        elif choice == '3':
            # --- FIX 1: Corrected filename from 'stu.csv' to 'student.csv' ---
            stu_data_full = login('student.csv')
            if any(stu_data_full):
                print('You are succesfully logged in as a student')
                
                # The rest of your student logic...
                stu_data_imp = (stu_data_full[0], stu_data_full[2], stu_data_full[3], stu_data_full[4])
                flag, stu_data_imp_updated = stu_menu(stu_data_imp)
                
                # --- FIX 2: Correctly update the student's record without deleting other students ---
                if flag != 0:
                    # Update the original full data with the changes from the menu
                    stu_data_full[-1] = stu_data_imp_updated[-1]

                    students = []
                    with open('student.csv', 'r', newline='') as f:
                        reader = csv.reader(f)
                        students = list(reader)

                    # Find the student and update their specific row
                    for i, stu in enumerate(students):
                        if stu and stu[0] == stu_data_full[0]:
                            students[i] = stu_data_full
                            break
                    
                    # Write all records (old and updated) back to the file
                    with open('student.csv', 'w', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerows(students)

        elif choice == '4':
            print("Exiting to main menu...")
            break
        else:
            print("Invalid choice. Try again.")
        
        input("Please press enter to continue")

if __name__ == '__main__':
    main_menu()