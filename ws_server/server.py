import logging
import asyncio
import json
import os
import websockets
from websockets.exceptions import ConnectionClosedOK

from utils import init_tickers, calculate_step

WEBSOCKET_HOST = os.getenv("WEBSOCKET_HOST", "ws-server")
WEBSOCKET_PORT = os.getenv("WEBSOCKET_PORT", 9999)
LOG_LEVEL_ENV = os.getenv("LOG_LEVEL", "debug")
LOG_LEVEL_MAP = {"debug": logging.DEBUG, "info": logging.INFO}

logging.basicConfig(encoding="utf-8", level=LOG_LEVEL_MAP[LOG_LEVEL_ENV])

connected = set()


async def handler(websocket):
    current_tickers = await init_tickers()

    while True:
        logging.info("Client connected!")
        connected.add(websocket)
        try:
            current_tickers = await calculate_step(current_tickers)
            message = json.dumps(current_tickers)
            await websocket.send(message)
            await asyncio.sleep(1)
        except (KeyboardInterrupt, ConnectionClosedOK):
            logging.info("Got signal to stop Websocket server")
            return
        finally:
            connected.remove(websocket)
            logging.info("Client disconnected!")


async def main():

    async with websockets.serve(handler, WEBSOCKET_HOST, WEBSOCKET_PORT):
        await asyncio.Future()


if __name__ == "__main__":
    logging.info(f"Websocket server started on {WEBSOCKET_HOST}:{WEBSOCKET_PORT}")
    asyncio.run(main())
