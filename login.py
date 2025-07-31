
import csv
def login(file_name):
    id_= input("Enter your ID : ")
    pass_=input("Enter your password : ")
    with open(file_name,'r',newline='') as f:
        reader=csv.reader(f)
        ids=list(reader)
    lis=[row for row in ids if row[0]==id_ and row[1]==pass_]
    if len(lis)==1:
        print(lis[0])
        return lis[0]
    else:
        print('Invalid ID or password ')
