#Hueland Hunter ID-2006702

import os
import stat

class PermissionManager:
    def modify_permissions(self, file_name, readable, writable, executable):
        if not isinstance(readable, bool) or not isinstance(writable, bool) or not isinstance(executable, bool):
            print("Error: Readable, writable, and executable must be boolean values.")
            return
        
        try:
            if not os.path.exists(file_name):
                print(f"Error: File '{file_name}' does not exist.")
                return

            mode = 0
            if readable:
                mode |= stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH  # Add read permissions for user, group, others
            if writable:
                mode |= stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH  # Add write permissions for user, group, others
            if executable:
                mode |= stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH  # Add execute permissions for user, group, others
                
            os.chmod(file_name, mode)
            print(f"Permissions set for '{file_name}': Readable={readable}, Writable={writable}, Executable={executable}")
        except FileNotFoundError:
            print(f"Error: File '{file_name}' does not exist.")
        except PermissionError:
            print(f"Error: Permission denied for file '{file_name}'.")
        except Exception as e:
            print(f"Error changing permissions for '{file_name}': {e}")
