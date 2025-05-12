from .parsers import EditFacilityParser, FacilityParser
from fastapi import APIRouter, Depends

from ..database import get_db
from .models import Facility
from CatringApp.session import CustomSession

Facility_db = []

router = APIRouter(prefix="/facility", tags=["facility"])

@router.get("/", response_model=list[FacilityParser])
async def list_events(db:CustomSession = Depends(get_db)):
   return Facility_db
   # facilities = db.query(Facility).all()
   # return facilities

@router.post("/", response_model=FacilityParser)
async def create_event(facility: FacilityParser, db:CustomSession = Depends(get_db)):
   # facility_instance = Facility(display_name=facility.display_name, status=facility.status)
   # db.add(facility_instance)
   # db.commit()
   # db.refresh(facility_instance)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
   # return facility_instance
   Facility_db.append(facility)
   return facility

@router.get("/{id}", response_model=FacilityParser)
async def get_event(id: int, db:CustomSession = Depends(get_db)):
   # facility = db.query(Facility).filter(Facility.id == id).first()
   # return facility
   for facility in Facility_db:
      if facility["id"] == id:
         return facility
   return {"Not Found"}
   
@router.put("/{id}", response_model=FacilityParser)
async def update_event(id: int, facility: EditFacilityParser, db:CustomSession = Depends(get_db)):
   # facility_instance = db.query(Facility).filter(Facility.id == id).first()
   # facility_instance.display_name = facility.display_name
   # db.add(facility_instance)
   # db.commit()
   # db.refresh(facility_instance)
   # return facility_instance
   for facility in Facility_db:
      if facility["id"] == id:
         facility["display_name"] = facility.display_name
         facility["status"] = facility.status
         return facility
   return {"Not Found"}

@router.delete("/{id}")
async def delete_event(id: int, db:CustomSession = Depends(get_db)):
   # facility = db.query(Facility).filter(Facility.id == id).first()
   # db.delete(facility)
   # db.commit()
   # return {"message": "Facility deleted successfully"}
   for facility in Facility_db:
      if facility["id"] == id:
         Facility_db.remove(facility)
         return {"message": "Facility deleted successfully"}
   return {"Not Found"}
