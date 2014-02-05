import unittest
import codegen
import ast

class TestCodegen(unittest.TestCase):

    def assertPreserved(self, code):
        result = codegen.to_source(ast.parse(code))
        self.assertEqual(result.rstrip(), code.rstrip())

    def test_Pow(self):
        self.assertPreserved("y = (x ** 2)")

    def test_del(self):
        self.assertPreserved("del l[0]")
        self.assertPreserved("del obj.x")

    def test_try_expect(self):
        source = ("try:\n"
                  "    '#'[2]\n"
                  "except IndexError:\n"
                  "    print 'What did you expect?!'")
        self.assertPreserved(source)
        source = ("try:\n"
                  "    l = []\n"
                  "    l[1]\n"
                  "except IndexError, index_error:\n"
                  "    print index_error")
        self.assertPreserved(source)

    def test_import(self):
        self.assertPreserved("import intertools as iterators")
        self.assertPreserved("from math import floor as fl, ceil as cl")


if __name__ == '__main__':
  unittest.main()
