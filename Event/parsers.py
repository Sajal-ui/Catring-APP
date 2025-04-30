from pydantic import BaseModel

class EventParser(BaseModel):
    id: int
    display_name: str

    class Config:
        orm = True
