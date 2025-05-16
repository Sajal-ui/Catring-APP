import uuid
from pydantic import BaseModel, Field

class MultilingualText(BaseModel):
    en: str
    hi: str

class ItemSubCategoryParser(BaseModel):
   id: str = Field(default_factory=lambda: str(uuid.uuid4()))
   item_category_id: str
   name: MultilingualText
   status: MultilingualText

   class Config:
      orm_mode = True


class EditItemSubCategoryParser(BaseModel):
   name: MultilingualText
   item_category_id: str
   status: MultilingualText
