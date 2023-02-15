import sqlite3
import json

#making QSQLITE
conn = sqlite3.connect('../fall_database.db')
c = conn.cursor()

query = "SELECT * FROM fall"
cursor = conn.execute(query)
for data in cursor:
    print(data)

# f = open('../falldown/all_falldown.json','r')
# data = json.load(f)
# f.close()

# for key in data:
#     dateTime = data[key]["date"] + " " + data[key]['time']
#     query = f"""
#     INSERT INTO fall (FileName, Event, DateTime, channel)
#     VALUES ('{key}', '{data[key]['event']}', '{dateTime}', '{data[key]['channel']}')
#     """
#     conn.execute(query)
    
# conn.commit()

# f = open('../falldown/all_falldown2.json','r')
# data = json.load(f)
# f.close()

# for key in data:
#     dateTime = data[key]["date"] + " " + data[key]['time']
#     query = f"""
#     INSERT INTO fall (FileName, Event, DateTime, channel)
#     VALUES ('{key}', '{data[key]['event']}', '{dateTime}', '{data[key]['channel']}')
#     """
#     conn.execute(query)
    
# conn.commit()

# f = open('../falldown/all_falldown3.json','r')
# data = json.load(f)
# f.close()

# for key in data:
#     dateTime = data[key]["date"] + " " + data[key]['time']
#     query = f"""
#     INSERT INTO fall (FileName, Event, DateTime, channel)
#     VALUES ('{key}', '{data[key]['event']}', '{dateTime}', '{data[key]['channel']}')
#     """
#     conn.execute(query)
    
# conn.commit()

# f = open('../falldown/all_falldown4.json','r')
# data = json.load(f)
# f.close()

# for key in data:
#     dateTime = data[key]["date"] + " " + data[key]['time']
#     query = f"""
#     INSERT INTO fall (FileName, Event, DateTime, channel)
#     VALUES ('{key}', '{data[key]['event']}', '{dateTime}', '{data[key]['channel']}')
#     """
#     conn.execute(query)
    
# conn.commit()
