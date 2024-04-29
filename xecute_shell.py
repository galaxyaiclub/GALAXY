import os
import subprocess

from server import server


def execute_shell_command_in_directory(directory, command):
    try:
        # Change the directory
        os.chdir(directory)
        # Execute the shell command
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during command execution
        print(f"Error executing command: {e}")
    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    directory_to_enter = "freegpt-webui-v2"
    command_to_execute = "python run.py"
  
server()
execute_shell_command_in_directory(directory_to_enter, command_to_execute)