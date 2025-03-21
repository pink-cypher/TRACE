from datetime import datetime
from databasemanager.databasemanager import db


class Project:
    def __init__(self, ID, name, owner, timestamp, status="Active", lockStatus=False, description=""):
        self.__ID = ID
        self.__name = name
        self.__owner = owner
        self.__timestamp = timestamp
        self.__status = status
        self.__lockStatus = lockStatus
        self.__description = description


    def getID(self):
            return self.__ID
    def getName(self):
        return self.__name
    def setName(self, newName):
        self.__name = newName

    def getOwner(self):
        return self.__owner

    def getTimestamp(self):
        return self.__timestamp

    def getStatus(self):
        return self.__status
    def setStatus(self, newStatus):
        self.__status = newStatus

    def getLockStatus(self):
        return self.__lockStatus
    def setLockStatus(self, newLockStatus):
        self.__lockStatus = newLockStatus

    def getDescription(self):
        return self.__description
    def setDescription(self, newDescription):
        self.__description = newDescription

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
        return db.storeProject(projectName,description,self.analyst.getMac(), datetime.now(), self.analyst.getInitials())      
    def saveProject(self, project):
        updates = {
            "ID": project.getID(),
            "name": project.getName(),
            "owner": project.getOwner(),
            "timestamp": project.getTimestamp(),
            "status": project.getStatus(),
            "lockStatus": project.getLockStatus(),
            "description": project.getDescription()
        }
        print(updates)

        updatedProject = db.saveProject(updates)
        return updatedProject if updatedProject else None
    def loadProject(self, projectID):
        project =  db.retrieveProject(projectID)
        if project:
            return Project(**project)
        return None

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