import node
import node_logic

d = node.Node(node.NodeType.BLUE, "A", "STATEMENT")
c = node.Node(node.NodeType.BLUE, "B", "STATEMENT")
p = node.Node(node.NodeType.BLUE, "D", "STATEMENT")

graph = node_logic.NodeGraph()

graph.injection(d)
graph.chain(d, c)
graph.chain(d, p)
graph.print()