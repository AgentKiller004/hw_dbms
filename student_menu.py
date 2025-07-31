# student_menu.py

# --- Import the student functions you created ---
from func_1_stu import view_all_hw
from func_2_stu import mark_done

def stu_menu(st_data):
    """
    Displays the menu for the student and handles their choices.
    The 'st_data' variable is passed directly from the login system.
    """
    flag = 0
    updated_st_data = st_data

    while True:
        # --- FIX: Display student name and class correctly from the tuple ---
        print("\n--- Student Menu ---")
        # Assuming st_data is (student_id, name, class, completions_str)
        print(f"Logged in as: {updated_st_data[1]} | Class: {updated_st_data[2]}")
        print("1. View My Homeworks")
        print("2. Mark a Homework as Done")
        print("3. Logout")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            # --- FIX: Call the function by its correct imported name ---
            view_all_hw(updated_st_data)
        elif choice == '2':
            # --- FIX: Call the function by its correct imported name ---
            flag, updated_st_data = mark_done(updated_st_data)
        elif choice == '3':
            print("\n👋 Logging out...")
            # Return the latest student data to be saved by the main menu
            return flag, updated_st_data
        else:
            print("❌ Invalid choice. Please try again.")

        input('\nPress Enter to continue...')