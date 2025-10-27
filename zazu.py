import asyncio
import base64
import json
import os
import websockets
from dotenv import load_dotenv


load_dotenv()

def sts_connect():
    api_key = os.getenv('DEEPGRAM_API_KEY')
    if not api_key:
        raise Exception("DEEPGRAM_API_KEY not found in environment variables.")
    
    sts_ws=websockets.connect("wss://agent.deepgram.com/v1/agent/converse"
        ,subprotocols=["token",api_key] )
    return sts_ws

def load_config():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config
#push to remove .env file with key