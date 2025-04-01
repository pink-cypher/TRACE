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


# needs to Pass ProjectID from front end
@router.post("/")
async def load_project(request: Request):
    data = await request.json()
    project_id = data.get("projectID")

    if not project_id:
        raise HTTPException(status_code=400, detail="Project ID is required")
    
    pm = ProjectManager()

    project = pm.loadProject(project_id)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # Return project info back to front end in json
    return {
        "id": project.getID(),
        "name": project.getName(),
        "owner": project.getOwner(),
        "timestamp": project.getTimestamp(),
        "status": project.getStatus(),
        "lockStatus": project.getLockStatus(),
        "description": project.getDescription(),
        "ips": project.getIps(),
        "ports": project.getPorts()
    }

# Get all projects
@router.post("/")
async def getAllProjects(request: Request):

    pass
