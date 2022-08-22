'''This Antivirus Created By Dr.Nick_Z (Manish Parihar)
    In This Antivirus Sha256 DataBase Is used By Anic.
    Md5 DataBase Organized By Dr. Nick_Z (Manish Parihar)'''

from hashlib import md5
from operator import le
import time
import os
start = time.time()


class Engine:

    def __init__(self, typeH):
        if typeH.lower() == "sha256":
            with open("DataBase\\HashDataBase\\Sha256\\virusHash.unibit", "r") as i:
                self.hashList = i.readlines()
                i.close()

        if typeH.lower() == "md5":
            with open("DataBase\\HashDataBase\\Md5\\md5HashOfVirus.unibit", "r") as i:
                self.hashList = i.readlines()
                i.close()

    def hashToFullNum(self, hash):

        alpha = 'abcdefghijklmnopqrstuvwxyz'
        alphaNum = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
                    'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
                    'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

        j = ''

        sampleHash = hash.lower()

        for i in sampleHash:
            if i in alpha:
                i = alphaNum[i]

            j = j + str(i)

        return int(j)

    def binaryTreeSearch(self, hList, valueToFind):
        initialValue = 0
        lenghtOfList = len(hList) - 1
        pointFound = 0

        while (initialValue < lenghtOfList and pointFound == 0):
            middle = (initialValue + lenghtOfList) // 2

            if hList[middle] == valueToFind:
                pointFound = 1
                positionOfPoint = middle

            if hList[middle] > valueToFind:
                lenghtOfList = middle

            if hList[middle] < valueToFind:
                initialValue = middle + 1

        if pointFound == 1:
            return positionOfPoint

        else:
            return None

    def sha256_hash(self, filename):
        import hashlib
        try:
            with open(filename, "rb") as f:
                bytes = f.read()
                sha256hash = hashlib.sha256(bytes).hexdigest()

                f.close()
            return sha256hash
        except:
            return 0

    def Md5_hash(self, filename):
        import hashlib
        try:
            with open(filename, "rb") as f:
                bytes = f.read()
                md5Hash = hashlib.md5(bytes).hexdigest()

                f.close()
            return md5Hash
        except:
            return 0

    def virusScannerSha256(self, path):
        import os

        self.virusPath = []
        self.virusHashCyPy = []

        ioList = []

        for i in self.hashList:
            ioList.append(self.hashToFullNum(i))

        ioList.sort()

        # Get the list of all files in directory tree at given path
        dir_list = list()
        for (dirpath, dirnames, filenames) in os.walk(path):
            dir_list += [os.path.join(dirpath, file) for file in filenames]

        for i in dir_list:
            try:
                vIHash = self.binaryTreeSearch(
                    ioList, self.hashToFullNum(self.sha256_hash(i)))
                print(i)
                if vIHash:
                    self.virusHashCyPy.append(vIHash)
                    self.virusPath.append(i)

            except:
                pass

        return self.virusHashCyPy, self.virusPath

    def virusScannerMd5(self, path):
        import os

        self.virusPath = []
        self.virusHashCyPy = []

        ioList = []

        for i in self.hashList:
            ioList.append(self.hashToFullNum(i))

        ioList.sort()

        # Get the list of all files in directory tree at given path
        dir_list = list()
        for (dirpath, dirnames, filenames) in os.walk(path):
            dir_list += [os.path.join(dirpath, file) for file in filenames]

        for i in dir_list:
            try:
                vIHash = self.binaryTreeSearch(
                    ioList, self.hashToFullNum(self.Md5_hash(i)))
                print(i)
                if vIHash:
                    self.virusHashCyPy.append(vIHash)
                    self.virusPath.append(i)

            except:
                pass

        return self.virusHashCyPy, self.virusPath

    def CacheFileRemover(self):

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

    def ramBooster(self):
        pass

    def FlowDetectorIo(self,path,bit_size):

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

    


io = Engine("md5")

end = time.time()
print(end - start)
