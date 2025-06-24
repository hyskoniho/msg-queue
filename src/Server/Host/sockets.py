# WebSocket URL where you want to send the data
WS_SERVER_URL = 'ws://<websocket_host>:<websocket_port>'


# Function to send content via WebSocket
def send_via_websocket(content):
    try:
        # Establish a WebSocket connection
        # You can use a library like websockets (asynchronously) or other WebSocket libraries
        import websockets
        import asyncio

        async def send():
            async with websockets.connect(WS_SERVER_URL) as websocket:
                await websocket.send(content)

        asyncio.run(send())

    except Exception as e:
        print(f"Error sending via WebSocket: {e}")