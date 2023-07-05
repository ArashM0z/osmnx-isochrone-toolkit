"""Smoke tests on a tiny synthetic graph."""
import networkx as nx
from iso.build import reachable_nodes


def test_reachable_includes_close_nodes() -> None:
    g = nx.MultiDiGraph()
    g.add_node(0, x=0, y=0)
    g.add_node(1, x=0.001, y=0)
    g.add_node(2, x=10, y=10)
    g.add_edge(0, 1, length=100)
    g.add_edge(1, 0, length=100)
    nodes = reachable_nodes(g, centre_node=0, minutes=5, mode="walking")
    assert 0 in nodes
    assert 1 in nodes
    assert 2 not in nodes
