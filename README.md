# jismesh

地域メッシュコードに関するユーティリティです。
対応するメッシュは以下です。

 - 地域メッシュコードの次数
	 - 1次(80km四方): 1
	 - 40倍(40km四方): 40000
	 - 20倍(20km四方): 20000
	 - 2次(10km四方): 2
   	 - 5倍(5km四方): 5000
	 - 2.5倍(2.5km四方): 2500
	 - 2倍(2km四方): 2000
 	 - 3次(1km四方): 3
	 - 4次(500m四方): 4
	 - 5次(250m四方): 5
	 - 6次(125m四方): 6

## インストール
    pip install jismesh

## 緯度経度から地域メッシュコードを求める

メッシュコードに変換する座標点（緯度経度）と変換するメッシュコードの次数を指定します。

### 使用例
    import jismesh.utils as ju

    # 緯度経度からメッシュコードを求める。
    meshcode = ju.to_meshcode(35.658581, 139.745433, 3)
    print meshcode

	# pandas DataFrame中の緯度経度をメッシュコードに変換する。
    import pandas as pd
    df = pd.DataFrame({'lat': [35.658581, 34.987574], 'lon':[139.745433, 135.759363]})
    print df
             lat         lon
    0  35.658581  139.745433
    1  34.987574  135.759363

    mesh_series = df.apply(lambda r: ju.to_meshcode(r.lat, r.lon, 3), axis=1)
    print mesh_series
    0    53393599
    1    52353680
    dtype: object



## 地域メッシュコードから次数を求める

メッシュコードからそのメッシュコードの次数を判定します。

### 使用例
    import jismesh.utils as ju

    # メッシュコードの次数を求める。
    meshlevel = ju.to_meshlevel('53393599')
    print meshlevel
    3

	# pandas DataFrame中のメッシュコードを次数に変換する。
	import pandas as pd
	df = pd.DataFrame({'meshcode': ['53393599', '52353680']})
	print df
	   meshcode
	0  53393599
	1  52353680
	level_series = df.apply(lambda r: ju.to_meshlevel(r.meshcode), axis=1)
	print level_series
	0    3
	1    3
	dtype: int64

 

## 地域メッシュコードから緯度経度を求める

求める緯度経度で表される点は、当該メッシュの基準点(南西端)から、
緯度座標上の点の位置(当該メッシュの単位経度の倍数)、経度座標上の点の位置(当該メッシュの単位緯度の倍数)
を指定します。

### 使用例
    import jismesh.utils as ju
    
    # 南西端の緯度経度を求める。
    lat_sw, lon_sw = ju.to_meshpoint('53393599', 0, 0)
    print lat_sw, lon_sw
    35.6583333333 139.7375
    
    # 北東端の緯度経度を求める。
    lat_ne, lon_ne = ju.to_meshpoint('53393599', 1, 1)
    print lat_ne, lon_ne
    35.6666666667 139.75
    
    # 中心点の緯度経度を求める。
    lat_c, lon_c = ju.to_meshpoint('53393599', 0.5, 0.5)
    print lat_c, lon_c
    35.6625 139.74375

	# 西隣接メッシュの中心点の緯度経度を求める。
	lat_west_neighbor_c, lon_west_neighbor_c = ju.to_meshpoint('53393599', 0.5, 1.5)
	print lat_west_neighbor_c, lon_west_neighbor_c
	35.6625 139.75625

	# pandas DataFrame中のメッシュコードを中心点に変換する。
	import pandas as pd
	df = pd.DataFrame({'meshcode': ['53393599', '52353680']})
	print df
	   meshcode
	0  53393599
	1  52353680
	cord_series = df.apply(lambda r: ju.to_meshpoint(r.meshcode, 0.5, 0.5), axis=1)
	print cord_series
	0    (35.6625, 139.74375)
	1    (34.9875, 135.75625)
	dtype: object
