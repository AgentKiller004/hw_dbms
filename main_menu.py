from student_menu import *
from teach_menu import *
from login import *
from ad_menu import *
import csv



import os
import csv

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
        
        choice=input('Enter you choice (1-4):').strip()
        if choice == '1':
            ad_id=input('Enter Admin ID')
            ad_pass=input('Enter Admin Pass')
            if ad_id=='1413@@abc' and ad_pass=='1413@@abc':
                print("logged in succesfully as an Admin")
                ad_menu()
            else : 
                print('Invalid ID or Password')
        
        
        elif choice == '2':
            teach_dat=login('teacher.csv')
            if teach_dat:
                print('You are succesfully logged in as a teacher ')
                teach_dat=[teach_dat[0],teach_dat[2].split(","),teach_dat[3]]
            
                teach_menu(teach_dat)
        
        
        elif choice == '3':
            stu_data_full = login('stu.csv')
            if any(stu_data_full):
                print('You are succesfully logged in as a student')
            
            stu_data_imp = (stu_data_full[0],stu_data_full[2:])
            flag , stu_data_imp = student_menu(stu_data_imp)
            stu_data_full[-1]=stu_data_imp[-1]
            if flag!= 0 :
                with open('student.csv','w+',newline='') as f :
                    reader=csv.reader(f)
                    students=list(reader)
                    lis = [[i]+stu for i,stu in enumerate(students) if stu[0]==stu_data_full[0] and stu[1]==stu_data_full[1]]
                    students[lis[0][0]]==[stu_data_full]
                    f.seek(0)
                    writer=csv.writer(f)
                    writer.writerows(students)
        elif choice == '4':
            print("Exiting to main menu...")
            break
        else:
            print("Invalid choice. Try again.")
        
        input("Please press enter to continue")
if __name__ == '__main__':
    main_menu()