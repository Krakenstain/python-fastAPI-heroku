import asyncio

from fastapi import WebSocket, APIRouter

router = APIRouter(
    prefix="/api/v1/websock",
    tags=["Websock"]
)


@router.websocket("")
async def websocket_endpoint(
        websocket: WebSocket):

        await websocket.accept()
        print("Websocket connected")

        while True:
            try:
                message = await websocket.receive_text()
                await websocket.send_text(message)
                print(message)
            except websocket.exceptions.ConnectionClosedOK:
                print("Websocket disconnected")
                break


        return {"message": "Websocket closed"}