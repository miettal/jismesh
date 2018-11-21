#!/usr/bin/env nosetests
# -*- coding: utf-8 -*-

import unittest
from jismesh.utils import to_meshcode

class TestToMeshcode(unittest.TestCase):
    # 東京タワー緯度 (度) 世界測地系
    lat_tokyo_tower = 35.658581
    # 東京タワー経度 (度) 世界測地系
    lon_tokyo_tower = 139.745433

    # 京都タワー緯度 (度) 世界測地系
    lat_kyoto_tower = 34.987574
    # 京都タワー経度 (度) 世界測地系
    lon_kyoto_tower = 135.759363

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_invalid_latitude(self):
        self.assertRaises(
            ValueError,
            lambda: to_meshcode(
                lat=-0.1,
                lon=self.lon_tokyo_tower,
                level=1))

        self.assertRaises(
            ValueError,
            lambda: to_meshcode(
                lat=66.66,
                lon=self.lon_tokyo_tower,
                level=1))

    def test_invalid_longitude(self):
        self.assertRaises(
            ValueError,
            lambda: to_meshcode(
                lat=self.lat_tokyo_tower,
                lon=99.99,
                level=1))

        self.assertRaises(
            ValueError,
            lambda: to_meshcode(
                lat=self.lat_tokyo_tower,
                lon=180,
                level=1))

    def test_unsupported_level(self):
        self.assertRaises(
            ValueError,
            lambda: to_meshcode(
                lat=self.lat_tokyo_tower,
                lon=self.lon_tokyo_tower,
                level=0))

    def _test_to_meshcode_helper(self, expected_meshcode, lat, lon, level):
        meshcode = to_meshcode(lat=lat, lon=lon, level=level)
        self.assertEqual(expected_meshcode, meshcode)

    def test_lv1_tokyo_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='5339',
            lat=self.lat_tokyo_tower,
            lon=self.lon_tokyo_tower,
            level=1)

    def test_40000_tokyo_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='53392',
            lat=self.lat_tokyo_tower,
            lon=self.lon_tokyo_tower,
            level=40000)

    def test_20000_tokyo_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='5339235',
            lat=self.lat_tokyo_tower,
            lon=self.lon_tokyo_tower,
            level=20000)

    def test_16000_tokyo_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='5339467',
            lat=self.lat_tokyo_tower,
            lon=self.lon_tokyo_tower,
            level=16000)

    def test_lv2_tokyo_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='533935',
            lat=self.lat_tokyo_tower,
            lon=self.lon_tokyo_tower,
            level=2)

    def test_8000_tokyo_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='5339476',
            lat=self.lat_tokyo_tower,
            lon=self.lon_tokyo_tower,
            level=8000)

    def test_5000_tokyo_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='5339354',
            lat=self.lat_tokyo_tower,
            lon=self.lon_tokyo_tower,
            level=5000)

    def test_4000_tokyo_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='533947637',
            lat=self.lat_tokyo_tower,
            lon=self.lon_tokyo_tower,
            level=4000)

    def test_2500_tokyo_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='533935446',
            lat=self.lat_tokyo_tower,
            lon=self.lon_tokyo_tower,
            level=2500)

    def test_2000_tokyo_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='533935885',
            lat=self.lat_tokyo_tower,
            lon=self.lon_tokyo_tower,
            level=2000)

    def test_lv3_tokyo_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='53393599',
            lat=self.lat_tokyo_tower,
            lon=self.lon_tokyo_tower,
            level=3)

    def test_lv4_tokyo_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='533935992',
            lat=self.lat_tokyo_tower,
            lon=self.lon_tokyo_tower,
            level=4)

    def test_lv5_tokyo_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='5339359921',
            lat=self.lat_tokyo_tower,
            lon=self.lon_tokyo_tower,
            level=5)

    def test_lv6_tokyo_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='53393599212',
            lat=self.lat_tokyo_tower,
            lon=self.lon_tokyo_tower,
            level=6)

    def test_lv1_kyoto_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='5235',
            lat=self.lat_kyoto_tower,
            lon=self.lon_kyoto_tower,
            level=1)

    def test_40000_kyoto_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='52352',
            lat=self.lat_kyoto_tower,
            lon=self.lon_kyoto_tower,
            level=40000)

    def test_20000_kyoto_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='5235245',
            lat=self.lat_kyoto_tower,
            lon=self.lon_kyoto_tower,
            level=20000)

    def test_16000_kyoto_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='5235467',
            lat=self.lat_kyoto_tower,
            lon=self.lon_kyoto_tower,
            level=16000)

    def test_lv2_kyoto_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='523536',
            lat=self.lat_kyoto_tower,
            lon=self.lon_kyoto_tower,
            level=2)

    def test_8000_kyoto_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='5235476',
            lat=self.lat_kyoto_tower,
            lon=self.lon_kyoto_tower,
            level=8000)

    def test_5000_kyoto_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='5235363',
            lat=self.lat_kyoto_tower,
            lon=self.lon_kyoto_tower,
            level=5000)

    def test_4000_kyoto_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='523547647',
            lat=self.lat_kyoto_tower,
            lon=self.lon_kyoto_tower,
            level=4000)

    def test_2500_kyoto_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='523536336',
            lat=self.lat_kyoto_tower,
            lon=self.lon_kyoto_tower,
            level=2500)

    def test_2000_kyoto_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='523536805',
            lat=self.lat_kyoto_tower,
            lon=self.lon_kyoto_tower,
            level=2000)

    def test_lv3_kyoto_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='52353680',
            lat=self.lat_kyoto_tower,
            lon=self.lon_kyoto_tower,
            level=3)

    def test_lv4_kyoto_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='523536804',
            lat=self.lat_kyoto_tower,
            lon=self.lon_kyoto_tower,
            level=4)

    def test_lv5_kyoto_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='5235368041',
            lat=self.lat_kyoto_tower,
            lon=self.lon_kyoto_tower,
            level=5)

    def test_lv6_kyoto_tower(self):
        self._test_to_meshcode_helper(
            expected_meshcode='52353680412',
            lat=self.lat_kyoto_tower,
            lon=self.lon_kyoto_tower,
            level=6)
