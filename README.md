# jismesh

地域メッシュコードに関するユーティリティです。

## to_meshpoint
地域メッシュコードから緯度経度を求める。

対応する地域メッシュは、1次、2次、5倍、2倍、3次、4次、5次、6次および100メートルメッシュです。  
求める緯度経度で表される点は、南西端、南東端、北西端、北東端、中心点から選択できます。  

### How to use
pip install jismesh

from jismesh.utils import to_meshpoint

meshcode='53393599'
level=3
point=0

lat, lon = to_meshpoint(meshcode=meshcode, level=level, point=point)

## to_meshcode
緯度経度から地域メッシュコードを求める。
対応する地域メッシュは、1次、2次、5倍、2倍、3次、4次、5次、6次および100メートルメッシュです。  

### How to use
pip install jismesh

from jismesh.utils import to_meshcode

lat=35.658581
lon=139.745433
level=3

meshcode = to_meshcode(lat=lat, lon=lon, level=level)
