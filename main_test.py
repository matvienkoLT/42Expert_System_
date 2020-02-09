import scanner
import node
import node_logic

# d = node.Node(node.NodeType.BLUE, "A", "STATEMENT")
# c = node.Node(node.NodeType.BLUE, "B", "STATEMENT")
# p = node.Node(node.NodeType.BLUE, "D", "STATEMENT")

graph = node_logic.NodeGraph()

test1 = ['AB+C+', '=>', 'D']
test2 = ['AB+C+G', '=>', 'C']

scanner.scanner(graph, test1, node.NodeType.RULE)
scanner.scanner(graph, test2, node.NodeType.RULE)

graph.print()