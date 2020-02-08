import node

class NodeGraph:
    def __init__(self):
        self.__vertices = dict()

    def __pushToGraph(self, value):
        if value.name in self.__vertices:
            return False
        else:
            self.__vertices[value.name] = list()
            return True

    def __chainChildToParent(self, parent, child):
        x = self.__vertices[parent.name]
        x.append(child)

    def injection(self, value):
        if isinstance(value, node.Node):
            self.__pushToGraph(value)
        else:
            raise Exception("Have you seen that? Just now you have shotten your leg")

    def chain(self, parent, child):
        if isinstance(parent, node.Node) and isinstance(child, node.Node):
            self.__chainChildToParent(parent, child)
        else:
            raise Exception("Hmmm, I suppose you're swift-developer")

    def print(self):
        for i in self.__vertices:
            print(f'{i} =>')
            for x in self.__vertices[i]:
                print(f'        >>>{x.name}')
