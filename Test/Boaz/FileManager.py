import os


class FileManager(object):
    def __init__(self, directory):
        self.homeDir = directory
        os.chdir(self.homeDir)
        pass

    def All_files(self):
        global filess
        filess = filter(os.path.isfile, os.listdir(self.homeDir))
        return filess

    def getAllFolders(self):
        dirs = os.listdir(self.homeDir)
        folderlist = []
        for x in dirs:
            if (os.path.isdir(x)):
                folderlist.append(x)
        return folderlist

    def get_all_Path(self, fnames):
        self.fnames = fnames
        for root, dirs, files in os.walk(self.homeDir):
            for name in files:
                if name == fnames:
                    print os.path.abspath(os.path.join(root, name))

    def path(self, fnames):
        self.fnames = fnames
        for f in filess:
            if fnames == f:
                return "path of the file: %s" % (os.path.join(self.homeDir, fnames))
        if fnames != f:
            return "There is no file by this name!"


if __name__ == '__main__':
    flm = FileManager("E:/phtonn/work");
    print flm.getAllFolders()
    print flm.All_files()
    print flm.get_all_Path('boaz.txt')
    print flm.path('text.txt')
