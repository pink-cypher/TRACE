# backEnd/databasemanager/config.py

import time
from neo4j import GraphDatabase
from neo4j.exceptions import Neo4jError
from databasemanager.config.config_loader import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD 

class Neo4jDB:
    def __init__(self, max_retries=3, retry_delay=3):
        self.uri = NEO4J_URI
        self.user = NEO4J_USER
        self.password = NEO4J_PASSWORD

        self.driver = None 
        self.max_retries = max_retries
        self.retry_delay = retry_delay

        self._connect_with_retries()

    def _connect_with_retries(self):
        for attempt in range(1, self.max_retries + 1):
            try:
                print(f"Attempting to connect to Neo4j (Attempt {attempt}/{self.max_retries})...")
                self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))
                self._test_connection()
                print("Successfully connected to Neo4j.")
                return
            except Neo4jError as e:
                print(f"ERROR: Could not connect to Neo4j. Retrying in {self.retry_delay} seconds...")
                time.sleep(self.retry_delay)
            except Exception as e:
                print(f"ERROR: {e}")
                break 

        print("ERROR: Failed to connect to Neo4j after multiple attempts.")
        self.driver = None 

    def _test_connection(self):
        session = None
        try:
            session = self.get_session()
            session.run("RETURN 1") 
        except Exception as e:
            print(f"ERROR: Connection test failed - {e}")
            raise e
        finally:
            if session:
                session.close()

    def get_session(self):
        if self.driver:
            return self.driver.session()
        else:
            raise ConnectionError("Neo4j is not connected.")

    def close_driver(self):
        if self.driver:
            self.driver.close()
            print("Neo4j driver closed.")

neo4jConn = Neo4jDB()