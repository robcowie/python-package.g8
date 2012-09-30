# -*- coding: utf-8 -*-

import unittest


class TestSomething(unittest.TestCase):
    def test_something_else(self):
        self.assertEqual(True, True)


def get_suite():
    """Return a unittest.TestSuite."""
    import $package_name;format="lower,snake"$.tests

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule($package_name;format="lower,snake"$.tests)
    return suite
