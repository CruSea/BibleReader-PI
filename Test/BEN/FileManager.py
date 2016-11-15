import os
class FileManager(object):
    def __init__(self,directory):
        self.homeDir = directory
        os.chdir(self.homeDir)
    def getAllFiles(self):
        dirs= filter(os.path.isfile, os.listdir(self.homeDir))
        return dirs
    def getAllFolders(self):
        dirs= filter(os.path.isdir, os.listdir(self.homeDir))
        return dirs

flm = FileManager("c:\\")
data = flm.getAllFolders()
print data
