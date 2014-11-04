#!/usr/bin/env python
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import doctest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_depends
from trytond.tests.test_tryton import doctest_setup, doctest_teardown


class Aeat340TestCase(unittest.TestCase):
    'Test AEAT 340 module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('aeat_340_es')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            Aeat340TestCase))
    suite.addTests(doctest.DocFileSuite('scenario_aeat340.rst',
            setUp=doctest_setup, tearDown=doctest_teardown, encoding='utf-8',
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE))
    return suite
