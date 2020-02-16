import node
import constant

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

    def __influence_scanner(self, value):
        if isinstance(value, str):
            for character in value:
                if character in self.__vertices and character not in constant.CONSTANTS.OPERATORS:
                    (self.__vertices[character][1]).append(self.__rules[value])
                    #print(character, self.__vertices[character])
        else:
            raise Exception("Terminated point")

    def chain(self, parent, child, child_type):
        if isinstance(parent, str) and isinstance(child, str) and isinstance(child_type, node.NodeType):
            childObj = [child, child_type]
            self.__chainChildToParent(parent, childObj)
        else:
            raise Exception("Hmmm, I suppose you're swift-developer")

    def print_rules(self):
        for i in self.__rules:
            print(f'{i} =>')
            for x in self.__rules[i]:
                print(f'        >>>{x}')

    def print_vertices(self):
        for i in self.__vertices:
            print(f'{i} ->')
            print(self.__vertices[i])


    def __pushToGraph(self, value, valueType):
        if valueType == node.NodeType.RULE:
            if value in self.__rules:
                return False
            else:
                self.__rules[value] = list()
                self.__influence_scanner(value)
                return True
        elif valueType == node.NodeType.SYMBOL:
            if value not in self.__vertices:
                self.__vertices[value] = [node.Node(valueType, value, False), list()]
            return True
        return False

    def changeStatement(self, value, state):
        if isinstance(value, str) and isinstance(state, bool):
            if value in self.__vertices:
                self.__vertices[value][0].statement = state



