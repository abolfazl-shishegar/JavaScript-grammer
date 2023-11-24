from anytree import Node, RenderTree
from anytree.exporter import DotExporter

# Define the grammar rules
grammar_rules = {
    "Program": ["StatementList"],
    "StatementList": ["Statement", "Statement ; StatementList"],
    "Statement": [
        "VariableDeclaration",
        "IfStatement",
        "WhileStatement",
        "FunctionDeclaration",
        "ExpressionStatement",
    ],
    "VariableDeclaration": ["let Identifier = Expression"],
    "IfStatement": [
        "if ( Expression ) { StatementList }",
        "if ( Expression ) { StatementList } else { StatementList }",
    ],
    "WhileStatement": ["while ( Expression ) { StatementList }"],
    "FunctionDeclaration": ["function Identifier ( ParameterList ) { StatementList }"],
    "ParameterList": ["ε", "IdentifierList"],
    "IdentifierList": ["Identifier", "Identifier, IdentifierList"],
    "ExpressionStatement": ["Expression"],
    "Expression": ["AssignmentExpression"],
    "AssignmentExpression": ["LogicalOrExpression", "LogicalOrExpression = AssignmentExpression"],
    "LogicalOrExpression": ["LogicalAndExpression", "LogicalOrExpression || LogicalAndExpression"],
    "LogicalAndExpression": ["EqualityExpression", "LogicalAndExpression && EqualityExpression"],
    "EqualityExpression": ["RelationalExpression", "EqualityExpression EqualityOperator RelationalExpression"],
    "EqualityOperator": ["==", "!="],
    "RelationalExpression": ["AdditiveExpression", "RelationalExpression RelationalOperator AdditiveExpression"],
    "RelationalOperator": ["<", "<=", ">", ">="],
    "AdditiveExpression": ["MultiplicativeExpression", "AdditiveExpression AdditiveOperator MultiplicativeExpression"],
    "AdditiveOperator": ["+", "-"],
    "MultiplicativeExpression": ["UnaryExpression", "MultiplicativeExpression MultiplicativeOperator UnaryExpression"],
    "MultiplicativeOperator": ["*", "/"],
    "UnaryExpression": ["PrimaryExpression", "! UnaryExpression", "UnaryOperator UnaryExpression"],
    "UnaryOperator": ["-", "+"],
    "PrimaryExpression": ["Literal", "( AssignmentExpression )", "Identifier", "FunctionCall"],
    "Literal": ["BooleanLiteral", "NumericLiteral", "StringLiteral"],
    "BooleanLiteral": ["true", "false"],
    "NumericLiteral": ["[0-9]+"],
    "StringLiteral": ['"[^"]*"', "'[^']*'"],
    "Identifier": ["[a-zA-Z_][a-zA-Z0-9_]*"],
    "FunctionCall": ["Identifier ( ArgumentList )"],
    "ArgumentList": ["ε", "AssignmentExpression", "AssignmentExpression, ArgumentList"],
}

# Create a tree based on the grammar
def create_tree(node, rule):
    for token in reversed(grammar_rules[rule]):
        child = Node(token, parent=node)
        if token in grammar_rules:
            create_tree(child, token)

# Create the root node and build the tree
root = Node("Program")
create_tree(root, "Program")

# Print the tree using anytree's RenderTree
for pre, fill, node in RenderTree(root):
    print(f"{pre}{node.name}")
    