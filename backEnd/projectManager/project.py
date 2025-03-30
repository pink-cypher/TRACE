class Project:
    def __init__(self, id, name, owner, timestamp, status="Active", lockStatus=False, description=""):
        self.__id = id
        self.__name = name
        self.__owner = owner
        self.__timestamp = timestamp
        self.__status = status
        self.__lockStatus = lockStatus
        self.__description = description

    def getID(self):
            return self.__id
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