#Richard Patterson - 2303690



class DirectoryManager:
    def make_directory(self, dir_name):
        try:
            os.makedirs(dir_name, exist_ok=True) 
            print(f"Directory '{dir_name}' created.")
        except Exception as e:
            print(f"Error creating directory '{dir_name}': {e}")

    def remove_directory(self, dir_name):
        try:
            os.rmdir(dir_name)
            print(f"Directory '{dir_name}' removed.")  #Creates the directory
        except FileNotFoundError:
            print(f"Error: Directory '{dir_name}' does not exist.") #Error if the directory being removed doesn't exist
        except OSError:
            print(f"Error: Directory '{dir_name}' is not empty or cannot be removed.")  #Error if the directory being removed is not empty
        except Exception as e:
            print(f"Error removing directory '{dir_name}': {e}")  #Handles any other error when removing the directory

    def change_directory(self, dir_name):
        try:
            os.chdir(dir_name)
            print(f"Changed directory to '{dir_name}'.")
        except FileNotFoundError:
            print(f"Error: Directory '{dir_name}' does not exist.")
        except Exception as e:
            print(f"Error changing directory: {e}")

