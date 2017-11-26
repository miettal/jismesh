#!/usr/bin/env nosetests
# -*- coding: utf-8 -*-

import unittest
from jismesh.utils import to_meshlevel

class TestToMeshlevel(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_invalid_meshcode(self):
        self.assertRaises(
            ValueError,
            lambda: to_meshlevel(meshcode='0'))

    def _test_to_meshlevel_helper(self, expected_level, meshcode):
        level = to_meshlevel(meshcode=meshcode)
        self.assertEqual(expected_level, level)

    def test_lv1(self):
        self._test_to_meshlevel_helper(
            expected_level=1,
            meshcode='5339')

    def test_40000(self):
        self._test_to_meshlevel_helper(
            expected_level=40000,
            meshcode='53392')

    def test_20000(self):
        self._test_to_meshlevel_helper(
            expected_level=20000,
            meshcode='5339235')

    def test_lv2(self):
        self._test_to_meshlevel_helper(
            expected_level=2,
            meshcode='533935')

    def test_5000(self):
        self._test_to_meshlevel_helper(
            expected_level=5000,
            meshcode='5339354')

    def test_2500(self):
        self._test_to_meshlevel_helper(
            expected_level=2500,
            meshcode='533935446')

    def test_2000(self):
        self._test_to_meshlevel_helper(
            expected_level=2000,
            meshcode='533935885')

    def test_lv3(self):
        self._test_to_meshlevel_helper(
            expected_level=3,
            meshcode='53393599')

    def test_lv4(self):
        self._test_to_meshlevel_helper(
            expected_level=4,
            meshcode='533935992')

    def test_lv5(self):
        self._test_to_meshlevel_helper(
            expected_level=5,
            meshcode='5339359921')

    def test_lv6(self):
        self._test_to_meshlevel_helper(
            expected_level=6,
            meshcode='53393599212')
