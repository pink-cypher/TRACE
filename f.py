from transactions.cypher import Cypher


query = "MATCH (n) RETURN n LIMIT 1"

result = Cypher.run_transaction(query)
print(result)

