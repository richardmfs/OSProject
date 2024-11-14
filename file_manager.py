#Monica Foreshaw ID-2104888
#ID-2104888
import os

class FileManager:
    # A method is created that takes two parameter self and the name of the file
    def creating_file(self, name):
        try:  # try block is for handling the exceptions
            with open(name, 'w') as f:  # this allows the file to be open in write mode
                pass
            # The message is printed when the file is created
            print(f"The file by the name of '{name}' is created.")
        except Exception as e:  # this except block allows the message to be printed when an error occurs
            print(f"There is an error creating a file '{name}': {e}")  # error message

    # method for deleting a file
    def deleting_file(self, name):
        try:  # try block handles any error
            os.remove(name)  # this removes the file according to its name
            print(f"The file '{name}' has been deleted.")  # message when file is deleted successfully
        except FileNotFoundError:  # this occurs when a file is not found
            print(f"Error: The file '{name}' does not exist.")  # printed if FileNotFoundError arises
        except Exception as e:  # handles unexpected errors
            print(f"Error deleting file '{name}': {e}")  # error message

    # method for renaming file
    def renaming_file(self, previous_name, new_name):
        try:  # try block handles any error
            os.rename(previous_name, new_name)  # renames file from previous name to new name
            print(f"The file renamed from '{previous_name}' to '{new_name}'.")  # success message
        except FileNotFoundError:  # occurs if file is not found
            print(f"Error: The file by the name of '{previous_name}' doesn't exist.")  # message if FileNotFoundError arises
        except Exception as e:  # handles unexpected errors that arises when running the file
            print(f"An error occurred when renaming the file: {e}")  # error message


