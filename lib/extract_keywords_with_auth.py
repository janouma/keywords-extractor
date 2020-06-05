from http.server import BaseHTTPRequestHandler
from api import extract_keywords
from pathlib import Path as get_path
import jwt
from jwt.exceptions import InvalidSignatureError
import re
import json
from lib.constants import ALGORITHM
from os import environ as env
import logging
from logging import INFO

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(INFO)

AUTH_TYPE = 'Bearer'
AUTH_FAILED_MSG = 'authentication failed'

root_dir = get_path(__file__).parent / '..'
spaces_pattern = re.compile(r'\s+')
jwt_secret = env.get('JWT_SECRET')
password = env.get('PASSWORD')

logger.info('JWT_SECRET: ' + str(jwt_secret))
logger.info('PASSWORD: ' + str(password))


class authenticatedHandler(BaseHTTPRequestHandler):
    def reject(self, message, code=401):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response_body = json.dumps({'message': message})
        self.wfile.write(response_body.encode())

    def do_POST(self):
        authorization = self.headers.get('Authorization')

        if authorization is None:
            self.reject(message='authorization required')
            return

        auth_type, api_key = spaces_pattern.split(authorization)

        if auth_type != AUTH_TYPE:
            self.reject(
                message='wrong authorization type "' + auth_type +
                '", "' + AUTH_TYPE + '" was expected'
            )
            return

        try:
            payload = jwt.decode(api_key, jwt_secret, algorithms=[ALGORITHM])
        except InvalidSignatureError:
            self.reject(message=AUTH_FAILED_MSG)
            return
        except Exception as error:
            print('Unexpected error:\n{0}'.format(error))

            self.reject(
                message=AUTH_FAILED_MSG,
                code=500
            )

            return

        if payload.get('password') != password:
            self.reject(message=AUTH_FAILED_MSG)
            return

        return extract_keywords.handler.do_POST(self)
