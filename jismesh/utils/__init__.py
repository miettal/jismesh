from __future__ import absolute_import

import numpy as _np

from . import vector as _vector
from . import scalar as _scalar

def unit_lat(level):
    if _np.isscalar(level):
        unit_lat = _scalar.unit_lat
    else:
        unit_lat = _vector.unit_lat
    
    return unit_lat(level)

def unit_lon(level):
    if _np.isscalar(level):
        unit_lon = _scalar.unit_lon
    else:
        unit_lon = _vector.unit_lon
    
    return unit_lon(level)

def to_meshcode(lat, lon, level, astype=str):
    if _np.isscalar(lat) and _np.isscalar(lon) and _np.isscalar(level):
        to_meshcode = _scalar.to_meshcode
    else:
        to_meshcode = _vector.to_meshcode
    
    return to_meshcode(lat, lon, level, astype)

def to_meshlevel(meshcode):
    if _np.isscalar(meshcode):
        to_meshlevel = _scalar.to_meshlevel
    else:
        to_meshlevel = _vector.to_meshlevel
    
    return to_meshlevel(meshcode)

def to_meshpoint(meshcode, lat_multiplier, lon_multiplier):
    if _np.isscalar(meshcode) and _np.isscalar(lat_multiplier) and _np.isscalar(lon_multiplier):
        to_meshpoint = _scalar.to_meshpoint
    else:
        to_meshpoint = _vector.to_meshpoint
    
    return to_meshpoint(meshcode, lat_multiplier, lon_multiplier)

def to_envelope(meshcode_sw, meshcode_ne):
    if _np.isscalar(meshcode_sw) and _np.isscalar(meshcode_sw):
        to_envelope = _scalar.to_envelope
    else:
        to_envelope = _vector.to_envelope
    
    return to_envelope(meshcode_sw, meshcode_ne)

def to_intersects(meshcode, to_level):
    if _np.isscalar(meshcode) and _np.isscalar(to_level):
        to_intersects = _scalar.to_intersects
    else:
        to_intersects = _vector.to_intersects
    
    return to_intersects(meshcode, to_level)
    