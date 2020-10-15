#Import Modules
import os 
import subprocess 
import sys 
import getpass 
  
  
username = input("Enter Username You Want To Delete\n") 
  
try: 
    output = subprocess.run(['userdel', username ]) 
    if output.returncode == 0: 
        print("User deleted!!!") 
  
except: 
    print("Failed to delete the user.") 
    sys.exit(1) 
  
