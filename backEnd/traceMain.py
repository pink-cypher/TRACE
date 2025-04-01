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
#     "20", 
#     "81",   
#     "423",  
#     "3306"  
# ]

# p.createProject("Test demo","testing project 3  ","SL", ips, ports)
# id = "4:9b85307e-5220-4f24-9712-4a463db95510:0"

# project = p.loadProject(id)

# print(vars(project))

# print(project.getIps())

# projectList = p.show_existing_projects()
# for project in projectList:
#     print("ID:", project["id"])
#     print("Name:", project["name"])
#     print("Owner:", project["owner"])
#     print("Timestamp:", project["timestamp"])
#     print("Status:", project["status"])
#     print("Lock Status:", project["lockStatus"])
#     print("Description:", project["description"])
#     print("-" * 40)