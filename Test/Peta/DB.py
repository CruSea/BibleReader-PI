import MySQLdb

class database(object):
    def __init__(self,host,user,password,dbname):
        self.host=host
        self.user=user
        self.password=password
        self.dbname=dbname

        global db
        db = MySQLdb.connect(
            host=self.host,
            user=self.user,
            passwd=self.password,
            db=self.dbname

            )
        print ("database connected succesfully")
        global cursor
        cursor = db.cursor()
    def getAllTestaments(self):
        cursor.execute('SELECT * FROM testament')
        for row in cursor.fetchall():
            print (row)

    def getAllTestaments_id(self, id):
        if id == 1:
            cursor.execute('SELECT * FROM content WHERE Testament = 1 ')
            print'old Testament'
            for row in cursor.fetchall():
                print (row)
        else:
            cursor.execute('SELECT * FROM content WHERE Testament = 2 ')
            print'New Testament'
            for row in cursor.fetchall():
                print (row)
    def getAllChapters(self, book_id):
        self.book_id = book_id
        cursor.execute("SELECT Chapter FROM CONTENT WHERE Book ='%s' " % (self.book_id))
        for row in cursor.fetchall():
            print (row)
    def getContentID(self, book_id, chapter_id):
        self.book_id = book_id
        self.chapter_id = chapter_id
        cursor.execute("SELECT id FROM CONTENT WHERE BOOK='%s' AND CHAPTER='%s'" % (self.book_id, self.chapter_id))
        g = cursor.fetchall()
        return g
    def getVerse(self, Content_ID,Number):
        self.Content_ID = Content_ID
        self.Number = Number
        cursor.execute("SELECT * FROM verse WHERE ContentID='%s' AND Number='%s'" % (self.Content_ID, self.Number))
        o = cursor.fetchall()
        return o
    def getVerses(self, ContentID, StartNumber, EndNumber):
        self.ContentID = ContentID
        self.StartNumber = StartNumber
        self.EndNumber = EndNumber
        cursor.execute("SELECT * FROM VERSE WHERE ContentID='%s' AND startSec='%s' AND endSec='%s'" %
                       (self.ContentID, self.StartNumber, self.EndNumber))
        f = cursor.fetchall()
        return f

    def getFile(self, content_id, number):
        self.content_id = content_id
        self.number = number
        cursor.execute("SELECT * FROM file WHERE ContentID='%s' AND id in(SELECT ContentID FROM VERSE WHERE NUMBER='%s')" % (self.content_id, self.number))
        f = cursor.fetchall()
        return f


obj = database('localhost', 'root', '', 'bible_reader')

print obj.getAllTestaments()
print obj.getAllTestaments_id(2)
print obj.getAllChapters(2)
print obj.getContentID('1', '2')
print obj.getVerse('1', '2')
print obj.getVerses('1', '1', '4')
print obj.getFile('1', '2')