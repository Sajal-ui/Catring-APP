from .parsers import EventParser, EditEventParser
<<<<<<< HEAD
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import status
# from CatringApp.database import get_db
from CatringApp.session import CustomSession
=======
from fastapi import APIRouter, Depends

from ..database import get_db
from ..session import CustomSession
>>>>>>> 42df18228bf6fe8ee37dc5282ef3406078f3bd88

Event_db = []

router = APIRouter(prefix="/events", tags=["events"])

@router.get("/")
async def list_events():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "Events fetched successfully",
            "data": [event.dict() for event in Event_db]
        }
    )



@router.post("/")
async def create_event(event: EventParser):
    Event_db.append(event)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "message": "Event added successfully",
            "data": event.dict()
        }
    )

@router.get("/{id}")
async def get_event(id: str):
   # event = db.query(Event).filter(Event.id == id).first()
   for event in Event_db:
      if event.id == id:
         return event
   return {"Not Found"}
   
@router.put("/{id}")
async def update_event(id: str, event: EditEventParser):
   # event_instance = db.query(Event).filter(Event.id == id).first()
   # event_instance.display_name = event.display_name
   # db.add(event_instance)
   # db.commit()
   # db.refresh(event_instance)
   for event_instance in Event_db:
      if event_instance.id == id:
         event_instance.display_name = event.display_name
         return event_instance
   return {"Not Found"}

@router.delete("/{id}")
async def delete_event(id: str):
   # event = db.query(Event).filter(Event.id == id).first()
   # db.delete(event)
   # db.commit()
   for event in Event_db:
      if event.id == id:
         Event_db.remove(event)
         return {"message": "Event deleted successfully"}
   return {"Not Found"}
