# -*- coding: utf-8 -*-

# RUNME as 'python -m $package_name;format="lower,snake"$.tests.__main__'

import unittest
import $package_name;format="lower,snake"$.tests


def main():
    "Run all of the tests when run as a module with -m."
    suite = $package_name;format="lower,snake"$.tests.get_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    main()
