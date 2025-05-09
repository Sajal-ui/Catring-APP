# import uuid
# from curses.ascii import isdigit
# from datetime import datetime
# from typing import Optional

# from fastapi import Depends

# from pydantic import BaseModel, root_validator, validator

# from Event.models import Event
# from ..database import get_db


# class BookingCreateParser(BaseModel):
#     start_date: datetime
#     end_date: datetime
#     customer_name: str
#     contact_no: str
#     email: str
#     address: str
#     event_identifier: int
#     event_venue: str
#     amount: float
#     advance: float

#     class Config:
#         json_encoders = {
#             datetime: lambda v: v.isoformat()
#         }

#     @root_validator
#     def validate_payload(cls, data):
#         event_start_date = data.get('start_date')
#         event_end_date = data.get('end_date')

#         if not (isinstance(event_start_date, datetime) and
#                 isinstance(event_end_date, datetime)
#                 and event_end_date> event_start_date
#         ):
#             raise ValueError('Please verify the start and end date for the event.')
#         return data

#     @validator('contactNo')
#     def check_contact_no_in_payload(cls, contact_no):
#         if any((not isdigit(part)) for part in contact_no) and (not len(contact_no) == 10):
#             raise ValueError('Please verify the contact number.')
#         return contact_no

#     @validator('event_type')
#     def check_event_type_in_payload(cls, event_identifier):
#         db = Depends(get_db)
#         event = db.query(Event).filter(Event.id==event_identifier).first()
#         if not event:
#             raise ValueError('Please verify the Event provided in the payload.')
#         return event


# class BookingDetailsParser(BaseModel):
#     id: int
#     customer_name: str
#     event_venue: str
#     amount: float

#     booking_id: Optional[str] = None

#     @root_validator(pre=True)
#     def generate_booking_id(cls, values):
#         if not values.get('booking_id'):
#             random_uid = uuid.uuid4().hex[:10]  # 10 char unique
#             values['booking_id'] = f"B{random_uid}"
#         return values

#     class Config:
#         orm_mode = True

