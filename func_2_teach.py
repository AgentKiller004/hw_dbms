import csv

def view_homeworks(teach_data):
    """
    Displays homework based on teacher's choice:
    1. All homework for one of their classes.
    2. All homework they have assigned.
    3. Homework they assigned to a specific class.
    """
    teach_id, teach_classes, teac_sub = teach_data
    
    while True:
        print("\n--- View Homework Options ---")
        print("1. All homework for one of my classes (by any teacher)")
        print("2. All homework I’ve ever assigned")
        print("3. Homework I assigned to a specific class")
        print("4. Exit to Teacher Menu")
        
        choice = input("Enter option (1-4): ").strip()

        if choice == '4':
            print("👋 Returning to Teacher Menu...")
            return

        try:
            with open('homework.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                # Skip header row for processing
                homeworks = list(reader)[1:]
        except FileNotFoundError:
            print("❌ homework.csv not found. Please ensure the file exists.")
            continue

        results = []
        if choice == '1':
            print("\nSelect from your classes:")
            for i, cls in enumerate(teach_classes, 1):
                print(f"{i}. {cls}")
            
            try:
                cls_choice = int(input("Enter class number: "))
                if 1 <= cls_choice <= len(teach_classes):
                    target_class = teach_classes[cls_choice - 1]
                    results = [hw for hw in homeworks if any(hw) and hw[2] == target_class]
                else:
                    print("❌ Invalid class number.")
            except ValueError:
                print("❌ Invalid input. Please enter a number.")

        elif choice == '2':
            results = [hw for hw in homeworks if any(hw) and hw[3] == teach_id]

        elif choice == '3':
            print("\nSelect from your classes:")
            for i, cls in enumerate(teach_classes, 1):
                print(f"{i}. {cls}")

            try:
                cls_choice = int(input("Enter class number: "))
                if 1 <= cls_choice <= len(teach_classes):
                    target_class = teach_classes[cls_choice - 1]
                    results = [hw for hw in homeworks if any(hw) and hw[2] == target_class and hw[3] == teach_id]
                else:
                    print("❌ Invalid class number.")
            except (ValueError, IndexError):
                print("❌ Invalid input. Please enter a number from the list.")
        
        else:
            print("❌ Invalid option. Please try again.")
            continue

        print("\n--- Homework List ---")
        if not results:
            print("No homework found matching your criteria.")
        else:
            # FIX: Iterate over the filtered 'results' list to show correct SR No.
            for srno, hw in enumerate(results, 1):
                # Assuming the homework columns are: Topic, Subject, Class, Teacher_ID, Due_Date
                print(f"SR No: {srno} | Topic: {hw[0]} | Subject: {hw[1]} | Class: {hw[2]} | Due: {hw[4]} | By: {hw[3]}")
        
        input('\nPress Enter to continue...')