from .parser import ItemCategoryParser, EditItemCatgoryParser
from fastapi import APIRouter

# from ..database import get_db
from .models import ItemCategory
# from CatringApp.session import CustomSession

ItemCategory_db = []

router = APIRouter(prefix="/item-category", tags=["item-category"])

@router.get("/")
async def list_itemcategory():
   return ItemCategory_db
   # facilities = db.query(Facility).all()
   # return facilities

@router.post("/")
async def create_event(itemcategory: ItemCategoryParser):
   # facility_instance = Facility(display_name=facility.display_name, status=facility.status)
   # db.add(facility_instance)
   # db.commit()
   # db.refresh(facility_instance)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
   # return facility_instance
   ItemCategory.append(itemcategory)
   return ItemCategory

@router.get("/{id}")
async def get_event(id: str):
   # facility = db.query(Facility).filter(Facility.id == id).first()
   # return facility
   for item_category in ItemCategory_db:
      if item_category.id == id:
         return item_category
   return {"Not Found"}
   
@router.put("/{id}")
async def update_event(id: str, item_category: EditItemCatgoryParser):
   # facility_instance = db.query(Facility).filter(Facility.id == id).first()
   # facility_instance.display_name = facility.display_name
   # db.add(facility_instance)
   # db.commit()
   # db.refresh(facility_instance)
   # return facility_instance
   for itemcategory_instance in ItemCategory_db:
      if itemcategory_instance.id == id:
         itemcategory_instance.name = item_category.name
         return itemcategory_instance
   return {"Not Found"}

@router.delete("/{id}")
async def delete_event(id: str):
   # facility = db.query(Facility).filter(Facility.id == id).first()
   # db.delete(facility)
   # db.commit()
   # return {"message": "Facility deleted successfully"}
   for itemcategory in ItemCategory_db:
      if itemcategory.id == id:
         ItemCategory_db.remove(itemcategory)
         return {"message": "Facility deleted successfully"}
   return {"Not Found"}
