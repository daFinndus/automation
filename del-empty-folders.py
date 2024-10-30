import sys
import os

import argparse
from pathlib import Path

def create_arg_parser():
    # Creates and returns the ArgumentParser object
    parser = argparse.ArgumentParser(description="Delete empty folders in a directory")

    parser.add_argument("path", help="Path to check for empty folders")
    return parser

def get_folders(path):
    # Returns a list of folders in the provided path
    folders = []

    print("Checking for folders in: ", path)

    for folder in os.listdir(path):
        folder_path = os.path.join(path, folder)
        if os.path.isdir(folder_path):
            folders.append(folder_path)

    print("Found folders: ", folders)
    return folders

def delete_empty_folders(folders):
    # Deletes empty folders from the provided list
    for folder in folders:
        if not os.listdir(folder):
            confirmation = input(f"Do you want to delete {folder}? [y/n] ").lower()

            if confirmation == "y" or confirmation == "yes":
                os.rmdir(folder)
                print(f"{folder} has been deleted.")


if __name__ == "__main__":
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    if os.path.exists(parsed_args.path):
        print("Path exists, continuing...")

        get_folders(parsed_args.path)
        delete_empty_folders(get_folders(parsed_args.path))
    else:
        print("Path does not exist")
        sys.exit(1)


