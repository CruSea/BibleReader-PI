import MySQLdb

class database(object):
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
        print ("succesfully connected")
        global cursor
        cursor=db.cursor()

obj = database('localhost', 'root', '', 'testdb')


           # CREATE table
# sql = """CREATE TABLE EMPLOYEE (
#           FIRST_NAME  CHAR(20) NOT NULL,
#           LAST_NAME  CHAR(20),
#           AGE INT,
#           SEX CHAR(1),
#           INCOME FLOAT )"""
#
# cursor.execute(sql)




               # TO Get All rows inside on table
# sql = "SELECT * FROM EMPLOYEE "
# try:
   # Execute the SQL command
   # cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   # results = cursor.fetchall()
   # for row in results:
   #    fname = row[0]
   #    lname = row[1]
   #    age = row[2]
   #    sex = row[3]
   #    income = row[4]
      # Now print fetched result
      # print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
      #        (fname, lname, age, sex, income )
# except:
#    print "Error: unable to fecth data"



              # ADD NEW RECORD.
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# try:
   # cursor.execute(sql)
   # db.commit()
# except:
   # db.rollback()



                    # SELECT SINGLE ROW BY FILTERING

# sql = "SELECT * FROM EMPLOYEE \
#        WHERE INCOME > '%d'" % (3000)
# try:
#    Execute the SQL command
#    cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   # results = cursor.fetchall()
   # for row in results:
   #    fname = row[0]
   #    lname = row[1]
   #    age = row[2]
   #    sex = row[3]
   #    income = row[4]
      # print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
      #        (fname, lname, age, sex, income )
# except:
#    print "Error: unable to fecth data"

          # ADD table
# sql = """CREATE TABLE FOOTBALL (
#           FIRST_NAME  CHAR(20) NOT NULL,
#           LAST_NAME  CHAR(20),
#           AGE INT,
#           SEX CHAR(1),
#           INCOME FLOAT )"""
#
# cursor.execute(sql)
# TO SELECT SINGLE ROW



                   #  EDITE required records

# Prepare SQL query to UPDATE required records
# sql = "UPDATE EMPLOYEE SET AGE = AGE + 1   WHERE SEX = '%c'" % ('M')
# try:
#    Execute the SQL command
#    cursor.execute(sql)
   # Commit your changes in the database
   # db.commit()
# except:
   # Rollback in case there is any error
   # db.rollback()

# prepare a cursor object using cursor() method
# cursor = db.cursor()


                          # to DELETE required records
# sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (25)
# try:
   # Execute the SQL command
   # cursor.execute(sql)
   # Commit your changes in the database
   # db.commit()
# except:
   # Rollback in case there is any error
   # db.rollback()
