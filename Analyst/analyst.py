from getmac import get_mac_address
from databasemanager.databasemanager import db

class Analyst:

    def __init__(self, id=None, initials=None, role=None, isLead=None, mac=None):
        self.__analystID = id
        self.__initials = initials
        self.__role = role
        self.__islead = isLead
        self.__mac = mac if mac else get_mac_address()

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

    def getMac(self):
        return self.__mac

    def checkAnalyst(self):
        if db.countAnalyst() == 0:
            return None
        analystResult = db.checkAnalyst(self.getMac())
        return analystResult

    def createAnalyst(self, initials, role, islead):
        self.setInitials(initials)
        self.setRole(role)
        self.setIslead(islead)
        createdAnalyst = db.createAnalyst(self.getInitials(), self.getRole(), self.getIslead(),self.getMac())
        self.setAnalystID(createdAnalyst["ID"])
        return True if createdAnalyst else False
