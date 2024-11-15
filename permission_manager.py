#Hueland Hunter ID-2006702
#Shamori Henry ID-2100438

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

    # Lists file attributes similar to 'ls -l' in Unix
    def list_attributes(self, file_name):
        try:
            # Retrieve file stats
            file_stats = os.stat(file_name)
            
            # File permissions
            permissions = stat.filemode(file_stats.st_mode)
            
            # File size in bytes
            size = file_stats.st_size
            
            # Last modified time
            last_modified = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(file_stats.st_mtime))
            
            # Display attributes
            print(f"{permissions} {size} bytes Last Modified: {last_modified} {file_name}")
        
        except FileNotFoundError:
            print(f"Error: File '{file_name}' does not exist.")
        except Exception as e:
            print(f"Error displaying attributes for '{file_name}': {e}")
