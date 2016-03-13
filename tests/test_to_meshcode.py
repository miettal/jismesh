#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from mesh.utils import to_meshcode

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

    def test_to_meshcode_illigal_lvel(self):
        self.assertRaises(
                ValueError, 
                lambda: to_meshcode(
                            lat=self.lat_tokyo_tower,
                            lon=self.lon_tokyo_tower,
                            level=0)
                )

    def _test_to_meshcode_helper(self, expected_meshcode, lat, lon, level):
        meshcode = to_meshcode(lat=lat, lon=lon, level=level)
        self.assertEqual(expected_meshcode, meshcode)

    def test_to_meshcode_lv1_tokyo_tower(self):
        self._test_to_meshcode_helper(
                expected_meshcode='5339',
                lat=self.lat_tokyo_tower,
                lon=self.lon_tokyo_tower,
                level=1)

    def test_to_meshcode_lv2_tokyo_tower(self):
        meshcode_lv2 = to_meshcode(
                lat=self.lat_tokyo_tower,
                lon=self.lon_tokyo_tower,
                level=2)

        expected_meshcode_lv2 = '533935'
        self.assertEqual(expected_meshcode_lv2, meshcode_lv2)
    
    def test_to_meshcode_5000_tokyo_tower(self):
        meshcode_5000 = to_meshcode(
                lat=self.lat_tokyo_tower,
                lon=self.lon_tokyo_tower,
                level=5000)

        expected_meshcode_5000 = '5339354'
        self.assertEqual(expected_meshcode_5000, meshcode_5000)

    def test_to_meshcode_2000_tokyo_tower(self):
        meshcode_2000 = to_meshcode(
                lat=self.lat_tokyo_tower,
                lon=self.lon_tokyo_tower,
                level=2000)

        expected_meshcode_2000 = '533935885'
        self.assertEqual(expected_meshcode_2000, meshcode_2000)

    def test_to_meshcode_lv3_tokyo_tower(self):
        meshcode_lv3 = to_meshcode(
                lat=self.lat_tokyo_tower,
                lon=self.lon_tokyo_tower,
                level=3)

        expected_meshcode_lv3 = '53393599'
        self.assertEqual(expected_meshcode_lv3, meshcode_lv3)

    def test_to_meshcode_lv4_tokyo_tower(self):
        meshcode_lv4 = to_meshcode(
                lat=self.lat_tokyo_tower,
                lon=self.lon_tokyo_tower,
                level=4)

        expected_meshcode_lv4 = '533935992'
        self.assertEqual(expected_meshcode_lv4, meshcode_lv4)

    def test_to_meshcode_lv5_tokyo_tower(self):
        meshcode_lv5 = to_meshcode(
                lat=self.lat_tokyo_tower,
                lon=self.lon_tokyo_tower,
                level=5)

        expected_meshcode_lv5 = '5339359921'
        self.assertEqual(expected_meshcode_lv5, meshcode_lv5)

    def test_to_meshcode_lv6_tokyo_tower(self):
        meshcode_lv6 = to_meshcode(
                lat=self.lat_tokyo_tower,
                lon=self.lon_tokyo_tower,
                level=6)

        expected_meshcode_lv6 = '53393599212'
        self.assertEqual(expected_meshcode_lv6, meshcode_lv6)

    def test_to_meshcode_100_tokyo_tower(self):
        meshcode_100 = to_meshcode(
                lat=self.lat_tokyo_tower,
                lon=self.lon_tokyo_tower,
                level=100)

        expected_meshcode_100 = '5339359906'
        self.assertEqual(expected_meshcode_100, meshcode_100)

    def test_to_meshcode_lv1_kyoto_tower(self):
        meshcode_lv1 = to_meshcode(
                lat=self.lat_kyoto_tower,
                lon=self.lon_kyoto_tower,
                level=1)

        expected_meshcode_lv1 = '5235'
        self.assertEqual(expected_meshcode_lv1, meshcode_lv1)

    def test_to_meshcode_lv2_kyoto_tower(self):
        meshcode_lv2 = to_meshcode(
                lat=self.lat_kyoto_tower,
                lon=self.lon_kyoto_tower,
                level=2)

        expected_meshcode_lv2 = '523536'
        self.assertEqual(expected_meshcode_lv2, meshcode_lv2)

    def test_to_meshcode_5000_kyoto_tower(self):
        meshcode_5000 = to_meshcode(
                lat=self.lat_kyoto_tower,
                lon=self.lon_kyoto_tower,
                level=5000)

        expected_meshcode_5000 = '5235363'
        self.assertEqual(expected_meshcode_5000, meshcode_5000)

    def test_to_meshcode_2000_kyoto_tower(self):
        meshcode_2000 = to_meshcode(
                lat=self.lat_kyoto_tower,
                lon=self.lon_kyoto_tower,
                level=2000)

        expected_meshcode_2000 = '523536805'
        self.assertEqual(expected_meshcode_2000, meshcode_2000)

    def test_to_meshcode_lv3_kyoto_tower(self):
        meshcode_lv3 = to_meshcode(
                lat=self.lat_kyoto_tower,
                lon=self.lon_kyoto_tower,
                level=3)

        expected_meshcode_lv3 = '52353680'
        self.assertEqual(expected_meshcode_lv3, meshcode_lv3)

    def test_to_meshcode_lv4_kyoto_tower(self):
        meshcode_lv4 = to_meshcode(
                lat=self.lat_kyoto_tower,
                lon=self.lon_kyoto_tower,
                level=4)

        expected_meshcode_lv4 = '523536804'
        self.assertEqual(expected_meshcode_lv4, meshcode_lv4)

    def test_to_meshcode_lv5_kyoto_tower(self):
        meshcode_lv5 = to_meshcode(
                lat=self.lat_kyoto_tower,
                lon=self.lon_kyoto_tower,
                level=5)

        expected_meshcode_lv5 = '5235368041'
        self.assertEqual(expected_meshcode_lv5, meshcode_lv5)

    def test_to_meshcode_lv6_kyoto_tower(self):
        meshcode_lv6 = to_meshcode(
                lat=self.lat_kyoto_tower,
                lon=self.lon_kyoto_tower,
                level=6)

        expected_meshcode_lv6 = '52353680412'
        self.assertEqual(expected_meshcode_lv6, meshcode_lv6)

    def test_to_meshcode_100_kyoto_tower(self):
        meshcode_100 = to_meshcode(
                lat=self.lat_kyoto_tower,
                lon=self.lon_kyoto_tower,
                level=100)

        expected_meshcode_100 = '5235368057'
        self.assertEqual(expected_meshcode_100, meshcode_100)

if __name__ == '__main__':
    unittest.main()
