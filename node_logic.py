import node
import constant
import logging
import operator
from datetime import datetime

class NodeGraph:
    def __init__(self, loggingMode):
        self.__vertices = dict()
        self.__rules = dict()
        if loggingMode:
            logging.basicConfig(filename=f'Logic_{str(datetime.now())}.log', level=logging.INFO)

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
                    (self.__vertices[character][1]).append(value)
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
                calculus = self.__PropositionalMath(value, self.__vertices).statement

    def solveRule(self, rule):
        calculus = self.__PropositionalMath(rule, self.__vertices).statement
        print(calculus)

    class __PropositionalMath:
        def __init__(self, rule, __vertices):
            self.__vertices = __vertices
            self.__rule = rule
            self.__statement = 'Undefined'
            if isinstance(rule, str):
                rule_size = len(rule)
                if rule_size <= 0: raise Exception("Rule isn't valid")  ### checking if string is empty
                elif rule_size == 1: ### checking if string have just one symbol.
                    object = self.__seekVertix(rule)
                    if object:
                        self.__statement = object.statement
                        print(self.__statement)
                else:
                    self.__doCalculus()
            else:
                raise Exception("Have you seen that? Just now you have shotten your leg")

        @property
        def statement(self):
            return self.__statement

        def __seekVertix(self, symbol):
            if symbol in self.__vertices:
                logging.info(f'Changed statement of object::{self.__vertices[symbol][0]} '\
                                                            f'{self.__vertices[symbol][0].name}::'\
                                                            f'{self.__vertices[symbol][0].statement}')
                return self.__vertices[symbol][0]
            else:
                return None

        def __calculusHelper(self, character):
            if character == constant.CONSTANTS.OPERATOR_NOT:
                return operator.not_
            elif character == constant.CONSTANTS.OPERATOR_AND:
                return operator.and_
            elif character == constant.CONSTANTS.OPERATOR_OR:
                return operator.or_
            elif character == constant.CONSTANTS.OPERATOR_XOR:
                return  operator.xor
            else:
                return  constant.CONSTANTS.OPERATOR_SYMBOL

        def __doCalculus(self):
            operand0 = None
            operand1 = None
            resultState = None

            for character in self.__rule:
                noDistributed = self.__calculusHelper(character)

                if noDistributed ==  constant.CONSTANTS.OPERATOR_SYMBOL:
                    if operand0 == None: operand0 = self.__vertices[character][0].statement
                    elif operand1 == None: operand1 =self.__vertices[character][0].statement
                    else: raise Exception('Involked undefined operand behavior')
                else:
                    curr_operator = noDistributed

                    if curr_operator == operator.not_:
                        resultState = curr_operator(operand0)
                    else:
                        resultState = curr_operator(operand0, operand1)
                    operand0 =resultState
                    operand1 = None
            print(resultState)
            ##print(resultState)

            ## Note: The first boolean is intialization status:
            # #False = Uninitialized
            ## Second Boolean is Statement of object
            # _operand0 = [False, False]
            # _operand1 = [False, False]
            # _operator = [False, None]

            # for character in self.__rule:
            #     tempOperator = self.__calculusHelper(character)
            #     if tempOperator == constant.CONSTANTS.OPERATOR_SYMBOL:
            #         if _operand0[0] == False:
            #             _operand0[0] = True
            #             _operand0[1] = self.__vertices[character][0].statement
            #             if _operator[0] and _operator[1] == operator.not_:
            #                 _operand0[1] = _operator[1](_operand0[1])
            #                 _operator[0] = False
            #         else:
            #             _operand1[0] = True
            #             _operand1[1] = self.__vertices[character][0].statement
            #             if _operator[0] and _operator[1] == operator.not_:
            #                 _operand1[1] = _operator[1](_operand1[1])
            #                 _operator[0] = False
            #     elif tempOperator == operator.not_:
            #         _operator[0] = True
            #         _operator[1] = tempOperator
            #     else:
            #         print('HERE')