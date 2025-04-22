import os
import sys


if __name__ == "__main__":

    # Get the current working directory
    current_directory = os.getcwd()

    # Get the absolute path of the script
    script_path = os.path.abspath(__file__)

    # Get the directory of the script
    script_directory = os.path.dirname(script_path)

    # Add the script directory to the system path
    sys.path.append(script_directory)

    print(f"Current Directory: {current_directory}")
    print(f"Script Path: {script_path}")
    print(f"Script Directory: {script_directory}")