from .config.neo4j_config import Neo4jDB

class DatabaseManager:

    def __init__(self):
        self.db = Neo4jDB()

    def runCypher(self, cypher, param=None, write=False):

        session = self.db.get_session()

        try:
            if write:
                return session.execute_write(self._run_transaction, cypher, param)
            else:
                return session.execute_read(self._run_transaction, cypher, param)
        finally:
            session.close()
    def _run_transaction(self,tx, cypher, param):
        try:
            return list(tx.run(cypher, param or {}))
        except Exception as e:
            print(f"ERROR: Transaction failed - {e}")
            raise e 

    def checkAnalyst(self, initials):
        cypher = """
                MATCH (analyst:Analyst {initials: $initials})
                RETURN analyst
                """
        return bool(self.runCypher(cypher, {"initials": initials}))
    def createAnalyst(self, initials, role):
        cypher = """
            CREATE (analyst:Analyst {
                initials: $initials, 
                role: $role
            })
            RETURN analyst {.*, id: elementid(analyst)}
            """
        
        param = {
                "initials": initials,
                "role": role
            }
        analystResult = self.runCypher(cypher, param, write=True)
        return analystResult[0].get("analyst") if analystResult else None 
    def loadAnalyst(self, initials):
        cypher = """
                MATCH (analyst:Analyst {initials: $initials})
                RETURN analyst {.*, id: elementid(analyst)}
                """
        result = self.runCypher(cypher, {"initials": initials})
        return result[0].get('analyst') if result else None
    def countAnalyst(self):
        cypher = """MATCH (a:Analyst) RETURN count(a) AS count"""
        anlaystResult = self.runCypher(cypher)
        return anlaystResult[0].get('count', 0) if anlaystResult else 0
    def saveAnalyst(self, initials, role):
        cypher = """MATCH  (a:Analyst {initials: $initials})
                    SET a.role = $role
                    RETURN a
                 """
        param = {
                "initials": initials,
                "role": role
            }
        return True if self.runCypher(cypher, param, write=True) else False

    def storeProject(self, projectName, description, owner, ips, ports):
        cypher = """
            CREATE (project:Project {
                name: $projectName,
                owner: $owner,
                timestamp: datetime(),
                status: "Active",
                lockStatus: False,
                description: $description,
                ips: $ips,
                ports: $ports
            })
            WITH project
            MATCH (analyst:Analyst {initials: $owner})
            MERGE (analyst)-[:CREATED]->(project)  
            RETURN project {.*, id: elementid(project)}
        """
        param = {
            "projectName": projectName,
            "owner": owner,
            "description": description,
            "initials":owner,
            "ips": ips,      
            "ports": ports
        }
        return True if self.runCypher(cypher, param, write=True) else False
    def retrieveProject(self, projectID):
        if projectID:
            cypher = "MATCH (project:Project) WHERE elementId(project)= $projectID RETURN project {.*, id: elementId(project)}"
            param = {"projectID": projectID}
        else:
            return None
        project = self.runCypher(cypher, param)
        return project[0].get('project') if project else None
    def saveProject(self, updates, id):
        set_clause = ", ".join([f"project.{key} = ${key}" for key in updates.keys()])
        updates["id"] = id
        cypher =f"""
                MATCH (project:Project) 
                WHERE elementId(project) = $id
                SET {set_clause}
                RETURN project
                """
        return True if self.runCypher(cypher, updates, write=True) else False
    
    def deleteProject(self, projectID):
        cypher = """
                MATCH (p:Project {ID: $ID})
                OPTIONAL MATCH (p)-[r]-(n)
                WHERE NOT n:Analyst
                DETACH DELETE r, n
                WITH p
                DETACH DELETE p
                RETURN true AS deleted
                """
        result = self.runCypher(cypher, {'ID':projectID}, write=True)
        if result and result[0]['deleted']:
            return True
        else:
            return False
        
    def archiveProject(self, projectID):
        cypher = """
                MATCH (project:Project)
                WHERE elementId(project)= $projectID
                SET project.status = "Archived"
                RETURN true as archived
                """
        result = self.runCypher(cypher, {'projectID':projectID}, write=True)
        return result and result[0].get('archived', False)

db = DatabaseManager()