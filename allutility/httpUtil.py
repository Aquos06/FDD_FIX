# -*- coding: utf-8 -*-

import sys, traceback, requests, json, socket
import urllib.parse
import base64
import time

def get(url, params=None, token=None):
  if(url is not None):
    print(url)
    reqUrl = url
    if(params is not None):
      print(params)
      subStr = ''
      if(type(params) is str):
        subStr += params
        if(subStr.find('?')):
          subStr = subStr.replace('?', '')
      elif(type(params) is dict):
        if(len(params)>0):
          for key in params.keys():
            if(subStr == ''):
              subStr = urllib.parse.quote(key) + '=' + urllib.parse.quote(params.get(key))
            else:
              subStr += '&' + urllib.parse.quote(key) + '=' + urllib.parse.quote(params.get(key))
      if(subStr != ''):
        if(reqUrl.find('?')>-1):
          reqUrl += '&' + subStr
        else:
          reqUrl += '?' + subStr
    headers = {"cache-control": "no-cache"}
    if(token is not None):
      headers['Authorization'] = 'Bearer ' + token
    print(reqUrl)
    print(headers)
    try:
      response = requests.get(reqUrl, headers=headers)
      resStatus = response.status_code
      print(resStatus)
      response.raise_for_status()
    except requests.exceptions.HTTPError as err:
      #print(err)
      error_class = err.__class__.__name__ #取得錯誤類型
      detail = err.args[0] #取得詳細內容
      cl, exc, tb = sys.exc_info() #取得Call Stack
      lastCallStack = traceback.extract_tb(tb)[0] #取得Call Stack的最後一筆資料
      fileName = lastCallStack[0] #取得發生的檔案名稱
      lineNum = lastCallStack[1] #取得發生的行號
      funcName = lastCallStack[2] #取得發生的函數名稱
      errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
      print(errMsg)
      #response.raise_for_status()
    resText = response.text
    resText = resText.strip()
    if(resText.startswith('{') and resText.endswith('}')):
      resJson = response.json()
      print(resJson)
      return resJson
    else:
      print(resText)
      return resText

def post(url, params, contentType='application/json', token=None):
  if(url is None or len(url.strip())==0 or params is None or (contentType is not None and len(contentType.strip())==0)):
    print('post(url:({}), params:({}), contentType:({})) fail! Please check input!!!'.format(url, params, contentType))
    return
  if(contentType is None or len(contentType.strip())==0):
    contentType = 'application/json'
  data = ''
  if(type(params) is str):
    data = params
  elif(type(params) is dict):
    data = json.dumps(params)
  else:
    print('Please check params({})'.format(params))
    return
  headers = {"cache-control": "no-cache", "Content-Type": contentType}
  if(token is not None):
    headers['Authorization'] = 'Bearer ' + token
  # print(url)
  # print(data)
  # print(headers)
  try:
    response = requests.post(url, data=data, headers=headers)
    resStatus = response.status_code
    print(resStatus)
    response.raise_for_status()
    return resStatus
  except requests.exceptions.HTTPError as err:
    error_class = err.__class__.__name__ #取得錯誤類型
    detail = err.args[0] #取得詳細內容
    cl, exc, tb = sys.exc_info() #取得Call Stack
    lastCallStack = traceback.extract_tb(tb)[0] #取得Call Stack的最後一筆資料
    fileName = lastCallStack[0] #取得發生的檔案名稱
    lineNum = lastCallStack[1] #取得發生的行號
    funcName = lastCallStack[2] #取得發生的函數名稱
    errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
    print(errMsg)
  resText = response.text
  resText = resText.strip()
  if(resText.startswith('{') and resText.endswith('}')):
    resJson = response.json()
    print(resJson)
    return resJson
  else:
    print(resText)
    return resText

def put(url, params, contentType='application/json', token=None):
  if(url is None or len(url.strip())==0 or params is None or (contentType is not None and len(contentType.strip())==0)):
    print('put(url:({}), params:({}), contentType:({})) fail! Please check input!!!'.format(url, params, contentType))
    return
  if(contentType is None or len(contentType.strip())==0):
    contentType = 'application/json'
  data = ''
  if(type(params) is str):
    data = params
  elif(type(params) is dict):
    data = json.dumps(params)
  else:
    print('Please check params({})'.format(params))
    return
  headers = {"cache-control": "no-cache", "Content-Type": contentType}
  if(token is not None):
    headers['Authorization'] = 'Bearer ' + token
  print(url)
  print(data)
  print(headers)
  try:
    response = requests.put(url, data=data, headers=headers)
    resStatus = response.status_code
    print(resStatus)
    response.raise_for_status()
  except requests.exceptions.HTTPError as err:
    error_class = err.__class__.__name__ #取得錯誤類型
    detail = err.args[0] #取得詳細內容
    cl, exc, tb = sys.exc_info() #取得Call Stack
    lastCallStack = traceback.extract_tb(tb)[0] #取得Call Stack的最後一筆資料
    fileName = lastCallStack[0] #取得發生的檔案名稱
    lineNum = lastCallStack[1] #取得發生的行號
    funcName = lastCallStack[2] #取得發生的函數名稱
    errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
    print(errMsg)
  resText = response.text
  resText = resText.strip()
  if(resText.startswith('{') and resText.endswith('}')):
    resJson = response.json()
    print(resJson)
    return resJson
  else:
    print(resText)
    return resText

def getIpAddr(defaultIP='192.168.0.99'):
  st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  try:
    st.connect(('192.168.255.255',1))
    IP = st.getsockname()[0]
  except Exception:
    IP = defaultIP
  finally:
    st.close()
  return IP

#SERVER_GIVE_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiZmFjZWFpIl0sInNjb3BlIjpbImFwaS1zZXJ2aWNlIl0sImV4cCI6MTkyMTE1MzI1OCwiYXV0aG9yaXRpZXMiOlsiYWl1bmlvbiJdLCJqdGkiOiI3ODI3YTBkYi0zMGQ3LTRhODItYjQyYy0yMTQ0NTMyZWRlNDEiLCJjbGllbnRfaWQiOiJhcGktY2xpZW50In0.mE8WnaGzVuWhS5LfT0ajQcBr_JP2TUOVfhch-5dJ6mA'

# GET DEVICE SETTINGS
#get('http://192.168.0.107/devices', 'deviceType=aibox&sourceUrl='+getIpAddr('192.168.0.99'), SERVER_GIVE_TOKEN)
# {'total': 1, 'code': 200, 'result': [{'id': 137, 'last_seen': None, 'source_url': '192.168.0.99', 'enabled': True, 'rtc_enabled': True, 'name': '99', 'device_type': 'aibox', 'category': {'id': 17, 'name': '二樓辦公室', 'enabled': True}, 'identity': '', 'username': 'admin', 'password': 'ai123456', 'temperature_threshold': 0.0, 'processed_by': None, 'min_threshold': 50.0, 'max_threshold': 77.0, 'punch': False, 'settings': {'camera': [{'ip': '192.168.0.100', 'title': 'ipcamera1', 'username': 'root', 'password': 'root', 'sourceUrl': 'rtsp://root:root@192.168.0.100'}, {'ip': '192.168.0.101', 'title': 'ipcamera2', 'username': 'admin', 'password': 'ai123456', 'sourceUrl': 'rtsp://admin:ai123456@192.168.0.101'}]}}], 'page_size': 100, 'page': 1}
# (code=0 or code=200) and total==1 ==>
# result.settings.camera[0] {'ip': '192.168.0.100', 'title': 'ipcamera1', 'username': 'root', 'password': 'root', 'sourceUrl': 'rtsp://root:root@192.168.0.100'}

# UPDATE DEVICE SETTINGS
#putData = {'id': 137, 'last_seen': None, 'source_url': '192.168.0.21', 'enabled': True, 'rtc_enabled': True, 'name': '99', 'device_type': 'aibox', 'category': {'id': 17, 'name': '二樓辦公室', 'enabled': True}, 'identity': '', 'username': 'admin', 'password': 'ai123456', 'temperature_threshold': 0.0, 'processed_by': None, 'min_threshold': 50.0, 'max_threshold': 77.0, 'punch': False, 'settings': {'camera': [{'ip': '192.168.0.21', 'title': 'ipcamera1', 'username': 'admin', 'password': 'ai123456', 'sourceUrl': 'rtsp://admin:ai123456@192.168.0.21', 'active': on}, {'ip': '192.168.0.111', 'title': 'ipcamera2', 'username': 'admin', 'password': 'ai123456', 'sourceUrl': 'rtsp://admin:ai123456@192.168.0.111'}]}}
#put('http://192.168.0.107/api/v2/devices/137',json.dumps(putData),None, SERVER_GIVE_TOKEN)

# ADD FALL DOWN EVENT
#with open("/home/faceai/Desktop/1.jpg", "rb") as img_file:
#    b64_string = base64.b64encode(img_file.read())    
#with open("/home/faceai/Desktop/2.jpg", "rb") as img_file:
#    b64_string2 = base64.b64encode(img_file.read())
  
#data = { 'deviceId': 137, 'cid': 0, 'captured_at': round(time.time() * 1000.0), 'type': 'falldown', 'photo': b64_string.decode('utf-8'), 'background': b64_string2.decode('utf-8') }
#post('http://192.168.0.107/api/v2/captures/fallDown',data, None, SERVER_GIVE_TOKEN)



