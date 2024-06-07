import pytest

from papertion.doi import get_item_from_doi
from papertion.item import Item


def test_doi():
    tests = [
        (
            "10.1103/PhysRevX.14.021001",
            Item(
                name="Clark2024",
                title="Theory of Coupled Neuronal-Synaptic Dynamics",
                first="David G. Clark",
                year=2024,
                journal="Physical Review X",
                authors=["David G. Clark", "L. F. Abbott"],
            ),
        ),
        (
            "https://doi.org/10.1103/PhysRevLett.61.259",
            Item(
                name="Sompolinsky1988",
                title="Chaos in Random Neural Networks",
                first="H. Sompolinsky",
                year=1988,
                journal="Physical Review Letters",
                authors=["H. Sompolinsky", "A. Crisanti", "H. J. Sommers"],
            ),
        ),
    ]

    for input, expected in tests:
        assert get_item_from_doi(input) == expected
