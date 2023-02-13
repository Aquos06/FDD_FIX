import sqlite3

#making QSQLITE
conn = sqlite3.connect('../fall_database.db')
c = conn.cursor()

c.execute('''
          CREATE TABLE fall
          ([id] INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
          [FileName] TEXT,[Event] TEXT, 
          [DateTime] DATETIME, 
          [channel] INTERGER)
          ''')