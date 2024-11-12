import os

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
            print(f"Directory '{dir_name}' removed.")
        except FileNotFoundError:
            print(f"Error: Directory '{dir_name}' does not exist.")
        except OSError:
            print(f"Error: Directory '{dir_name}' is not empty or cannot be removed.")
        except Exception as e:
            print(f"Error removing directory '{dir_name}': {e}")

    def change_directory(self, dir_name):
        try:
            os.chdir(dir_name)
            print(f"Changed directory to '{dir_name}'.")
        except FileNotFoundError:
            print(f"Error: Directory '{dir_name}' does not exist.")
        except Exception as e:
            print(f"Error changing directory: {e}")
