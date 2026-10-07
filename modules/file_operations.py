# =====================================================
# CREATE A NEW FILE
# =====================================================

def create_file():

    file_name = input(
        "\nEnter file name: "
    )

    file = open(
        file_name,
        "a"
    )

    file.close()

    print(
        "File created successfully!"
    )


# =====================================================
# WRITE TO A FILE
# =====================================================

def write_file():

    file_name = input(
        "\nEnter file name: "
    )

    data = input(
        "\nEnter data to write: "
    )

    file = open(
        file_name,
        "w"
    )

    file.write(data)

    file.close()

    print(
        "Data written successfully!"
    )


# =====================================================
# READ FROM A FILE
# =====================================================

def read_file():

    file_name = input(
        "\nEnter file name: "
    )

    file = open(
        file_name,
        "r"
    )

    data = file.read()

    file.close()

    print("\nFile Content:")
    print(data)


# =====================================================
# APPEND TO A FILE
# =====================================================

def append_file():

    file_name = input(
        "\nEnter file name: "
    )

    data = input(
        "\nEnter data to append: "
    )

    file = open(
        file_name,
        "a"
    )

    file.write(data)

    file.close()

    print(
        "Data appended successfully!"
    )


# =====================================================
# FILE OPERATIONS MENU
# =====================================================

def file_menu():

    while True:

        print("\nFile Operations:")

        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":

            create_file()

        elif choice == "2":

            write_file()

        elif choice == "3":

            read_file()

        elif choice == "4":

            append_file()

        elif choice == "5":

            break

        else:

            print(
                "Invalid choice. Please try again."
            )