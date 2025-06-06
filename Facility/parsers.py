import uuid
from pydantic import BaseModel, Field

class MultilingualText(BaseModel):
    en: str
    hi: str

class FacilityParser(BaseModel):
   id: str = Field(default_factory=lambda: str(uuid.uuid4()))
   display_name: MultilingualText
   status: MultilingualText

   class Config:
      orm_mode = True


class EditFacilityParser(BaseModel):
   display_name: MultilingualText
   status: MultilingualText
      