'''This Antivirus Created By Dr.Nick_Z (Manish Parihar)
    In This Antivirus DataBase Is used By Anic.'''

import hashlib
import os

#Global Variable
malware_hashes = list(open("DataBase\\HashDataBase\\Sha256\\virusHash.unibit","r").read().split('\n'))
virusInfo = list(open("DataBase\\HashDataBase\\Sha256\\virusInfo.unibit","r").read().split('\n'))


#Get Hash Of File
def sha256_hash(filename):
    try:
        with open(filename,"rb") as f:
            bytes = f.read()
            sha256hash = hashlib.sha256(bytes).hexdigest()

            f.close()
        # print(sha256hash)
        return sha256hash
    except:
        return 0
    
#Malware Dectection By Hash
def malware_checker(pathOfFile):
    global malware_hashes
    global virusInfo
    
    hash_malware_check = sha256_hash(pathOfFile)
    counter = 0


    for i in malware_hashes:
        if i == hash_malware_check:
            return virusInfo[counter]
        counter += 1

    return 0


#Malware Dectection In Folder
virusName = []
virusPath = []

def virusScanner(path):

    # Get the list of all files in directory tree at given path
    dir_list = list()
    for (dirpath, dirnames, filenames) in os.walk(path):
        dir_list += [os.path.join(dirpath, file) for file in filenames]

    for i in dir_list:
        if malware_checker(i) != 0:
            print(i)
            virusName.append(malware_checker(i)+" :: File :: "+i)
            virusPath.append(i)


# Virus Remover
def virusRemover(path):
    virusScanner(path)
    if virusPath:
        for i in virusPath:
            os.remove(i)
    else:
        return 0
 


def juckFileRemover():

    # Temp Files Remover

    temp_list = list()

    # Windows username

    username = os.environ.get('USERNAME').upper().split(" ")

    for (dirpath, dirnames, filenames) in os.walk("C:\\Windows\\Temp"):
        temp_list += [os.path.join(dirpath, file) for file in filenames]
        temp_list += [os.path.join(dirpath, file) for file in dirnames]

    for (dirpath, dirnames, filenames) in os.walk("C:\\Users\\{}~1\\AppData\\Local\\Temp".format(username[0])):
        temp_list += [os.path.join(dirpath, file) for file in filenames]
        temp_list += [os.path.join(dirpath, file) for file in dirnames]
        

    for (dirpath, dirnames, filenames) in os.walk("C:\\Windows\\Prefetch"):
        temp_list += [os.path.join(dirpath, file) for file in filenames]
        temp_list += [os.path.join(dirpath, file) for file in dirnames]


    if temp_list:
        
            for i in temp_list:
                print(i)

                try:
                    os.remove(i)

                except:
                    pass

                try:
                    os.rmdir(i)

                except:
                    pass
        
        

    else:
        return 0


def ramBooster():

    taskList = ["notepad.exe","chrome.exe","AnyDesk.exe","TeamViewer_Service.exe","msedge.exe","cmd.exe"
                ,"IDMan.exe",]

    # Task Kill

    for i in taskList:

            os.system("taskkill /f /im  {}".format(i))



def FlowDetectorIo(path,bit_size):

    with open("DataBase\\Flow Detection\\flow_exe.unibit", "r") as rFile:
        io = rFile.readlines()
        rFile.close()

    with open(path, "rb") as rFile:
        nj = list(rFile.read())
        rFile.close()

    njStr = ''

    for i in nj:
        njStr += str(i)

    bX = 0

    for f in io:
        for i in range(0, len(f), bit_size):
            if njStr.find(f[i:i+bit_size]) != -1:
                bX += 1

        if flen := len(f)/bit_size:
            prLen = (bX/flen)*100

    return prLen

print(FlowDetectorIo("keylogger\\17augs.exe",4))