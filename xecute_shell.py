import os
import subprocess

def install_flask_and_flask_babel():
    try:
        # Install Flask and Flask-Babel
        subprocess.run("pip install flask flask_babel", shell=True, check=True)
        print("Flask and Flask-Babel installed successfully.")
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during installation
        print(f"Error installing Flask and Flask-Babel: {e}")
    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    install_flask_and_flask_babel()

