from databasemanager.databasemanager import db

class Analyst:

    def __init__(self, id=None, initials=None, role=None, isLead=None):
        self.__analystID = id
        self.__initials = initials
        self.__role = role
        self.__islead = isLead

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
        return self.__islead
    def setIslead(self, islead):
        self.__islead = islead

    def checkAnalyst(self, initals):
        if db.countAnalyst() == 0:
            return False
        return db.checkAnalyst(initals)

    def createAnalyst(self, initials, role, islead):

        createdAnalyst = db.createAnalyst(initials, role, islead)
        if createdAnalyst:
            self.setInitials(createdAnalyst.get("initials"))
            self.setRole(createdAnalyst.get("role"))
            self.setIslead(createdAnalyst.get("islead"))
            self.setAnalystID(createdAnalyst.get("id"))
            return True
        else:
            False

    
    def loadAnalyst(self,initials):
        return db.loadAnalyst(initials)
       
    def saveAnalyst(self, initials, role, islead):

        if db.saveAnalyst(initials, role, islead):
            self.setRole(role)
            self.setIslead(islead)
            return True
        else:
            False