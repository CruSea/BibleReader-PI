import MySQLdb
import Module

class db_bible(object):
    def __init__(self,host, user, password, dbname):
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname

        global db
        db =MySQLdb.connect(
            host=self.host,
            user=self.user,
            passwd=self.password,
            db=self.dbname

            )
        print ("database connected succesfully")
        global cursor
        cursor = db.cursor()

    def get_All_Testaments(self):
        cursor.execute("SELECT * FROM TESTAMENT")
        found = cursor.fetchall()
        testaments = []
        for item in found:
            hydrate_testaments = Module.Testament()
            hydrate_testaments.hydrate(item)
            testaments.append(hydrate_testaments)
        return testaments


    def get_All_Books(self, Testament_Id):
        self.Testament_Id = Testament_Id
        sql_query=("SELECT * FROM BOOK WHERE id in(SELECT BOOK FROM CONTENT WHERE TESTAMENT='%s' and id in(SELECT CONTENTID FROM FILE))")\
                  %self.Testament_Id
        cursor.execute(sql_query)
        books = cursor.fetchall()
        book = []
        for items in books:
            hydrate_book = Module.Book()
            hydrate_book.hydrate(items)
            book.append(hydrate_book)
        return book

    def get_All_Chapters(self, Book_id):
        self.Book_id = Book_id
        sql_query=("SELECT CHAPTER FROM CONTENT WHERE BOOK='%s' ") % self.Book_id
        cursor.execute(sql_query)
        chapters = cursor.fetchall()
        hydrate_chapter = Module.Content()
        hydrate_chapter.Chapter = chapters
        return hydrate_chapter

    def get_Content_Id(self, Book_Id, Chapter_Id):
        self.Book_Id = Book_Id
        self.Chapter_Id = Chapter_Id
        sql_query = ("SELECT ID FROM CONTENT WHERE BOOK='%s' AND CHAPTER='%s'") % (self.Book_Id, self.Chapter_Id)
        cursor.execute(sql_query)
        content_id = cursor.fetchall()
        hydrate_content = Module.Content()
        hydrate_content.ID = content_id
        return hydrate_content
    def get_Single_Verse(self, Content_Id, Number):
        self.Content_Id=Content_Id
        self.Number=Number
        cursor.execute(("SELECT * FROM verse WHERE contentID='%s' AND NUMBER='%s'")% (self.Content_Id, self.Number))
        found = cursor.fetchall()
        verse = []
        for items in found:
            hydrate_verse = Module.File()
            hydrate_verse.hydrate(items)
            verse.append(hydrate_verse)
        return verse
    def get_Verses(self, Content_id, Start_Number, End_Number):
        self.Content_id = Content_id
        self.Start_Number = Start_Number
        self.End_Number = End_Number
        verses=[]
        x = int(self.Start_Number)
        y = int(self.End_Number)
        for x in range(x, y+1):
            cursor.execute("SELECT * FROM VERSE WHERE CONTENTID='%s' AND NUMBER='%s'" %
                       (self.Content_id, x))
            found = cursor.fetchone()
            verses.append(found)
        file = []
        for items in verses:
            hydrate_file = Module.File()
            hydrate_file.hydrate(items)
            file.append(hydrate_file)
        return file

    def get_File(self, Content_Id, Number):
        self.Content_Id = Content_Id
        self.Number = Number
        cursor.execute(("SELECT * FROM FILE WHERE CONTENTID='%s' AND id in(SELECT CONTENTID FROM VERSE WHERE NUMBER='%s')")%
                       (self.Content_Id, self.Number))
        found = cursor.fetchall()
        file = []
        for items in found:
            hydrate_file = Module.File()
            hydrate_file.hydrate(items)
            file.append(hydrate_file)
        return file


obj = db_bible('localhost', 'root', '', 'bible_pi')
print obj.get_All_Testaments()
print obj.get_All_Books('1')
print obj.get_All_Chapters('1')
print obj.get_Content_Id('1', '1')
print obj.get_Single_Verse('1', '2')
print obj.get_Verses('1', '1', '3')
print obj.get_File('1', '1')[0].Folder
