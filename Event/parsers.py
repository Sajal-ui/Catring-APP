import uuid
from pydantic import BaseModel, Field

class MultilingualText(BaseModel):
    en: str
    hi: str

class EventParser(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    display_name: MultilingualText

    class Config:
        orm_mode = True


class EditEventParser(BaseModel):
    display_name: MultilingualText
