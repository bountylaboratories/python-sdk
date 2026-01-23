# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "RawUserCountParams",
    "Filters",
    "FiltersEq",
    "FiltersNotEq",
    "FiltersIn",
    "FiltersNotIn",
    "FiltersLt",
    "FiltersLte",
    "FiltersGt",
    "FiltersGte",
    "FiltersGlob",
    "FiltersNotGlob",
    "FiltersIGlob",
    "FiltersNotIGlob",
    "FiltersRegex",
    "FiltersContainsAllTokens",
    "FiltersUnionMember139",
    "FiltersUnionMember139Filter",
    "FiltersUnionMember139FilterUnionMember0",
    "FiltersUnionMember139FilterUnionMember1",
    "FiltersUnionMember139FilterUnionMember2",
    "FiltersUnionMember139FilterUnionMember3",
    "FiltersUnionMember139FilterUnionMember4",
    "FiltersUnionMember139FilterUnionMember5",
    "FiltersUnionMember139FilterUnionMember6",
    "FiltersUnionMember139FilterUnionMember7",
    "FiltersUnionMember139FilterUnionMember8",
    "FiltersUnionMember139FilterUnionMember9",
    "FiltersUnionMember139FilterUnionMember10",
    "FiltersUnionMember139FilterUnionMember11",
    "FiltersUnionMember139FilterUnionMember12",
    "FiltersUnionMember139FilterUnionMember13",
    "FiltersUnionMember139FilterUnionMember14",
    "FiltersUnionMember139FilterUnionMember15",
    "FiltersUnionMember139FilterUnionMember16",
    "FiltersUnionMember139FilterUnionMember17",
    "FiltersUnionMember139FilterUnionMember18",
    "FiltersUnionMember139FilterUnionMember19",
    "FiltersUnionMember139FilterUnionMember20",
    "FiltersUnionMember139FilterUnionMember21",
    "FiltersUnionMember139FilterUnionMember22",
    "FiltersUnionMember139FilterUnionMember23",
    "FiltersUnionMember139FilterUnionMember24",
    "FiltersUnionMember139FilterUnionMember25",
    "FiltersUnionMember139FilterUnionMember26",
    "FiltersUnionMember139FilterUnionMember27",
    "FiltersUnionMember139FilterUnionMember28",
    "FiltersUnionMember139FilterUnionMember29",
    "FiltersUnionMember139FilterUnionMember30",
    "FiltersUnionMember139FilterUnionMember31",
    "FiltersUnionMember139FilterUnionMember32",
    "FiltersUnionMember139FilterUnionMember33",
    "FiltersUnionMember139FilterUnionMember34",
    "FiltersUnionMember139FilterUnionMember35",
    "FiltersUnionMember139FilterUnionMember36",
    "FiltersUnionMember139FilterUnionMember37",
    "FiltersUnionMember139FilterUnionMember38",
    "FiltersUnionMember139FilterUnionMember39",
    "FiltersUnionMember139FilterUnionMember40",
    "FiltersUnionMember139FilterUnionMember41",
    "FiltersUnionMember139FilterUnionMember42",
    "FiltersUnionMember139FilterUnionMember43",
    "FiltersUnionMember139FilterUnionMember44",
    "FiltersUnionMember139FilterUnionMember45",
    "FiltersUnionMember139FilterUnionMember46",
    "FiltersUnionMember139FilterUnionMember47",
    "FiltersUnionMember139FilterUnionMember48",
    "FiltersUnionMember139FilterUnionMember49",
    "FiltersUnionMember139FilterUnionMember50",
    "FiltersUnionMember139FilterUnionMember51",
    "FiltersUnionMember139FilterUnionMember52",
    "FiltersUnionMember139FilterUnionMember53",
    "FiltersUnionMember139FilterUnionMember54",
    "FiltersUnionMember139FilterUnionMember55",
    "FiltersUnionMember139FilterUnionMember56",
    "FiltersUnionMember139FilterUnionMember57",
    "FiltersUnionMember139FilterUnionMember58",
    "FiltersUnionMember139FilterUnionMember59",
    "FiltersUnionMember139FilterUnionMember60",
    "FiltersUnionMember139FilterUnionMember61",
    "FiltersUnionMember139FilterUnionMember62",
    "FiltersUnionMember139FilterUnionMember63",
    "FiltersUnionMember139FilterUnionMember64",
    "FiltersUnionMember139FilterUnionMember65",
    "FiltersUnionMember139FilterUnionMember66",
    "FiltersUnionMember139FilterUnionMember67",
    "FiltersUnionMember139FilterUnionMember68",
    "FiltersUnionMember139FilterUnionMember69",
    "FiltersUnionMember139FilterUnionMember70",
    "FiltersUnionMember139FilterUnionMember71",
    "FiltersUnionMember139FilterUnionMember72",
    "FiltersUnionMember139FilterUnionMember73",
    "FiltersUnionMember139FilterUnionMember74",
    "FiltersUnionMember139FilterUnionMember75",
    "FiltersUnionMember139FilterUnionMember76",
    "FiltersUnionMember139FilterUnionMember77",
    "FiltersUnionMember139FilterUnionMember78",
    "FiltersUnionMember139FilterUnionMember79",
    "FiltersUnionMember139FilterUnionMember80",
    "FiltersUnionMember139FilterUnionMember81",
    "FiltersUnionMember139FilterUnionMember82",
    "FiltersUnionMember139FilterUnionMember83",
    "FiltersUnionMember139FilterUnionMember84",
    "FiltersUnionMember139FilterUnionMember85",
    "FiltersUnionMember139FilterUnionMember86",
    "FiltersUnionMember139FilterUnionMember87",
    "FiltersUnionMember139FilterUnionMember88",
    "FiltersUnionMember139FilterUnionMember89",
    "FiltersUnionMember139FilterUnionMember90",
    "FiltersUnionMember139FilterUnionMember91",
    "FiltersUnionMember139FilterUnionMember92",
    "FiltersUnionMember139FilterUnionMember93",
    "FiltersUnionMember139FilterUnionMember94",
    "FiltersUnionMember139FilterUnionMember95",
    "FiltersUnionMember139FilterUnionMember96",
    "FiltersUnionMember139FilterUnionMember97",
    "FiltersUnionMember139FilterUnionMember98",
    "FiltersUnionMember139FilterUnionMember99",
    "FiltersUnionMember139FilterUnionMember100",
    "FiltersUnionMember139FilterUnionMember101",
    "FiltersUnionMember139FilterUnionMember102",
    "FiltersUnionMember139FilterUnionMember103",
    "FiltersUnionMember139FilterUnionMember104",
    "FiltersUnionMember139FilterUnionMember105",
    "FiltersUnionMember139FilterUnionMember106",
    "FiltersUnionMember139FilterUnionMember107",
    "FiltersUnionMember139FilterUnionMember108",
    "FiltersUnionMember139FilterUnionMember109",
    "FiltersUnionMember139FilterUnionMember110",
    "FiltersUnionMember139FilterUnionMember111",
    "FiltersUnionMember139FilterUnionMember112",
    "FiltersUnionMember139FilterUnionMember113",
    "FiltersUnionMember139FilterUnionMember114",
    "FiltersUnionMember139FilterUnionMember115",
    "FiltersUnionMember139FilterUnionMember116",
    "FiltersUnionMember139FilterUnionMember117",
    "FiltersUnionMember139FilterUnionMember118",
    "FiltersUnionMember139FilterUnionMember119",
    "FiltersUnionMember139FilterUnionMember120",
    "FiltersUnionMember139FilterUnionMember121",
    "FiltersUnionMember139FilterUnionMember122",
    "FiltersUnionMember139FilterUnionMember123",
    "FiltersUnionMember139FilterUnionMember124",
    "FiltersUnionMember139FilterUnionMember125",
    "FiltersUnionMember139FilterUnionMember126",
    "FiltersUnionMember139FilterUnionMember127",
    "FiltersUnionMember139FilterUnionMember128",
    "FiltersUnionMember139FilterUnionMember129",
    "FiltersUnionMember139FilterUnionMember130",
    "FiltersUnionMember139FilterUnionMember131",
    "FiltersUnionMember139FilterUnionMember132",
    "FiltersUnionMember139FilterUnionMember133",
    "FiltersUnionMember139FilterUnionMember134",
    "FiltersUnionMember139FilterUnionMember135",
    "FiltersUnionMember139FilterUnionMember136",
    "FiltersUnionMember139FilterUnionMember137",
    "FiltersUnionMember139FilterUnionMember138",
    "FiltersUnionMember140",
    "FiltersUnionMember140Filter",
    "FiltersUnionMember140FilterUnionMember0",
    "FiltersUnionMember140FilterUnionMember1",
    "FiltersUnionMember140FilterUnionMember2",
    "FiltersUnionMember140FilterUnionMember3",
    "FiltersUnionMember140FilterUnionMember4",
    "FiltersUnionMember140FilterUnionMember5",
    "FiltersUnionMember140FilterUnionMember6",
    "FiltersUnionMember140FilterUnionMember7",
    "FiltersUnionMember140FilterUnionMember8",
    "FiltersUnionMember140FilterUnionMember9",
    "FiltersUnionMember140FilterUnionMember10",
    "FiltersUnionMember140FilterUnionMember11",
    "FiltersUnionMember140FilterUnionMember12",
    "FiltersUnionMember140FilterUnionMember13",
    "FiltersUnionMember140FilterUnionMember14",
    "FiltersUnionMember140FilterUnionMember15",
    "FiltersUnionMember140FilterUnionMember16",
    "FiltersUnionMember140FilterUnionMember17",
    "FiltersUnionMember140FilterUnionMember18",
    "FiltersUnionMember140FilterUnionMember19",
    "FiltersUnionMember140FilterUnionMember20",
    "FiltersUnionMember140FilterUnionMember21",
    "FiltersUnionMember140FilterUnionMember22",
    "FiltersUnionMember140FilterUnionMember23",
    "FiltersUnionMember140FilterUnionMember24",
    "FiltersUnionMember140FilterUnionMember25",
    "FiltersUnionMember140FilterUnionMember26",
    "FiltersUnionMember140FilterUnionMember27",
    "FiltersUnionMember140FilterUnionMember28",
    "FiltersUnionMember140FilterUnionMember29",
    "FiltersUnionMember140FilterUnionMember30",
    "FiltersUnionMember140FilterUnionMember31",
    "FiltersUnionMember140FilterUnionMember32",
    "FiltersUnionMember140FilterUnionMember33",
    "FiltersUnionMember140FilterUnionMember34",
    "FiltersUnionMember140FilterUnionMember35",
    "FiltersUnionMember140FilterUnionMember36",
    "FiltersUnionMember140FilterUnionMember37",
    "FiltersUnionMember140FilterUnionMember38",
    "FiltersUnionMember140FilterUnionMember39",
    "FiltersUnionMember140FilterUnionMember40",
    "FiltersUnionMember140FilterUnionMember41",
    "FiltersUnionMember140FilterUnionMember42",
    "FiltersUnionMember140FilterUnionMember43",
    "FiltersUnionMember140FilterUnionMember44",
    "FiltersUnionMember140FilterUnionMember45",
    "FiltersUnionMember140FilterUnionMember46",
    "FiltersUnionMember140FilterUnionMember47",
    "FiltersUnionMember140FilterUnionMember48",
    "FiltersUnionMember140FilterUnionMember49",
    "FiltersUnionMember140FilterUnionMember50",
    "FiltersUnionMember140FilterUnionMember51",
    "FiltersUnionMember140FilterUnionMember52",
    "FiltersUnionMember140FilterUnionMember53",
    "FiltersUnionMember140FilterUnionMember54",
    "FiltersUnionMember140FilterUnionMember55",
    "FiltersUnionMember140FilterUnionMember56",
    "FiltersUnionMember140FilterUnionMember57",
    "FiltersUnionMember140FilterUnionMember58",
    "FiltersUnionMember140FilterUnionMember59",
    "FiltersUnionMember140FilterUnionMember60",
    "FiltersUnionMember140FilterUnionMember61",
    "FiltersUnionMember140FilterUnionMember62",
    "FiltersUnionMember140FilterUnionMember63",
    "FiltersUnionMember140FilterUnionMember64",
    "FiltersUnionMember140FilterUnionMember65",
    "FiltersUnionMember140FilterUnionMember66",
    "FiltersUnionMember140FilterUnionMember67",
    "FiltersUnionMember140FilterUnionMember68",
    "FiltersUnionMember140FilterUnionMember69",
    "FiltersUnionMember140FilterUnionMember70",
    "FiltersUnionMember140FilterUnionMember71",
    "FiltersUnionMember140FilterUnionMember72",
    "FiltersUnionMember140FilterUnionMember73",
    "FiltersUnionMember140FilterUnionMember74",
    "FiltersUnionMember140FilterUnionMember75",
    "FiltersUnionMember140FilterUnionMember76",
    "FiltersUnionMember140FilterUnionMember77",
    "FiltersUnionMember140FilterUnionMember78",
    "FiltersUnionMember140FilterUnionMember79",
    "FiltersUnionMember140FilterUnionMember80",
    "FiltersUnionMember140FilterUnionMember81",
    "FiltersUnionMember140FilterUnionMember82",
    "FiltersUnionMember140FilterUnionMember83",
    "FiltersUnionMember140FilterUnionMember84",
    "FiltersUnionMember140FilterUnionMember85",
    "FiltersUnionMember140FilterUnionMember86",
    "FiltersUnionMember140FilterUnionMember87",
    "FiltersUnionMember140FilterUnionMember88",
    "FiltersUnionMember140FilterUnionMember89",
    "FiltersUnionMember140FilterUnionMember90",
    "FiltersUnionMember140FilterUnionMember91",
    "FiltersUnionMember140FilterUnionMember92",
    "FiltersUnionMember140FilterUnionMember93",
    "FiltersUnionMember140FilterUnionMember94",
    "FiltersUnionMember140FilterUnionMember95",
    "FiltersUnionMember140FilterUnionMember96",
    "FiltersUnionMember140FilterUnionMember97",
    "FiltersUnionMember140FilterUnionMember98",
    "FiltersUnionMember140FilterUnionMember99",
    "FiltersUnionMember140FilterUnionMember100",
    "FiltersUnionMember140FilterUnionMember101",
    "FiltersUnionMember140FilterUnionMember102",
    "FiltersUnionMember140FilterUnionMember103",
    "FiltersUnionMember140FilterUnionMember104",
    "FiltersUnionMember140FilterUnionMember105",
    "FiltersUnionMember140FilterUnionMember106",
    "FiltersUnionMember140FilterUnionMember107",
    "FiltersUnionMember140FilterUnionMember108",
    "FiltersUnionMember140FilterUnionMember109",
    "FiltersUnionMember140FilterUnionMember110",
    "FiltersUnionMember140FilterUnionMember111",
    "FiltersUnionMember140FilterUnionMember112",
    "FiltersUnionMember140FilterUnionMember113",
    "FiltersUnionMember140FilterUnionMember114",
    "FiltersUnionMember140FilterUnionMember115",
    "FiltersUnionMember140FilterUnionMember116",
    "FiltersUnionMember140FilterUnionMember117",
    "FiltersUnionMember140FilterUnionMember118",
    "FiltersUnionMember140FilterUnionMember119",
    "FiltersUnionMember140FilterUnionMember120",
    "FiltersUnionMember140FilterUnionMember121",
    "FiltersUnionMember140FilterUnionMember122",
    "FiltersUnionMember140FilterUnionMember123",
    "FiltersUnionMember140FilterUnionMember124",
    "FiltersUnionMember140FilterUnionMember125",
    "FiltersUnionMember140FilterUnionMember126",
    "FiltersUnionMember140FilterUnionMember127",
    "FiltersUnionMember140FilterUnionMember128",
    "FiltersUnionMember140FilterUnionMember129",
    "FiltersUnionMember140FilterUnionMember130",
    "FiltersUnionMember140FilterUnionMember131",
    "FiltersUnionMember140FilterUnionMember132",
    "FiltersUnionMember140FilterUnionMember133",
    "FiltersUnionMember140FilterUnionMember134",
    "FiltersUnionMember140FilterUnionMember135",
    "FiltersUnionMember140FilterUnionMember136",
    "FiltersUnionMember140FilterUnionMember137",
    "FiltersUnionMember140FilterUnionMember138",
    "FiltersUnionMember140FilterUnionMember139",
    "FiltersUnionMember140FilterUnionMember139Filter",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember0",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember1",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember2",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember3",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember4",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember5",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember6",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember7",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember8",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember9",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember10",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember11",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember12",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember13",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember14",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember15",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember16",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember17",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember18",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember19",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember20",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember21",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember22",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember23",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember24",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember25",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember26",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember27",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember28",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember29",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember30",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember31",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember32",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember33",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember34",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember35",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember36",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember37",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember38",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember39",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember40",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember41",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember42",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember43",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember44",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember45",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember46",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember47",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember48",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember49",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember50",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember51",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember52",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember53",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember54",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember55",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember56",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember57",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember58",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember59",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember60",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember61",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember62",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember63",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember64",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember65",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember66",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember67",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember68",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember69",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember70",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember71",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember72",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember73",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember74",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember75",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember76",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember77",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember78",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember79",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember80",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember81",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember82",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember83",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember84",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember85",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember86",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember87",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember88",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember89",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember90",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember91",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember92",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember93",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember94",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember95",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember96",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember97",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember98",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember99",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember100",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember101",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember102",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember103",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember104",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember105",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember106",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember107",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember108",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember109",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember110",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember111",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember112",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember113",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember114",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember115",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember116",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember117",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember118",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember119",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember120",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember121",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember122",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember123",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember124",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember125",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember126",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember127",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember128",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember129",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember130",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember131",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember132",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember133",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember134",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember135",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember136",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember137",
    "FiltersUnionMember140FilterUnionMember139FilterUnionMember138",
]


class RawUserCountParams(TypedDict, total=False):
    filters: Required[Filters]
    """Optional filters for users.

    Supports fields like login, company, location, resolvedCountry, resolvedState,
    resolvedCity. Operators: Eq, NotEq, In, NotIn, Lt, Lte, Gt, Gte.
    """


class FiltersEq(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersNotEq(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersIn(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersNotIn(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersLt(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersLte(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersGt(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersGte(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersNotGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersIGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersNotIGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersRegex(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersContainsAllTokens(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember139FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember139FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember139FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember139FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember139FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember139FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember139FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember139FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember139FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember139FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember139FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember139FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember139FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember139FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember139FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember139FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember139FilterUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember139FilterUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember139FilterUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember139FilterUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember139FilterUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


FiltersUnionMember139Filter: TypeAlias = Union[
    FiltersUnionMember139FilterUnionMember0,
    FiltersUnionMember139FilterUnionMember1,
    FiltersUnionMember139FilterUnionMember2,
    FiltersUnionMember139FilterUnionMember3,
    FiltersUnionMember139FilterUnionMember4,
    FiltersUnionMember139FilterUnionMember5,
    FiltersUnionMember139FilterUnionMember6,
    FiltersUnionMember139FilterUnionMember7,
    FiltersUnionMember139FilterUnionMember8,
    FiltersUnionMember139FilterUnionMember9,
    FiltersUnionMember139FilterUnionMember10,
    FiltersUnionMember139FilterUnionMember11,
    FiltersUnionMember139FilterUnionMember12,
    FiltersUnionMember139FilterUnionMember13,
    FiltersUnionMember139FilterUnionMember14,
    FiltersUnionMember139FilterUnionMember15,
    FiltersUnionMember139FilterUnionMember16,
    FiltersUnionMember139FilterUnionMember17,
    FiltersUnionMember139FilterUnionMember18,
    FiltersUnionMember139FilterUnionMember19,
    FiltersUnionMember139FilterUnionMember20,
    FiltersUnionMember139FilterUnionMember21,
    FiltersUnionMember139FilterUnionMember22,
    FiltersUnionMember139FilterUnionMember23,
    FiltersUnionMember139FilterUnionMember24,
    FiltersUnionMember139FilterUnionMember25,
    FiltersUnionMember139FilterUnionMember26,
    FiltersUnionMember139FilterUnionMember27,
    FiltersUnionMember139FilterUnionMember28,
    FiltersUnionMember139FilterUnionMember29,
    FiltersUnionMember139FilterUnionMember30,
    FiltersUnionMember139FilterUnionMember31,
    FiltersUnionMember139FilterUnionMember32,
    FiltersUnionMember139FilterUnionMember33,
    FiltersUnionMember139FilterUnionMember34,
    FiltersUnionMember139FilterUnionMember35,
    FiltersUnionMember139FilterUnionMember36,
    FiltersUnionMember139FilterUnionMember37,
    FiltersUnionMember139FilterUnionMember38,
    FiltersUnionMember139FilterUnionMember39,
    FiltersUnionMember139FilterUnionMember40,
    FiltersUnionMember139FilterUnionMember41,
    FiltersUnionMember139FilterUnionMember42,
    FiltersUnionMember139FilterUnionMember43,
    FiltersUnionMember139FilterUnionMember44,
    FiltersUnionMember139FilterUnionMember45,
    FiltersUnionMember139FilterUnionMember46,
    FiltersUnionMember139FilterUnionMember47,
    FiltersUnionMember139FilterUnionMember48,
    FiltersUnionMember139FilterUnionMember49,
    FiltersUnionMember139FilterUnionMember50,
    FiltersUnionMember139FilterUnionMember51,
    FiltersUnionMember139FilterUnionMember52,
    FiltersUnionMember139FilterUnionMember53,
    FiltersUnionMember139FilterUnionMember54,
    FiltersUnionMember139FilterUnionMember55,
    FiltersUnionMember139FilterUnionMember56,
    FiltersUnionMember139FilterUnionMember57,
    FiltersUnionMember139FilterUnionMember58,
    FiltersUnionMember139FilterUnionMember59,
    FiltersUnionMember139FilterUnionMember60,
    FiltersUnionMember139FilterUnionMember61,
    FiltersUnionMember139FilterUnionMember62,
    FiltersUnionMember139FilterUnionMember63,
    FiltersUnionMember139FilterUnionMember64,
    FiltersUnionMember139FilterUnionMember65,
    FiltersUnionMember139FilterUnionMember66,
    FiltersUnionMember139FilterUnionMember67,
    FiltersUnionMember139FilterUnionMember68,
    FiltersUnionMember139FilterUnionMember69,
    FiltersUnionMember139FilterUnionMember70,
    FiltersUnionMember139FilterUnionMember71,
    FiltersUnionMember139FilterUnionMember72,
    FiltersUnionMember139FilterUnionMember73,
    FiltersUnionMember139FilterUnionMember74,
    FiltersUnionMember139FilterUnionMember75,
    FiltersUnionMember139FilterUnionMember76,
    FiltersUnionMember139FilterUnionMember77,
    FiltersUnionMember139FilterUnionMember78,
    FiltersUnionMember139FilterUnionMember79,
    FiltersUnionMember139FilterUnionMember80,
    FiltersUnionMember139FilterUnionMember81,
    FiltersUnionMember139FilterUnionMember82,
    FiltersUnionMember139FilterUnionMember83,
    FiltersUnionMember139FilterUnionMember84,
    FiltersUnionMember139FilterUnionMember85,
    FiltersUnionMember139FilterUnionMember86,
    FiltersUnionMember139FilterUnionMember87,
    FiltersUnionMember139FilterUnionMember88,
    FiltersUnionMember139FilterUnionMember89,
    FiltersUnionMember139FilterUnionMember90,
    FiltersUnionMember139FilterUnionMember91,
    FiltersUnionMember139FilterUnionMember92,
    FiltersUnionMember139FilterUnionMember93,
    FiltersUnionMember139FilterUnionMember94,
    FiltersUnionMember139FilterUnionMember95,
    FiltersUnionMember139FilterUnionMember96,
    FiltersUnionMember139FilterUnionMember97,
    FiltersUnionMember139FilterUnionMember98,
    FiltersUnionMember139FilterUnionMember99,
    FiltersUnionMember139FilterUnionMember100,
    FiltersUnionMember139FilterUnionMember101,
    FiltersUnionMember139FilterUnionMember102,
    FiltersUnionMember139FilterUnionMember103,
    FiltersUnionMember139FilterUnionMember104,
    FiltersUnionMember139FilterUnionMember105,
    FiltersUnionMember139FilterUnionMember106,
    FiltersUnionMember139FilterUnionMember107,
    FiltersUnionMember139FilterUnionMember108,
    FiltersUnionMember139FilterUnionMember109,
    FiltersUnionMember139FilterUnionMember110,
    FiltersUnionMember139FilterUnionMember111,
    FiltersUnionMember139FilterUnionMember112,
    FiltersUnionMember139FilterUnionMember113,
    FiltersUnionMember139FilterUnionMember114,
    FiltersUnionMember139FilterUnionMember115,
    FiltersUnionMember139FilterUnionMember116,
    FiltersUnionMember139FilterUnionMember117,
    FiltersUnionMember139FilterUnionMember118,
    FiltersUnionMember139FilterUnionMember119,
    FiltersUnionMember139FilterUnionMember120,
    FiltersUnionMember139FilterUnionMember121,
    FiltersUnionMember139FilterUnionMember122,
    FiltersUnionMember139FilterUnionMember123,
    FiltersUnionMember139FilterUnionMember124,
    FiltersUnionMember139FilterUnionMember125,
    FiltersUnionMember139FilterUnionMember126,
    FiltersUnionMember139FilterUnionMember127,
    FiltersUnionMember139FilterUnionMember128,
    FiltersUnionMember139FilterUnionMember129,
    FiltersUnionMember139FilterUnionMember130,
    FiltersUnionMember139FilterUnionMember131,
    FiltersUnionMember139FilterUnionMember132,
    FiltersUnionMember139FilterUnionMember133,
    FiltersUnionMember139FilterUnionMember134,
    FiltersUnionMember139FilterUnionMember135,
    FiltersUnionMember139FilterUnionMember136,
    FiltersUnionMember139FilterUnionMember137,
    FiltersUnionMember139FilterUnionMember138,
]


class FiltersUnionMember139(TypedDict, total=False):
    filters: Required[Iterable[FiltersUnionMember139Filter]]

    op: Required[Literal["And", "Or"]]


class FiltersUnionMember140FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember140FilterUnionMember139FilterUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


FiltersUnionMember140FilterUnionMember139Filter: TypeAlias = Union[
    FiltersUnionMember140FilterUnionMember139FilterUnionMember0,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember1,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember2,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember3,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember4,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember5,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember6,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember7,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember8,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember9,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember10,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember11,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember12,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember13,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember14,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember15,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember16,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember17,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember18,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember19,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember20,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember21,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember22,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember23,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember24,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember25,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember26,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember27,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember28,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember29,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember30,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember31,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember32,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember33,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember34,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember35,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember36,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember37,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember38,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember39,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember40,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember41,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember42,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember43,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember44,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember45,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember46,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember47,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember48,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember49,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember50,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember51,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember52,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember53,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember54,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember55,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember56,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember57,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember58,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember59,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember60,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember61,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember62,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember63,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember64,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember65,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember66,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember67,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember68,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember69,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember70,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember71,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember72,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember73,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember74,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember75,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember76,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember77,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember78,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember79,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember80,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember81,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember82,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember83,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember84,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember85,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember86,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember87,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember88,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember89,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember90,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember91,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember92,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember93,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember94,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember95,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember96,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember97,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember98,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember99,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember100,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember101,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember102,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember103,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember104,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember105,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember106,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember107,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember108,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember109,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember110,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember111,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember112,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember113,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember114,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember115,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember116,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember117,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember118,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember119,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember120,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember121,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember122,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember123,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember124,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember125,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember126,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember127,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember128,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember129,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember130,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember131,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember132,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember133,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember134,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember135,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember136,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember137,
    FiltersUnionMember140FilterUnionMember139FilterUnionMember138,
]


class FiltersUnionMember140FilterUnionMember139(TypedDict, total=False):
    filters: Required[Iterable[FiltersUnionMember140FilterUnionMember139Filter]]

    op: Required[Literal["And", "Or"]]


FiltersUnionMember140Filter: TypeAlias = Union[
    FiltersUnionMember140FilterUnionMember0,
    FiltersUnionMember140FilterUnionMember1,
    FiltersUnionMember140FilterUnionMember2,
    FiltersUnionMember140FilterUnionMember3,
    FiltersUnionMember140FilterUnionMember4,
    FiltersUnionMember140FilterUnionMember5,
    FiltersUnionMember140FilterUnionMember6,
    FiltersUnionMember140FilterUnionMember7,
    FiltersUnionMember140FilterUnionMember8,
    FiltersUnionMember140FilterUnionMember9,
    FiltersUnionMember140FilterUnionMember10,
    FiltersUnionMember140FilterUnionMember11,
    FiltersUnionMember140FilterUnionMember12,
    FiltersUnionMember140FilterUnionMember13,
    FiltersUnionMember140FilterUnionMember14,
    FiltersUnionMember140FilterUnionMember15,
    FiltersUnionMember140FilterUnionMember16,
    FiltersUnionMember140FilterUnionMember17,
    FiltersUnionMember140FilterUnionMember18,
    FiltersUnionMember140FilterUnionMember19,
    FiltersUnionMember140FilterUnionMember20,
    FiltersUnionMember140FilterUnionMember21,
    FiltersUnionMember140FilterUnionMember22,
    FiltersUnionMember140FilterUnionMember23,
    FiltersUnionMember140FilterUnionMember24,
    FiltersUnionMember140FilterUnionMember25,
    FiltersUnionMember140FilterUnionMember26,
    FiltersUnionMember140FilterUnionMember27,
    FiltersUnionMember140FilterUnionMember28,
    FiltersUnionMember140FilterUnionMember29,
    FiltersUnionMember140FilterUnionMember30,
    FiltersUnionMember140FilterUnionMember31,
    FiltersUnionMember140FilterUnionMember32,
    FiltersUnionMember140FilterUnionMember33,
    FiltersUnionMember140FilterUnionMember34,
    FiltersUnionMember140FilterUnionMember35,
    FiltersUnionMember140FilterUnionMember36,
    FiltersUnionMember140FilterUnionMember37,
    FiltersUnionMember140FilterUnionMember38,
    FiltersUnionMember140FilterUnionMember39,
    FiltersUnionMember140FilterUnionMember40,
    FiltersUnionMember140FilterUnionMember41,
    FiltersUnionMember140FilterUnionMember42,
    FiltersUnionMember140FilterUnionMember43,
    FiltersUnionMember140FilterUnionMember44,
    FiltersUnionMember140FilterUnionMember45,
    FiltersUnionMember140FilterUnionMember46,
    FiltersUnionMember140FilterUnionMember47,
    FiltersUnionMember140FilterUnionMember48,
    FiltersUnionMember140FilterUnionMember49,
    FiltersUnionMember140FilterUnionMember50,
    FiltersUnionMember140FilterUnionMember51,
    FiltersUnionMember140FilterUnionMember52,
    FiltersUnionMember140FilterUnionMember53,
    FiltersUnionMember140FilterUnionMember54,
    FiltersUnionMember140FilterUnionMember55,
    FiltersUnionMember140FilterUnionMember56,
    FiltersUnionMember140FilterUnionMember57,
    FiltersUnionMember140FilterUnionMember58,
    FiltersUnionMember140FilterUnionMember59,
    FiltersUnionMember140FilterUnionMember60,
    FiltersUnionMember140FilterUnionMember61,
    FiltersUnionMember140FilterUnionMember62,
    FiltersUnionMember140FilterUnionMember63,
    FiltersUnionMember140FilterUnionMember64,
    FiltersUnionMember140FilterUnionMember65,
    FiltersUnionMember140FilterUnionMember66,
    FiltersUnionMember140FilterUnionMember67,
    FiltersUnionMember140FilterUnionMember68,
    FiltersUnionMember140FilterUnionMember69,
    FiltersUnionMember140FilterUnionMember70,
    FiltersUnionMember140FilterUnionMember71,
    FiltersUnionMember140FilterUnionMember72,
    FiltersUnionMember140FilterUnionMember73,
    FiltersUnionMember140FilterUnionMember74,
    FiltersUnionMember140FilterUnionMember75,
    FiltersUnionMember140FilterUnionMember76,
    FiltersUnionMember140FilterUnionMember77,
    FiltersUnionMember140FilterUnionMember78,
    FiltersUnionMember140FilterUnionMember79,
    FiltersUnionMember140FilterUnionMember80,
    FiltersUnionMember140FilterUnionMember81,
    FiltersUnionMember140FilterUnionMember82,
    FiltersUnionMember140FilterUnionMember83,
    FiltersUnionMember140FilterUnionMember84,
    FiltersUnionMember140FilterUnionMember85,
    FiltersUnionMember140FilterUnionMember86,
    FiltersUnionMember140FilterUnionMember87,
    FiltersUnionMember140FilterUnionMember88,
    FiltersUnionMember140FilterUnionMember89,
    FiltersUnionMember140FilterUnionMember90,
    FiltersUnionMember140FilterUnionMember91,
    FiltersUnionMember140FilterUnionMember92,
    FiltersUnionMember140FilterUnionMember93,
    FiltersUnionMember140FilterUnionMember94,
    FiltersUnionMember140FilterUnionMember95,
    FiltersUnionMember140FilterUnionMember96,
    FiltersUnionMember140FilterUnionMember97,
    FiltersUnionMember140FilterUnionMember98,
    FiltersUnionMember140FilterUnionMember99,
    FiltersUnionMember140FilterUnionMember100,
    FiltersUnionMember140FilterUnionMember101,
    FiltersUnionMember140FilterUnionMember102,
    FiltersUnionMember140FilterUnionMember103,
    FiltersUnionMember140FilterUnionMember104,
    FiltersUnionMember140FilterUnionMember105,
    FiltersUnionMember140FilterUnionMember106,
    FiltersUnionMember140FilterUnionMember107,
    FiltersUnionMember140FilterUnionMember108,
    FiltersUnionMember140FilterUnionMember109,
    FiltersUnionMember140FilterUnionMember110,
    FiltersUnionMember140FilterUnionMember111,
    FiltersUnionMember140FilterUnionMember112,
    FiltersUnionMember140FilterUnionMember113,
    FiltersUnionMember140FilterUnionMember114,
    FiltersUnionMember140FilterUnionMember115,
    FiltersUnionMember140FilterUnionMember116,
    FiltersUnionMember140FilterUnionMember117,
    FiltersUnionMember140FilterUnionMember118,
    FiltersUnionMember140FilterUnionMember119,
    FiltersUnionMember140FilterUnionMember120,
    FiltersUnionMember140FilterUnionMember121,
    FiltersUnionMember140FilterUnionMember122,
    FiltersUnionMember140FilterUnionMember123,
    FiltersUnionMember140FilterUnionMember124,
    FiltersUnionMember140FilterUnionMember125,
    FiltersUnionMember140FilterUnionMember126,
    FiltersUnionMember140FilterUnionMember127,
    FiltersUnionMember140FilterUnionMember128,
    FiltersUnionMember140FilterUnionMember129,
    FiltersUnionMember140FilterUnionMember130,
    FiltersUnionMember140FilterUnionMember131,
    FiltersUnionMember140FilterUnionMember132,
    FiltersUnionMember140FilterUnionMember133,
    FiltersUnionMember140FilterUnionMember134,
    FiltersUnionMember140FilterUnionMember135,
    FiltersUnionMember140FilterUnionMember136,
    FiltersUnionMember140FilterUnionMember137,
    FiltersUnionMember140FilterUnionMember138,
    FiltersUnionMember140FilterUnionMember139,
]


class FiltersUnionMember140(TypedDict, total=False):
    filters: Required[Iterable[FiltersUnionMember140Filter]]

    op: Required[Literal["And", "Or"]]


Filters: TypeAlias = Union[
    FiltersEq,
    FiltersNotEq,
    FiltersIn,
    FiltersNotIn,
    FiltersLt,
    FiltersLte,
    FiltersGt,
    FiltersGte,
    FiltersGlob,
    FiltersNotGlob,
    FiltersIGlob,
    FiltersNotIGlob,
    FiltersRegex,
    FiltersEq,
    FiltersNotEq,
    FiltersIn,
    FiltersNotIn,
    FiltersLt,
    FiltersLte,
    FiltersGt,
    FiltersGte,
    FiltersGlob,
    FiltersNotGlob,
    FiltersIGlob,
    FiltersNotIGlob,
    FiltersRegex,
    FiltersContainsAllTokens,
    FiltersEq,
    FiltersNotEq,
    FiltersIn,
    FiltersNotIn,
    FiltersLt,
    FiltersLte,
    FiltersGt,
    FiltersGte,
    FiltersGlob,
    FiltersNotGlob,
    FiltersIGlob,
    FiltersNotIGlob,
    FiltersRegex,
    FiltersContainsAllTokens,
    FiltersEq,
    FiltersNotEq,
    FiltersIn,
    FiltersNotIn,
    FiltersLt,
    FiltersLte,
    FiltersGt,
    FiltersGte,
    FiltersGlob,
    FiltersNotGlob,
    FiltersIGlob,
    FiltersNotIGlob,
    FiltersRegex,
    FiltersContainsAllTokens,
    FiltersEq,
    FiltersNotEq,
    FiltersIn,
    FiltersNotIn,
    FiltersLt,
    FiltersLte,
    FiltersGt,
    FiltersGte,
    FiltersGlob,
    FiltersNotGlob,
    FiltersIGlob,
    FiltersNotIGlob,
    FiltersRegex,
    FiltersContainsAllTokens,
    FiltersEq,
    FiltersNotEq,
    FiltersIn,
    FiltersNotIn,
    FiltersLt,
    FiltersLte,
    FiltersGt,
    FiltersGte,
    FiltersGlob,
    FiltersNotGlob,
    FiltersIGlob,
    FiltersNotIGlob,
    FiltersRegex,
    FiltersContainsAllTokens,
    FiltersEq,
    FiltersNotEq,
    FiltersIn,
    FiltersNotIn,
    FiltersLt,
    FiltersLte,
    FiltersGt,
    FiltersGte,
    FiltersGlob,
    FiltersNotGlob,
    FiltersIGlob,
    FiltersNotIGlob,
    FiltersRegex,
    FiltersContainsAllTokens,
    FiltersEq,
    FiltersNotEq,
    FiltersIn,
    FiltersNotIn,
    FiltersLt,
    FiltersLte,
    FiltersGt,
    FiltersGte,
    FiltersGlob,
    FiltersNotGlob,
    FiltersIGlob,
    FiltersNotIGlob,
    FiltersRegex,
    FiltersContainsAllTokens,
    FiltersEq,
    FiltersNotEq,
    FiltersIn,
    FiltersNotIn,
    FiltersLt,
    FiltersLte,
    FiltersGt,
    FiltersGte,
    FiltersGlob,
    FiltersNotGlob,
    FiltersIGlob,
    FiltersNotIGlob,
    FiltersRegex,
    FiltersContainsAllTokens,
    FiltersEq,
    FiltersNotEq,
    FiltersIn,
    FiltersNotIn,
    FiltersLt,
    FiltersLte,
    FiltersGt,
    FiltersGte,
    FiltersGlob,
    FiltersNotGlob,
    FiltersIGlob,
    FiltersNotIGlob,
    FiltersRegex,
    FiltersContainsAllTokens,
    FiltersUnionMember139,
    FiltersUnionMember140,
]
