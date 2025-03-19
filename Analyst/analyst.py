import os
from transactions.cypher import Cypher


class Analyst:

    def __init__(self, analystId=None, initials=None, role=None, isLead=None, mac=None):
        self.analystID = analystId
        self.initials = initials
        self.role = role
        self.islead = isLead
        self.mac = mac if mac else self.getMac()

    def getMac(self):
        return [line.split()[-1] for line in (x.strip() for x in os.popen("ifconfig | grep ether")) if line][0]

    def checkAnalyst(self):
        
        cypher = """
            MATCH (a:Analyst) RETURN count(a) AS count
            """
        result = Cypher.run_transaction(cypher)

        if result[0]["count"] == 0:
            return None 
        
        cypher = """
                MATCH (analyst:Analyst {mac: $mac})
                RETURN analyst
                """
        anlaystResult = Cypher.run_transaction(cypher, {"mac": self.mac})
        return anlaystResult[0]["analyst"] if  anlaystResult else None
    
    def createAnalyst(self, initials, role, isLead):
        cypher = """
            MATCH (aMax:Analyst)
            WITH coalesce(max(aMax.ID),0) + 1 as newID
            CREATE (a:Analyst {
                ID: newID,
                mac: $mac, 
                initials: $initials, 
                role: $role,
                isLead: $isLead
            })
            RETURN a
            """
        
        param = {
                "mac": self.mac,
                "initials": initials,
                "role": role,
                "isLead": isLead
            }
        analystResult = Cypher.run_transaction(cypher, param, write=True)
        return analystResult[0]["a"]

