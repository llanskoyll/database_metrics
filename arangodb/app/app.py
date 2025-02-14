from arango import ArangoClient
import os

url = os.getenv("ARANGODB_URL")
client = ArangoClient(url)
db = client.db("_system")

graph_already = False
for el in db.graphs():
    if "school" in el["name"]:
        graph_already = True
        break

if graph_already == False:
    graph = db.create_graph("school")

    students = graph.create_vertex_collection("students")
    lectures = graph.create_vertex_collection("lectures")

    edges = graph.create_edge_definition(
        edge_collection="register",
        from_vertex_collections=["students"],
        to_vertex_collections=["lectures"]
    )

    students.insert({"_key": "01", "full_name": "Anna Smith"})
    students.insert({"_key": "02", "full_name": "Jake Clark"})
    students.insert({"_key": "03", "full_name": "Lisa Jones"})

    lectures.insert({"_key": "MAT101", "title": "Calculus"})
    lectures.insert({"_key": "STA101", "title": "Statistics"})
    lectures.insert({"_key": "CSC101", "title": "Algorithms"})

    edges.insert({"_from": "students/01", "_to": "lectures/MAT101"})
    edges.insert({"_from": "students/01", "_to": "lectures/STA101"})
    edges.insert({"_from": "students/01", "_to": "lectures/CSC101"})
    edges.insert({"_from": "students/02", "_to": "lectures/MAT101"})
    edges.insert({"_from": "students/02", "_to": "lectures/STA101"})
    edges.insert({"_from": "students/03", "_to": "lectures/CSC101"})

query = """
    FOR v, e, p IN 1..3 OUTBOUND 'students/01' GRAPH 'school'
    OPTIONS { bfs: true, uniqueVertices: 'global' }
    RETURN {vertex: v, edge: e, path: p}
    """
cursor = db.aql.execute(query)
