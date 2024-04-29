import os
import subprocess

def execute_shell_command_in_directory(directory, command, install_dependencies=False, install_flask=False):
    try:
        # Change the directory
        os.chdir(directory)
        
        # Install dependencies if specified
        if install_dependencies:
            if install_flask:
                subprocess.run("pip install flask flask_babel", shell=True, check=True)
            else:
                subprocess.run("pip install flask_babel", shell=True, check=True)
        
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
    directory_to_enter = ""
    command_to_execute = "python run.py"
    
    # Set to True if you want to install dependencies before running the command
    install_dependencies = True
    
    # Set to True if you want to install Flask along with Flask-Babel
    install_flask = True

    execute_shell_command_in_directory(directory_to_enter, command_to_execute, install_dependencies, install_flask)

