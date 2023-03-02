from http.server import HTTPServer
from lib.extract_keywords_with_auth import authenticatedHandler
import logging
from logging import INFO
from os import environ as env
import socket

DEFAULT_PORT = 8900
port_env = env.get('KEYWORD_EXTRACTOR_PORT', env.get('PORT', DEFAULT_PORT))
port = int(port_env)

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(INFO)

class HTTPServerV6(HTTPServer):
  address_family = socket.AF_INET6

if env.get('IPV6') == 'yes':
  address = ('::', port)
  server = HTTPServerV6(address, authenticatedHandler)
else:
  address = ('', port)
  server = HTTPServer(address, authenticatedHandler)

logger.info('serving at ' + str(address))
server.serve_forever()
