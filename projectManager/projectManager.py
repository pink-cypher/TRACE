from databasemanager.databasemanager import db
from projectManager.project import Project

class ProjectManager:

    def __init__(self, analyst):
        self.analyst = analyst

    def isLead(self):
        return self.analyst.getIslead()
    def isOwner(self):
        pass

    def isMember(self):
        pass

    def createProject(self, projectName, description):
        return db.storeProject(projectName,description, self.analyst.getInitials()) 
         
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

    def deleteOrArchiveProject(self, projectID, permanent):

        if permanent: # delete
            success = db.deleteProject(projectID)
            if success:
                return True
            else:
                return False
        else: # archieve
            result = db.archiveProject(projectID)
            return result if result else False