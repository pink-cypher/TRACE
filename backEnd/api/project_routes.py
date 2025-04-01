from fastapi import APIRouter, Request, HTTPException
from projectManager.projectManager import ProjectManager
from Analyst.analyst import Analyst
# from ProjectManager.project import Project

router = APIRouter()

@router.post("/")
async def toggleLock(request: Request):
    data = await request.json()
    id = data.get('id')
    lock = data.get('lock')
    
    if not id or not lock:
        raise HTTPException(status_code=400, detail="Missing required fields")

    pm = ProjectManager()
    success = pm.toggleLock(id,lockState=lock)
    return {"success": success}

@router.post("/")
async def toggleProjectStatus(request: Request):
    data = await request.json()
    id = data.get("id")
    status = data.get('status')

    if not id or not status:
        raise HTTPException(status_code=400, detail="Missing required fields")
    pm = ProjectManager()
    
    success = pm.toggleStatus(id, status)
    return {"success": success}

@router.post("/")
async def exportProject(request: Request):
    data = await request.json()
    id = data.get('id')
    format = data.get('format')

    if not id or not format:
        raise HTTPException(status_code=400, detail="Missing required fields")
    
    pm = ProjectManager()
    
    success = pm.exportProject(id, format)
    return {"success": success}

@router.post("/")
async def saveProject(request: Request):
    pass

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
    manager = ProjectManager()

    success = manager.createProject(name, description,initials, ips, ports)
    return {"success": success}
 
# needs to Pass ProjectID from front end
@router.post("/load")
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
@router.post("/list")
async def getAllProjects(request: Request):
    pm = ProjectManager()

    projects = pm.showExisting()

    # Return list of project dictionaries
    return {
        "projects": projects
    }

@router.post("/delete")
async def deleteProject(request: Request):
    pm = ProjectManager()
    data = await request.json()
    project_id = data.get("projectID")

    print(project_id)
    if not project_id:
        raise HTTPException(status_code=400, detail="Project ID is required.")
    print(project_id)
    try:
        success = pm.deleteProject(project_id)
        if success:
            print("Project is deleted")
            return {"message": "Project deleted successfully."}
        else:
            print("failed to deleteee")
            raise HTTPException(status_code=404, detail="Project not found or deletion failed.")
    except Exception as e :
        print(f"Error occured delteing project{str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")