from .parser import ItemSubCategoryParser, EditItemSubCategoryParser
from fastapi import APIRouter

# from ..database import get_db
from .models import ItemSubCategory
# from CatringApp.session import CustomSession

ItemSubCategory_db = []

router = APIRouter(prefix="/item-subcategory", tags=["item-subcategory"])

@router.get("/")
async def list_itemsubcategory():
   return ItemSubCategory_db
   # facilities = db.query(Facility).all()
   # return facilities

@router.post("/")
async def create_event(itemsubcategory: ItemSubCategoryParser):
   # facility_instance = Facility(display_name=facility.display_name, status=facility.status)
   # db.add(facility_instance)
   # db.commit()
   # db.refresh(facility_instance)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
   # return facility_instance
   ItemSubCategory.append(itemsubcategory)
   return ItemSubCategory

@router.get("/{id}")
async def get_event(id: str):
   # facility = db.query(Facility).filter(Facility.id == id).first()
   # return facility
   for item_subcategory in ItemSubCategory_db:
      if item_subcategory.id == id:
         return item_subcategory
   return {"Not Found"}
   
@router.put("/{id}")
async def update_event(id: str, item_subcategory: EditItemSubCategoryParser):
   # facility_instance = db.query(Facility).filter(Facility.id == id).first()
   # facility_instance.display_name = facility.display_name
   # db.add(facility_instance)
   # db.commit()
   # db.refresh(facility_instance)
   # return facility_instance
   for itemsubcategory_instance in ItemSubCategory_db:
      if itemsubcategory_instance.id == id:
         itemsubcategory_instance.name = item_subcategory.name
         return itemsubcategory_instance
   return {"Not Found"}

@router.delete("/{id}")
async def delete_event(id: str):
   # facility = db.query(Facility).filter(Facility.id == id).first()
   # db.delete(facility)
   # db.commit()
   # return {"message": "Facility deleted successfully"}
   for itemsubcategory in ItemSubCategory_db:
      if itemsubcategory.id == id:
         ItemSubCategory_db.remove(itemsubcategory)
         return {"message": "Facility deleted successfully"}
   return {"Not Found"}
