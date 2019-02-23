# -*- coding: utf-8 -*-

from __future__ import division

import unittest
from jismesh.utils import to_meshpoint

class TestToMeshpoint(unittest.TestCase):

    DICT_LEVEL_UNIT = {
        1: (40/60, 1),
        40000: (40/120, 1/2),
        20000: (40/240, 1/4),
        16000: (40/300, 1/5),
        2: (5/60, 7.5/60),
        8000: (4/60, 6/60),
        5000: (2.5/60, 3.75/60),
        4000: (2/60, 3/60),
        2500: (2.5/120, 3.75/120),
        2000: (1/60, 1.5/60),
        3: (30/3600, 45/3600),
        4: (15/3600, 22.5/3600),
        5: (7.5/3600, 11.25/3600),
        6: (3.75/3600, 5.625/3600)
    }

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _test_helper(
            self,
            meshcode,
            lat_multiplier,
            lon_multiplier,
            expected_lat,
            expected_lon):

        lat, lon = to_meshpoint(
            meshcode=meshcode,
            lat_multiplier=lat_multiplier,
            lon_multiplier=lon_multiplier)

        self.assertAlmostEqual(expected_lat, lat)
        self.assertAlmostEqual(expected_lon, lon)

    def _test_helper_corners(self, meshcode, level, lat_sw, lon_sw):
        # common
        unit_lat, unit_lon = self.DICT_LEVEL_UNIT[level]

        # sw
        lat_multiplier = 0
        lon_multiplier = 0
        self._test_helper(
            meshcode=meshcode,
            lat_multiplier=lat_multiplier,
            lon_multiplier=lon_multiplier,
            expected_lat=lat_sw+unit_lat*lat_multiplier,
            expected_lon=lon_sw+unit_lon*lon_multiplier)

        # se
        lat_multiplier = 0
        lon_multiplier = 1
        self._test_helper(
            meshcode=meshcode,
            lat_multiplier=lat_multiplier,
            lon_multiplier=lon_multiplier,
            expected_lat=lat_sw+unit_lat*lat_multiplier,
            expected_lon=lon_sw+unit_lon*lon_multiplier)

        # nw
        lat_multiplier = 1
        lon_multiplier = 0
        self._test_helper(
            meshcode=meshcode,
            lat_multiplier=lat_multiplier,
            lon_multiplier=lon_multiplier,
            expected_lat=lat_sw+unit_lat*lat_multiplier,
            expected_lon=lon_sw+unit_lon*lon_multiplier)

        # ne
        lat_multiplier = 1
        lon_multiplier = 1
        self._test_helper(
            meshcode=meshcode,
            lat_multiplier=lat_multiplier,
            lon_multiplier=lon_multiplier,
            expected_lat=lat_sw+unit_lat*lat_multiplier,
            expected_lon=lon_sw+unit_lon*lon_multiplier)

        # center
        lat_multiplier = 0.5
        lon_multiplier = 0.5
        self._test_helper(
            meshcode=meshcode,
            lat_multiplier=lat_multiplier,
            lon_multiplier=lon_multiplier,
            expected_lat=lat_sw+unit_lat*lat_multiplier,
            expected_lon=lon_sw+unit_lon*lon_multiplier)

    def test_lv1(self):
        self._test_helper_corners(
            meshcode="5339",
            level=1,
            lat_sw=35+1/3,
            lon_sw=139)

    def test_40000(self):
        self._test_helper_corners(
            meshcode="53391",
            level=40000,
            lat_sw=35+1/3,
            lon_sw=139)

    def test_20000(self):
        self._test_helper_corners(
            meshcode="5339115",
            level=20000,
            lat_sw=35+1/3,
            lon_sw=139)

    def test_16000(self):
        self._test_helper_corners(
            meshcode="5339007",
            level=16000,
            lat_sw=35+1/3,
            lon_sw=139)

    def test_lv2(self):
        self._test_helper_corners(
            meshcode="533900",
            level=2,
            lat_sw=35+1/3,
            lon_sw=139)

    def test_8000(self):
        self._test_helper_corners(
            meshcode="5339006",
            level=8000,
            lat_sw=35+1/3,
            lon_sw=139)

    def test_5000(self):
        self._test_helper_corners(
            meshcode="5339001",
            level=5000,
            lat_sw=35+1/3,
            lon_sw=139)

    def test_4000(self):
        self._test_helper_corners(
            meshcode="533900617",
            level=4000,
            lat_sw=35+1/3,
            lon_sw=139)

    def test_2500(self):
        self._test_helper_corners(
            meshcode="533900116",
            level=2500,
            lat_sw=35+1/3,
            lon_sw=139)

    def test_2000(self):
        self._test_helper_corners(
            meshcode="533900005",
            level=2000,
            lat_sw=35+1/3,
            lon_sw=139)

    def test_lv3(self):
        self._test_helper_corners(
            meshcode="53390000",
            level=3,
            lat_sw=35+1/3,
            lon_sw=139)

    def test_lv4(self):
        self._test_helper_corners(
            meshcode="533900001",
            level=4,
            lat_sw=35+1/3,
            lon_sw=139)

    def test_lv5(self):
        self._test_helper_corners(
            meshcode="5339000011",
            level=5,
            lat_sw=35+1/3,
            lon_sw=139)

    def test_lv6(self):
        self._test_helper_corners(
            meshcode="53390000111",
            level=6,
            lat_sw=35+1/3,
            lon_sw=139)
