from http.server import HTTPServer
from lib.extract_keywords_with_auth import authenticatedHandler
import logging
from logging import INFO
from os import environ as env

DEFAULT_PORT = 8900
port_env = env.get('KEYWORD_EXTRACTOR_PORT', env.get('PORT', DEFAULT_PORT))
port = int(port_env)

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(INFO)

address = ('', port)
server = HTTPServer(address, authenticatedHandler)

logger.info('serving at ' + str(address))
server.serve_forever()
