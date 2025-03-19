from config.neo4j_config import neo4jConn

class Cypher:
    @staticmethod
    def run_transaction(cypher, param=None, write=False):
        """
        Runs a transaction safely with retries.
        
        - `write=False`: Runs a **read query** (`execute_read()`).
        - `write=True`:  Runs a **write query** (`execute_write()`).
        """
        session = neo4jConn.get_session()  

        try:
            if write:
                return session.execute_write(Cypher._transaction_with_rollback, cypher, param)
            else:
                return session.execute_read(Cypher._transaction_run, cypher, param)
        finally:
            session.close()  

    @staticmethod
    def _transaction_run(tx, query, parameters):
        return list(tx.run(query, parameters))  
    
    @staticmethod
    def _transaction_with_rollback(tx, query, parameters):
        try:
            result = list(tx.run(query, parameters))
            return result  
        except Exception as e:
            raise e  
