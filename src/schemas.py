"""Application schemas module."""
import typing as t
import uuid
from enum import Enum

import pydantic


class EventType(Enum):
    # Server updates
    SERVERS = 'SERVERS'
    # Logs
    LOGS = 'LOGS'


class EventSchema(pydantic.BaseModel):
    type: EventType
    data: t.Dict[str, t.Any]


class NewEventSchema(pydantic.BaseModel):
    to: uuid.UUID
    event: EventSchema
