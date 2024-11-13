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
            print(f" There is a error creating a file '{name}': {e}")

    def deleteFile(self, name):
        try:
            os.remove(name)
            print(f"File '{name}' deleted.")
        except FileNotFoundError:
            print(f"Error: File '{name}' does not exist.")
        except Exception as e:
            print(f"Error deleting file '{name}': {e}")

    def renameFile(self, old_name, new_name):
        try:
            os.rename(old_name, new_name)
            print(f"File renamed from '{old_name}' to '{new_name}'.")
        except FileNotFoundError:
            print(f"Error: File '{old_name}' does not exist.")
        except Exception as e:
            print(f"Error renaming file: {e}")






