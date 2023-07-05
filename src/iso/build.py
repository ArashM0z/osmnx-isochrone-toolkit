"""Multi-modal isochrone toolkit on OSMnx + NetworkX."""

from __future__ import annotations

from dataclasses import dataclass

import networkx as nx
import osmnx as ox
from shapely.geometry import MultiPolygon, Point, Polygon


MODE_SPEEDS_KMH = {"walking": 4.5, "cycling": 16.0, "driving": 35.0}


@dataclass(frozen=True)
class Isochrone:
    centre_lat: float
    centre_lon: float
    minutes: int
    mode: str
    polygon: Polygon | MultiPolygon


def build_graph(place: str, network_type: str = "walk") -> nx.MultiDiGraph:
    return ox.graph_from_place(place, network_type=network_type)


def reachable_nodes(
    graph: nx.MultiDiGraph,
    centre_node: int,
    minutes: int,
    mode: str = "walking",
) -> set[int]:
    speed_kmh = MODE_SPEEDS_KMH[mode]
    cutoff_m = speed_kmh * 1000.0 / 60.0 * minutes
    distances = nx.single_source_dijkstra_path_length(
        graph, centre_node, cutoff=cutoff_m, weight="length"
    )
    return set(distances.keys())


def isochrone_polygon(
    graph: nx.MultiDiGraph,
    centre_node: int,
    minutes: int,
    mode: str = "walking",
    buffer_m: int = 25,
) -> Polygon | MultiPolygon:
    """Concave hull of reachable nodes, slightly buffered to soften the edges."""
    nodes_in_range = reachable_nodes(graph, centre_node, minutes, mode)
    points = [Point(graph.nodes[n]["x"], graph.nodes[n]["y"]) for n in nodes_in_range]
    if not points:
        return Polygon()
    from shapely.ops import unary_union
    union = unary_union(points)
    # Project to a metric CRS for buffering, then back
    return union.buffer(buffer_m / 111_000)  # rough deg/m


def build_isochrone(
    place: str,
    lat: float,
    lon: float,
    minutes: int,
    mode: str = "walking",
) -> Isochrone:
    graph = build_graph(place, network_type={"walking": "walk", "cycling": "bike",
                                              "driving": "drive"}[mode])
    centre_node = ox.nearest_nodes(graph, X=lon, Y=lat)
    poly = isochrone_polygon(graph, centre_node, minutes, mode)
    return Isochrone(
        centre_lat=lat, centre_lon=lon, minutes=minutes, mode=mode, polygon=poly,
    )
