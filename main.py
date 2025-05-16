from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from .Users.router import router as users_router
from .Event.router import router as event_router
from .Facility.router import router as facility_router
from .Indegreints.router import router as indegreint_router
from .ItemCategory.router import router as item_category_router
from .ItemSubCategory.router import router as item_sub_category_router

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def get_config():
    return JSONResponse(content={
        "app_name": "CatringApp",
        "author": "Sajal Pathak",
        "description": "This is a demo catring app"
    })

# Routers
app.include_router(users_router)
app.include_router(event_router)
app.include_router(facility_router)
app.include_router(indegreint_router)
app.include_router(item_category_router)
app.include_router(item_sub_category_router)
