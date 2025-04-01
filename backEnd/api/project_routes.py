from fastapi import APIRouter, Request, HTTPException
from projectManager.projectManager import ProjectManager
from Analyst.analyst import Analyst
# from ProjectManager.project import Project

router = APIRouter()

@router.post("/create")
async def create_project(request: Request):
    data = await request.json()
    name = data.get("name")
    description = data.get("description", "")
    ips = data.get("ips", [])
    ports = data.get("ports", [])
    initials = data.get("initials")  

    if not name or not initials:
        raise HTTPException(status_code=400, detail="Missing required fields")

    analyst = Analyst()
    analyst.loadAnalyst(initials)
    manager = ProjectManager(analyst)

    success = manager.createProject(name, description,initials, ips, ports)
    return {"success": success}



@router.post("/")
async def load_project(request: Request):
    pass