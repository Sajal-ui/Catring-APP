from .parsers import EventParser, EditEventParser
from fastapi import APIRouter, Depends

from ..database import get_db
from ..session import CustomSession

Event_db = []

router = APIRouter(prefix="/events", tags=["events"])

@router.get("/", response_model=list[EventParser])
async def list_events(db:CustomSession = Depends(get_db)):
   # events = db.query(Event).all()
   events = Event_db
   return events

@router.post("/", response_model=EventParser)
async def create_event(event: EventParser, db:CustomSession = Depends(get_db)):
   # event_instance = Event(display_name=event.display_name)
   # db.add(event_instance)
   # db.commit()
   # db.refresh(event_instance)
   Event_db.append(event)
   # return event_instance
   return event

@router.get("/{id}", response_model=EventParser)
async def get_event(id: int, db:CustomSession = Depends(get_db)):
   # event = db.query(Event).filter(Event.id == id).first()
   for event in Event_db:
      if event["id"] == id:
         return event
   return {"Not Found"}
   
@router.put("/{id}", response_model=EventParser)
async def update_event(id: int, event: EditEventParser, db:CustomSession = Depends(get_db)):
   # event_instance = db.query(Event).filter(Event.id == id).first()
   # event_instance.display_name = event.display_name
   # db.add(event_instance)
   # db.commit()
   # db.refresh(event_instance)
   for event in Event_db:
      if event["id"] == id:
         event["display_name"] = event.display_name
         return event
   return {"Not Found"}

@router.delete("/{id}")
async def delete_event(id: int, db:CustomSession = Depends(get_db)):
   # event = db.query(Event).filter(Event.id == id).first()
   # db.delete(event)
   # db.commit()
   for event in Event_db:
      if event["id"] == id:
         Event_db.remove(event)
         return {"message": "Event deleted successfully"}
   return {"Not Found"}
