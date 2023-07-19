from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long as b2l
with open('privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem', 'r') as f:
    contents = RSA.importKey(f.read())
print(contents.d)