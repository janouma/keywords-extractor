# Keywords-extractor

Python service to automatically extract keywords from a text.


## Requirements

- Python >= 3.7.1
- pip >= 18.1


## Install

```bash
pip3 install -r requirements.txt
```

## Start up

```bash
KEYWORD_EXTRACTOR_PORT=3005 python3 server.py
```
or

```bash
PORT=3005 python3 server.py
```

> port is set to 8900 when `KEYWORD_EXTRACTOR_PORT` and `PORT` enviroment variables are missing


## Generate API key

The following command will generate and print out a new api key to be used for api calls.
It also stores the api key in the file `.api_key` for further references.

```bash
python create_api_key.py
```

## Usage

### Call

_The following code snippet can be used as is with **Vscode REST Client** extension_

```bash
POST http://localhost:3005
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNzd29yZCI6ImMzYTBhODM1LWY0OWEtNDJiNi04NzEzLWFkMTA3OTkzOWViZSJ9.x77HXBgnPgvq7aGKpLqB8Q8lcMTbjtMJhIPTQygLxjc

{
	"lang": "en",
	"limitRatio": 15,
	"max": 20,
	"text": "The Wandering Earth, described as China’s first big-budget science fiction thriller, quietly made it onto screens at AMC theaters in North America this weekend, and it shows a new side of Chinese filmmaking — one focused toward futuristic spectacles rather than China’s traditionally grand, massive historical epics. At the same time, The Wandering Earth feels like a throwback to a few familiar eras of American filmmaking. While the film’s cast, setting, and tone are all Chinese, longtime science fiction fans are going to see a lot on the screen that reminds them of other movies, for better or worse."
}
```

### Response

```bash
HTTP/1.0 200 OK
Server: BaseHTTP/0.6 Python/3.7.1
Date: Tue, 21 Apr 2020 08:49:07 GMT
Content-type: application/json

{
  "keywords": [
    "fiction",
    "science",
    "china",
    "filmmaking",
    "earth"
  ],
  "wordsCount": 102
}
```

> _`wordsCount` is the total count of words in the provided text, not only the keywords._

### Parameters _(all are required)_

| Name | Type | Description |
|------|------|-------------|
| lang | 'en', 'fr', 'de', 'es', 'pt', 'it', 'nl', 'el', 'nb', 'lt' | The language of the provided text |
| limitRatio | integer | The percentage of keywords to retain among the extracted list
| max | integer | The absolute maximum keywords to retain _(the minimum amount between `limitRatio` and `max` will be kept)_
| text | string | The text to parse |
