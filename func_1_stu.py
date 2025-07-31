#func_1_stu 
import csv
from datetime import datetime
def view_all_hw(stu_dat):
    st_id,st_name,st_cl,st_comp=stu_dat
    while True:
        print('1. View all HW ')
        print('2. View completed HW ')
        print('3. View all incomplete HW')
        print('4. Exit')
        
        ch=input('Enter your choice(1-4):')
        if ch not in ['1','2','3','4']:
            print("Invalid input")
        elif ch=='4':
            break
        elif ch=='1':
            with open('homework.csv','r',newline='') as f:
                reader = csv.reader(f)
                hws= list(reader)
            
            lis=[[i]+hw for i,hw in enumerate(hws) if any(hw) and st_cl==hw[2]]
            for j,i in enumerate(lis):
                if i[5] <= datetime.now() and i[0] not in st_comp  :
                    pend='OverDue '
                elif i[5] <= datetime.now() and i[0] not in st_comp : 
                    pend='Completed'
                else: pend='Time remaining'
                
                print(f"""
Sr no. : {j} | Topic : {i[1]} | Subject : {i[2]} | Teacher : {i[4]} | Due date : {i[5]} | {pend} |
""")
        elif ch=="2":
            
            with open('homework.csv','r',newline='') as f:
                reader = csv.reader(f)
                hws= list(reader)
            
            lis=[[i]+hw for i,hw in enumerate(hws) if any(hw) and st_cl==hw[2] and i in st_comp]
            
            for j,i in enumerate(lis):
                print(f"""
Sr no. : {j} | Topic : {i[1]} | Subject : {i[2]} | Teacher : {i[4]} | Due date : {i[5]} |""")

            
        elif ch=='3':
            with open('homework.csv','r',newline='') as f:
                reader = csv.reader(f)
                hws= list(reader)
            
            lis=[[i]+hw for i,hw in enumerate(hws) if any(hw) and st_cl==hw[2] and i not in st_comp]
            for j,i in enumerate(lis):
                if i[5] <= datetime.now() and i[0] not in st_comp  :
                    pend='OverDue '
                else: pend='Time remaining'
                
                print(f"""
Sr no. : {j} | Topic : {i[1]} | Subject : {i[2]} | Teacher : {i[4]} | Due date : {i[5]} | {pend} |
""")
            