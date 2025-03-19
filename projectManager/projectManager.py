from transactions.cypher import Cypher
import json


class ProjectManager:

    # Project ID is automatically generated in DB and is unique
    # project name is unique
    # project owner who created the project
    # timestamp is when project was created
    # activeRange is when project is active
    # projectStatus is if project is "archieved or active"
    # losckStatus is if project is locked or unlocked
    # description is what project will do
    def createProject(projectName, owner, timeStamp, activeRange, projectStatus, lockStatus,description):
        cypher = """
            MATCH (pMaxID:Project)
            WITH coalesce(max(pMaxID.ID),0) + 1 as newID
            CREATE (project:Project {
                ID: newID, 
                name: $projectName,
                timestamp: $timeStamp,
                activeRange: $activeRange,
                status: $projectStatus,
                lockStatus: $lockStatus,
                description: $description,
            })
            WITH project
            MATCH (analyst:Analyst {name: $owner})
            MERGE (analyst)-[:CREATED]->(project)  
            RETURN project
            """
        param = {
            "projectName": projectName,
            "owner": owner,
            "timeStamp": timeStamp,
            "activeRange": activeRange,
            "projectStatus": projectStatus,
            "lockStatus": lockStatus,
            "description": description
            }
        
        try:
            CreatedProject =  Cypher.run_transaction(cypher=cypher, parameters=param, write=True)
            return CreatedProject
        except Exception as e:
            print("Error")
            return None