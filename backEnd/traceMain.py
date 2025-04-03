from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.analyst_routes import router as analyst_router
from api.project_routes import router as project_router
from api.crawler_routes import router as crawler_router
from api.setting_routes import router as setting_router
from api.ai_routes import router as ai_router
from api.http_routes import router as http_router


app = FastAPI()

# Allow frontend to access backend during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

#Team2
# Prefix all project routes with /api/project
app.include_router(project_router, prefix="/api/projects")
# Prefix all analyst routes with /api/analyst
app.include_router(analyst_router, prefix="/api/analyst")
app.include_router(setting_router, prefix="/api/settings")

# Team11
# Prefix all crawler routes with /api/crawler
app.include_router(crawler_router, prefix="/api/cralwer")
# Prefix all ai routes with /api/ai
app.include_router(ai_router, prefix="/api/ai")


# Team4
app.include_router(http_router, prefix="/api/http")


