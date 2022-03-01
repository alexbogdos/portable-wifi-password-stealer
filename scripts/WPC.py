import os, sys, subprocess
import string

# ASSETS
class color:
   CYAN = '\033[96m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# FUNCTIONS
def quitScript():
    input("---------   PRESS ANY KEY TO EXIT   ---------")
    sys.exit()   

# Get current directory name and directory to store the logs
log_folder = os.path.join('\Assets\logs')

# Create log directory if it doesn't  exist
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# os.system('cmd /c "netsh wlan show profile"')  
output = subprocess.getoutput('cmd /c "netsh wlan show profile"')  
print(output) 

profile = str(input(f"{color.BOLD}{color.YELLOW}Profile:{color.END} {color.RED}"))
print(f"{color.END}")

if (profile in ["0", "exit"]):
    quitScript()    
else:
    os.system(f'cmd /c "netsh wlan show profile {profile} key=clear"')  

    file_name = str(f"{profile}.txt")
    out_file = f"{log_folder}\\{file_name}"
    print(out_file)
    command = f'netsh wlan show profile "{profile}" key=clear > "{out_file}"'
    print(command)
    os.system(str(command))

quitScript()