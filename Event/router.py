from .parsers import EventParser
from fastapi import APIRouter, Depends

from CatringApp.database import get_db

router = APIRouter(prefix="/events", tags=["events"])

@router.get("/", response_model=list[EventParser])
async def list_events(db:CustomSession = Depends(get_db)):
   events = db.query(Event).all()
   return events

@router.post("/", response_model=EventParser)
async def create_event(event: EventParser, db:CustomSession = Depends(get_db)):
   event_instance = Event(display_name=event.display_name)
   db.add(event_instance)
   db.commit()
   db.refresh(event_instance)
   return event_instance

@router.get("/{id}", response_model=EventParser)
async def get_event(id: int, db:CustomSession = Depends(get_db)):
   event = db.query(Event).filter(Event.id == id).first()
   return event
   
@router.put("/{id}", response_model=EventParser)
async def update_event(id: int, event: EditEventParser, db:CustomSession = Depends(get_db)):
   event_instance = db.query(Event).filter(Event.id == id).first()
   event_instance.display_name = event.display_name
   db.add(event_instance)
   db.commit()
   db.refresh(event_instance)
   return event_instance

@router.delete("/{id}")
async def delete_event(id: int, db:CustomSession = Depends(get_db)):
   event = db.query(Event).filter(Event.id == id).first()
   db.delete(event)
   db.commit()
   return {"message": "Event deleted successfully"}
