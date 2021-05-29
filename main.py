from fastapi import FastAPI
from datetime import datetime
import uuid

app = FastAPI()


keyPair = {}

# Generates timestamps
def generateTimestamp():
    return datetime.now()

# Generates unique Id
def generateUUID():
    return uuid.uuid1()

@app.get("/")
def generate():
    '''
    Generates a new uuid and pairs it with the time it was created
    '''
    timestamp = generateTimestamp()
    uniqueId = generateUUID()
    keyPair[timestamp] = uniqueId
    return keyPair