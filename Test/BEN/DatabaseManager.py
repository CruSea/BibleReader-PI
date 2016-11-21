import mysql.connector
import Testament as Testament

class DatabaseManager(object):
    def __init__(self,host,user,password,database):
        self.DBHost = host
        self.DBUser = user
        self.DBPass = password
        self.DBName = database
        try:
            self.Conn = mysql.connector.connect(user=self.DBUser,password=self.DBPass,host=self.DBHost,database=self.DBName)
            self.Cursor = self.Conn.cursor()
        except mysql.connector.Error as error:
            print error
            exit()
        pass
    def getAllTestaments(self):
        self.Cursor.execute("SELECT * FROM testament")
        testaments = []
        found = self.Cursor.fetchall()
        for item in found:
            tt = Testament.Testament()
            tt.hydrate(item)
            testaments.append(tt)
        return testaments

    def getAllBooks(self,testamentID):
        pass
    def getAllChapters(self,bookID):
        pass
    def getContentID(self,bookID,chapterID):
        pass
    def getVerse(self,contentID,chapterID):
        pass
    def getVerses(self,contentID,startNum,endNumd):
        pass


mydatabase = DatabaseManager("localhost","ben","passben","BibleRaspberyPI")
print  mydatabase.getAllTestaments()
