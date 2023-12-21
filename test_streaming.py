from fastapi.responses import StreamingResponse
from fastapi import FastAPI
import time
import json

app = FastAPI()

def stream_json_data():
    data = {"name": "English is a West Germanic language in the Indo-European language family. Originating in early medieval England, today English is both the most spoken language in the world and the third most spoken native language, after Mandarin Chinese and Spanish.", "age": 30}

    for i in data["name"]:
        time.sleep(1)
        yield i

@app.get("/stream_json")
async def stream():
    response = StreamingResponse(stream_json_data(), media_type="application/json")
    return response