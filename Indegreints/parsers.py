import uuid
from pydantic import BaseModel, Field

class MultilingualText(BaseModel):
    en: str
    hi: str

class IndegreintsParser(BaseModel):
   id: str = Field(default_factory=lambda: str(uuid.uuid4()))
   name: MultilingualText
   unit_for_measurement: MultilingualText
   status: MultilingualText

   class Config:
      orm_mode = True


class EditIndegreintsParser(BaseModel):
   name: MultilingualText
   unit_for_measurement: MultilingualText
   status: MultilingualText
      