import datetime
import time
import math
import random
import uuid
import os



from Moduler_Package.file_operator import file_operator
from Moduler_Package.math_operator import math_operator


#=================================
#Datetime and Time Operations
#=================================

def datetime_menu():
    while True:
        print("\n--- Datetime and Time Operations ---")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            current = datetime.datetime.now()
            print("Current Date and Time:",
                  current.strftime("%Y-%m-%d %H:%M:%S"))

        elif choice == "2":
            try:
                first = input("Enter the first date (YYYY-MM-DD): ")
                second = input("Enter the second date (YYYY-MM-DD): ")

                date1 = datetime.datetime.strptime(first, "%Y-%m-%d")
                date2 = datetime.datetime.strptime(second, "%Y-%m-%d")

                difference = abs((date2 - date1).days)
                print("Difference:", difference, "days")

            except ValueError:
                print("Invalid date format!")

        elif choice == "3":
            try:
                date_text = input("Enter date (YYYY-MM-DD): ")
                date_obj = datetime.datetime.strptime(
                    date_text, "%Y-%m-%d"
                )

                print("Formatted Date:",
                      date_obj.strftime("%d-%m-%Y"))
                print("Day:", date_obj.strftime("%A"))
                print("Month:", date_obj.strftime("%B"))

            except ValueError:
                print("Invalid date format!")

        elif choice == "4":
            print("Stopwatch started. Press Enter to stop.")

            start = time.perf_counter()
            input()

            elapsed = time.perf_counter() - start
            print(f"Elapsed Time: {elapsed:.2f} seconds")

        elif choice == "5":
            try:
                seconds = int(input("Enter countdown time in seconds: "))

                if seconds < 0:
                    print("Enter a positive number.")
                    continue

                for remaining in range(seconds, 0, -1):
                    print(
                        f"Time remaining: {remaining} seconds",
                        end="\r"
                    )
                    time.sleep(1)

                print("\nTime's up!")

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "6":
            break

        else:
            print("Invalid choice!")
            print("===============================")

#==============================
#Mathematical Operations
#==============================

def math_operator():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        # 1. Factorial
        if choice == "1":
            number = int(input("\nEnter a number: "))

            if number < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                factorial = math.factorial(number)
                print(f"Factorial: {factorial}")

        # 2. Compound Interest
        elif choice == "2":
            principal = float(input("\nEnter principal amount: "))
            rate = float(input("Enter rate of interest (in %): "))
            time = float(input("Enter time (in years): "))

            amount = principal * (1 + rate / 100) ** time
            compound_interest = amount - principal

            print(f"Compound Interest: {compound_interest:.2f}")

        # 3. Trigonometric Calculations
        elif choice == "3":
            angle = float(input("\nEnter angle in degrees: "))

            radians = math.radians(angle)

            print(f"Sin({angle}): {math.sin(radians):.4f}")
            print(f"Cos({angle}): {math.cos(radians):.4f}")
            print(f"Tan({angle}): {math.tan(radians):.4f}")

        # 4. Area of Geometric Shapes
        elif choice == "4":
            print("\nArea of Geometric Shapes:")
            print("1. Circle")
            print("2. Rectangle")
            print("3. Triangle")

            shape = input("Enter your choice: ")

            if shape == "1":
                radius = float(input("Enter radius: "))
                area = math.pi * radius ** 2
                print(f"Area of Circle: {area:.2f}")

            elif shape == "2":
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                area = length * width
                print(f"Area of Rectangle: {area:.2f}")

            elif shape == "3":
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                area = 0.5 * base * height
                print(f"Area of Triangle: {area:.2f}")

            else:
                print("Invalid choice.")

        # 5. Back to Main Menu
        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")
            print("===============================")

#===============================
#Random Data Generation
#===============================

def random_menu():
    while True:
        print("\n--- Random Data Generation ---")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Random Sampling")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Random Number:", random.randint(1, 100))

        elif choice == "2":
            numbers = [
                random.randint(1, 100)
                for _ in range(5)
            ]

            print("Random List:", numbers)

        elif choice == "3":
            try:
                length = int(input("Enter password length: "))

                if length <= 0:
                    print("Length must be greater than 0.")
                    continue

                characters = (
                    "abcdefghijklmnopqrstuvwxyz"
                    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    "0123456789!@#$%^&*"
                )

                password = "".join(
                    random.choice(characters)
                    for _ in range(length)
                )

                print("Generated Password:", password)

            except ValueError:
                print("Please enter a valid length.")

        elif choice == "4":
            otp = random.randint(100000, 999999)
            print("Generated OTP:", otp)

        elif choice == "5":
            data = input(
                "Enter items separated by commas: "
            ).split(",")

            data = [
                item.strip()
                for item in data
                if item.strip()
            ]

            if not data:
                print("No items entered.")
                continue

            try:
                count = int(
                    input("How many items to sample? ")
                )

                if count < 1 or count > len(data):
                    print(
                        "Sample size must be between 1 and",
                        len(data)
                    )
                else:
                    print(
                        "Random Sample:",
                        random.sample(data, count)
                    )

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "6":
            break

        else:
            print("Invalid choice!")
            print("===============================")

#===================================
#Generate Unique Identifiers (UUID)
#===================================

def uuid_menu():
    print("\n--- Generate Unique Identifiers (UUID) ---")
    print("Generated UUID:", uuid.uuid4())

#===============================
#File Operations
#===============================

def file_operator():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        # 1. Create a new file
        if choice == "1":
            filename = input("\nEnter file name: ")

            try:
                with open(filename, "x"):
                    pass
                print("File created successfully!")
            except FileExistsError:
                print("File already exists!")

        # 2. Write to a file
        elif choice == "2":
            filename = input("\nEnter file name: ")
            data = input("Enter data to write: ")

            with open(filename, "w") as file:
                file.write(data)

            print("Data written successfully!")

        # 3. Read from a file
        elif choice == "3":
            filename = input("\nEnter file name: ")

            try:
                with open(filename, "r") as file:
                    content = file.read()

                print("File Content:")
                print(content)

            except FileNotFoundError:
                print("File not found!")

        # 4. Append to a file
        elif choice == "4":
            filename = input("\nEnter file name: ")
            data = input("Enter data to append: ")

            with open(filename, "a") as file:
                file.write(data)

            print("Data appended successfully!")

        # 5. Back to Main Menu
        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")
            print("===============================")

#===============================
#Explore Module Attributes (dir())
#===============================

def explore_module():
        print("Explore Module Attributes:")

        module_name = input("Enter module name to explore: ")

        try:
            module = __import__(module_name)

            attributes = dir(module)

            print(f"Available Attributes in {module_name} module:")
            print(attributes[:20])
           
        except ModuleNotFoundError:
            print("Module not found!")
            print("===============================")


#===============================
#Main Function 
#===============================

def main():
    while True:
        print("\n==============================")
        print("Welcome to Multi-Utility Toolkit")
        print("==============================")

        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
         datetime_menu()

        elif choice == "2":
          math_operator()

        elif choice == "3":
         random_menu()

        elif choice == "4":
          uuid_menu()

        elif choice == "5":
         file_operator()

        elif choice == "6":
            explore_module()

        elif choice == "7":
           print("\n==============================")
           print("Thank you for using the Multi-Utility Toolkit!")
           print("==============================")
           break



        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
