import node

class NodeGraph:
    def __init__(self):
        self.__vertices = dict()
        self.__rules = dict()

    def __chainChildToParent(self, parent, child):
        x = self.__rules[parent]

        for item in x:
            if item[0] == child[0]:
                raise Exception("HERE WE GO")
        x.append(child)

    def injection(self, value, valueType):
        if isinstance(value, str) and isinstance(valueType, node.NodeType):
            if self.__pushToGraph(value, valueType):
                return True
            else:
                return False
        else:
            raise Exception("Have you seen that? Just now you have shotten your leg")

    def chain(self, parent, child, child_type):
        if isinstance(parent, str) and isinstance(child, str) and isinstance(child_type, node.NodeType):
            childObj = [child, child_type]
            self.__chainChildToParent(parent, childObj)
        else:
            raise Exception("Hmmm, I suppose you're swift-developer")

    def print(self):
        for i in self.__rules:
            print(f'{i} =>')
            for x in self.__rules[i]:
                print(f'        >>>{x}')

    def __pushToGraph(self, value, valueType):
        if valueType == node.NodeType.RULE:
            if value in self.__rules:
                return False
            else:
                self.__rules[value] = list()
                return True
        elif valueType == node.NodeType.SYMBOL:
            self.__vertices[value] = node.Node(valueType, value, False)
            return True
        return False

    # def __scanner(self, value):
    #     if value.type == NodeType.BLUE:
    #         self.__pushToGraph(value)
    #     elif value.type == NodeType.RED:
    #         ...
    #     elif value.type == NodeType.GREEN:
    #         ...
    #     else:
    #         raise Exception("Undefined type of Node")

