from http.server import BaseHTTPRequestHandler
from api import extract_keywords
from pathlib import Path as get_path
import jwt
from jwt.exceptions import InvalidSignatureError
import re
import json
from lib.constants import JWT_SECRET_FILE, PASSWORD_FILE, ALGORITHM

AUTH_TYPE = 'Bearer'
AUTH_FAILED_MSG = 'authentication failed'

root_dir = get_path(__file__).parent / '..'
spaces_pattern = re.compile(r'\s+')

with open(root_dir / JWT_SECRET_FILE, 'r') as jwt_secret_file:
    jwt_secret = jwt_secret_file.read()

with open(root_dir / PASSWORD_FILE, 'r') as password_file:
    password = password_file.read()


def reject(handler_instance, message, code=401):
    handler_instance.send_response(code)
    handler_instance.send_header('Content-type', 'application/json')
    handler_instance.end_headers()

    response_body = json.dumps({'message': message})
    handler_instance.wfile.write(response_body.encode())


class authenticatedHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        authorization = self.headers.get('Authorization')

        if authorization is None:
            reject(handler_instance=self, message='authorization required')
            return

        auth_type, api_key = spaces_pattern.split(authorization)

        if auth_type != AUTH_TYPE:
            reject(
                handler_instance=self,
                message='wrong authorization type "' + auth_type +
                '", "' + AUTH_TYPE + '" was expected'
            )
            return

        try:
            payload = jwt.decode(api_key, jwt_secret, algorithms=[ALGORITHM])
        except InvalidSignatureError:
            reject(handler_instance=self, message=AUTH_FAILED_MSG)
            return
        except Exception as error:
            print('Unexpected error:\n{0}'.format(error))

            reject(
                handler_instance=self,
                message=AUTH_FAILED_MSG,
                code=500
            )

            return

        if payload.get('password') != password:
            reject(handler_instance=self, message=AUTH_FAILED_MSG)
            return

        return extract_keywords.handler.do_POST(self)
