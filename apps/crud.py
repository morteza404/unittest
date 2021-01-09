import sqlite3

def db_connection():
    return sqlite3.connect("./apps/test.db")

def create():     
    with db_connection() as db:        
        try:        
            cur = db.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS Student (
                                                  Id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                  Name VARCHAR(20),
                                                  Address VARCHAR(20)
                                                  )
                        """)
            print ("table created successfully")
        except:
            print ("error in operation")
            db.rollback()

def insert(name, address):     
    with db_connection() as db:        
        query="INSERT INTO Student (Name, Address) VALUES(?, ?);"
        try:
            cur=db.cursor()
            cur.execute(query, (name, address))
            db.commit()
            print ("one record added successfully")
        except:
            print ("error in operation")
            db.rollback()

def read(id):    
    with db_connection() as db:        
        query = "SELECT * FROM Student WHERE Id=?;"
        cur = db.cursor()
        cur.execute(query, str(id))
        while True:
            record=cur.fetchone()
            if record == None:
                break
            print (record)

if __name__ == "__main__":
    # create()
    # insert("Alex", "LA")
    read(3)