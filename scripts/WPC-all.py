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
    sys.exit()
    
def parseProfiles(output):
    stringMatch = "All User Profile     : "
    index = 0
    indexes = []
    while (index != -1):
        index = output.find(stringMatch, index+1)
        if (index != -1):
            indexes.append(index)
    
    _profiles = []
    for i in indexes:
        pr = ""
        j = i + len(stringMatch)
        while  output[j] != "\n":
            pr += output[j]
            j += 1
        _profiles.append(pr)
    return _profiles
    
    

# Get current directory name and directory to store the logs
log_folder = os.path.join('\Assets\logs')

# Create log directory if it doesn't  exist
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# os.system('cmd /c "netsh wlan show profile"')  
output = subprocess.getoutput('cmd /c "netsh wlan show profile"')  
profiles = parseProfiles(output)


for pr in profiles:
    os.system(f'cmd /c "netsh wlan show profile {pr} key=clear"')  

    file_name = str(f"{pr}.txt")
    out_file = f"{log_folder}\\{file_name}"
    print(out_file)
    command = f'netsh wlan show profile "{pr}" key=clear > "{out_file}"'
    os.system(command)
    
quitScript()