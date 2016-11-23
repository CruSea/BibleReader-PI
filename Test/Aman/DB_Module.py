class Testament(object):
    def __init__(self):
        self.ID = None
        self.Name = None
    def hydrate(self, data):
        self.ID = data[0]
        self.Name = data[1]
class Verse(object):
    def __init__(self):
        self.ID = None
        self.ContentID = None
        self.Number = None
        self.StartSec = None
        self.EndSec = None
    def hydrate(self, data):
        self.ID = data[0]
        self.ContentID = data[1]
        self.Number = data[2]
        self.StartSec = data[3]
        self.EndSec = data[4]
class File(object):
    def __init__(self):
        self.ID = None
        self.ContentID = None
        self.Folder = None
        self.FileName = None
    def hydrate(self, data):
        self.ID = data[0]
        self.ContentID = data[1]
        self.Folder = data[2]
        self.FileName = data[3]
class Book(object):
    def __init__(self):
        self.ID = None
        self.Name = None
    def hydrate(self, data):
        self.ID = data[0]
        self.Name = data[1]
class Content(object):
    def __init__(self):
        self.ID = None
        self.Testament = None
        self.Book = None
        self.Chapter = None
    def hydrate(self, data):
        self.ID = data[0]
        self.Testament = data[1]
        self.Book = data[2]
        self.Chapter = data[3]














