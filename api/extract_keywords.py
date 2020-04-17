from http.server import BaseHTTPRequestHandler
from cerberus import Validator
import json
from lib.keywords_extractor import KeywordsExtractor
from lib.words_counter import count_words

body_schema = {
    'lang': {
        'type': 'string',
        'allowed': ['en', 'fr', 'de', 'es', 'pt', 'it', 'nl', 'el', 'nb', 'lt'],
        'required': True
    },

    'text': {
        'type': 'string',
        'required': True
    },

    'limitRatio': {
        'type': 'integer',
        'required': True
    },

    'max': {
        'type': 'integer',
        'required': True
    }
}

validator = Validator(body_schema)


class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        body_length = int(self.headers.get('Content-Length'))
        raw_body = self.rfile.read(body_length)
        json_body = json.loads(raw_body)

        is_body_valid = validator.validate(json_body)

        if is_body_valid is True:
            extractor = KeywordsExtractor(json_body['lang'])

            extractor.analyze(
                json_body['text'],
                candidate_pos=['NOUN', 'PROPN', 'VERB'],
                window_size=4,
                lower=True
            )

            keywords = extractor.get_keywords(
                percent=json_body['limitRatio'],
                max_keywords=json_body['max']
            )

            words_count = count_words(json_body['text'])

            response_body = json.dumps({
                'keywords': keywords,
                'wordsCount': words_count
            })

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(response_body.encode())
        else:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            response_body = json.dumps({
                'message': 'body validation failed',
                'errors': validator.errors
            })

            self.wfile.write(response_body.encode())

        return
