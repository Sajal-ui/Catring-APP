from pydantic import BaseModel, Json

class EventParser(BaseModel):
    id: int
    display_name: Json

    class Config:
        orm_mode = True


class EditEventParser(BaseModel):
    display_name: Json
