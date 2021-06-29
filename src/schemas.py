"""Application schemas module."""
import uuid
from enum import Enum

import pydantic


class EventType(Enum):
    NOTIFICATION = 'NOTIFICATION'


class EventSchema(pydantic.BaseModel):
    type: EventType


class NewEventSchema(pydantic.BaseModel):
    to: uuid.UUID
    event: EventSchema
