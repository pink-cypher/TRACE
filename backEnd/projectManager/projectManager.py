from databasemanager.databasemanager import db
from projectManager.project import Project

class ProjectManager:

    def __init__(self,):
        pass
        

    # def createProject(self, projectName, description):
    #     return db.storeProject(projectName,description, self.analyst.getInitials()) 
    def createProject(self, projectName, description, initials, ips, ports):
        return db.storeProject(projectName,description, initials, ips, ports) 
         
    def saveProject(self, project):
        updates = {
            "name": project.getName(),
            "owner": project.getOwner(),
            "timestamp": project.getTimestamp(),
            "status": project.getStatus(),
            "lockStatus": project.getLockStatus(),
            "description": project.getDescription()
        }

        return db.saveProject(updates,project.getID()) if True else False
    
    def loadProject(self, projectID):
        project =  db.retrieveProject(projectID)

        return Project(**project) if project else None

    def deleteProject(self, projectID):

        success = db.deleteProject(projectID)
        return True if success else False
