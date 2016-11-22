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
        print ("database connected succesfully")
        global cursor
        cursor=db.cursor()

    def create_table(self,table_name,atr1,atr2,atr3):
        self.table_name=table_name
        self.atr1=atr1
        self.atr2=atr2
        self.atr3=atr3
        sql_query = "CREATE TABLE  " + self.table_name + "(" + self.atr1 + " TEXT, " + self.atr2 + " INT, " + self.atr3 + " TEXT)"
        # print sql_query
        cursor.execute(sql_query)
        db.commit()
    def Insert_datas(self,table_name,d1,d2,d3):
        self.table_name=table_name
        # self.atr1 = atr1
        # self.atr2 = atr2
        # self.atr3 = atr3
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        try:
            sql_query = "INSERT INTO  %s VALUES ('%s','%s','%s')" % (self.table_name,self.d1,self.d2,self.d3)
            cursor.execute(sql_query)
            db.commit()
            print "datas inserted Successfully"
        except Exception as e:
            print "datas are not Inserted"
    def get_all_tables(self):
        # self.db_name=db_name
        sql_query = "SHOW TABLES"
        cursor.execute(sql_query)
        r=cursor.fetchall()
        return  r
    def get_all_rows(self,table_name):
        self.table_name=table_name

        sql_query= "SELECT * FROM %s " % (self.table_name)
        cursor.execute(sql_query)

        row=cursor.fetchall()
        return row
    def get_single_row(self,table_name,row_id):
        self.table_name = table_name
        self.row_id = row_id
        sql_query = "SELECT * FROM %s WHERE id='%s'" % (self.table_name,row_id)
        cursor.execute(sql_query)

        row = cursor.fetchall()
        return row
    def edit_row(self,table_name,data_tobe_inserted,id):
        self.table_name=table_name
        self.data=data_tobe_inserted
        self.id=id
        sql_query = "UPDATE %s SET %s WHERE %s" %(self.table_name,self.data,self.id)
        cursor.execute(sql_query)
        db.commit()
        print "data updated Successfully"
    def delet_row(self,table_name,id):
        self.table_name=table_name
        self.id=id
        sql_query = "DELETE FROM %s WHERE %s" % (self.table_name,self.id)
        cursor.execute(sql_query)
        db.commit()
        print "row successfully deleted"








obj=database('localhost','root','','python')
obj.create_table('student','name','id','department')
# obj.Insert_datas('student','Boaz','98','Electrical')
# print obj.get_all_tables()
# print obj.get_all_rows('STUDENT')
# print obj.get_single_row('STUDENT','98')
# obj.edit_row('STUDENT','id=120','id=98')
# obj.delet_row('STUDENT','id=99')


