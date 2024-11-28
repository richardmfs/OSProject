#Monica Foreshaw ID-2104888
#ID-2104888

class FileManager:
    # A method is created that takes two parameters: self and the name of the file
    def create_file(self, file_name):
        try:  # Try block is for handling the exceptions
            with open(file_name, 'w') as f:  # This allows the file to be opened in write mode
                pass
            # The message is printed when the file is created
            print(f"File '{file_name}' created.")
        except Exception as e:  # This except block allows the message to be printed when an error occurs
            print(f"Error creating file '{file_name}': {e}")  # Error message

    # A method for deleting a file
    def delete_file(self, file_name):
        try:  # Try block handles any error
            os.remove(file_name)  # This removes the file according to its name
            print(f"File '{file_name}' deleted.")  # Message when the file is deleted successfully
        except FileNotFoundError:  # This occurs when a file is not found
            print(f"Error: File '{file_name}' does not exist.")  # Printed if FileNotFoundError arises
        except Exception as e:  # Handles unexpected errors
            print(f"Error deleting file '{file_name}': {e}")  # Error message

    # A method for renaming a file
    def rename_file(self, old_name, new_name):
        try:  # Try block handles any error
            os.rename(old_name, new_name)  # Renames file from old_name to new_name
            print(f"File renamed from '{old_name}' to '{new_name}'.")  # Success message
        except FileNotFoundError:  # Occurs if the file is not found
            print(f"Error: File '{old_name}' does not exist.")  # Message if FileNotFoundError arises
        except Exception as e:  # Handles unexpected errors that arise when running the file
            print(f"Error renaming file: {e}")  # Error message

