#Hueland Hunter ID-2006702, Monica Foreshaw - 2104888, Richard Patterson - 2303690, Shamori Henry - 2100438

import subprocess
import os
from file_manager import FileManager
from directory_manager import DirectoryManager
from permission_manager import PermissionManager

class Shell:
    # Initializes the shell with instances of file, directory, and permission managers
    def __init__(self):
        self.file_manager = FileManager()
        self.directory_manager = DirectoryManager()
        self.permission_manager = PermissionManager()

    # Main loop of the shell
    def start(self):
        while True:
            # Display the shell prompt
            command = input("custom-shell> ").strip()
            if not command:
                continue  # Skip empty input

            # Check for special commands
            if command.endswith("&"):
                # Background command if it ends with "&"
                command = command[:-1].strip()  # Remove "&"
                self.run_in_background(command.split())
            elif "|" in command:
                # Handle piping if "|" is present
                self.handle_piping(command)
            elif ">" in command or "<" in command:
                # Handle redirection if ">" or "<" is present
                self.handle_redirection(command)
            else:
                # Regular command handling
                args = command.split()
                self.handle_command(args)

    # Handles internal and external commands
    def handle_command(self, args):
        if args[0] == "exit":
            exit(0)  # Exit the shell
        elif args[0] == "help":
            self.display_help()  # Display help information
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
        elif args[0] == "modify" and len(args) == 5:
            # Set permissions based on True/False values for read, write, execute
            readable = args[2].lower() == 'true'
            writable = args[3].lower() == 'true'
            executable = args[4].lower() == 'true'
            self.permission_manager.modify_permissions(args[1], readable, writable, executable)
        else:
            # Execute external command if it’s not an internal command
            self.execute_external_command(args)

    # Executes external commands using subprocess
    def execute_external_command(self, args):
        try:
            # Run the command and wait for it to complete
            result = subprocess.run(args, check=True)
            if result.returncode != 0:
                print(f"Command '{' '.join(args)}' failed with code {result.returncode}")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
        except FileNotFoundError:
            print(f"Error: Command '{args[0]}' not found.")
        except Exception as e:
            print(f"Error executing command '{args[0]}': {e}")

    # Handles input/output redirection
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
        # Split commands by pipe (|) symbol and create a list of commands
        commands = [cmd.strip().split() for cmd in command.split("|")]
        processes = []

        # Set up the pipeline chain
        for i, cmd in enumerate(commands):
            if i == 0:
                # First command takes input from stdin
                processes.append(subprocess.Popen(cmd, stdout=subprocess.PIPE))
            elif i == len(commands) - 1:
                # Last command outputs to stdout
                processes.append(subprocess.Popen(cmd, stdin=processes[-1].stdout))
            else:
                # Middle commands, pipe input and output
                processes.append(subprocess.Popen(cmd, stdin=processes[-1].stdout, stdout=subprocess.PIPE))

        # Wait for the last process in the pipeline to complete
        processes[-1].wait()

    # Runs commands in the background
    def run_in_background(self, args):
        try:
            subprocess.Popen(args)  # Run without waiting for completion
            print(f"Running {' '.join(args)} in background")
        except Exception as e:
            print(f"Error running in background: {e}")

    # Displays help information for supported commands
    def display_help(self):
        print("Supported commands:")
        print("create <file_name> - Create a new file")
        print("delete <file_name> - Delete an existing file")
        print("rename <old_name> <new_name> - Rename a file")
        print("make <dir_name> - Create a new directory")
        print("remove <dir_name> - Remove an empty directory")
        print("change <dir_name> - Change the current working directory")
        print("modify <file_name> <readable> <writable> <executable> - Set file permissions")
        print("Use > or < for output/input redirection, e.g., `ls > output.txt` or `wc < input.txt`")
        print("Use | for piping commands, e.g., `ls | grep txt`")
        print("Use & at the end of a command to run it in the background, e.g., `sleep 5 &`")
        print("exit - Exit the shell")
