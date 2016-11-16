import os
spath = r"F:\h\New folder (3)"
dirs = next(os.walk(spath))[0]
print ("Dirs = %s" %dirs)
files = next(os.walk(spath))[1]
print ("Files = %s" %files)

class FileManager(object):
    def __init__(self, directory):
        self.homeDir = directory
        os.chdir(self.homeDir)
        pass

    def get_all_Path(self, fnames):
        self.fnames = fnames
        for root, dirs, files in os.walk(self.homeDir):
            for name in files:
                if name == fnames:
                    print os.path.abspath(os.path.join(root, name))

    def path(self, fnames):
        global filess
        filess = filter(os.path.isfile, os.listdir(self.homeDir))
        return filess
        self.fnames = fnames
        for f in filess:
            if fnames == f:
                return "path of the file: %s" % (os.path.join(self.homeDir, fnames))
        if fnames != f:
            return "There is no file by this name!"


if __name__ == '__main__':
    flm = FileManager("F:\h\New folder (3)");
    print flm.get_all_Path('k.txt')
    print flm.path('k.txt')
