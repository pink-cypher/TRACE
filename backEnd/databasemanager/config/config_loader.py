import os
import configparser

config_path = os.path.join(os.path.dirname(__file__), 'config.ini')

config = configparser.ConfigParser()
config.read(config_path)

# JWT settings
SECRET_KEY = config.get("JWT", "SECRET_KEY")
ALGORITHM = config.get("JWT", "ALGORITHM")

# Neo4j settings 
NEO4J_URI = config.get("NEO4J", "URI")
NEO4J_USER = config.get("NEO4J", "USER")
NEO4J_PASSWORD = config.get("NEO4J", "PASSWORD")