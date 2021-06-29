"""Http routes module."""
from fastapi import APIRouter

from manager import manager
from schemas import NewEventSchema

router = APIRouter()


@router.post('/events')
async def new_event(
    item: NewEventSchema,
):
    """Receive new event."""
    await manager.new_private_event(item.to, item.event)
    return {'status': 'ok'}
