from func_1_teach import *
from func_2_teach import *
from func_3_teach import *
from func_4_teach import *
from func_5_teach import *
def teach_menu(teach_data):
    while True:
        print("\n📚 TEACHER MENU")
        print("1. Assign Homework")
        print("2. View Assigned Homework")
        print("3. Edit Homework Due Date")
        print("4. Delete a Homework")
        print("5. Search Homework")
        print("6. Students with complete HW ")
        print("7. Exit to Main Menu")

        choice = input("Enter choice (1-7): ").strip()

        if choice == '1':
            assign_homework(teach_data)
        elif choice == '2':
            view_homeworks(teach_data)
        elif choice == '3':
            edit_homework_due_date(teach_data)
        elif choice == '4':
            delete_homework(teach_data)
        elif choice == '5':
            search_homework(teach_data)
        elif choice == '6':
            view_stu_w_comp_hw(teacher_data)
        elif choice == '7':
            print("👋 Exiting to main menu...")
            return
        else:
            print("❌ Invalid choice. Try again.")
        
        input("Please press enter to continue")