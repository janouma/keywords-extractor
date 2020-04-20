import jwt
from lib.constants import JWT_SECRET_FILE, PASSWORD_FILE, ALGORITHM
from uuid import uuid4

API_KEY_FILE = '.api_key'

secret = str(uuid4())
password = str(uuid4())

with open(JWT_SECRET_FILE, 'w') as jwt_secret_file:
    jwt_secret_file.write(secret)

with open(PASSWORD_FILE, 'w') as password_file:
    password_file.write(password)

api_key = jwt.encode({
    'password': password}, secret,
    algorithm=ALGORITHM
).decode()

with open(API_KEY_FILE, 'w') as api_key_file:
    api_key_file.write(api_key)

print(api_key)
