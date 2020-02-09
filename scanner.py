import constant as symbols
import node
import  node_logic

def scanner(graphObj, formula):
    ### Formula -> list()
    ### Example: ['+AB', '=>', 'D'].
    ### formula[0] = '+AB'
    ### formula = const implies character. see at constant import.

    ### Take implies symbol
    if formula[1] == symbols.CONSTANTS.IMPLIES:
        graphObj.injection(formula[0], node.NodeType.RULE)
        graphObj.chain(formula[0], formula[2], node.NodeType.IMPLIES)
    elif formula[1] == symbols.CONSTANTS.DUBLEX_IMPLIES:
        graphObj.chain(formula[0], formula[2], node.NodeType.BICONDITIONAL)
    else:
        raise Exception('Undefined implies character')

    ## Take every character and put it to exist data-graph.
    for character in formula[0]:
        if character.isalpha():
            graphObj.injection(character, node.NodeType.SYMBOL)

    ## The same action for implies formula.
    for character in formula[2]:
        if character.isalpha():
            graphObj.injection(character, node.NodeType.SYMBOL)