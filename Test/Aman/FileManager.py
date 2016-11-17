import os,fnmatch

class FileManager(object):

     def __init__(self,directory):
         self.givendir=directory
         os.chdir(self.givendir)
         pass
     def All_folders(self):

         dirs= filter(os.path.isdir, os.listdir(self.givendir))
         return dirs

     def All_files(self):

         global files
         files= filter(os.path.isfile, os.listdir(self.givendir))
         return files
     def get_Full_Path(self,fname):
         self.fname=fname

         for path,dir,file in os.walk(self.givendir):
              for f in file:
                  name=self.fname
                  if name==f:
                      repath = os.path.abspath(os.path.join(path, self.fname))

                      print "Path  of a file named %s :- %s" %(f,repath)
                  # elif fnama==f:
                  #     print "There is no a file named %s"%(f)
     def path(self,fname):
         self.fname=fname
         name=self.fname
         # file=[]
         # file.extend(files)
         for f in files:
             if name==f:
                 return "path of the file  :-%s"%(os.path.join(self.givendir,name))
         if name!=f:
                 return "There is no a file named %s in this directory " %name






obj=FileManager("D:\Books")


print obj.All_folders()
print obj.All_files()
print obj.get_Full_Path("Let Us Pray.pdf")
print obj.path("Let Us Pray.pdf")

