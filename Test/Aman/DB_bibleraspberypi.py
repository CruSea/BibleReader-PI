import MySQLdb

class db_bible(object):
    def __init__(self,host,user,password,dbname):
        self.host=host
        self.user=user
        self.password=password
        self.dbname=dbname

        global db
        db =MySQLdb.connect(
            host=self.host,
            user=self.user,
            passwd=self.password,
            db=self.dbname

            )
        print ("database connected succesfully")
        global cursor
        cursor=db.cursor()

    def get_all_testaments(self):
        Sql_query=("SELECT * FROM TESTAMENT")
        cursor.execute(Sql_query)
        testaments=cursor.fetchall()
        print "Testaments in the Bible"
        for x in testaments:
           print x
        # return testaments

    def get_all_books(self,testament_id):
        self.testament_id=testament_id
        sql_query=("SELECT * FROM BOOK WHERE id in(SELECT BOOK FROM CONTENT WHERE TESTAMENT='%s' and id in(SELECT CONTENTID FROM FILE))")%self.testament_id
        cursor.execute(sql_query)
        books = cursor.fetchall()
        print "Books in the tetameent "
        for x in books:
            print x

    def get_all_chapters(self,book_id):
        self.book_id=book_id
        sql_query=("SELECT CHAPTER FROM CONTENT WHERE BOOK='%s' ") % self.book_id
        cursor.execute(sql_query)
        chapters=cursor.fetchall()
        print "Chapters in the book"
        for x in chapters:
            print x

    def get_content_id(self,book_id,chapter_id):
        self.book_id=book_id
        self.chapter_id=chapter_id
        sql_query=("SELECT ID FROM CONTENT WHERE BOOK='%s' AND CHAPTER='%s'") % (self.book_id,self.chapter_id)
        cursor.execute(sql_query)
        content_id=cursor.fetchall()
        # c=int(content_id)
        print "The Id of the content"
        return content_id
    def get_verse(self,content_id,number):
        self.content_id=content_id
        self.number=number
        # sql_query=()
        cursor.execute(("SELECT * FROM verse WHERE contentID='%s' AND NUMBER='%s'")% (self.content_id,self.number))
        verse=cursor.fetchall()
        print "Verse table Entry"
        return verse
    def get_verses(self,contentt_id,start_time,end_time):
        self.contentt_id=contentt_id
        self.start_number=start_time
        self.end_number=end_time
        cursor.execute(("SELECT * FROM VERSE WHERE CONTENTID='%s' AND STARTSEC='%s' AND ENDSEC='%s'")%(self.contentt_id,self.start_number,self.end_number))
        verses=cursor.fetchall()
        return verses
    def get_file(self,content_id,number):
        self.content_id=content_id
        self.number=number
        cursor.execute(("SELECT * FROM FILE WHERE CONTENTID='%s' AND id in(SELECT CONTENTID FROM VERSE WHERE NUMBER='%s')")%(self.content_id,self.number))
        files=cursor.fetchall()
        print "File table Entry"
        return files








obj=db_bible('localhost','root','','bibleraspberypi')
obj.get_all_testaments()
obj.get_all_books('1')
obj.get_all_chapters('2')
print obj.get_content_id('1','1')
print obj.get_verse('1','2')
print obj.get_file('1','1')
