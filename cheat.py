try:
 import os, sys, random
 import requests
 from time import sleep
 from telethon.tl.functions.messages import GetHistoryRequest
 from telethon.tl.functions.messages import ImportChatInviteRequest
 from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
 from telethon import TelegramClient, sync, events
 from telethon.errors import SessionPasswordNeededError, FloodWaitError
 from telethon.tl.functions.contacts import BlockRequest
 from telethon.tl.functions.channels import JoinChannelRequest
except:
 os.system("pip install random")
 os.system("pip install telethon")
 
os.system("clear")
a = input("\033[1;32m Nhập Link Join or Username group : \033[1;33m")
b = input("\033[1;32m Nhập ID or Username Group : \033[1;33m")
t = input("\033[1;32m Nhập Tin Nhắn : \033[1;33m")
k= "\033[1;30m******\033[1;31m*****\033[1;32m*****\033[1;33m*****\033[1;34m******\033[1;35m******\033[1;36m******\033[1;0m"
print(k)
api_id = 1614433
api_hash = '04b7f0e33ff8f18224a6e6d9b686328f'

if not os.path.exists("session"):
 os.makedirs("session")

if not os.path.exists("phone.txt"):
 f = open("phone.txt", "w")
 f.write(input("\033[1;32mLần Đầu Chạy Vui Lòng Nhập Số Điện Thoại: \033[1;31m: \033[1;33m"))
 f.close()
 
f = open("phone.txt", "r")

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
for i in f:

  phone = str(i.strip())
  
  client = connect(phone)
  
  sleep (0)
  print(" \033[1;33m[P] Số Điện Thoại  :",phone,)
  try:
  	client(ImportChatInviteRequest(a))
  except:
  	sleep(0)
  try:
  	client(JoinChannelRequest(a))
  except:
  	sleep(0)
  
  try:
      client.send_message((b), (t))
  except:
  	print("\033[1;31m     ...Không Gửi Được Tin Nhắn...")
  else:
  	print("\033[1;32m    ...Đã Gửi Tin Nhắn Đến Group...")
  print(k)
  client.disconnect()
  continue
  sleep(0)
