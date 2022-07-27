import asyncio
import json

import websockets
from websockets.exceptions import ConnectionClosedOK

from logic import init_tickers, calculate_step

WEBSOCKET_HOST = "localhost"
WEBSOCKET_PORT = 8765

connected = set()

async def handler(websocket):
    current_tickers = await init_tickers()

    while True:
        connected.add(websocket)
        try:
            current_tickers = await calculate_step(current_tickers)
            message = json.dumps(current_tickers)
            await asyncio.sleep(1)
            await websocket.send(message)
        except (KeyboardInterrupt, ConnectionClosedOK):
            return
        finally:
            connected.remove(websocket)

async def main():
    async with websockets.serve(handler, WEBSOCKET_HOST, WEBSOCKET_PORT):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
