import sqlite3
db = sqlite3.connect('database.db')
c = db.cursor()
def table():
    c.execute('CREATE TABLE IF NOT EXISTS Data (Name text, Age int, Sex text )')
def Data_entery():
    a = str(raw_input('Name: '))
    b = int(raw_input('Age: '))
    d = str(raw_input('sex: '))
    c.execute('INSERT INTO Data (Name, Age, Sex) VALUES (?, ?, ?)', (a, b, d))
    db.commit()
def read_db():
    c.execute('SELECT * FROM Data')
    for row in c.fetchall():
        print(row)

def filter_row():
    Z = str(raw_input('Enter the Name: '))
    c.execute("SELECT NAme FROM Data WHERE Name = '(?)'", Z)
    for row in c.fetchall():
        print(row)

def update_row():
    c.execute("Update Data Set")
    for row in c.fetchall():
         print(row)
def delete_row():
    c.execute("DELETE FROM Data Where Name='Peta'")
    for row in c.fetchall():
        print(row)
def get_all_tables(self):
        c.execute('SHOW TABLES')
        r = c.fetchall()
        return r
#table()
#Data_entery()
#read_db()
Filter_db()