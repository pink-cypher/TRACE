from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.analyst_routes import router as analyst_router
from api.project_routes import router as project_router

# from api.test_routes import router as test_router

 
app = FastAPI()

# Allow frontend to access backend during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 
app.include_router(project_router, prefix="/api/projects")

# Prefix all analyst routes with /api/analyst
app.include_router(analyst_router, prefix="/api/analyst")



# from projectManager.projectManager import ProjectManager

# p = ProjectManager()
# ips = [
#     "192.168.1.10",
#     "192.168.1.15",
#     "10.0.0.5",
#     "172.16.0.3"
# ]
# ports = [
#     "22", 
#     "80",   
#     "443",  
#     "3306"  
# ]

# p.createProject("Test1","testing project","RP", ips, ports)
