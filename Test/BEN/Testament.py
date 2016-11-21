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

