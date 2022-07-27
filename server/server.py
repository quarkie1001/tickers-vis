import asyncio
import json

import websockets

from settings import WEBSOCKET_HOST, WEBSOCKET_PORT
from logic import calculate_step

connected = set()
tickers = [0, ] * 100

async def handler(websocket):

    while True:
        connected.add(websocket)
        try:
            step_values = await calculate_step()
            message = json.dumps(step_values)
            await asyncio.sleep(1)
            print(f"sended {message}. Connected: {len(connected)}")
            await websocket.send(message)
        except KeyboardInterrupt:
            return
        finally:
            connected.remove(websocket)

async def main():
    async with websockets.serve(handler, WEBSOCKET_HOST, WEBSOCKET_PORT):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
