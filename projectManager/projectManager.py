from transactions.cypher import Cypher
from datetime import datetime


class ProjectManager:

    def __init__(self, analyst):
        self.analyst = analyst

    def isLead(self):
        return self.analyst.islead
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

        cypher = """
            MATCH (pMaxID:Project)
            WITH coalesce(max(pMaxID.ID),0) + 1 as newID
            CREATE (project:Project {
                ID: newID, 
                name: $projectName,
                timestamp: $timeStamp,
                status: $projectStatus,
                lockStatus: $lockStatus,
                description: $description
            })
            WITH project
            MATCH (analyst:Analyst {mac: $mac})
            MERGE (analyst)-[:CREATED]->(project)  
            RETURN project
            """
        param = {
            "mac": self.analyst.mac,
            "projectName": projectName,
            "owner": self.analyst.initials,
            "timeStamp": datetime.now(),
            "projectStatus": "Active",
            "lockStatus": False,
            "description": description
            }
        
        try:
            CreatedProject =  Cypher.run_transaction(cypher=cypher, param=param, write=True)
            return CreatedProject
        except Exception as e:
            print(f"Error {e}")
            return None
        
    def saveProject():
        pass
    def loadProject():
        pass