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

    def get_all_testaments(self):
        Sql_query = "SELECT * FROM TESTAMENT"
        cursor.execute(Sql_query)
        testaments = cursor.fetchall()
        print "Testaments in the Bible"
        sql = "SHOW COLUMNS FROM testament"
        cursor.execute(sql)
        testaments = []
        found = cursor.fetchall()
        for item in found:
            hydrate_testaments = Module.Testament()
            hydrate_testaments.hydrate(item)
            testaments.append(hydrate_testaments)
        return testaments


    def get_all_books(self, testament_id):
        self.testament_id=testament_id
        sql_query=("SELECT * FROM BOOK WHERE id in(SELECT BOOK FROM CONTENT WHERE TESTAMENT='%s' and id in(SELECT CONTENTID FROM FILE))")\
                  %self.testament_id
        cursor.execute(sql_query)
        book = []
        books = cursor.fetchall()
        for items in books:
            hydrate_book = Module.Book()
            hydrate_book.hydrate(items)
            book.append(hydrate_book)
        return book

    def get_all_chapters(self, book_id):
        self.book_id=book_id
        sql_query=("SELECT CHAPTER FROM CONTENT WHERE BOOK='%s' ") % self.book_id
        cursor.execute(sql_query)
        chapters=cursor.fetchall()
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
        v = []
        cursor.execute(("SELECT * FROM verse WHERE contentID='%s' AND NUMBER='%s'")% (self.Content_Id, self.Number))
        verse = cursor.fetchall()
        for items in verse:
            vv = Module.File()
            vv.hydrate(items)
            v.append(vv)
        return v
    def get_Verses(self, Content_id, Start_Number, End_Number):
        self.Content_id = Content_id
        self.Start_Number = Start_Number
        self.End_Number = End_Number
        cursor.execute(("SELECT * FROM VERSE WHERE contentID='%s' AND NUMBER='%s'")%
                       (self.Content_id, self.Start_Number))
        verses1=cursor.fetchall()

        cursor.execute(("SELECT * FROM VERSE WHERE contentID='%s' AND NUMBER='%s'")%
                       (self.Content_id, self.End_Number))
        verses2=cursor.fetchall()
        return verses1 + verses2
    def get_File(self, Content_Id, Number):
        self.Content_Id = Content_Id
        self.Number = Number
        f = []
        cursor.execute(("SELECT * FROM FILE WHERE CONTENTID='%s' AND id in(SELECT CONTENTID FROM VERSE WHERE NUMBER='%s')")%
                       (self.Content_Id,self.Number))
        files = cursor.fetchall()
        for items in files:
            ff = Module.File()
            ff.hydrate(items)
            f.append(ff)
        return f


obj=db_bible('localhost', 'root', '', 'bible_pi')
# print obj.get_all_testaments()
# print obj.get_all_books('1')
print obj.get_all_chapters('1')
# print obj.get_Content_Id('1', '1')
# print obj.get_Single_Verse('1' ,'2')
# print obj.get_Verses('1', '1', '3x')
# print obj.get_File('1', '1')
