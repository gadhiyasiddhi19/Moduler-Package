from modules.operations import (
    datetime_menu,
    mathematical_menu,
    random_menu,
    generate_uid,
    explore_module
)

from modules.file_operations import file_menu


# =====================================================
# MAIN MENU
# =====================================================

def main():
    while True:

        print("\nWelcome to Multi-Utility Toolkit")

        print("\nChoose an option:")

        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            datetime_menu()

        elif choice == "2":

            mathematical_menu()

        elif choice == "3":

            random_menu()

        elif choice == "4":

            print(
                "\nGenerate Unique Identifiers (UID):"
            )

            generate_uid()

        elif choice == "5":

            file_menu()

        elif choice == "6":

            explore_module()

        elif choice == "7":

            print(
                "\nThank you for using "
                "Multi-Utility Toolkit!"
            )

            break

        else:

            print(
                "\nInvalid choice. Please try again."
            )


# =====================================================
# MAIN EXECUTION
# =====================================================

if __name__ == "__main__":

    main()