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

<!-- maint 2025-04-21 -->

<!-- maint 2025-05-31 -->

<!-- maint 2025-07-08 -->

<!-- maint 2025-08-17 -->

<!-- maint 2025-09-24 -->

<!-- maint 2025-11-03 -->

<!-- maint 2025-12-11 -->

<!-- maint 2024-02-13 -->

<!-- maint 2024-04-06 -->

<!-- maint 2024-05-28 -->

<!-- maint 2024-07-18 -->

<!-- maint 2024-09-08 -->

<!-- maint 2024-10-31 -->

<!-- maint 2024-12-22 -->

<!-- maint 2023-02-28 -->

<!-- m 2023-08-30T19:06:00-06:00 -->

<!-- m 2026-04-13T18:05:00-06:00 -->
