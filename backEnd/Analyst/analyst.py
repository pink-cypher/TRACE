from databasemanager.databasemanager import db
class Analyst:

    def __init__(self, id=None, initials=None, role=None):
        self.__analystID = id
        self.__initials = initials
        self.__role = role

    def getAnalystID(self):
        return self.__analystID
    def setAnalystID(self,newID):
        self.__analystID = newID

    def getInitials(self):
        return self.__initials
    def setInitials(self, initials):
        self.__initials = initials

    def getRole(self):
        return self.__role
    def setRole(self, role):
        self.__role = role

    def getIslead(self):
        return self.getRole() == "Lead"


    def checkAnalyst(self, initals):
        if db.countAnalyst() == 0:
            return False
        return db.checkAnalyst(initals)

    def createAnalyst(self, initials, role):

        createdAnalyst = db.createAnalyst(initials, role)
        if createdAnalyst:
            self.setInitials(createdAnalyst.get("initials"))
            self.setRole(createdAnalyst.get("role"))
            self.setAnalystID(createdAnalyst.get("id"))
            return True
        else:
            return False

    
    def loadAnalyst(self,initials):
        return db.loadAnalyst(initials)
       
    def saveAnalyst(self, initials, role):

        if db.saveAnalyst(initials, role):
            self.setRole(role)
            return True
        else:
            return False