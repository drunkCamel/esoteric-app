from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.utils.exceptions import InvalidDataError, InvalidTypeError
from app.routers import birthdate, name


app = FastAPI(title="My Esoteric App",
              description = "An API that provides esoteric calculations based on birthdate and name data.", 
              version="1.0")

# Exception handlers for custom exceptions
@app.exception_handler(InvalidTypeError)
async def invalid_type_handler(request: Request, exc: InvalidTypeError):
    return JSONResponse(status_code=422, content={"error": "invalid_type", "detail": str(exc)})

@app.exception_handler(InvalidDataError)
async def invalid_data_handler(request: Request, exc: InvalidDataError):
    return JSONResponse(status_code=400, content={"error": "invalid_data", "detail": str(exc)})

# Configure CORS to allow React frontend to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(birthdate.router, prefix = "/api")  # Include the birthdate router
app.include_router(name.router, prefix = "/api")  # Include the name router
