import json

import requests

response = requests.get("http://localhost:8000/stream_json")

for line in response.content:
    data = json.loads(line)
    print(data)