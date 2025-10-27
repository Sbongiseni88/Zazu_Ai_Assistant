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

async def handle_barge_in(decoded,twilio_ws,streamsid):
    pass 

async def handle_text(decoded,twilio_ws,sts_ws,streamsid):
    pass

async def sts_sender(sts_ws,audio_queue):
    pass

async def sts_receiver(sts_ws,twilio_ws,streamsid_queue):
    pass

async def twilio_receiver(twilio_ws,audio_queue,streamsid_queue):
    pass

async def twilio_handler(twilio_ws):
    pass

async def main():
    await websockets.serve(twilio_handler, "localhost", 5000)
    print("Twilio WebSocket server started on ws://localhost:5000")
    await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
