"""Export isochrones to GeoJSON / Kepler.gl HTML."""

from __future__ import annotations

import json
from pathlib import Path

from shapely.geometry import mapping

from iso.build import Isochrone


def to_geojson(isochrones: list[Isochrone], out: Path) -> None:
    fc = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "minutes": iso.minutes,
                    "mode": iso.mode,
                    "centre_lat": iso.centre_lat,
                    "centre_lon": iso.centre_lon,
                },
                "geometry": mapping(iso.polygon),
            }
            for iso in isochrones
        ],
    }
    Path(out).write_text(json.dumps(fc))
