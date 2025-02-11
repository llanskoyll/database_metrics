from neo4j import GraphDatabase
import os
import logging

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def log():
    return logging.getLogger(__name__)


class Driver:
    def __init__(self):
        try:
            uri = os.getenv("NEO4J_URI", "neo4j://neo4j:7687")
            username = os.getenv("NEO4J_USER", "neo4j")
            password = os.getenv("NEO4J_PASSWORD", "Neo4j")
            self.__driver = GraphDatabase.driver(
                uri, auth=(username, password), encrypted=False
            )
            self.__driver.verify_connectivity()
            log().info("Success connect to database")
        except Exception as e:
            log().error(f"Failed open driver: {e}")

    def __del__(self):
        try:
            if self.__driver:
                self.__driver.close()
                log().info("Success close to database")
        except Exception as e:
            log().error(f"Failed close driver: {e}")

    def get_driver(self):
        if self.__driver != None:
            return self.__driver
        else:
            raise Exception("Driver not load")
