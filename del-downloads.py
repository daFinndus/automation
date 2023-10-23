import os
import shutil
import time


# Main function to confirm that the user wants to clear the downloads
def main():
    confirmation = input(
        "Hello, do you wanna delete everything in your downloads folder? [y/n] "
    )

    if confirmation.lower() == "y" or confirmation.lower() == "yes":
        print(
            "\nThank you for using this program. First you need to enter your username."
        )
        print(
            "The username is needed to detect the path of your download folder, which we wanna clear.\n"
        )

        set_direction()

    elif confirmation.lower() == "n" or confirmation.lower() == "no":
        print("Okay, have a great day tho!")
        time.sleep(3)
        exit()

    else:
        print(
            "Sorry, I wasn't able to understand that. Please answer with yes (y) or no (n)."
        )
        main()


# Function to set the directory which will be cleared
def set_direction():
    print(
        "Normally the folder path will look something like this: 'C:\\Users\\your_username_here\\Downloads'.\n"
    )

    username = input("Enter your username here > ")

    direction = f"C:\\Users\\{username}\\Downloads"

    delete_downloads(direction)


# Function to delete everything in a certain directory
def delete_downloads(direction):
    num_files = 0
    num_dirs = 0

    try:
        files = os.listdir(direction)

        if files:
            print(f"Found following files: {files}\n")

            for root, dirs, files in os.walk(direction):
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    confirmation = input(f"Do you wanna delete {file_name}? [y/n] ")
                    if confirmation.lower() == "y" or confirmation.lower() == "yes":
                        try:
                            os.remove(file_path)
                            num_files += 1
                            print(f"Deleted file: {file_path}")
                        except Exception as e:
                            print(f"Error: {e}")
                    else:
                        print(
                            f"Okay, {file_name} will stay in your download directory."
                        )

                for dir_name in dirs:
                    dir_path = os.path.join(root, dir_name)
                    try:
                        shutil.rmtree(dir_path)
                        num_dirs += 1
                        print(f"Deleted directory: {dir_path}")
                    except Exception as e:
                        print(f"Error: {e}")

            print(f"\nDeleted {num_dirs} directories and {num_files} files.\n")
            input("Press enter twice to exit the program.")
        else:
            print("\nNo files detected in the download folder.")
            time.sleep(1)
            print("See you next time, hopefully with a full download directory.")
            time.sleep(3)
            quit()

    except FileNotFoundError:
        print("\nThe user couldn't be recognized. Let's try again.\n")
        time.sleep(3)
        set_direction()


if __name__ == "__main__":
    main()
