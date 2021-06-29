"""WebSocket connection manager module."""
import typing as t
import uuid
from queue import Queue

from fastapi import WebSocket

from schemas import EventSchema


class ConnectionManager:
    """WebSocket manager."""

    def __init__(self):
        self.connections: t.List[t.Dict[str, t.Any]] = []

    async def new_private_event(self, to: uuid.UUID, event: EventSchema):
        """New event for specific connection."""
        for connection in self.connections:
            if connection['id'] == to:
                await connection['websocket'].send_json(event.json())

    async def register(self, connection_id: uuid.UUID, connection: WebSocket):
        """Accept and register new WebSocket connection."""
        await connection.accept()
        self.connections.append({
            'id': connection_id,
            'websocket': connection
        })

    def disconnect(self, connection_id: uuid.UUID, connection: WebSocket):
        """Remove connection."""
        self.connections.remove({
            'id': connection_id,
            'websocket': connection,
        })

manager = ConnectionManager()
