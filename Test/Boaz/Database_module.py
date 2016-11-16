import MySQLdb
import sys
class database(object):
    def __init__(self, host, user, passwrd, dbname):
        self.host = host
        self.user = user
        self.passwrd = passwrd
        self.dbname = dbname
        try:
            global db
            db = MySQLdb.connect(
                host = self.host,
                user = self.user,
                passwd = self.passwrd,
                db = self.dbname,
            )
            print("connected susesfully")
            global cursor
            cursor = db.cursor()
        except Exception as e:
            sys.exit("There is no database by the name " + self.dbname)

    def create_table(self, table_name, sname):
        self.table_name = table_name
        at = []
        for n in sname.split(":"):
            at.append(n)
        while at.__len__():
            pass

        # sql_query = "CREATE TABLE IF NOT EXISTS "+self.table_name+"("+self.at1+" INT, "+self.at2+" TEXT, "+self.at3+" TEXT)"
        # print sql_query
        # cursor.execute(sql_query)
        # cursor.execute("CREATE TABLE IF NOT EXISTS %s (%s INT, %s TEXT, %s TEXT)", (self.table_name), (self.at1, self.at2, self.at3))
        db.commit()
    def insert_data(self, table_name, at1, at2, at3, d1, d2, d3):
        self.table_name = table_name
        self.at1 = at1
        self.at2 = at2
        self.at3 = at3
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        cursor.execute("INSERT INTO %s(%s, %s, %s) VALUES ((%s), (%s), (%s))",
                       self.table_name (self.at1, self.at2, self.at3,), (self.d1, self.d2, self.d3,))
        db.commit()
    def get_single_row(self, table_name, at, value):
        self.table_name = table_name
        self.at = at
        self.value = value
        cursor.execute("SELECT * FROM %s WHERE (%s) = (%s)", self.table_name (self.at) (self.value))
        rsult = cursor.fetchall()
        return rsult
    def select_all_tables(self):
        cursor.execute("SHOW TABLES")
        t = cursor.fetchall()
        return t
    def delete_row(self, table_name, at, value):
        self.table_name = table_name
        self.at = at
        self.value = value
        sql_query = "DELETE * FROM "+self.table_name+" WHERE "+self.at+" = "+self.value
        print sql_query
        # cursor.execute(sql_query)
        db.commit()
        # cursor.execute("DELETE * FROM %s WHERE %s = %s", self.table_name, self.at, self.value)
        # db.commit()

if __name__ == '__main__':
    obj = database('localhost', 'root', '', 'python')
    obj.create_table('he','we:hill:f:gill:bot:M:jesus:is:lord:for:god:so:love:the:world')
    # obj.insert_data('she','id', 'name', 'sex', '1', 'boaz', 'm')
    # print obj.get_single_row('she','id', '1')
    # print obj.select_all_tables()
    # obj.delete_row('she', 'id', '1')