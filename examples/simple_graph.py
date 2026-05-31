from infoweave import Graph

graph = Graph()

graph.add_concept(
    id="reasoning",
    name="Reasoning"
)

graph.add_concept(
    id="planning",
    name="Planning"
)

graph.link(
    "reasoning",
    "supports",
    "planning"
)

print(graph)
