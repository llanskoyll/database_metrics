from neo4j import RoutingControl


class DBWrapper:
    def __init__(self, driver):
        self.driver = driver

    def execute_query_write(self, query, **params):
        return self.driver.get_driver().execute_query(
            query, params, database_="neo4j", routing_=RoutingControl.WRITE
        )

    def execute_query_read(self, query, **params):
        return self.driver.get_driver().execute_query(
            query, params, database_="neo4j", routing_=RoutingControl.READ
        )
