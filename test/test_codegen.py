import codegen
import ast

def to_ast_and_back_again(source):
    return codegen.to_source(ast.parse(source))

def test_del():
    source = "del l[0]"
    assert source == to_ast_and_back_again(source)
    source = "del obj.x"
    assert source == to_ast_and_back_again(source)

def test_try_expect():
    source = ("try:\n"
              "    '#'[2]\n"
              "except IndexError:\n"
              "    print 'What did you expect?!'")
    assert source == to_ast_and_back_again(source)
    source = ("try:\n"
              "    l = []\n"
              "    l[1]\n"
              "except IndexError, index_error:\n"
              "    print index_error")
    assert source == to_ast_and_back_again(source)

def test_import():
    source = "import intertools as iterators"
    assert source == to_ast_and_back_again(source)
    source = "from math import floor as fl, ceil as cl"
    assert source == to_ast_and_back_again(source)
