import os
class FileManager(object):
    def __init__(self,directory):
        self.homeDir = directory
        pass
    def getAllFiles(self):

        dirs = os.listdir(self.homeDir)

        return dirs
    def getAllFolders(self):
        dirs = os.listdir(self.homeDir)
        return dirs

flm = FileManager("C:\Users\Amanuel\Desktop\New folder2")
print flm.getAllFolders()
