#func_1_stu 
import csv
from datetime import datetime

def view_all_hw(stu_dat):
    st_id, st_name, st_cl, st_comp_str = stu_dat
    # Convert completion list from string to list of integers
    st_comp = eval(st_comp_str) if isinstance(st_comp_str, str) else st_comp_str

    while True:
        print('\n1. View all HW ')
        print('2. View completed HW ')
        print('3. View all incomplete HW')
        print('4. Exit')
        
        ch = input('Enter your choice(1-4):')
        if ch not in ['1', '2', '3', '4']:
            print("Invalid input")
            continue
        elif ch == '4':
            break
        
        with open('homework.csv', 'r', newline='') as f:
            reader = csv.reader(f)
            hws = list(reader)
        
        # Skip header row for processing
        all_class_hws = [[i] + hw for i, hw in enumerate(hws) if any(hw) and hw[2] == st_cl]

        if ch == '1':
            print("\n--- All Homework ---")
            if not all_class_hws:
                print("No homework assigned for your class.")
                continue
            
            for j, i in enumerate(all_class_hws, 1):
                try:
                    # --- FIX: Convert string to datetime object for comparison ---
                    due_date = datetime.strptime(i[5], "%Y-%m-%d")
                    
                    if i[0] in st_comp:
                        pend = 'Completed'
                    elif due_date < datetime.now():
                        pend = 'Overdue'
                    else:
                        pend = 'Pending'
                    
                    print(f"Sr no. : {j} | Topic : {i[1]} | Subject : {i[2]} | Teacher : {i[4]} | Due date : {i[5]} | Status: {pend}")
                except (ValueError, IndexError):
                    # Skip malformed rows
                    continue
        
        elif ch == "2":
            print("\n--- Completed Homework ---")
            completed_hws = [hw for hw in all_class_hws if hw[0] in st_comp]
            if not completed_hws:
                print("You have not completed any homework yet.")
                continue

            for j, i in enumerate(completed_hws, 1):
                print(f"Sr no. : {j} | Topic : {i[1]} | Subject : {i[2]} | Teacher : {i[4]} | Due date : {i[5]}")

        elif ch == '3':
            print("\n--- Incomplete Homework ---")
            incomplete_hws = [hw for hw in all_class_hws if hw[0] not in st_comp]
            if not incomplete_hws:
                print("No incomplete homework. Great job!")
                continue

            for j, i in enumerate(incomplete_hws, 1):
                try:
                    # --- FIX: Convert string to datetime object for comparison ---
                    due_date = datetime.strptime(i[5], "%Y-%m-%d")
                    pend = 'Overdue' if due_date < datetime.now() else 'Pending'
                    
                    print(f"Sr no. : {j} | Topic : {i[1]} | Subject : {i[2]} | Teacher : {i[4]} | Due date : {i[5]} | Status: {pend}")
                except (ValueError, IndexError):
                    continue