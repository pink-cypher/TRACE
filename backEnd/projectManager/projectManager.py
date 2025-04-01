from databasemanager.databasemanager import db
from projectManager.project import Project

class ProjectManager:

    def __init__(self,):
        pass
        
    def createProject(self, projectName, description, initials, ips, ports):
        return db.storeProject(projectName,description, initials, ips, ports)        
    def loadProject(self, projectID):
        project =  db.retrieveProject(projectID)

        return Project(**project) if project else None   
    def showExisting(self):
        return db.getAllProjects()
    # Used in full on edit project and clicks save
    def updateProject(self, project):
        updates = {
            "name": project.getName(),
            "owner": project.getOwner(),
            "timestamp": project.getTimestamp(),
            "status": project.getStatus(),
            "lockStatus": project.getLockStatus(),
            "description": project.getDescription(),
            "ips": project.getIps(),
            "ports": project.getPorts()
        }

        # Filter out None values
        updates = {k: v for k, v in updates.items() if v is not None}
        return db.saveProject(updates,project.getID())
    # Lock status update lock or unlock
    def toggleLock(self, projectID, lockState):
        return db.toggleLock(projectID, lockState)
    def toggleStatus(self, id, status):
        return db.toggleStatus(id, status)
    
    def exportProject(self, projectID, format="CSV"):
        pass
    
    # Delete project data
    def deleteProject(self, projectID):
        return db.deleteProject(projectID)
        
