#Hueland Hunter ID-2006702
#Shamori Henry ID-2100438

class PermissionManager:
    
    # A method is created that modifies file permissions based on boolean flags for read, write, and execute
    def modify_permissions(self, file_name, readable, writable, executable):
        
        try:  # Try block is for handling the exceptions
            mode = 0  # Initialize mode to 0
            
            if readable:  
                mode |= 0o444  # Add read permissions (octal value 444)
                
            if writable:  
                mode |= 0o222  # Add write permissions (octal value 222)
                
            if executable:  
                mode |= 0o111  # Add execute permissions (octal value 111)
                
            os.chmod(file_name, mode)  # Change the file permissions using chmod
            
            # The message is printed when the permissions are successfully set
            print(f"Permissions set for '{file_name}': Readable={readable}, Writable={writable}, Executable={executable}")
            
        except FileNotFoundError: 
            
            # This occurs when the specified file is not found
            print(f"Error: File '{file_name}' does not exist.")  # Printed if FileNotFoundError arises
            
        except Exception as e:  
            
            # Handles unexpected errors that occur while modifying permissions
            print(f"Error changing permissions for '{file_name}': {e}")  # Error message

