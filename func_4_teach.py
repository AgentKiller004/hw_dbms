import csv

def delete_homework(teacher_data):
    """
    Deletes a homework record assigned by the logged-in teacher.
    """
    teach_id, teach_classes, teac_sub = teacher_data

    try:
        with open('homework.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            homeworks = list(reader)
    except FileNotFoundError:
        print("❌ homework.csv not found. Please ensure the file exists.")
        return

    # --- FIX: Store original index along with homework data ---
    # We enumerate the original homeworks list (including the header)
    # but filter based on the data rows (homeworks[1:])
    my_homeworks = [
        [i, hw] for i, hw in enumerate(homeworks) 
        if i > 0 and any(hw) and hw[3] == teach_id
    ]

    if not my_homeworks:
        print("\nℹ️ You haven't assigned any homework yet.")
        return

    print("\n--- Your Assigned Homework ---")
    # Display a clean serial number (1, 2, 3...) to the user
    for display_srno, (original_index, hw) in enumerate(my_homeworks, 1):
        print(f"Sr No: {display_srno} | Topic: {hw[0]} | Subject: {hw[1]} | Class: {hw[2]} | Due: {hw[4]}")

    while True:
        try:
            # Ask the user for the clean serial number
            choice = int(input("\nEnter the Sr No of the homework you want to delete: "))
            if 1 <= choice <= len(my_homeworks):
                break
            else:
                print(f"❌ Invalid choice. Please enter a number between 1 and {len(my_homeworks)}.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            
    # --- FIX: Identify the correct row to delete using the stored original index ---
    # Get the original index from our 'my_homeworks' list based on the user's choice
    index_to_delete = my_homeworks[choice - 1][0]

    # Remove the row from the original 'homeworks' list.
    # We use pop() for a clean removal.
    deleted_hw = homeworks.pop(index_to_delete)

    try:
        with open('homework.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(homeworks)
        
        print(f"\n✅ Homework '{deleted_hw[0]}' was deleted successfully.")
    except IOError:
        print("❌ Error: Could not write to homework.csv.")