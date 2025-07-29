def teacher_menu(teach_data):
    while True:
        print("\n📚 TEACHER MENU")
        print("1. Assign Homework")
        print("2. View Assigned Homework")
        print("3. Edit Homework Due Date")
        print("4. Delete a Homework")
        print("5. Search Homework")
        print("6. Exit to Main Menu")

        choice = input("Enter choice (1-6): ").strip()

        if choice == '1':
            assign_homework(teach_data)
        elif choice == '2':
            view_homeworks(teach_data)
        elif choice == '3':
            edit_homework_due_date(teach_data)
        elif choice == '4':
            delete_homework(teach_data)
        elif choice == '5':
            search_homework()
        elif choice == '6':
            print("👋 Exiting to main menu...")
            return
        else:
            print("❌ Invalid choice. Try again.")
