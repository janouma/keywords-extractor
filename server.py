from http.server import HTTPServer
from api import extract_keywords
import logging
from logging import INFO
from os import environ as env

DEFAULT_PORT = 8900
port_env = env.get('KEYWORD_EXTRACTOR_PORT')
port = int(port_env) if port_env else DEFAULT_PORT

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(INFO)

address = ('', port)
server = HTTPServer(address, extract_keywords.handler)

logger.info('serving at ' + str(address))
server.serve_forever()
