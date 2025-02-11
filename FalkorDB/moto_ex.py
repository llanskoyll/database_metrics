from falkordb import FalkorDB

db = FalkorDB(host="falkordb", port=6379)

g = db.select_graph("MotoGP")
g.query(
    """CREATE (:Rider {name:'Valentino Rossi'})-[:rides]->(:Team {name:'Yamaha'}),
                  (:Rider {name:'Dani Pedrosa'})-[:rides]->(:Team {name:'Honda'}),
                  (:Rider {name:'Andrea Dovizioso'})-[:rides]->(:Team {name:'Ducati'})"""
)

res = g.query(
    """MATCH (r:Rider)-[:rides]->(t:Team)
                 WHERE t.name = 'Yamaha'
                 RETURN r.name"""
)

for row in res.result_set:
    print(row[0])

res = g.query(
    """MATCH (r:Rider)-[:rides]->(t:Team {name:'Ducati'})
                 RETURN count(r)"""
)

print(res.result_set[0][0])
