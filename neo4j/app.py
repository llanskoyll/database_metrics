import db_driver
import db_wrapper

def print_accounts(wrapper, name):
    query = (
        "MATCH (b:Bank)-[:HAVE]->(a:Account) WHERE b.name = $name "
        "RETURN a.sum ORDER BY a.sum"
    )
    # records, _, _ = wrapper.execute_query_read(query, name=name)
    # for record in records:
    #         print(record["a.sum"])


def add_accounts(wrapper, name, sums):
    query = """
    MERGE (b:Bank {name: $name})
    WITH b, $sums AS accountSums
    UNWIND accountSums AS accountSum
    CREATE (a:Account {id: randomUUID(), sum: accountSum})
    MERGE (b)-[:HAVE]->(a)
    """
    wrapper.execute_query_write(query, name=name, sums=sums)


if __name__ == "__main__":
    wrapper = db_wrapper.DBWrapper(db_driver.Driver())

    account_sums = list(range(100))
    add_accounts(wrapper, "SBER", account_sums)
    print_accounts(wrapper, "SBER")
