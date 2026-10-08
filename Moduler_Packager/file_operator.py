import os


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