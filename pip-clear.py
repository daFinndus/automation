import subprocess


def get_installed_packages():
    try:
        installed_packages = subprocess.check_output(["pip", "list"]).decode("utf-8")
        return [
            package.strip().split()[0]
            for package in installed_packages.splitlines()[2:]
        ]
    except subprocess.CalledProcessError as e:
        print(f"Error getting list of installed packages: {e}")
        return []


def uninstall_package(package_name):
    try:
        subprocess.run(["pip", "uninstall", package_name], check=True)
        print(f"{package_name} has been uninstalled successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error uninstalling {package_name}: {e}")


def main():
    installed_packages = get_installed_packages()

    if not installed_packages:
        print("No packages found.")
        return

    print("\nYou have these packages installed:\n")

    for package in installed_packages:
        print(package)

    print("\nWe will ask you for permission to remove the packages.\n")

    for package in installed_packages:
        if package == "pip":
            print(f"The {package} cannot be uninstalled.")
        else:
            confirmation = input(f"Do you want to delete {package}? [y/n] ").lower()
            if confirmation == "y" or confirmation == "yes":
                uninstall_package(package)
            else:
                print(f"Okay, we will not delete {package}.")

    print("\nAll packages have been managed.")


if __name__ == "__main__":
    main()
