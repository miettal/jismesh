#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

import unittest
from jismesh.utils import to_meshpoint

class TestToMeshpoint(unittest.TestCase):

    INTERVAL_LAT_LV1 = 40/60
    INTERVAL_LON_LV1 = 1
    INTERVAL_LAT_LV2 = 5/60
    INTERVAL_LON_LV2 = 7.5/60
    INTERVAL_LAT_5000 = 2.5/60
    INTERVAL_LON_5000 = 3.75/60
    INTERVAL_LAT_2000 = 1/60
    INTERVAL_LON_2000 = 1.5/60
    INTERVAL_LAT_LV3 = 30/3600
    INTERVAL_LON_LV3 = 45/3600
    INTERVAL_LAT_LV4 = 15/3600
    INTERVAL_LON_LV4 = 22.5/3600
    INTERVAL_LAT_LV5 = 7.5/3600
    INTERVAL_LON_LV5 = 11.25/3600
    INTERVAL_LAT_LV6 = 3.75/3600
    INTERVAL_LON_LV6 = 5.625/3600
    INTERVAL_LAT_100 = 3/3600
    INTERVAL_LON_100 = 4.5/3600

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _test_to_meshpoint_helper(self, meshcode, level, point, expected_lat, expected_lon):
        lat, lon = to_meshpoint(meshcode=meshcode, level=level, point=point)
        self.assertAlmostEqual(expected_lat, lat)
        self.assertAlmostEqual(expected_lon, lon)

    def test_to_meshpoint_lv1_0(self):
        self._test_to_meshpoint_helper(meshcode="5339", level=1, point=0, expected_lat=35+1/3, expected_lon=139)

    def test_to_meshpoint_lv1_1(self):
        self._test_to_meshpoint_helper(meshcode="5339", level=1, point=1, expected_lat=35+1/3, expected_lon=139+self.INTERVAL_LON_LV1)

    def test_to_meshpoint_lv1_2(self):
        self._test_to_meshpoint_helper(meshcode="5339", level=1, point=2, expected_lat=35+1/3+self.INTERVAL_LAT_LV1, expected_lon=139)

    def test_to_meshpoint_lv1_3(self):
        self._test_to_meshpoint_helper(meshcode="5339", level=1, point=3, expected_lat=35+1/3+self.INTERVAL_LAT_LV1, expected_lon=139+self.INTERVAL_LON_LV1)

    def test_to_meshpoint_lv1_4(self):
        self._test_to_meshpoint_helper(meshcode="5339", level=1, point=4, expected_lat=35+1/3+self.INTERVAL_LAT_LV1/2, expected_lon=139+self.INTERVAL_LON_LV1/2)

    def test_to_meshpoint_lv2_0(self):
        self._test_to_meshpoint_helper(meshcode="533945", level=2, point=0, expected_lat=35.75-self.INTERVAL_LAT_LV2, expected_lon=139.75-self.INTERVAL_LON_LV2)

    def test_to_meshpoint_lv2_1(self):
        self._test_to_meshpoint_helper(meshcode="533945", level=2, point=1, expected_lat=35.75-self.INTERVAL_LAT_LV2, expected_lon=139.75)

    def test_to_meshpoint_lv2_2(self):
        self._test_to_meshpoint_helper(meshcode="533945", level=2, point=2, expected_lat=35.75, expected_lon=139.75-self.INTERVAL_LON_LV2)

    def test_to_meshpoint_lv2_3(self):
        self._test_to_meshpoint_helper(meshcode="533945", level=2, point=3, expected_lat=35.75, expected_lon=139.75)

    def test_to_meshpoint_lv2_4(self):
        self._test_to_meshpoint_helper(meshcode="533945", level=2, point=4, expected_lat=35.75-self.INTERVAL_LAT_LV2/2, expected_lon=139.75-self.INTERVAL_LON_LV2/2)

    def test_to_meshpoint_5000_0(self):
        self._test_to_meshpoint_helper(meshcode="5339454", level=5000, point=0, expected_lat=35.75-self.INTERVAL_LAT_5000, expected_lon=139.75-self.INTERVAL_LON_5000)

    def test_to_meshpoint_5000_1(self):
        self._test_to_meshpoint_helper(meshcode="5339454", level=5000, point=1, expected_lat=35.75-self.INTERVAL_LAT_5000, expected_lon=139.75)

    def test_to_meshpoint_5000_2(self):
        self._test_to_meshpoint_helper(meshcode="5339454", level=5000, point=2, expected_lat=35.75, expected_lon=139.75-self.INTERVAL_LON_5000)

    def test_to_meshpoint_5000_3(self):
        self._test_to_meshpoint_helper(meshcode="5339454", level=5000, point=3, expected_lat=35.75, expected_lon=139.75)

    def test_to_meshpoint_5000_4(self):
        self._test_to_meshpoint_helper(meshcode="5339454", level=5000, point=4, expected_lat=35.75-self.INTERVAL_LAT_5000/2, expected_lon=139.75-self.INTERVAL_LON_5000/2)

    def test_to_meshpoint_2000_0(self):
        self._test_to_meshpoint_helper(meshcode="533945885", level=2000, point=0, expected_lat=35.75-self.INTERVAL_LAT_2000, expected_lon=139.75-self.INTERVAL_LON_2000)

    def test_to_meshpoint_2000_1(self):
        self._test_to_meshpoint_helper(meshcode="533945885", level=2000, point=1, expected_lat=35.75-self.INTERVAL_LAT_2000, expected_lon=139.75)

    def test_to_meshpoint_2000_2(self):
        self._test_to_meshpoint_helper(meshcode="533945885", level=2000, point=2, expected_lat=35.75, expected_lon=139.75-self.INTERVAL_LON_2000)

    def test_to_meshpoint_2000_3(self):
        self._test_to_meshpoint_helper(meshcode="533945885", level=2000, point=3, expected_lat=35.75, expected_lon=139.75)

    def test_to_meshpoint_2000_4(self):
        self._test_to_meshpoint_helper(meshcode="533945885", level=2000, point=4, expected_lat=35.75-self.INTERVAL_LAT_2000/2, expected_lon=139.75-self.INTERVAL_LON_2000/2)

    def test_to_meshpoint_lv3_0(self):
        self._test_to_meshpoint_helper(meshcode="53394508", level=3, point=0, expected_lat=35.675-self.INTERVAL_LAT_LV3, expected_lon=139.7375-self.INTERVAL_LON_LV3)

    def test_to_meshpoint_lv3_1(self):
        self._test_to_meshpoint_helper(meshcode="53394508", level=3, point=1, expected_lat=35.675-self.INTERVAL_LAT_LV3, expected_lon=139.7375)

    def test_to_meshpoint_lv3_2(self):
        self._test_to_meshpoint_helper(meshcode="53394508", level=3, point=2, expected_lat=35.675, expected_lon=139.7375-self.INTERVAL_LON_LV3)

    def test_to_meshpoint_lv3_3(self):
        self._test_to_meshpoint_helper(meshcode="53394508", level=3, point=3, expected_lat=35.675, expected_lon=139.7375)

    def test_to_meshpoint_lv3_4(self):
        self._test_to_meshpoint_helper(meshcode="53394508", level=3, point=4, expected_lat=35.675-self.INTERVAL_LAT_LV3/2, expected_lon=139.7375-self.INTERVAL_LON_LV3/2)

    def test_to_meshpoint_lv4_0(self):
        self._test_to_meshpoint_helper(meshcode="533945084", level=4, point=0, expected_lat=35.675-self.INTERVAL_LAT_LV4, expected_lon=139.7375-self.INTERVAL_LON_LV4)

    def test_to_meshpoint_lv4_1(self):
        self._test_to_meshpoint_helper(meshcode="533945084", level=4, point=1, expected_lat=35.675-self.INTERVAL_LAT_LV4, expected_lon=139.7375)

    def test_to_meshpoint_lv4_2(self):
        self._test_to_meshpoint_helper(meshcode="533945084", level=4, point=2, expected_lat=35.675, expected_lon=139.7375-self.INTERVAL_LON_LV4)

    def test_to_meshpoint_lv4_3(self):
        self._test_to_meshpoint_helper(meshcode="533945084", level=4, point=3, expected_lat=35.675, expected_lon=139.7375)

    def test_to_meshpoint_lv4_4(self):
        self._test_to_meshpoint_helper(meshcode="533945084", level=4, point=4, expected_lat=35.675-self.INTERVAL_LAT_LV4/2, expected_lon=139.7375-self.INTERVAL_LON_LV4/2)

    def test_to_meshpoint_lv5_0(self):
        self._test_to_meshpoint_helper(meshcode="5339450842", level=5, point=0, expected_lat=35.672916666-self.INTERVAL_LAT_LV5, expected_lon=139.7375-self.INTERVAL_LON_LV5)

    def test_to_meshpoint_lv5_1(self):
        self._test_to_meshpoint_helper(meshcode="5339450842", level=5, point=1, expected_lat=35.672916666-self.INTERVAL_LAT_LV5, expected_lon=139.7375)

    def test_to_meshpoint_lv5_2(self):
        self._test_to_meshpoint_helper(meshcode="5339450842", level=5, point=2, expected_lat=35.672916666, expected_lon=139.7375-self.INTERVAL_LON_LV5)

    def test_to_meshpoint_lv5_3(self):
        self._test_to_meshpoint_helper(meshcode="5339450842", level=5, point=3, expected_lat=35.672916666, expected_lon=139.7375)

    def test_to_meshpoint_lv5_4(self):
        self._test_to_meshpoint_helper(meshcode="5339450842", level=5, point=4, expected_lat=35.672916666-self.INTERVAL_LAT_LV5/2, expected_lon=139.7375-self.INTERVAL_LON_LV5/2)

    def test_to_meshpoint_lv6_0(self):
        self._test_to_meshpoint_helper(meshcode="53394508423", level=6, point=0, expected_lat=35.672916666-self.INTERVAL_LAT_LV6, expected_lon=139.7359375-self.INTERVAL_LON_LV6)

    def test_to_meshpoint_lv6_1(self):
        self._test_to_meshpoint_helper(meshcode="53394508423", level=6, point=1, expected_lat=35.672916666-self.INTERVAL_LAT_LV6, expected_lon=139.7359375)

    def test_to_meshpoint_lv6_2(self):
        self._test_to_meshpoint_helper(meshcode="53394508423", level=6, point=2, expected_lat=35.672916666, expected_lon=139.7359375-self.INTERVAL_LON_LV6)

    def test_to_meshpoint_lv6_3(self):
        self._test_to_meshpoint_helper(meshcode="53394508423", level=6, point=3, expected_lat=35.672916666, expected_lon=139.7359375)

    def test_to_meshpoint_lv6_4(self):
        self._test_to_meshpoint_helper(meshcode="53394508423", level=6, point=4, expected_lat=35.672916666-self.INTERVAL_LAT_LV6/2, expected_lon=139.7359375-self.INTERVAL_LON_LV6/2)

    def test_to_meshpoint_100_0(self):
        self._test_to_meshpoint_helper(meshcode="5339450899", level=100, point=0, expected_lat=35.675-self.INTERVAL_LAT_100, expected_lon=139.7375-self.INTERVAL_LON_100)

    def test_to_meshpoint_100_1(self):
        self._test_to_meshpoint_helper(meshcode="5339450899", level=100, point=1, expected_lat=35.675-self.INTERVAL_LAT_100, expected_lon=139.7375)

    def test_to_meshpoint_100_2(self):
        self._test_to_meshpoint_helper(meshcode="5339450899", level=100, point=2, expected_lat=35.675, expected_lon=139.7375-self.INTERVAL_LON_100)

    def test_to_meshpoint_100_3(self):
        self._test_to_meshpoint_helper(meshcode="5339450899", level=100, point=3, expected_lat=35.675, expected_lon=139.7375)

    def test_to_meshpoint_100_4(self):
        self._test_to_meshpoint_helper(meshcode="5339450899", level=100, point=4, expected_lat=35.675-self.INTERVAL_LAT_100/2, expected_lon=139.7375-self.INTERVAL_LON_100/2)

if __name__ == '__main__':
    unittest.main()
