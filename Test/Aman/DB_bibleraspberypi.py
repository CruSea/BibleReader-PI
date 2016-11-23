import MySQLdb
import DB_Module


class db_bible(object):
    def __init__(self, host, user, password, db_name):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name

        global db
        db = MySQLdb.connect(
            host=self.host,
            user=self.user,
            passwd=self.password,
            db=self.db_name

        )
        print ("database connected succesfully")
        global cursor
        cursor = db.cursor()

    def get_All_Testaments(self):
        cursor.execute("SELECT * FROM TESTAMENT")
        testaments = []
        found = cursor.fetchall()
        # print cursor.description
        print "Testaments in the Bible"
        # print found
        for items in found:
            hydrate_testaments = DB_Module.Testament()
            hydrate_testaments.hydrate(items)
            testaments.append(hydrate_testaments)
        return testaments


    def get_All_Books(self, Testament_Id):
        self.Testament_Id = Testament_Id
        cursor.execute( "SELECT * FROM BOOK WHERE id in(SELECT BOOK FROM CONTENT WHERE TESTAMENT='%s' and id in(SELECT CONTENTID FROM FILE))" % self.Testament_Id)
        found = cursor.fetchall()
        books=[]
        print "Books in the tetameent "
        for items in found:
            hydrate_books= DB_Module.Book()
            hydrate_books.hydrate(items)
            books.append(hydrate_books)
        return books

    def get_All_Chapters(self, Book_Id):
        self.Book_Id = Book_Id
        cursor.execute("SELECT CHAPTER FROM CONTENT WHERE BOOK='%s' " % self.Book_Id)
        found = cursor.fetchall()
        chapters=[]
        print "Chapters in the book"
        for items in found:
            hydrate_chapter=DB_Module.Content()
            hydrate_chapter.hydrate(items)
            chapters.append(hydrate_chapter)
        return chapters


    def get_Content_Id(self, book_id, chapter_id):
        self.book_id = book_id
        self.chapter_id = chapter_id
        cursor.execute( "SELECT ID FROM CONTENT WHERE BOOK='%s' AND CHAPTER='%s'" % (self.book_id, self.chapter_id))
        found = cursor.fetchall()
        content_id=[]
        print "The Id of the content"

        hydrate_content_id = DB_Module.Content()
        hydrate_content_id.ID = found
        content_id.append(hydrate_content_id)

        return content_id

    def get_Verse(self, Content_Id, Number):
        self.Content_Id = Content_Id
        self.number = Number
        cursor.execute("SELECT * FROM verse WHERE contentID='%s' AND NUMBER='%s'" % (self.Content_Id, self.number))
        found = cursor.fetchall()
        verse = []
        print "Verse table Entry"

        for items in found:
            hydrate_verse = DB_Module.Verse()
            hydrate_verse.hydrate(items)
            verse.append(hydrate_verse)
        return verse



    def get_Verses(self, contentt_id, start_number, end_number):
        self.contentt_id = contentt_id
        self.start_number = start_number
        self.end_number = end_number
        v=[]
        verse=[]
        x=int(self.start_number)
        y=int(self.end_number)

        for x in range(x,y+1):
            cursor.execute("SELECT * FROM VERSE WHERE CONTENTID='%s' AND NUMBER='%s'" %
                       (self.contentt_id, x))
            found=cursor.fetchone()
            v.append(found)



        print "---------Verse-------------"
       
        for items in v:
            hydrate_verses = DB_Module.Verse()
            hydrate_verses.hydrate(items)
            verse.append(hydrate_verses)
        return verse

    def get_File(self, content_id, number):
        self.content_id = content_id
        self.number = number
        cursor.execute ("SELECT * FROM FILE WHERE CONTENTID='%s' AND id in(SELECT CONTENTID FROM VERSE WHERE NUMBER='%s')" % (self.content_id, self.number))
        found = cursor.fetchall()
        files=[]
        print "File table Entry"
        for items in found:
            hydrate_file= DB_Module.File()
            hydrate_file.hydrate(items)
            files.append(hydrate_file)
        return files





obj = db_bible('localhost', 'root', '', 'bibleraspberypi')
# print obj.get_All_Testaments()
# print obj.get_All_Books('1')
# print obj.get_all_chapters('2')
# print obj.get_Content_Id('1', '1')
# print obj.get_Verse('1','2')[0].StartSec
print obj.get_Verses('1', '1', '3') [2].StartSec
# print obj.get_File('1', '1')[0].FileName
