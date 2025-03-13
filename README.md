# OSMnx Isochrone Toolkit

Build walking / cycling / driving isochrones from any OSM-covered place. Returns Shapely polygons; export to GeoJSON or Kepler.gl.

## Use

```python
from iso import build_isochrone, to_geojson

iso = build_isochrone("Calgary, Alberta, Canada",
                      lat=51.0461, lon=-114.0612,
                      minutes=15, mode="walking")
to_geojson([iso], "out.geojson")
```

## Speed presets

| Mode | km/h |
|---|---|
| Walking | 4.5 |
| Cycling | 16.0 |
| Driving | 35.0 |

<!-- 2024-09 -->

<!-- maint 2025-02-02 -->

<!-- maint 2025-03-13 -->
