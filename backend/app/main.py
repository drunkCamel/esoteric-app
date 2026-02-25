from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.utils.exceptions import InvalidDataError, InvalidTypeError
from app.routers import birthdate, name


app = FastAPI(title="My Esoteric App", version="1.0")

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


@app.get("/")   #home route - 
def home():
    return {"message": "Hello from FastAPI!"}

@app.get("/api/items")
def get_items():
    return {
        "items": [
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"},
            {"id": 3, "name": "Item 3"}
        ]
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
