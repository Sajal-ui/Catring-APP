import uuid
from pydantic import BaseModel, Field

class MultilingualText(BaseModel):
    en: str
    hi: str

class ItemCategoryParser(BaseModel):
   id: str = Field(default_factory=lambda: str(uuid.uuid4()))
   name: MultilingualText
   status: MultilingualText

   class Config:
      orm_mode = True


class EditItemCatgoryParser(BaseModel):
   name: MultilingualText
   status: MultilingualText
