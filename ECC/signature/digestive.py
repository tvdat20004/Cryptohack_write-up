import requests
import json 
s = requests.Session()

url = 'https://web.cryptohack.org/digestive/'

def sign(username):
	recv = json.loads(s.get(url + "sign/" + username).text)
	signature = recv["signature"]
	return signature

def verify(msg, signature):
	recv = json.loads(s.get(url + "verify/" + msg + "/" + signature).text)
	return recv

signature = sign('tvdat20004')
msg = '{"admin": false, "username": "admin", "admin": true}' # don't use json.dumps

print(verify(msg,signature))
