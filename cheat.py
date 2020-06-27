try:
 import os, sys, random
 import requests
 from time import sleep
 from telethon.tl.functions.messages import GetHistoryRequest
 from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
 from telethon import TelegramClient, sync, events
 from telethon.errors import SessionPasswordNeededError, FloodWaitError
 from telethon.tl.functions.contacts import BlockRequest
 from telethon.tl.functions.channels import JoinChannelRequest
except:
 os.system("pip install random")
 os.system("pip install telethon")
 
os.system("clear")


k= "\033[1;30m******\033[1;31m*****\033[1;32m*****\033[1;33m*****\033[1;34m******\033[1;35m******\033[1;36m******"
join = input(" \033[1;32mNhập Username Group: \033[1;033m")
a = input(" \033[1;32mNhập Tin Nhắn : \033[1;033m")
print ("\033[0m")
join1 = '@acvtip'
api_id = 1386891
api_hash = 'c6ac9c8d6baa179ff3d360b35fc0e588'

if not os.path.exists("session"):
 os.makedirs("session")

if not os.path.exists("phon.txt"):
 f = open("phon.txt", "w")
 f.write(input("\033[1;32mLần Đầu Chạy Vui Lòng Nhập Số Điện Thoại: \033[1;31m: \033[1;33m"))
 f.close()
 
f = open("phon.txt", "r")

def connect(phone):
    client = TelegramClient('session/'+phone,api_id,api_hash)
    client.connect()
    if not client.is_user_authorized():
        try:
         client.send_code_request(phone)
        except:
         return client
        code = input("\n\033[1;34mNhập Code Đăng Nhập \033[1;31m: \033[1;33m")
        client.sign_in(phone)
        try:
         client.sign_in(code=code)
        except SessionPasswordNeededError:
         f2a = input("\033[1;32mNhập Mã Bảo Vệ \033[1;31m: \033[1;33m")
         client.sign_in(password=f2a)
         
    return client
 
print(k)

for i in f:

  phone = str(i.strip())
  
  client = connect(phone)
  
  sleep (0)
  
  print(" \033[1;33m[P] Số Điện Thoại  :",phone,)
  
  try:
  	client(JoinChannelRequest(join))
  except:
  	print ("\033[1;32m")
  
  try:
  	client.send_message((join), (a))
  except:
  	print (" \033[1;31m[×] Lỗi Không Gửi Được Tin Nhắn")
  print(k)

  client.disconnect()
  continue
  sleep (0)