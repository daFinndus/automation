import shutil
import sys
import os

import argparse
import time


def create_arg_parser():
    # Creates and returns the ArgumentParser object
    parser = argparse.ArgumentParser(description="Delete empty folders in a directory")

    parser.add_argument("path", help="Path to check for empty folders")
    return parser


# This function will return a list of empty folders in the provided path
def get_empty_folders(path):
    folders = []

    print("Checking for empty folders in: ", path)

    try:
        for folder in os.listdir(path):
            folder_path = os.path.join(path, folder)
            if os.path.isdir(folder_path) and not os.listdir(folder_path):
                folders.append(folder_path)

        if folders:
            print("Found empty folders: ", folders)
        else:
            print("No empty folders found.")
    except PermissionError:
        print("Permission denied for a folder!")
    except Exception as e:
        print("An error occurred: ", e)

    return folders


# This function will return a list of folders in the provided path that do not contain any .mp4 or .mov files
def get_folders_without_videos(path):
    folders = []

    print("Checking for folders without videos in: ", path)

    try:
        for folder in os.listdir(path):
            folder_path = os.path.join(path, folder)
            if os.path.isdir(folder_path) and not any(
                    file.endswith((".mp4", ".mov", ".mkv")) for file in os.listdir(folder_path)):
                folders.append(folder_path)

        if folders:
            print("Found folders without videos: ", folders)
        else:
            print("No folders without videos found.")
    except PermissionError:
        print("Permission denied for a folder!")
    except Exception as e:
        print("An error occurred: ", e)

    return folders


# This function will delete the folders after asking for permission
def delete_with_permission(folders):
    if folders:
        # Deletes folders from the provided list
        for folder in folders:
            confirmation = input(f"Do you want to delete {folder}? [y/n] ").lower()
            if confirmation == "y" or confirmation == "yes":
                try:
                    shutil.rmtree(folder)
                    print(f"{folder} has been deleted.")
                except PermissionError:
                    print(f"Permission denied for {folder}!")
    else:
        print("No empty folders found.")


# This function will delete the folders without asking for permission
def just_delete_folders(folders):
    if folders:
        for folder in folders:
            try:
                shutil.rmtree(folder)
                print(f"{folder} has been deleted.")
            except PermissionError:
                print(f"Permission denied for {folder}!")


if __name__ == "__main__":
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    if os.path.exists(parsed_args.path):
        print("Path exists, continuing...")

        just_delete_folders(get_folders_without_videos(parsed_args.path))
        time.sleep(2.5)
    else:
        print("Path does not exist")
        sys.exit(1)
