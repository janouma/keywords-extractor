from http.server import BaseHTTPRequestHandler
from jsonschema import validate
import json
from lib.keywords_extractor import KeywordsExtractor
from lib.words_counter import count_words

body_schema = {
    'type': 'object',
    'properties': {
        'lang': {
            'type': 'string',
            'enum': ['en']
        },
        'text': {'type': 'string'},
        'limitRatio': {'type': 'integer'},
        'max': {'type': 'integer'}
    }
}


class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        body_length = int(self.headers.get('Content-Length'))
        raw_body = self.rfile.read(body_length)
        json_body = json.loads(raw_body)

        validate(json_body, body_schema)

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
        self.wfile.write(response_body)
        return
