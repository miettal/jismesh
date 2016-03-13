#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

# unit in degree of latitude and longitude for each mesh level. 
unit_lat_lv1 = lambda: 2/3
unit_lon_lv1 = lambda: 1
unit_lat_lv2 = lambda: unit_lat_lv1()/8
unit_lon_lv2 = lambda: unit_lon_lv1()/8
unit_lat_5000 = lambda: unit_lat_lv2()/2
unit_lon_5000 = lambda: unit_lon_lv2()/2
unit_lat_2000 = lambda: unit_lat_lv2()/5
unit_lon_2000 = lambda: unit_lon_lv2()/5
unit_lat_lv3 = lambda: unit_lat_lv2()/10
unit_lon_lv3 = lambda: unit_lon_lv2()/10
unit_lat_lv4 = lambda: unit_lat_lv3()/2
unit_lon_lv4 = lambda: unit_lon_lv3()/2
unit_lat_lv5 = lambda: unit_lat_lv4()/2
unit_lon_lv5 = lambda: unit_lon_lv4()/2
unit_lat_lv6 = lambda: unit_lat_lv5()/2
unit_lon_lv6 = lambda: unit_lon_lv5()/2
unit_lat_100 = lambda: unit_lat_lv3()/10
unit_lon_100 = lambda: unit_lon_lv3()/10

def to_meshcode(lat, lon, level):
    """緯度経度から指定次の地域メッシュコードを算出する。
    
    Args:
        lat: 世界測地系の緯度(度単位)
        lon: 世界測地系の経度(度単位)
        level: 地域メッシュコードの次数 
                1次:1
                2次:2
                5倍:5000
                2倍:2000
                3次:3
                4次:4
                5次:5
                6次:6
                100メートル:100
    Return:
        指定次の地域メッシュコード

    """

    # reminder of latitude and longitude by its unit in degree of mesh level.
    rem_lat_lv0 = lambda lat: lat
    rem_lon_lv0 = lambda lon: lon % 100
    rem_lat_lv1 = lambda lat: rem_lat_lv0(lat) % unit_lat_lv1()
    rem_lon_lv1 = lambda lon: rem_lon_lv0(lon) % unit_lon_lv1()
    rem_lat_lv2 = lambda lat: rem_lat_lv1(lat) % unit_lat_lv2()
    rem_lon_lv2 = lambda lon: rem_lon_lv1(lon) % unit_lon_lv2()
    rem_lat_5000 = lambda lat: rem_lat_lv2(lat) % unit_lat_5000()
    rem_lon_5000 = lambda lon: rem_lon_lv2(lon) % unit_lon_5000()
    rem_lat_2000 = lambda lat: rem_lat_lv2(lat) % unit_lat_2000()
    rem_lon_2000 = lambda lon: rem_lon_lv2(lon) % unit_lon_2000()
    rem_lat_lv3 = lambda lat: rem_lat_lv2(lat) % unit_lat_lv3()
    rem_lon_lv3 = lambda lon: rem_lon_lv2(lon) % unit_lon_lv3()
    rem_lat_lv4 = lambda lat: rem_lat_lv3(lat) % unit_lat_lv4()
    rem_lon_lv4 = lambda lon: rem_lon_lv3(lon) % unit_lon_lv4()
    rem_lat_lv5 = lambda lat: rem_lat_lv4(lat) % unit_lat_lv5()
    rem_lon_lv5 = lambda lon: rem_lon_lv4(lon) % unit_lon_lv5()
    rem_lat_lv6 = lambda lat: rem_lat_lv5(lat) % unit_lat_lv6()
    rem_lon_lv6 = lambda lon: rem_lon_lv5(lon) % unit_lon_lv6()
    rem_lat_100 = lambda lat: rem_lat_lv3(lat) % unit_lat_100()
    rem_lon_100 = lambda lon: rem_lon_lv3(lon) % unit_lon_100()

    def meshcode_lv1(lat, lon):
        ab = int(rem_lat_lv0(lat) / unit_lat_lv1())
        cd = int(rem_lon_lv0(lon) / unit_lon_lv1())
        return str(ab) + str(cd)
    
    def meshcode_lv2(lat, lon):
        e = int(rem_lat_lv1(lat) / unit_lat_lv2())
        f = int(rem_lon_lv1(lon) / unit_lon_lv2())
        return meshcode_lv1(lat, lon) + str(e) + str(f)

    def meshcode_5000(lat, lon):
        g = int(rem_lat_lv2(lat) / unit_lat_5000())*2 + int(rem_lon_lv2(lon) / unit_lon_5000()) + 1
        return meshcode_lv2(lat, lon) + str(g)

    def meshcode_2000(lat, lon):
        g = int(rem_lat_lv2(lat) / unit_lat_2000())*2
        h = int(rem_lon_lv2(lon) / unit_lon_2000())*2
        i = 5
        return meshcode_lv2(lat, lon) + str(g) + str(h) + str(i)

    def meshcode_lv3(lat, lon):
        g = int(rem_lat_lv2(lat) / unit_lat_lv3())
        h = int(rem_lon_lv2(lon) / unit_lon_lv3())
        return meshcode_lv2(lat, lon) + str(g) + str(h)

    def meshcode_lv4(lat, lon):
        i = int(rem_lat_lv3(lat) / unit_lat_lv4())*2 + int(rem_lon_lv3(lon) / unit_lon_lv4()) + 1
        return meshcode_lv3(lat, lon) + str(i)

    def meshcode_lv5(lat, lon):
        j = int(rem_lat_lv4(lat) / unit_lat_lv5())*2 + int(rem_lon_lv4(lon) / unit_lon_lv5()) + 1
        return meshcode_lv4(lat, lon) + str(j)

    def meshcode_lv6(lat, lon):
        k = int(rem_lat_lv5(lat) / unit_lat_lv6())*2 + int(rem_lon_lv5(lon) / unit_lon_lv6()) + 1
        return meshcode_lv5(lat, lon) + str(k)

    def meshcode_100(lat, lon):
        i = int(rem_lat_lv3(lat) / unit_lat_100())
        j = int(rem_lon_lv3(lon) / unit_lon_100())
        return meshcode_lv3(lat, lon) + str(i) + str(j)
    
    if level == 1:
        return meshcode_lv1(lat, lon)

    if level == 2:
        return meshcode_lv2(lat, lon)

    if level == 5000:
        return meshcode_5000(lat, lon)

    if level == 2000:
        return meshcode_2000(lat, lon)

    if level == 3:
        return meshcode_lv3(lat, lon)

    if level == 4:
        return meshcode_lv4(lat, lon)

    if level == 5:
        return meshcode_lv5(lat, lon)

    if level == 6:
        return meshcode_lv6(lat, lon)

    if level == 100:
        return meshcode_100(lat, lon)

    raise ValueError("不正な次数が指定されています。")

def to_meshpoint(meshcode, level, point):
    """地域メッシュコードから緯度経度を算出する。
    1次、2次、5倍メッシュ、2倍メッシュ、3次、4次、
    5次、6次、100メートルメッシュに対応している。

    Args:
        meshcode: 指定次の地域メッシュコード
        level: 地域メッシュコードの次数 
                1次:1
                2次:2
                5倍:5000
                2倍:2000
                3次:3
                4次:4
                5次:5
                6次:6
                100メートル:100
        point: 点の位置 0:南西端、1:南東端、2:北西端、3:北東端、4:中心
    Return:
        lat: 世界測地系の緯度(度単位)
        lon: 世界測地系の経度(度単位)

    """
    
    # 1次メッシュ
    def mesh_lv1_start_point(meshcode):
        ab = int(meshcode[0:2])
        cd = int(meshcode[2:4])
        lat_lv1 = ab * unit_lat_lv1() + 0
        lon_lv1 = cd * unit_lon_lv1() + 100
        return lat_lv1, lon_lv1
    
    # 2次メッシュ
    def mesh_lv2_start_point(meshcode):
        lat_lv1, lon_lv1 = mesh_lv1_start_point(meshcode)
        e = int(meshcode[4:5])
        f = int(meshcode[5:6])
        lat_lv2 = e * unit_lat_lv2() + lat_lv1
        lon_lv2 = f * unit_lon_lv2() + lon_lv1
        return lat_lv2, lon_lv2

    # 5倍メッシュ
    def mesh_5000_start_point(meshcode):
        lat_lv2, lon_lv2 = mesh_lv2_start_point(meshcode)
        g = int(meshcode[6:7])
        g_lat = int(bin(g-1)[2:].zfill(2)[0:1])
        g_lon = int(bin(g-1)[2:].zfill(2)[1:2])
        lat_5000 = g_lat * unit_lat_5000() + lat_lv2
        lon_5000 = g_lon * unit_lon_5000() + lon_lv2
        return lat_5000, lon_5000

    # 2倍メッシュ
    def mesh_2000_start_point(meshcode):
        lat_lv2, lon_lv2 = mesh_lv2_start_point(meshcode)
        g = int(meshcode[6:7])
        h = int(meshcode[7:8])
        lat_2000 = g/2 * unit_lat_2000() + lat_lv2
        lon_2000 = h/2 * unit_lon_2000() + lon_lv2
        return lat_2000, lon_2000

    # 3次メッシュ
    def mesh_lv3_start_point(meshcode):
        lat_lv2, lon_lv2 = mesh_lv2_start_point(meshcode)
        g = int(meshcode[6:7])
        h = int(meshcode[7:8])
        lat_lv3 = g * unit_lat_lv3() + lat_lv2
        lon_lv3 = h * unit_lon_lv3() + lon_lv2
        return lat_lv3, lon_lv3

    # 4次メッシュ 
    def mesh_lv4_start_point(meshcode):
        lat_lv3, lon_lv3 = mesh_lv3_start_point(meshcode)
        i = int(meshcode[8:9])
        i_lat = int(bin(i-1)[2:].zfill(2)[0:1])
        i_lon = int(bin(i-1)[2:].zfill(2)[1:2])
        lat_lv4 = i_lat * unit_lat_lv4() + lat_lv3
        lon_lv4 = i_lon * unit_lon_lv4() + lon_lv3
        return lat_lv4, lon_lv4

    # 5次メッシュ 
    def mesh_lv5_start_point(meshcode):
        lat_lv4, lon_lv4 = mesh_lv4_start_point(meshcode)
        j = int(meshcode[9:10])
        j_lat = int(bin(j-1)[2:].zfill(2)[0:1])
        j_lon = int(bin(j-1)[2:].zfill(2)[1:2])
        lat_lv5 = j_lat * unit_lat_lv5() + lat_lv4
        lon_lv5 = j_lon * unit_lon_lv5() + lon_lv4
        return lat_lv5, lon_lv5

    # 6次メッシュ 
    def mesh_lv6_start_point(meshcode):
        lat_lv5, lon_lv5 = mesh_lv5_start_point(meshcode)
        k = int(meshcode[10:11])
        k_lat = int(bin(k-1)[2:].zfill(2)[0:1])
        k_lon = int(bin(k-1)[2:].zfill(2)[1:2])
        lat_lv6 = k_lat * unit_lat_lv6() + lat_lv5
        lon_lv6 = k_lon * unit_lon_lv6() + lon_lv5
        return lat_lv6, lon_lv6

    # 100mメッシュ
    def mesh_100_start_point(meshcode):
        lat_lv3, lon_lv3 = mesh_lv3_start_point(meshcode)
        i_100 = int(meshcode[8:9])
        j_100 = int(meshcode[9:10])
        lat_100 = i_100 * unit_lat_100() + lat_lv3
        lon_100 = j_100 * unit_lon_100() + lon_lv3
        return lat_100, lon_100

    def point_lat_lon(meshcode, point, func_mesh_start_point, func_unit_lat, func_unit_lon):
        lat, lon = func_mesh_start_point(meshcode=meshcode)
        unit_lat = func_unit_lat()
        unit_lon = func_unit_lon()
        if point == 0:
            return lat, lon
        elif point == 1:
            return lat, lon + unit_lon
        elif point == 2:
            return lat + unit_lat, lon
        elif point == 3:
            return lat + unit_lat, lon + unit_lon
        elif point == 4:
            return lat + unit_lat/2, lon + unit_lon/2
        else:
            raise ValueError("pointは0から4まで。")

    if level == 1:
        return point_lat_lon(meshcode, point, mesh_lv1_start_point, unit_lat_lv1, unit_lon_lv1)
    
    if level == 2:
        return point_lat_lon(meshcode, point, mesh_lv2_start_point, unit_lat_lv2, unit_lon_lv2)

    if level == 5000:
        return point_lat_lon(meshcode, point, mesh_5000_start_point, unit_lat_5000, unit_lon_5000)

    if level == 2000:
        return point_lat_lon(meshcode, point, mesh_2000_start_point, unit_lat_2000, unit_lon_2000)

    if level == 3:
        return point_lat_lon(meshcode, point, mesh_lv3_start_point, unit_lat_lv3, unit_lon_lv3)

    if level == 4:
        return point_lat_lon(meshcode, point, mesh_lv4_start_point, unit_lat_lv4, unit_lon_lv4)

    if level == 5:
        return point_lat_lon(meshcode, point, mesh_lv5_start_point, unit_lat_lv5, unit_lon_lv5)

    if level == 6:
        return point_lat_lon(meshcode, point, mesh_lv6_start_point, unit_lat_lv6, unit_lon_lv6)

    if level == 100:
        return point_lat_lon(meshcode, point, mesh_100_start_point, unit_lat_100, unit_lon_100)

    raise ValueError("不正な次数が指定されています。")

