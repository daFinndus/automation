import psutil
import time
import os

# Program to detect and delete all empty folders


# Function to execute the whole code
def main():
    print("Hello, this program is used to clear all empty folders off your drives.")
    time.sleep(1)

    drives = set_drives()  # Get selected drives from user

    path_storage = []  # Save every path in a list

    for drive in drives:
        path_storage.append(save_files(drive))  # It's stored as a list in a list

    folder_storage = []  # Store every directory in a list

    for path_list in path_storage:
        for path in path_list:
            if check_if_folder(path) is not None:
                folder_storage.append(path)

    for folder in folder_storage:
        if check_if_empty(folder) is not None:
            delete_folder(folder)

    print("\nThe process is complete. Every empty folder got managed.")
    input("Press enter to exit the application. ")


# Ask which drives should be scanned
def set_drives():
    drives = []

    for partition in psutil.disk_partitions():
        confirmation = input(
            f"\nWe found '{partition.device}'. Do you want to add it to the scan? [y/n] "
        ).lower()

        if confirmation == "y" or confirmation == "yes":
            print(f"We added the drive {partition.device} to our scannable drives.")
            drives.append(partition.device)
        else:
            print(f"Okay, we will not scan '{partition.device}'.")

    if drives:
        print(
            f"\nSetup is complete. We got these drives for the scan now: '{drives}'.\n"
        )
        return drives
    else:
        print(
            "\nYou do not have any drives left to scan. The program will close now.\n"
        )
        time.sleep(3)
        quit()


# Check drive for files and translate them into a path
def save_files(drive):
    path_storage = []

    hidden_files = input(
        f"Do you also wanna see the hidden directories on '{drive}'? [y/n] "
    ).lower()
    print("")

    for directory in os.listdir(drive):
        if hidden_files == "n" or hidden_files == "no":
            if directory.startswith("$"):
                continue

        path = os.path.join(drive, directory)  # Translate drive and directory to a path
        path_storage.append(path)  # Save the path in our 'storage'

    return path_storage


# Function to check if the directory is a directory and not just a file
def check_if_folder(path):
    try:
        if os.path.isdir(path):
            return path
    except PermissionError as e:
        print(f"We do not have permission to check '{path}'.")
        print(f"Error: {e}")


# Function to check if the given directory is empty
def check_if_empty(folder):
    try:
        if not os.listdir(folder):
            return folder  # Add every empty folder in list
    except PermissionError as e:
        print(f"\nWe do not have access to scan '{folder}'.")
        print(f"Error: {e}")


# Delete chosen path
def delete_folder(folder):
    delete_folder_confirmation = input(
        f"\nDo you wanna delete '{folder}'? [y/n] "
    ).lower()

    if delete_folder_confirmation == "y" or delete_folder_confirmation == "yes":
        try:
            os.rmdir(folder)
            print(f"Deleted '{folder}'.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
