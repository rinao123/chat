# -*- coding:utf-8 -*-

import unittest
from tool import string

class TestString(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIsStringLike(self):
        self.assertEqual(string.isStringLike("啊啊啊"), True)
        self.assertEqual(string.isStringLike(u"棒棒棒"), True)
        self.assertEqual(string.isStringLike(111.2), False)
        self.assertEqual(string.isStringLike(True), False)
        self.assertEqual(string.isStringLike([1, 2, 3]), False)
        self.assertEqual(string.isStringLike({1:1, 2:2}), False)
        self.assertEqual(string.isStringLike(object()), False)
        self.assertEqual(string.isStringLike(None), False)

    def testDecodeIfNotUnicode(self):
        self.assertEqual(isinstance(string.decodeIfNotUnicode("啊啊啊", "utf-8"), unicode), True)
        self.assertEqual(isinstance(string.decodeIfNotUnicode(u"错错错", "utf-8"), unicode), True)
        self.assertEqual(isinstance(string.decodeIfNotUnicode(1.111, "utf-8"), unicode), True)
        self.assertEqual(isinstance(string.decodeIfNotUnicode(True, "utf-8"), unicode), True)
        self.assertEqual(isinstance(string.decodeIfNotUnicode([1, 2, 3], "utf-8"), unicode), True)
        self.assertEqual(isinstance(string.decodeIfNotUnicode({1:1, 2:2}, "utf-8"), unicode), True)
        self.assertEqual(isinstance(string.decodeIfNotUnicode(object(), "utf-8"), unicode), True)
        self.assertEqual(isinstance(string.decodeIfNotUnicode(None, "utf-8"), unicode), True)

if __name__ == "__main__":
    unittest.main()