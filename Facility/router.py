from .parsers import EditFacilityParser, FacilityParser
from fastapi import APIRouter

# from ..database import get_db
from .models import Facility
<<<<<<< HEAD
# from CatringApp.session import CustomSession
=======
from ..session import CustomSession
>>>>>>> 42df18228bf6fe8ee37dc5282ef3406078f3bd88

Facility_db = []

router = APIRouter(prefix="/facility", tags=["facility"])

@router.get("/")
async def list_events():
   return Facility_db
   # facilities = db.query(Facility).all()
   # return facilities

@router.post("/")
async def create_event(facility: FacilityParser):
   # facility_instance = Facility(display_name=facility.display_name, status=facility.status)
   # db.add(facility_instance)
   # db.commit()
   # db.refresh(facility_instance)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
   # return facility_instance
   Facility_db.append(facility)
   return facility

@router.get("/{id}")
async def get_event(id: str):
   # facility = db.query(Facility).filter(Facility.id == id).first()
   # return facility
   for facility in Facility_db:
      if facility.id == id:
         return facility
   return {"Not Found"}
   
@router.put("/{id}")
async def update_event(id: str, facility: EditFacilityParser):
   # facility_instance = db.query(Facility).filter(Facility.id == id).first()
   # facility_instance.display_name = facility.display_name
   # db.add(facility_instance)
   # db.commit()
   # db.refresh(facility_instance)
   # return facility_instance
   for facility_instance in Facility_db:
      if facility_instance.id == id:
         facility_instance.display_name = facility.display_name
         facility_instance.status = facility.status
         return facility_instance
   return {"Not Found"}

@router.delete("/{id}")
async def delete_event(id: str):
   # facility = db.query(Facility).filter(Facility.id == id).first()
   # db.delete(facility)
   # db.commit()
   # return {"message": "Facility deleted successfully"}
   for facility in Facility_db:
      if facility.id == id:
         Facility_db.remove(facility)
         return {"message": "Facility deleted successfully"}
   return {"Not Found"}
