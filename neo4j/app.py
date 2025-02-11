import db_driver
import db_wrapper
import time


def print_friends(wrapper, name):
    query = (
        "MATCH (a:Person)-[:KNOWS]->(friend) WHERE a.name = $name "
        "RETURN friend.name ORDER BY friend.name"
    )
    records, _, _ = wrapper.execute_query_read(query, name=name)
    for record in records:
        print(record["friend.name"])


def add_friend(wrapper, name, friend_name):
    query = (
        "MERGE (a:Person {name: $name}) "
        "MERGE (friend:Person {name: $friend_name}) "
        "MERGE (a)-[:KNOWS]->(friend)"
    )
    wrapper.execute_query_write(query, name=name, friend_name=friend_name)


if __name__ == "__main__":
    time.sleep(6)
    wrapper = db_wrapper.DBWrapper(db_driver.Driver())

    add_friend(wrapper, "Arthur", "Guinevere")
    add_friend(wrapper, "Arthur", "Lancelot")
    add_friend(wrapper, "Arthur", "Merlin")
    print_friends(wrapper, "Arthur")
