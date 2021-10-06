import unittest
from unittest import TestCase

import lca


class Test(unittest.TestCase):
    def test_find_lca(self):
        #self.fail()
        self.tree =lca.build()

        def test(self):

            assert(lca.findLCA(self.tree, 6, 7 ) ==3)
            assert (lca.findLCA(self.tree, 4, 5) == 2)
            assert (lca.findLCA(self.tree, 4, 6) == 1)
