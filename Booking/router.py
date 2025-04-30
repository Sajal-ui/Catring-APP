from fastapi import APIRouter, Depends

from CatringApp.Booking.parsers import BookingCreateParser
from CatringApp.Booking.models import Booking
from CatringApp.database import get_db

router = APIRouter(prefix="/booking", tags=["booking"])

@router.get("/")
async def list_booking():
    pass


@router.post("/", response_model=BookingCreateParser)
async def create_booking(booking: BookingCreateParser, db: Depends(get_db)):
    booking_instance = Booking(
       start_date=booking.start_date,
       end_date=booking.end_date,
       customer_name=booking.customer_name,
       contact_no=booking.contact_no,
       email=booking.email,
       address=booking.address,
       event_identifier=booking.event_identifier,
       event_venue=booking.event_venue,
       amount=booking.amount,
       advance=booking.advance
    )
    db.add(booking_instance)
    db.commit()
    db.refresh(booking_instance)
    return booking_instance
