from fastapi import FastAPI
from datetime import datetime
import uuid

app = FastAPI()


keyPair = {}

def generateTimestamp():
    return datetime.now()

def generateUUID():
    return uuid.uuid1()

@app.get("/")
def generate():
    timestamp = generateTimestamp()
    uniqueId = generateUUID()
    keyPair[timestamp] = uniqueId
    return keyPair