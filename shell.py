#Hueland Hunter ID-2006702, Monica Foreshaw - 2104888, Richard Patterson - 2303690, Shamori Henry - 2100438

import os
import subprocess
from file_manager import FileManager
from directoryManagement import DirectoryManager
from permissions_manager import PermissionManager

class Shell:
    # Initializes the shell and creates instances of file, directory, and permission managers
    def __init__(self):
        self.file_manager = FileManager()
        self.directory_manager = DirectoryManager()
        self.permissions_manager = PermissionManager()

    # Main loop of the shell, takes user input and processes commands
    def start(self):
        while True:
            # Display shell prompt and read command from user
            command = input("custom-shell> ")
            if not command.strip():  # Ignore empty input
                continue

            # Split the input command into arguments
            args = command.split()

            # Check for and handle internal shell commands
            if args[0] == "exit":
                break
            elif args[0] == "help":
                self.display_help()
            elif args[0] == "create" and len(args) == 2:
                self.file_manager.create_file(args[1])
            elif args[0] == "delete" and len(args) == 2:
                self.file_manager.delete_file(args[1])
            elif args[0] == "rename" and len(args) == 3:
                self.file_manager.rename_file(args[1], args[2])
            elif args[0] == "make" and len(args) == 2:
                self.directory_manager.make_directory(args[1])
            elif args[0] == "remove" and len(args) == 2:
                self.directory_manager.remove_directory(args[1])
            elif args[0] == "change" and len(args) == 2:
                self.directory_manager.change_directory(args[1])
            elif args[0] == "modify":
                # Check for correct number of arguments for modify command
                if len(args) == 5:
                    # Parse boolean flags for readable, writable, and executable permissions
                    readable = args[2].lower() == 'true'
                    writable = args[3].lower() == 'true'
                    executable = args[4].lower() == 'true'
                    self.permissions_manager.modify_permissions(args[1], readable, writable, executable)
                else:
                    print("Usage: modify <file_name> <readable> <writable> <executable>")
                    
            else:
                # If it's not an internal command, treat it as an external command
                self.execute_external_command(args)

    # Executes external commands using subprocess
    def execute_external_command(self, args):
        try:
            # Run the command with the current environment's PATH
            result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=os.environ)
            if result.returncode == 0:
                print(result.stdout.decode())  # Print the output of the command
            else:
                print(f"Command '{' '.join(args)}' failed with code {result.returncode}")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
        except FileNotFoundError:
            print(f"Error: Command '{args[0]}' not found.")
        except Exception as e:
            print(f"Error executing command '{args[0]}': {1}")
            
            
    # Displays a list of supported commands and their usage
    def display_help(self):
        print("Supported commands:")
        print("create <file_name> - Create a new file")
        print("delete <file_name> - Delete an existing file")
        print("rename <previous_name> <new_name> - Rename a file")
        print("make <dir_name> - Create a new directory")
        print("remove <dir_name> - Remove an empty directory")
        print("change <dir_name> - Change the current working directory")
        print("modify <file_name> <readable> <writable> <executable> - Set file permissions")
        print("Use > or < for output/input redirection, e.g., `ls > output.txt` or `wc < input.txt`")
        print("Use | for piping commands, e.g., `ls | grep txt`")
        print("Use & at the end of a command to run it in the background, e.g., `sleep 5 &`")
        print("exit - Exit the shell")