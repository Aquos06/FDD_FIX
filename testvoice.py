import json

f = open('config2Channels.json','r')
data = json.load(f)
f.close()
print(data)