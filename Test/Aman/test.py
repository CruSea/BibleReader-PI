import os

class FileManager(object):
     def __init__(self,directory):
         self.givendir=directory
         os.chdir(self.givendir)
         pass
     def All_folders(self):

        dirs= filter(os.path.isdir, os.listdir(self.givendir))
        print dirs

     def All_files(self):
         dirs = filter(os.path.isfile, os.listdir(self.givendir))
         print dirs
obj=FileManager("D:\Books")

print obj.All_folders()
print obj.All_files()