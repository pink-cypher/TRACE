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

    # Project ID is automatically generated in DB and is unique
    # project name is unique
    # project owner who created the project
    # timestamp is when project was created
    # projectStatus is if project is "archieved or active"
    # losckStatus is if project is locked or unlocked
    # description is what project will do
    def createProject(self, projectName, description):
        return db.storeProject(projectName,description,self.analyst.getMac(), datetime.now(), self.analyst.getInitials())
        
    def saveProject(self, project):
        updatedProject = db.saveProject(project)
        return updatedProject if updatedProject else None

    def loadProject(self, projectID):
        project =  db.loadProject(projectID)
        if project:
            return Project(**project)
        return None
