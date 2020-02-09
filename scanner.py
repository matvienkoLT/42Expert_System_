import constant as symbols
import node
import  node_logic

def scanner(graphObj, formula, type):
    ###AB+C+
    ###C
    if graphObj.injection(node.Node(type, formula[0], False)):
        graphObj.chain(formula[0], node.Node(node.NodeType.SYMBOL, formula[2], False))
    else:
        print('Current mode forbid overwriting for existing rules')

    if formula[1] == symbols.CONSTANTS.IMPLIES:
        ...
    else:
        ...

    for character in formula[0]:
        if character.isalpha():
            graphObj.injection(node.Node(type, character, False))