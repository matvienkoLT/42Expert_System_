import scanner
import node
import node_logic

# d = node.Node(node.NodeType.BLUE, "A", "STATEMENT")
# c = node.Node(node.NodeType.BLUE, "B", "STATEMENT")
# p = node.Node(node.NodeType.BLUE, "D", "STATEMENT")

graph = node_logic.NodeGraph()

test1 = ['AB+C+', '=>', 'D']
test2 = ['AB+C+G', '=>', 'C']
test5 = ['AB+C+G', '=>', 'KC+']
test3 = ['CD|', '=>', 'K']
test4 = ['AB+', '=>', 'Y+Z']

scanner.scanner(graph, test1)
scanner.scanner(graph, test2)
scanner.scanner(graph, test3)
scanner.scanner(graph, test4)
scanner.scanner(graph, test5)
#scanner.scanner(graph, test5)

graph.print()