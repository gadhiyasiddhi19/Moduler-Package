import datetime
import time
import math
import random
import uuid


# =====================================================
# DATETIME AND TIME OPERATIONS
# =====================================================

def datetime_menu():

    while True:

        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            current_datetime = datetime.datetime.now()

            print(
                "Current Date and Time:",
                current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            )

        elif choice == "2":

            first_date = input(
                "Enter the first date (YYYY-MM-DD): "
            )

            second_date = input(
                "Enter the second date (YYYY-MM-DD): "
            )

            date1 = datetime.datetime.strptime(
                first_date,
                "%Y-%m-%d"
            )

            date2 = datetime.datetime.strptime(
                second_date,
                "%Y-%m-%d"
            )

            difference = abs((date2 - date1).days)

            print("Difference:", difference, "days")

        elif choice == "3":

            date_input = input(
                "Enter date (YYYY-MM-DD): "
            )

            date_value = datetime.datetime.strptime(
                date_input,
                "%Y-%m-%d"
            )

            formatted_date = date_value.strftime(
                "%d-%m-%Y"
            )

            print("Formatted Date:", formatted_date)

        elif choice == "4":

            print("\nStopwatch Started!")

            start_time = time.time()

            input("Press Enter to stop the stopwatch.")

            end_time = time.time()

            elapsed_time = end_time - start_time

            print(
                "Elapsed Time:",
                round(elapsed_time, 2),
                "seconds"
            )

        elif choice == "5":

            seconds = int(
                input("Enter countdown time in seconds: ")
            )

            print("\nCountdown Started!")

            while seconds > 0:

                print(seconds)

                time.sleep(1)

                seconds = seconds - 1

            print("Time's up!")

        elif choice == "6":

            break

        else:

            print("Invalid choice. Please try again.")


# =====================================================
# MATHEMATICAL OPERATIONS
# =====================================================

def mathematical_menu():

    while True:

        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            number = int(
                input("\nEnter a number: ")
            )

            factorial = math.factorial(number)

            print("Factorial:", factorial)

        elif choice == "2":

            principal = float(
                input("\nEnter principal amount: ")
            )

            rate = float(
                input("Enter rate of interest (in %): ")
            )

            years = float(
                input("Enter time (in years): ")
            )

            amount = principal * (
                1 + rate / 100
            ) ** years

            print(
                "Compound Interest:",
                format(amount, ".2f")
            )

        elif choice == "3":

            angle = float(
                input("\nEnter angle in degrees: ")
            )

            radians = math.radians(angle)

            print(
                "Sine:",
                round(math.sin(radians), 4)
            )

            print(
                "Cosine:",
                round(math.cos(radians), 4)
            )

            print(
                "Tangent:",
                round(math.tan(radians), 4)
            )

        elif choice == "4":

            print("\nArea of Geometric Shapes:")
            print("1. Circle")
            print("2. Rectangle")
            print("3. Triangle")

            shape_choice = input(
                "Enter your choice: "
            )

            if shape_choice == "1":

                radius = float(
                    input("\nEnter radius: ")
                )

                area = math.pi * radius * radius

                print(
                    "Area of Circle:",
                    round(area, 2)
                )

            elif shape_choice == "2":

                length = float(
                    input("\nEnter length: ")
                )

                width = float(
                    input("Enter width: ")
                )

                area = length * width

                print(
                    "Area of Rectangle:",
                    round(area, 2)
                )

            elif shape_choice == "3":

                base = float(
                    input("\nEnter base: ")
                )

                height = float(
                    input("Enter height: ")
                )

                area = 0.5 * base * height

                print(
                    "Area of Triangle:",
                    round(area, 2)
                )

            else:

                print("Invalid choice.")

        elif choice == "5":

            break

        else:

            print("Invalid choice. Please try again.")


# =====================================================
# RANDOM DATA GENERATION
# =====================================================

def random_menu():

    while True:

        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            number = random.randint(1, 100)

            print(
                "\nGenerated Random Number:",
                number
            )

        elif choice == "2":

            size = int(
                input("\nEnter list size: ")
            )

            random_list = []

            for i in range(size):

                random_list.append(
                    random.randint(1, 100)
                )

            print(
                "Generated Random List:",
                random_list
            )

        elif choice == "3":

            length = int(
                input("\nEnter password length: ")
            )

            characters = (
                "abcdefghijklmnopqrstuvwxyz"
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                "0123456789"
                "@#$%&!"
            )

            password = ""

            for i in range(length):

                password = password + random.choice(
                    characters
                )

            print(
                "Generated Password:",
                password
            )

        elif choice == "4":

            otp = random.randint(
                100000,
                999999
            )

            print(
                "\nGenerated Random OTP:",
                otp
            )

        elif choice == "5":

            break

        else:

            print("Invalid choice. Please try again.")


# =====================================================
# UNIQUE IDENTIFIER
# =====================================================

def generate_uid():

    unique_id = uuid.uuid4()

    print(
        "\nGenerated UID:",
        unique_id
    )


# =====================================================
# DYNAMIC MODULE EXPLORATION
# =====================================================

def explore_module():

    print("\nExplore Module Attributes:")

    module_name = input(
        "Enter module name to explore: "
    )

    available_modules = {
        "datetime": datetime,
        "time": time,
        "math": math,
        "random": random,
        "uuid": uuid
    }

    if module_name in available_modules:

        module = available_modules[module_name]

        print(
            "\nAvailable Attributes in",
            module_name,
            "module:"
        )

        print(dir(module))

    else:

        print("Module not available.")