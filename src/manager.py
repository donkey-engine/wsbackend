"""WebSocket connection manager module."""
import typing as t
import uuid
from queue import Queue

from fastapi import WebSocket

from schemas import EventSchema


class ConnectionManager:
    """WebSocket manager."""

    def __init__(self):
        self.connections: t.Dict[uuid.UUID, WebSocket] = {}
        self.queue = Queue()

    async def new_private_event(self, to: uuid.UUID, event: EventSchema):
        """New event for specific connection."""
        websocket = self.connections.get(to)
        if websocket:
            await websocket.send_json(event.json())

    # async def new_public_event(self, event: EventSchema):
    #     """New event for all connections."""
    #     for _, websocket in self.connections.items():
    #         websocket.send_json(event)

    async def register(self, connection_id: uuid.UUID, connection: WebSocket):
        """Accept and register new WebSocket connection."""
        await connection.accept()
        self.connections[connection_id] = connection

    def disconnect(self, connection_id: uuid.UUID):
        """Remove connection."""
        del self.connections[connection_id]

manager = ConnectionManager()
