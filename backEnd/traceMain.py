from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.analyst_routes import router as analyst_router
from api.test_routes import router as test_router

 
app = FastAPI()

# Allow frontend to access backend during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 
app.include_router(test_router, prefix="/api/test")
# Prefix all analyst routes with /api/analyst
app.include_router(analyst_router, prefix="/api/analyst")

