from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import StreamingResponse
import io
from projectManager.projectManager import ProjectManager
from projectManager.collaboration import CollaborationManager
from Analyst.analyst import Analyst
import csv
import xml.etree.ElementTree as ET

router = APIRouter()

@router.post("/lock")
async def toggleLock(request: Request):
    data = await request.json()
    #print(data)
    id = data.get('id')
    #print({id})
    lock = data.get('lock')
    #print({lock})
    if not id or lock is None:
        raise HTTPException(status_code=400, detail="Missing required fields")

    pm = ProjectManager()
    success = pm.toggleLock(projectID=id,lockState=lock)
    return {"success": success}

@router.post("/status")
async def toggleProjectStatus(request: Request):
    data = await request.json()
    id = data.get("id")
    status = data.get('status')

    if not id or not status:
        raise HTTPException(status_code=400, detail="Missing required fields")
    pm = ProjectManager()
    
    success = pm.toggleStatus(id, status)
    return {"success": success}

@router.post("/export")
async def export_project(request: Request):
    data = await request.json()
    id = data.get('id')
    format = data.get('format')

    if not id or not format:
        raise HTTPException(status_code=400, detail="Missing required fields")
    
    pm = ProjectManager()

    if format.upper() == "CSV":
        csv_result = pm.exportProjectCSV(id)
        if not csv_result:
            raise HTTPException(status_code=404, detail="Project not found")

        csv_data = csv_result["csv"]
        return StreamingResponse(
            io.StringIO(csv_data),
            media_type="text/csv",
            headers={"Content-Disposition": f"attachment; filename=project_{id}.csv"}
        )
    elif format.upper() == "XML":
        csv_result = pm.exportProjectCSV(id)
        if not csv_result:
            raise HTTPException(status_code=404, detail="Project not found")

        csv_data = csv_result["csv"]

        # Convert CSV string to XML in-memory
        reader = csv.DictReader(io.StringIO(csv_data))
        root = ET.Element("records")

        for row in reader:
            record = ET.SubElement(root, "record")
            for key, value in row.items():
                elem = ET.SubElement(record, key)
                elem.text = value

        xml_io = io.StringIO()
        ET.ElementTree(root).write(xml_io, encoding='unicode', xml_declaration=True)
        xml_io.seek(0)

        return StreamingResponse(
            xml_io,
            media_type="application/xml",
            headers={"Content-Disposition": f"attachment; filename=project_{id}.xml"}
        )

    else:
        raise HTTPException(status_code=400, detail="Unsupported format")


@router.post("/create")
async def create_project(request: Request):
    data = await request.json()
    #print(data)
    name = data.get("projectName")
    #print(name)
    description = data.get("description", "")
    #print(description)
    ips = data.get("ips", [])
    #print(ips)
    ports = data.get("ports", [])
    #print(ports)
    initials = data.get("owner")
    #print(initials)  

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

    #print(project_id)
    if not project_id:
        raise HTTPException(status_code=400, detail="Project ID is required.")
    #print(project_id)
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
    
@router.post("/save")
async def saveProject(request: Request):
    pm = ProjectManager()
    data = await request.json()
    print(data)
    project_id = data.get("projectID")
    print(project_id)
    if not project_id:
        raise HTTPException(status_code=400, detail="Project ID is required.")
    try:
        project = pm.loadProject(project_id)
        if not project:
            raise HTTPException(status_code=404, detail="Project not found.")
        print(project)
        # Update project attributes from request data
        project.setName(data.get("name", project.getName()))
        project.setOwner(data.get("owner", project.getOwner()))
        project.setTimestamp(data.get("timestamp", project.getTimestamp()))
        project.setStatus(data.get("status", project.getStatus()))
        project.setLockStatus(data.get("lockStatus", project.getLockStatus()))
        project.setDescription(data.get("description", project.getDescription()))
        project.setIps(data.get("ips", project.getIps()))
        project.setPorts(data.get("ports", project.getPorts()))

        success = pm.updateProject(project)

        if success:
            return {"message": "Project updated successfully."}
        else:
            raise HTTPException(status_code=500, detail="Failed to update the project.")
    except Exception as e:
        print(f"Error occurred while saving project: {str(e)}")


@router.post("/invite")
async def inviteCollaborator():
    pass

@router.post("/listCollaborators")
async def getAllCollaborators():
    pass

@router.post("/uninvite")
async def removeCollaborator():
    pass

