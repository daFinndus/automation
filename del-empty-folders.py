import sys
import os

import argparse


def create_arg_parser():
    # Creates and returns the ArgumentParser object
    parser = argparse.ArgumentParser(description="Delete empty folders in a directory")

    parser.add_argument("path", help="Path to check for empty folders")
    return parser


def get_folders(path):
    # Returns a list of folders in the provided path
    folders = []

    print("Checking for empty folders in: ", path)

    try:
        for folder in os.listdir(path):
            folder_path = os.path.join(path, folder)
            if os.path.isdir(folder_path) and not os.listdir(folder_path):
                folders.append(folder_path)
                print("Found empty folders: ", folders)
    except PermissionError:
        print("Permission denied for a folder!")
    except Exception as e:
        print("An error occurred: ", e)

    return folders


def delete_empty_folders(folders):
    if folders:
        # Deletes folders from the provided list
        for folder in folders:
            confirmation = input(f"Do you want to delete {folder}? [y/n] ").lower()
            if confirmation == "y" or confirmation == "yes":
                os.rmdir(folder)
                print(f"{folder} has been deleted.")
    else:
        print("No empty folders found.")


if __name__ == "__main__":
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    if os.path.exists(parsed_args.path):
        print("Path exists, continuing...")

        delete_empty_folders(get_folders(parsed_args.path))
    else:
        print("Path does not exist")
        sys.exit(1)
