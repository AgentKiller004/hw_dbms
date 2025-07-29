# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 10:10:20 2025

@author: Ishanvi krishna
"""

import csv

def search_homework(teach_data):
    teach_id,teach_classes,teac_sub=teach_data
    while True:
        print("\nSEARCH HOMEWORK DATABASE")
        print("1. Search by Class")
        print("2. Search by Subject")
        print("3. Search by Class & Subject")
        print("4. Return to Teacher Menu")

        choice = input("Enter choice (1-4): ").strip()

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Try again.")
            continue

        if choice == '4':
            return  # Go back to teacher menu

        with open('homework.csv', newline='') as file:
            reader = csv.reader(file)
            homeworks = list(reader)

        data = homeworks[1:]
        if choice == '1':
            target_class=input('Class you want to search for')
            results=[hw for hw in data if any(hw) and hw[2]==target_class ]

        elif choice == '2':
            subject_filter = input("Enter subject to search for: ").strip().title()
            results = [ hw for hw in data if any(hw) and hw[1] == subject_filter]
        elif choice == '3':
            target_class = input("Enter class to search for: ").strip()
            subject_filter = input("Enter subject to search for: ").strip().title()
            results = [hw for hw in data if any(hw) and hw[2] == target_class and (hw[1] == subject_filter)]

        if not results:
            print(" No homework found matching your criteria.")
        else:
            print("\n Matching Homework:")
            for hw in results:
                print(f"Topic: {hw[0]} | Subject: {hw[1]} | Class: {hw[2]} | Teacher: {hw[3]} | Due: {hw[4]} | Done: {hw[5]}")
