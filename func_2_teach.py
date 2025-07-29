import csv
def view_homeworks(teach_data):
    while True:       
        teach_id,teach_classes,teac_sub=teach_data
        print("\nView Homework Options:")
        print("1. All homework for one of my classes (by any teacher)")
        print("2. All homework I’ve ever assigned")
        print("3. Homework I assigned to a specific class")
        print("4. Exit ")
        choice = input("Enter option (1/2/3): ").strip()
    
        # Load homework.csv
        with open('homework.csv', newline='') as file:
            reader = csv.reader(file)
            homeworks = list(reader)
    
        results = []
        if choice == '4':
            return
        elif choice == '1':
            # View by class (any teacher)
            print("\nSelect from your classes:")
            for i, cls in enumerate(teach_classes):
                print(f"{i+1}. {cls}")
            while True:
                print("\nYour Classes:")
                for i, cls in enumerate(teach_classes):
                    print(f"{i+1}. {cls}")
    
                try:
                    cls_choice = int(input("Enter class number: "))
                    target_class = teach_classes[cls_choice - 1]
                    break
                    
                except (ValueError, IndexError):
                    print("Invalid input. Enter a number from the list.")
    
    
            results = [hw for hw in homeworks if any(hw) and hw[2] == target_class]
    
        elif choice == '2':
            # View all assigned by me
            results = [hw for hw in homeworks if any(hw) and hw[3] == teach_id]
    
        elif choice == '3':
            # View assigned by me to a class
            print("\nSelect from your classes:")
            for i, cls in enumerate(teach_classes):
                print(f"{i+1}. {cls}")
            while True:
                print("\nYour Classes:")
                for i, cls in enumerate(teach_classes, start=1):
                    print(f"{i}. {cls}")
    
                try:
                    cls_choice = int(input("Enter class number: "))
                    target_class = teach_classes[cls_choice - 1]
                    break
                except (ValueError, IndexError):
                    print("Invalid input. Enter a number from the list .")
    
            results = [hw for hw in homeworks if any(hw) and hw[2] == target_class and hw[3] == teach_id]
    
        else:
            print("Invalid option.")
            return
    
        # Show results
        if not results:
            print("No homework found.")
            return
    
        print("\nHomework List:")
        for srno, hw in enumerate(homeworks):
            if hw in results:
                print(f"SR No: {srno} | Topic: {hw[0]} | Subject: {hw[1]} | Class: {hw[2]} | Due: {hw[4]} | By: {hw[3]}")
