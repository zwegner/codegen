import codegen
import ast

def to_ast_and_back_again(source):
    return codegen.to_source(ast.parse(source))

def test_del():
    source = "del l[0]"
    assert source == to_ast_and_back_again(source)
    source = "del obj.x"
    assert source == to_ast_and_back_again(source)
    assert source == to_ast_and_back_again(source)
