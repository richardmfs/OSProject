#Richard Patterson - 2303690

import os

class DirectoryManager: 
    #Allows the user to create a directory
    def make_directory(self, dir_name):
        #Outputs the message "Directory" <user directory> "created." when the user makes a directory and outputs an error message using a 
        #fstring if the directory already exists or if there were any errors when creating it
        try:
            os.makedirs(dir_name, exist_ok=True)
            print(f"Directory '{dir_name}' created.")  
        except Exception as e:
            print(f"Error creating directory '{dir_name}': {e}")

    #Allows the user to remove a directory
    def remove_directory(self, dir_name):
        try:
            os.rmdir(dir_name)
            print(f"Directory '{dir_name}' removed.") # Removes an empty directory
        except FileNotFoundError:
            print(f"Error: Directory '{dir_name}' does not exist.")#Error message if the directory being removed does not exist
        except OSError:
            print(f"Error: Directory '{dir_name}' is not empty or cannot be removed.")#Error message if the directory has file contents and cannot be removed
        except Exception as e:
            print(f"Error removing directory '{dir_name}': {e}")#Error message for any other errors while removing a directory

    def change_directory(self, dir_name):
        try:
            os.chdir(dir_name)
            print(f"Changed directory to '{dir_name}'.")#Changes to another directory
        except FileNotFoundError:
            print(f"Error: Directory '{dir_name}' does not exist.")#Error message if the directory being specified does not exist
        except Exception as e:
            print(f"Error changing directory: {e}")#Error message for any other errors that occur while changing the directory
