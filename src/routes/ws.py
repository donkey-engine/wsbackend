"""WebSocket routes module."""
import uuid

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from manager import manager

router = APIRouter()


@router.websocket('/ws/{connection_id}')
async def websocket_route(
    connection_id: uuid.UUID,
    websocket: WebSocket,
):
    """WebSocket route."""
    await manager.register(connection_id, websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(connection_id)
