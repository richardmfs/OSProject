#Hueland Hunter ID-2006702, Monica Foreshaw - 2104888, Richard Patterson - 2303690, Shamori Henry - 2100438

import os
import subprocess
from file_manager import FileManager
from directory_manager import DirectoryManager
from permissions_manager import PermissionManager

class Shell:
    # Initializes the shell and creates instances of file, directory, and permission managers
    def __init__(self):
        self.file_manager = FileManager()
        self.directory_manager = DirectoryManager()
        self.permission_manager = PermissionManager()

    # Main loop of the shell, takes user input and processes commands
    
    def start(self):
        while True:
            command = input("custom-shell> ")
            if not command.strip():
                continue

        # Handle exit and help commands
            if command.strip() == "exit":
                break
            elif command.strip() == "help":
                self.display_help()
                continue
                
            if "|" in command:
                self.handle_piping(command)
                continue

        # Check for redirection in the command and handle it
            if ">" in command or "<" in command:
                self.handle_redirection(command)
                continue
            # Split the input command into arguments for non-redirection commands
            args = command.split()
            # Handle internal commands or execute as external
            if args[0] == "create":
                if len(args) != 2:
                    print("Usage: create <file_name> - Create a new file")
                else:
                    self.file_manager.create_file(args[1])
            elif args[0] == "delete":
                if len(args) != 2:
                    print("Usage: delete <file_name> - Delete an existing file")
                else:
                    self.file_manager.delete_file(args[1])
            elif args[0] == "rename":
                if len(args) != 3:
                    print("Usage: rename <previous_name> <new_name> - Rename a file")
                else:
                    self.file_manager.rename_file(args[1], args[2])
            elif args[0] == "make":
                if len(args) != 2:
                    print("Usage: make <dir_name> - Create a new directory")
                else:
                    self.directory_manager.make_directory(args[1])
            elif args[0] == "remove":
                if len(args) != 2:
                    print("Usage: remove <dir_name> - Remove an empty directory")
                else:
                    self.directory_manager.remove_directory(args[1])
            elif args[0] == "change":
                if len(args) != 2:
                    print("Usage: change <dir_name> - Change the current working directory")
                else:
                    self.directory_manager.change_directory(args[1])
            elif args[0] == "modify":
                if len(args) != 5:
                    print("Usage: modify <file_name> <readable> <writable> <executable> - Set file permissions")
                else:
                    readable = args[2].lower() == 'true'
                    writable = args[3].lower() == 'true'
                    executable = args[4].lower() == 'true'
                    self.permission_manager.modify_permissions(args[1], readable, writable, executable)
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
            print(f"Error executing command '{args[0]}': {e}")
            
            
    def handle_redirection(self, command):
        if ">" in command:
            # Output redirection: command > filename
            parts = command.split(">")
            cmd = parts[0].strip().split()  # Command part
            filename = parts[1].strip()  # File to write to
            with open(filename, "w") as f:
                subprocess.run(cmd, stdout=f)  # Redirect stdout to file
            print(f"Output redirected to {filename}")
        elif "<" in command:
            # Input redirection: command < filename
            parts = command.split("<")
            cmd = parts[0].strip().split()  # Command part
            filename = parts[1].strip()  # File to read from
            with open(filename, "r") as f:
                subprocess.run(cmd, stdin=f)  # Redirect stdin from file
            print(f"Input redirected from {filename}")

    # Handles piping between commands
    def handle_piping(self, command):
        commands = [cmd.strip().split() for cmd in command.split("|")]
        processes = []
        for i, cmd in enumerate(commands):
            if i == 0:
                processes.append(subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE))
            elif i == len(commands) - 1:
                processes.append(subprocess.Popen(cmd, stdin=processes[-1].stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE))
            else:
                processes.append(subprocess.Popen(cmd, stdin=processes[-1].stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE))
                processes[-2].stdout.close()
        stdout, stderr = processes[-1].communicate()
        if stdout:
            print(stdout.decode())
        if stderr:
            print(stderr.decode())
        for p in processes:
            p.wait()


    # Displays a list of supported commands and their usage
    def display_help(self):
        print("Supported commands:")
        print(" ")
        print("create <file_name> - Create a new file")
        print(" ")
        print("delete <file_name> - Delete an existing file")
        print(" ")
        print("rename <previous_name> <new_name> - Rename a file")
        print(" ")
        print("make <dir_name> - Create a new directory")
        print(" ")
        print("remove <dir_name> - Remove an empty directory")
        print(" ")
        print("change <dir_name> - Change the current working directory")
        print(" ")
        print("modify <file_name> <readable> <writable> <executable> example = modify file.txt true false false (changes file permissions to readable) - Set file permissions")
        print(" ")
        print("ls -l - List file attributes")
        print(" ")
        print("Use > or < for output/input redirection, e.g., `ls > output.txt` or `wc < input.txt`")
        print(" ")
        print("Use | for piping commands, e.g., `ls | grep txt`")
        print(" ")
        print("exit - Exit the shell")




           
