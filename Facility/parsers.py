from pydantic import BaseModel, Json

class FacilityParser(BaseModel):
   id: int
   display_name: Json
   status: Json

   class Config:
      orm_mode = True


class EditFacilityParser(BaseModel):
   display_name: Json
   status: Json
      