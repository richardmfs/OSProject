#Monica Foreshaw
#2104888
import os
class FileManager:
    #A method is created that takes two parameter self and the name of the file
    def creating_file(self, name):
        try: # try block is for handling the exceptions
            with open(name, 'w') as f: # this allows the file to be open in write mode
                pass
            #The message is printed when the file is created
            print(f"The file by the name of '{name}' is created.")
        except Exception as e: #this except block allow the message to be printed when a error occurs
            print(f" There is a error creating a file '{name}': {e}") #the error message that is printed if there is a error in creating the file
#method for deleting a file
    def deleting_file(self, name):
        try: # try block handles any error
            os.remove(name) # this is removing the file according to its name
            print(f" The file '{name}' has been deleted.")  # error message when the file is deleted successfully
        except FileNotFoundError:# this takes place when a file is not found
            print(f"Error: The file '{name}' does not exist.") #If the FileNotFoundError arise , this statement is printed
        except Exception as e: # this happens if there is a unexpected error
            print(f"Error deleting file '{name}': {e}") # error message is printed

    def renaming_file(self, previous_name, new_name):
        try:
            os.rename(previous_name, new_name)
            print(f"The file renamed from '{previous_name}' to '{new_name}'.")
        except FileNotFoundError: #this takes place when a file is not found
            print(f"Error: The file by the name of '{previous_name}' doesn't exist.") #If the FileNotFoundError arise , this statement is printed
        except Exception as e:
            print(f"An error occur when renaming the file: {e}") # error message occur







