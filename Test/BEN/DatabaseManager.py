import mysql.connector

class DatabaseManager(object):
    def __init__(self,host,user,password,database):
        self.DBHost = host
        self.DBUser = user
        self.DBPass = password
        self.DBName = database
        try:
            self.Conn = mysql.connector.connect(user=self.DBUser,password=self.DBPass,host=self.DBHost,database=self.DBName)
        except mysql.connector.Error as error:
            print error
            exit()
        pass
    def createTable(self,tableName,tableFields):
        pass
    def addNewEntry(self,tableName,fields):
        pass
    def getEntry(self,tableName,filter):
        pass
    def excuteSQL(self,sql_query):
        pass



mydatabase = DatabaseManager("localhost","ben","passben","DeepLife")
mydatabase.createTable()
