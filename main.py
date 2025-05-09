from fastapi import FastAPI
from fastapi.responses import JSONResponse

# from Booking.router import router as booking_router
from .Users.router import router as users_router
from .Event.router import router as event_router
from .Facility.router import router as facility_router

app = FastAPI()

@app.get("/")
async def get_config():
    APP_NAME = "CatringApp"
    AUTHOR = "Sajal Pathak"
    DESCRIPTION = "This is a demo catring app"

    return JSONResponse(content={"app_name": APP_NAME, "author": AUTHOR, "description": DESCRIPTION}, status_code=200)

app.include_router(users_router)
# app.include_router(booking_router)
app.include_router(event_router)
app.include_router(facility_router)
