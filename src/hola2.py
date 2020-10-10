import hashlib
import os
from  dotenv import load_dotenv


load_dotenv()
message = b'This is a super secret message! do not share'
salt = os.getenv('SALT').encode()
print("salt >", salt)
# salt = b'80th9saon+fyzkyesrv$ov9gash*)48n07jp*5zx%di1j$inod'

hashed_message = hashlib.pbkdf2_hmac('sha256', message, salt, 1000000).hex()
print(hashed_message)
hashed_message = hashlib.pbkdf2_hmac('sha512', message, salt, 1000000).hex()
print(hashed_message)
# unhashed_message = hashlib.pbkdf2_hmac('sha256', message, salt, 10).hex()
# print(unhashed_message)

# salt = input('Type a password: ').encode()

# if unhashed_message == hashed_message:
#     print('The password is correct')
# print(hashed_message)
