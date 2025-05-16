from .parsers import EditIndegreintsParser, IndegreintsParser
from fastapi import APIRouter

# from ..database import get_db
from .models import Indegreints
# from CatringApp.session import CustomSession

Indegreints_db = []

router = APIRouter(prefix="/indegrients", tags=["indegrients"])

@router.get("/")
async def list_indegreints():
   return Indegreints_db
   # facilities = db.query(Facility).all()
   # return facilities

@router.post("/")
async def create_event(indegreint: IndegreintsParser):
   # facility_instance = Facility(display_name=facility.display_name, status=facility.status)
   # db.add(facility_instance)
   # db.commit()
   # db.refresh(facility_instance)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
   # return facility_instance
   Indegreints_db.append(indegreint)
   return indegreint

@router.get("/{id}")
async def get_event(id: str):
   # facility = db.query(Facility).filter(Facility.id == id).first()
   # return facility
   for indegreint in Indegreints_db:
      if indegreint.id == id:
         return indegreint
   return {"Not Found"}
   
@router.put("/{id}")
async def update_event(id: str, indegreint: EditIndegreintsParser):
   # facility_instance = db.query(Facility).filter(Facility.id == id).first()
   # facility_instance.display_name = facility.display_name
   # db.add(facility_instance)
   # db.commit()
   # db.refresh(facility_instance)
   # return facility_instance
   for indegreint_instance in Indegreints_db:
      if indegreint_instance.id == id:
         indegreint_instance.name = indegreint.name
         indegreint_instance.unit_for_measurement = indegreint.unit_for_measurement
         indegreint_instance.status = indegreint.status
         return indegreint_instance
   return {"Not Found"}

@router.delete("/{id}")
async def delete_event(id: str):
   # facility = db.query(Facility).filter(Facility.id == id).first()
   # db.delete(facility)
   # db.commit()
   # return {"message": "Facility deleted successfully"}
   for indegreint in Indegreints_db:
      if indegreint.id == id:
         Indegreints_db.remove(indegreint)
         return {"message": "Facility deleted successfully"}
   return {"Not Found"}
