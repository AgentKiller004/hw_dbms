
import csv
import datetime

def mark_done(stu_dat):
    st_id,st_name,st_cl,st_comp=stu_dat
    with open('homework.csv','r',newline='') as f:
        reader = csv.reader(f)
        hws= list(reader)
            
    lis=[[i]+hw for i,hw in enumerate(hws) if any(hw) and st_cl==hw[2] and i not in st_comp]
    if len(lis)==0 :
        print('No pending hw. Yay!')
        return 0,stu_dat 
    for j,i in enumerate(lis):
        if i[5] <= datetime.now() and i[0] not in st_comp  :
            pend='OverDue '
        else: pend='Time remaining'
                
        print(f"""
Sr no. : {j} | Topic : {i[1]} | Subject : {i[2]} | Teacher : {i[4]} | Due date : {i[5]} | {pend} |
""")
    while True:
        try:
            ch= int(input('Enter which hw to make complete  '))
            if 0<ch<=len(lis):
                break
            else:
                print("Entered value is greater than no. of hws pending")
        except ValueError:
            print('Invalid input. Entered value is not a nunmber')
    srno = lis[ch-1][0]
    st_comp.append(srno)
    return 1,(st_id,st_name,st_cl,st_comp)


