import scanner
import node
import node_logic

# d = node.Node(node.NodeType.BLUE, "A", "STATEMENT")
# c = node.Node(node.NodeType.BLUE, "B", "STATEMENT")
# p = node.Node(node.NodeType.BLUE, "D", "STATEMENT")

graph = node_logic.NodeGraph()

test1 = ['C', '=>', 'E']
test2 = ['AB+C+', '=>', 'D']
test5 = ['AB|', '=>', 'C']
test3 = ['A!B+', '=>', 'F']
test4 = ['C!G|', '=>', 'H']
test5 = ['VW^', '=>', 'X']
test6 = ['AB+', '=>', 'YZ+']
test7 = ['CD|', '=>', 'XV|']
test8 = ['EF+', '=>', '!V']
test9 = ['AB+', '=>', 'C']
#test10 = ['EF+', '=>', '!V']




scanner.scanner(graph, test1)
scanner.scanner(graph, test2)
scanner.scanner(graph, test3)
scanner.scanner(graph, test4)
scanner.scanner(graph, test5)
scanner.scanner(graph, test6)
scanner.scanner(graph, test7)
scanner.scanner(graph, test8)
scanner.scanner(graph, test9)


#scanner.scanner(graph, test5)

graph.print_vertices()