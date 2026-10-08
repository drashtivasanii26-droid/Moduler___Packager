import math


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