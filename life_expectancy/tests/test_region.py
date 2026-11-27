"""Tests for the Region enum."""
from life_expectancy.region import Region


def test_get_countries_excludes_aggregates():
    countries = Region.get_countries()

    assert Region.PT in countries
    assert Region.FR in countries
    assert {
        Region.DE_TOT,
        Region.EA18,
        Region.EA19,
        Region.EEA30_2007,
        Region.EEA31,
        Region.EFTA,
        Region.EU27_2007,
        Region.EU27_2020,
        Region.EU28,
        Region.FX,
    }.isdisjoint(countries)