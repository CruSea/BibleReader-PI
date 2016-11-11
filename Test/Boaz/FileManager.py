import os
class FileManager(object):
    def __init__(self, directory):
        self.homeDir = directory
        os.chdir(self.homeDir)
        pass

    def getAllFiles(self):

        dirs = os.listdir(self.homeDir)
        folderlist = []
        for r in dirs:
            if (os.path.isfile(r)):
                folderlist.append(r)
        print folderlist

    def getAllFolders(self):
        dirs = os.listdir(self.homeDir)
        folderlist = []
        for x in dirs:
            if (os.path.isdir(x)):
                folderlist.append(x)
        print folderlist


if __name__ == '__main__':
    flm = FileManager("E:/phtonn/work");
    print flm.getAllFolders()
    print flm.getAllFiles()


