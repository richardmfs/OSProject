import os

class PermissionManager:
    # Modifies file permissions based on boolean flags for read, write, and execute
    def modify_permissions(self, file_name, readable, writable, executable):
        try:
            mode = 0
            if readable:
                mode |= 0o444  # Add read permissions
            if writable:
                mode |= 0o222  # Add write permissions
            if executable:
                mode |= 0o111  # Add execute permissions
            os.chmod(file_name, mode)
            print(f"Permissions set for '{file_name}': Readable={readable}, Writable={writable}, Executable={executable}")
        except FileNotFoundError:
            print(f"Error: File '{file_name}' does not exist.")
        except Exception as e:
            print(f"Error changing permissions for '{file_name}': {e}")