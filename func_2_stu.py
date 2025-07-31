import csv
from datetime import datetime

def mark_done(stu_dat):
    st_id, st_name, st_cl, st_comp_str = stu_dat
    # Convert completion list from string to list of integers
    st_comp = eval(st_comp_str) if isinstance(st_comp_str, str) else st_comp_str

    with open('homework.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        hws = list(reader)
    
    # Filter for pending homework for the student's class
    lis = [[i] + hw for i, hw in enumerate(hws) if any(hw) and hw[2] == st_cl and i not in st_comp]
    
    if not lis:
        print('No pending homework. Yay!')
        return 0, stu_dat 
    
    print("\n--- Mark Homework as Done ---")
    for j, i in enumerate(lis, 1):
        try:
            # --- FIX: Convert string to datetime object for comparison ---
            due_date = datetime.strptime(i[5], "%Y-%m-%d")
            pend = 'Overdue' if due_date < datetime.now() else 'Pending'
                    
            print(f"Sr no. : {j} | Topic : {i[1]} | Subject : {i[2]} | Teacher : {i[4]} | Due date : {i[5]} | Status: {pend}")
        except (ValueError, IndexError):
            continue

    while True:
        try:
            ch = int(input('\nEnter which homework to mark as complete (Sr no.): '))
            if 0 < ch <= len(lis):
                break
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(lis)}.")
        except ValueError:
            print('Invalid input. Please enter a number.')

    srno_to_complete = lis[ch - 1][0]
    st_comp.append(srno_to_complete)
    print("✅ Homework marked as complete.")
    
    # Return the updated student data
    updated_stu_dat = (st_id, st_name, st_cl, str(st_comp))
    return 1, updated_stu_dat