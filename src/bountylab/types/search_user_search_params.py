# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "SearchUserSearchParams",
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
    "IncludeAttributes",
    "IncludeAttributesContributes",
    "IncludeAttributesContributesFilters",
    "IncludeAttributesContributesFiltersEq",
    "IncludeAttributesContributesFiltersNotEq",
    "IncludeAttributesContributesFiltersIn",
    "IncludeAttributesContributesFiltersNotIn",
    "IncludeAttributesContributesFiltersLt",
    "IncludeAttributesContributesFiltersLte",
    "IncludeAttributesContributesFiltersGt",
    "IncludeAttributesContributesFiltersGte",
    "IncludeAttributesContributesFiltersGlob",
    "IncludeAttributesContributesFiltersNotGlob",
    "IncludeAttributesContributesFiltersIGlob",
    "IncludeAttributesContributesFiltersNotIGlob",
    "IncludeAttributesContributesFiltersRegex",
    "IncludeAttributesContributesFiltersContainsAllTokens",
    "IncludeAttributesContributesFiltersUnionMember139",
    "IncludeAttributesContributesFiltersUnionMember139Filter",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember0",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember1",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember2",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember3",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember4",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember5",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember6",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember7",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember8",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember9",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember10",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember11",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember12",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember13",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember14",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember15",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember16",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember17",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember18",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember19",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember20",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember21",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember22",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember23",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember24",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember25",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember26",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember27",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember28",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember29",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember30",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember31",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember32",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember33",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember34",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember35",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember36",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember37",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember38",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember39",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember40",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember41",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember42",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember43",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember44",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember45",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember46",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember47",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember48",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember49",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember50",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember51",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember52",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember53",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember54",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember55",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember56",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember57",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember58",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember59",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember60",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember61",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember62",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember63",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember64",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember65",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember66",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember67",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember68",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember69",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember70",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember71",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember72",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember73",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember74",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember75",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember76",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember77",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember78",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember79",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember80",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember81",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember82",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember83",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember84",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember85",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember86",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember87",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember88",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember89",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember90",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember91",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember92",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember93",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember94",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember95",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember96",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember97",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember98",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember99",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember100",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember101",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember102",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember103",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember104",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember105",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember106",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember107",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember108",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember109",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember110",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember111",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember112",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember113",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember114",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember115",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember116",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember117",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember118",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember119",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember120",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember121",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember122",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember123",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember124",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember125",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember126",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember127",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember128",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember129",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember130",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember131",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember132",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember133",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember134",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember135",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember136",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember137",
    "IncludeAttributesContributesFiltersUnionMember139FilterUnionMember138",
    "IncludeAttributesContributesFiltersUnionMember140",
    "IncludeAttributesContributesFiltersUnionMember140Filter",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember0",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember1",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember2",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember3",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember4",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember5",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember6",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember7",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember8",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember9",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember10",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember11",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember12",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember13",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember14",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember15",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember16",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember17",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember18",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember19",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember20",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember21",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember22",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember23",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember24",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember25",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember26",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember27",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember28",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember29",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember30",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember31",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember32",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember33",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember34",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember35",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember36",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember37",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember38",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember39",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember40",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember41",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember42",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember43",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember44",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember45",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember46",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember47",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember48",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember49",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember50",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember51",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember52",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember53",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember54",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember55",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember56",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember57",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember58",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember59",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember60",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember61",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember62",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember63",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember64",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember65",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember66",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember67",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember68",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember69",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember70",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember71",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember72",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember73",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember74",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember75",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember76",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember77",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember78",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember79",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember80",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember81",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember82",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember83",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember84",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember85",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember86",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember87",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember88",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember89",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember90",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember91",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember92",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember93",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember94",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember95",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember96",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember97",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember98",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember99",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember100",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember101",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember102",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember103",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember104",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember105",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember106",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember107",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember108",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember109",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember110",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember111",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember112",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember113",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember114",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember115",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember116",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember117",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember118",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember119",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember120",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember121",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember122",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember123",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember124",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember125",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember126",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember127",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember128",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember129",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember130",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember131",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember132",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember133",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember134",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember135",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember136",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember137",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember138",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139Filter",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember0",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember1",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember2",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember3",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember4",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember5",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember6",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember7",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember8",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember9",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember10",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember11",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember12",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember13",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember14",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember15",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember16",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember17",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember18",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember19",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember20",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember21",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember22",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember23",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember24",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember25",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember26",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember27",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember28",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember29",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember30",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember31",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember32",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember33",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember34",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember35",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember36",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember37",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember38",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember39",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember40",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember41",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember42",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember43",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember44",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember45",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember46",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember47",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember48",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember49",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember50",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember51",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember52",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember53",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember54",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember55",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember56",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember57",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember58",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember59",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember60",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember61",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember62",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember63",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember64",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember65",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember66",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember67",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember68",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember69",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember70",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember71",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember72",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember73",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember74",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember75",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember76",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember77",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember78",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember79",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember80",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember81",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember82",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember83",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember84",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember85",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember86",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember87",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember88",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember89",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember90",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember91",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember92",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember93",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember94",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember95",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember96",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember97",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember98",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember99",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember100",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember101",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember102",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember103",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember104",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember105",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember106",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember107",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember108",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember109",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember110",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember111",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember112",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember113",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember114",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember115",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember116",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember117",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember118",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember119",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember120",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember121",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember122",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember123",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember124",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember125",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember126",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember127",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember128",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember129",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember130",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember131",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember132",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember133",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember134",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember135",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember136",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember137",
    "IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember138",
    "IncludeAttributesFollowers",
    "IncludeAttributesFollowersFilters",
    "IncludeAttributesFollowersFiltersEq",
    "IncludeAttributesFollowersFiltersNotEq",
    "IncludeAttributesFollowersFiltersIn",
    "IncludeAttributesFollowersFiltersNotIn",
    "IncludeAttributesFollowersFiltersLt",
    "IncludeAttributesFollowersFiltersLte",
    "IncludeAttributesFollowersFiltersGt",
    "IncludeAttributesFollowersFiltersGte",
    "IncludeAttributesFollowersFiltersGlob",
    "IncludeAttributesFollowersFiltersNotGlob",
    "IncludeAttributesFollowersFiltersIGlob",
    "IncludeAttributesFollowersFiltersNotIGlob",
    "IncludeAttributesFollowersFiltersRegex",
    "IncludeAttributesFollowersFiltersContainsAllTokens",
    "IncludeAttributesFollowersFiltersUnionMember139",
    "IncludeAttributesFollowersFiltersUnionMember139Filter",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember0",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember1",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember2",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember3",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember4",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember5",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember6",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember7",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember8",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember9",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember10",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember11",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember12",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember13",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember14",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember15",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember16",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember17",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember18",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember19",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember20",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember21",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember22",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember23",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember24",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember25",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember26",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember27",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember28",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember29",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember30",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember31",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember32",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember33",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember34",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember35",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember36",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember37",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember38",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember39",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember40",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember41",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember42",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember43",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember44",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember45",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember46",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember47",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember48",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember49",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember50",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember51",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember52",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember53",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember54",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember55",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember56",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember57",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember58",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember59",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember60",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember61",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember62",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember63",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember64",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember65",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember66",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember67",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember68",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember69",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember70",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember71",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember72",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember73",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember74",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember75",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember76",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember77",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember78",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember79",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember80",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember81",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember82",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember83",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember84",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember85",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember86",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember87",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember88",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember89",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember90",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember91",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember92",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember93",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember94",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember95",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember96",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember97",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember98",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember99",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember100",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember101",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember102",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember103",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember104",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember105",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember106",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember107",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember108",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember109",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember110",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember111",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember112",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember113",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember114",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember115",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember116",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember117",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember118",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember119",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember120",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember121",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember122",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember123",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember124",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember125",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember126",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember127",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember128",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember129",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember130",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember131",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember132",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember133",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember134",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember135",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember136",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember137",
    "IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember138",
    "IncludeAttributesFollowersFiltersUnionMember140",
    "IncludeAttributesFollowersFiltersUnionMember140Filter",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember0",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember1",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember2",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember3",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember4",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember5",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember6",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember7",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember8",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember9",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember10",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember11",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember12",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember13",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember14",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember15",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember16",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember17",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember18",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember19",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember20",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember21",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember22",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember23",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember24",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember25",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember26",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember27",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember28",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember29",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember30",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember31",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember32",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember33",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember34",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember35",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember36",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember37",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember38",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember39",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember40",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember41",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember42",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember43",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember44",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember45",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember46",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember47",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember48",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember49",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember50",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember51",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember52",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember53",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember54",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember55",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember56",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember57",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember58",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember59",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember60",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember61",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember62",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember63",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember64",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember65",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember66",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember67",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember68",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember69",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember70",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember71",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember72",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember73",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember74",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember75",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember76",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember77",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember78",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember79",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember80",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember81",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember82",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember83",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember84",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember85",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember86",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember87",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember88",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember89",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember90",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember91",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember92",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember93",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember94",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember95",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember96",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember97",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember98",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember99",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember100",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember101",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember102",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember103",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember104",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember105",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember106",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember107",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember108",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember109",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember110",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember111",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember112",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember113",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember114",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember115",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember116",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember117",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember118",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember119",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember120",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember121",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember122",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember123",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember124",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember125",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember126",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember127",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember128",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember129",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember130",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember131",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember132",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember133",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember134",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember135",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember136",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember137",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember138",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139Filter",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember0",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember1",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember2",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember3",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember4",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember5",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember6",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember7",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember8",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember9",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember10",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember11",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember12",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember13",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember14",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember15",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember16",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember17",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember18",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember19",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember20",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember21",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember22",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember23",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember24",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember25",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember26",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember27",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember28",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember29",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember30",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember31",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember32",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember33",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember34",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember35",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember36",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember37",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember38",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember39",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember40",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember41",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember42",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember43",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember44",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember45",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember46",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember47",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember48",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember49",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember50",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember51",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember52",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember53",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember54",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember55",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember56",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember57",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember58",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember59",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember60",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember61",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember62",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember63",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember64",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember65",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember66",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember67",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember68",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember69",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember70",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember71",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember72",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember73",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember74",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember75",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember76",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember77",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember78",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember79",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember80",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember81",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember82",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember83",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember84",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember85",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember86",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember87",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember88",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember89",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember90",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember91",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember92",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember93",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember94",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember95",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember96",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember97",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember98",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember99",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember100",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember101",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember102",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember103",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember104",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember105",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember106",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember107",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember108",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember109",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember110",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember111",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember112",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember113",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember114",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember115",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember116",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember117",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember118",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember119",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember120",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember121",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember122",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember123",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember124",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember125",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember126",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember127",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember128",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember129",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember130",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember131",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember132",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember133",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember134",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember135",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember136",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember137",
    "IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember138",
    "IncludeAttributesFollowing",
    "IncludeAttributesFollowingFilters",
    "IncludeAttributesFollowingFiltersEq",
    "IncludeAttributesFollowingFiltersNotEq",
    "IncludeAttributesFollowingFiltersIn",
    "IncludeAttributesFollowingFiltersNotIn",
    "IncludeAttributesFollowingFiltersLt",
    "IncludeAttributesFollowingFiltersLte",
    "IncludeAttributesFollowingFiltersGt",
    "IncludeAttributesFollowingFiltersGte",
    "IncludeAttributesFollowingFiltersGlob",
    "IncludeAttributesFollowingFiltersNotGlob",
    "IncludeAttributesFollowingFiltersIGlob",
    "IncludeAttributesFollowingFiltersNotIGlob",
    "IncludeAttributesFollowingFiltersRegex",
    "IncludeAttributesFollowingFiltersContainsAllTokens",
    "IncludeAttributesFollowingFiltersUnionMember139",
    "IncludeAttributesFollowingFiltersUnionMember139Filter",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember0",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember1",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember2",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember3",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember4",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember5",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember6",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember7",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember8",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember9",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember10",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember11",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember12",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember13",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember14",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember15",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember16",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember17",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember18",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember19",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember20",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember21",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember22",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember23",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember24",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember25",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember26",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember27",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember28",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember29",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember30",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember31",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember32",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember33",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember34",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember35",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember36",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember37",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember38",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember39",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember40",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember41",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember42",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember43",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember44",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember45",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember46",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember47",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember48",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember49",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember50",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember51",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember52",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember53",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember54",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember55",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember56",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember57",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember58",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember59",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember60",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember61",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember62",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember63",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember64",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember65",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember66",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember67",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember68",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember69",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember70",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember71",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember72",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember73",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember74",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember75",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember76",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember77",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember78",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember79",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember80",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember81",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember82",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember83",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember84",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember85",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember86",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember87",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember88",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember89",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember90",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember91",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember92",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember93",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember94",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember95",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember96",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember97",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember98",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember99",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember100",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember101",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember102",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember103",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember104",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember105",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember106",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember107",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember108",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember109",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember110",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember111",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember112",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember113",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember114",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember115",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember116",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember117",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember118",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember119",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember120",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember121",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember122",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember123",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember124",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember125",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember126",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember127",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember128",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember129",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember130",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember131",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember132",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember133",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember134",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember135",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember136",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember137",
    "IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember138",
    "IncludeAttributesFollowingFiltersUnionMember140",
    "IncludeAttributesFollowingFiltersUnionMember140Filter",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember0",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember1",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember2",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember3",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember4",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember5",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember6",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember7",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember8",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember9",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember10",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember11",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember12",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember13",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember14",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember15",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember16",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember17",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember18",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember19",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember20",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember21",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember22",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember23",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember24",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember25",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember26",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember27",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember28",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember29",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember30",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember31",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember32",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember33",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember34",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember35",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember36",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember37",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember38",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember39",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember40",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember41",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember42",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember43",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember44",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember45",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember46",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember47",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember48",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember49",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember50",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember51",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember52",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember53",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember54",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember55",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember56",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember57",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember58",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember59",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember60",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember61",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember62",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember63",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember64",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember65",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember66",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember67",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember68",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember69",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember70",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember71",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember72",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember73",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember74",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember75",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember76",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember77",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember78",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember79",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember80",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember81",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember82",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember83",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember84",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember85",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember86",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember87",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember88",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember89",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember90",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember91",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember92",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember93",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember94",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember95",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember96",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember97",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember98",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember99",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember100",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember101",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember102",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember103",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember104",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember105",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember106",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember107",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember108",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember109",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember110",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember111",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember112",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember113",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember114",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember115",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember116",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember117",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember118",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember119",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember120",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember121",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember122",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember123",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember124",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember125",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember126",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember127",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember128",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember129",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember130",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember131",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember132",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember133",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember134",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember135",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember136",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember137",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember138",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139Filter",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember0",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember1",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember2",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember3",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember4",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember5",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember6",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember7",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember8",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember9",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember10",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember11",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember12",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember13",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember14",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember15",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember16",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember17",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember18",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember19",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember20",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember21",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember22",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember23",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember24",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember25",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember26",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember27",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember28",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember29",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember30",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember31",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember32",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember33",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember34",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember35",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember36",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember37",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember38",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember39",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember40",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember41",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember42",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember43",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember44",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember45",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember46",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember47",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember48",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember49",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember50",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember51",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember52",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember53",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember54",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember55",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember56",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember57",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember58",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember59",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember60",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember61",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember62",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember63",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember64",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember65",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember66",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember67",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember68",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember69",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember70",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember71",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember72",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember73",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember74",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember75",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember76",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember77",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember78",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember79",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember80",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember81",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember82",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember83",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember84",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember85",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember86",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember87",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember88",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember89",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember90",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember91",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember92",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember93",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember94",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember95",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember96",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember97",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember98",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember99",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember100",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember101",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember102",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember103",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember104",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember105",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember106",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember107",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember108",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember109",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember110",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember111",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember112",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember113",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember114",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember115",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember116",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember117",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember118",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember119",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember120",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember121",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember122",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember123",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember124",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember125",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember126",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember127",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember128",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember129",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember130",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember131",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember132",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember133",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember134",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember135",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember136",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember137",
    "IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember138",
    "IncludeAttributesOwns",
    "IncludeAttributesOwnsFilters",
    "IncludeAttributesOwnsFiltersEq",
    "IncludeAttributesOwnsFiltersNotEq",
    "IncludeAttributesOwnsFiltersIn",
    "IncludeAttributesOwnsFiltersNotIn",
    "IncludeAttributesOwnsFiltersLt",
    "IncludeAttributesOwnsFiltersLte",
    "IncludeAttributesOwnsFiltersGt",
    "IncludeAttributesOwnsFiltersGte",
    "IncludeAttributesOwnsFiltersGlob",
    "IncludeAttributesOwnsFiltersNotGlob",
    "IncludeAttributesOwnsFiltersIGlob",
    "IncludeAttributesOwnsFiltersNotIGlob",
    "IncludeAttributesOwnsFiltersRegex",
    "IncludeAttributesOwnsFiltersContainsAllTokens",
    "IncludeAttributesOwnsFiltersUnionMember139",
    "IncludeAttributesOwnsFiltersUnionMember139Filter",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember0",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember1",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember2",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember3",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember4",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember5",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember6",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember7",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember8",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember9",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember10",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember11",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember12",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember13",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember14",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember15",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember16",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember17",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember18",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember19",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember20",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember21",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember22",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember23",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember24",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember25",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember26",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember27",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember28",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember29",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember30",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember31",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember32",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember33",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember34",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember35",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember36",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember37",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember38",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember39",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember40",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember41",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember42",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember43",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember44",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember45",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember46",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember47",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember48",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember49",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember50",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember51",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember52",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember53",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember54",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember55",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember56",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember57",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember58",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember59",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember60",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember61",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember62",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember63",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember64",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember65",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember66",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember67",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember68",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember69",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember70",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember71",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember72",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember73",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember74",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember75",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember76",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember77",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember78",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember79",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember80",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember81",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember82",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember83",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember84",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember85",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember86",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember87",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember88",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember89",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember90",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember91",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember92",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember93",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember94",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember95",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember96",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember97",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember98",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember99",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember100",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember101",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember102",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember103",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember104",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember105",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember106",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember107",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember108",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember109",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember110",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember111",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember112",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember113",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember114",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember115",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember116",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember117",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember118",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember119",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember120",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember121",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember122",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember123",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember124",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember125",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember126",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember127",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember128",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember129",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember130",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember131",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember132",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember133",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember134",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember135",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember136",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember137",
    "IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember138",
    "IncludeAttributesOwnsFiltersUnionMember140",
    "IncludeAttributesOwnsFiltersUnionMember140Filter",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember0",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember1",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember2",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember3",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember4",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember5",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember6",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember7",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember8",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember9",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember10",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember11",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember12",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember13",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember14",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember15",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember16",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember17",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember18",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember19",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember20",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember21",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember22",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember23",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember24",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember25",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember26",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember27",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember28",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember29",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember30",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember31",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember32",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember33",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember34",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember35",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember36",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember37",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember38",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember39",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember40",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember41",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember42",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember43",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember44",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember45",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember46",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember47",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember48",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember49",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember50",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember51",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember52",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember53",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember54",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember55",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember56",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember57",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember58",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember59",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember60",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember61",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember62",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember63",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember64",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember65",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember66",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember67",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember68",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember69",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember70",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember71",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember72",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember73",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember74",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember75",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember76",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember77",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember78",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember79",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember80",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember81",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember82",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember83",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember84",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember85",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember86",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember87",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember88",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember89",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember90",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember91",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember92",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember93",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember94",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember95",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember96",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember97",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember98",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember99",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember100",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember101",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember102",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember103",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember104",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember105",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember106",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember107",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember108",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember109",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember110",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember111",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember112",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember113",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember114",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember115",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember116",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember117",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember118",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember119",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember120",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember121",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember122",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember123",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember124",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember125",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember126",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember127",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember128",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember129",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember130",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember131",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember132",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember133",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember134",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember135",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember136",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember137",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember138",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139Filter",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember0",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember1",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember2",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember3",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember4",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember5",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember6",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember7",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember8",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember9",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember10",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember11",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember12",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember13",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember14",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember15",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember16",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember17",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember18",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember19",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember20",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember21",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember22",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember23",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember24",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember25",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember26",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember27",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember28",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember29",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember30",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember31",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember32",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember33",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember34",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember35",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember36",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember37",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember38",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember39",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember40",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember41",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember42",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember43",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember44",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember45",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember46",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember47",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember48",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember49",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember50",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember51",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember52",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember53",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember54",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember55",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember56",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember57",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember58",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember59",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember60",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember61",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember62",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember63",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember64",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember65",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember66",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember67",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember68",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember69",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember70",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember71",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember72",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember73",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember74",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember75",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember76",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember77",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember78",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember79",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember80",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember81",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember82",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember83",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember84",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember85",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember86",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember87",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember88",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember89",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember90",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember91",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember92",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember93",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember94",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember95",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember96",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember97",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember98",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember99",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember100",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember101",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember102",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember103",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember104",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember105",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember106",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember107",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember108",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember109",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember110",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember111",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember112",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember113",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember114",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember115",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember116",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember117",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember118",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember119",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember120",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember121",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember122",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember123",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember124",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember125",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember126",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember127",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember128",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember129",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember130",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember131",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember132",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember133",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember134",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember135",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember136",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember137",
    "IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember138",
    "IncludeAttributesStars",
    "IncludeAttributesStarsFilters",
    "IncludeAttributesStarsFiltersEq",
    "IncludeAttributesStarsFiltersNotEq",
    "IncludeAttributesStarsFiltersIn",
    "IncludeAttributesStarsFiltersNotIn",
    "IncludeAttributesStarsFiltersLt",
    "IncludeAttributesStarsFiltersLte",
    "IncludeAttributesStarsFiltersGt",
    "IncludeAttributesStarsFiltersGte",
    "IncludeAttributesStarsFiltersGlob",
    "IncludeAttributesStarsFiltersNotGlob",
    "IncludeAttributesStarsFiltersIGlob",
    "IncludeAttributesStarsFiltersNotIGlob",
    "IncludeAttributesStarsFiltersRegex",
    "IncludeAttributesStarsFiltersContainsAllTokens",
    "IncludeAttributesStarsFiltersUnionMember139",
    "IncludeAttributesStarsFiltersUnionMember139Filter",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember0",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember1",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember2",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember3",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember4",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember5",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember6",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember7",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember8",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember9",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember10",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember11",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember12",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember13",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember14",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember15",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember16",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember17",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember18",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember19",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember20",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember21",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember22",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember23",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember24",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember25",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember26",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember27",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember28",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember29",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember30",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember31",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember32",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember33",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember34",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember35",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember36",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember37",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember38",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember39",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember40",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember41",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember42",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember43",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember44",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember45",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember46",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember47",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember48",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember49",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember50",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember51",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember52",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember53",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember54",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember55",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember56",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember57",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember58",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember59",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember60",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember61",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember62",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember63",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember64",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember65",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember66",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember67",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember68",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember69",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember70",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember71",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember72",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember73",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember74",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember75",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember76",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember77",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember78",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember79",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember80",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember81",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember82",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember83",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember84",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember85",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember86",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember87",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember88",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember89",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember90",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember91",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember92",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember93",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember94",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember95",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember96",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember97",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember98",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember99",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember100",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember101",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember102",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember103",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember104",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember105",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember106",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember107",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember108",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember109",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember110",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember111",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember112",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember113",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember114",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember115",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember116",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember117",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember118",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember119",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember120",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember121",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember122",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember123",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember124",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember125",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember126",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember127",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember128",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember129",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember130",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember131",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember132",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember133",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember134",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember135",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember136",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember137",
    "IncludeAttributesStarsFiltersUnionMember139FilterUnionMember138",
    "IncludeAttributesStarsFiltersUnionMember140",
    "IncludeAttributesStarsFiltersUnionMember140Filter",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember0",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember1",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember2",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember3",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember4",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember5",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember6",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember7",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember8",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember9",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember10",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember11",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember12",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember13",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember14",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember15",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember16",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember17",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember18",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember19",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember20",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember21",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember22",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember23",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember24",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember25",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember26",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember27",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember28",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember29",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember30",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember31",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember32",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember33",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember34",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember35",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember36",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember37",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember38",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember39",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember40",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember41",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember42",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember43",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember44",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember45",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember46",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember47",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember48",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember49",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember50",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember51",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember52",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember53",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember54",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember55",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember56",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember57",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember58",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember59",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember60",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember61",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember62",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember63",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember64",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember65",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember66",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember67",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember68",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember69",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember70",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember71",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember72",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember73",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember74",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember75",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember76",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember77",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember78",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember79",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember80",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember81",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember82",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember83",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember84",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember85",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember86",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember87",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember88",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember89",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember90",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember91",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember92",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember93",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember94",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember95",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember96",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember97",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember98",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember99",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember100",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember101",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember102",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember103",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember104",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember105",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember106",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember107",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember108",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember109",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember110",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember111",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember112",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember113",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember114",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember115",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember116",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember117",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember118",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember119",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember120",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember121",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember122",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember123",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember124",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember125",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember126",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember127",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember128",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember129",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember130",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember131",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember132",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember133",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember134",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember135",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember136",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember137",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember138",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139Filter",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember0",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember1",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember2",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember3",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember4",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember5",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember6",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember7",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember8",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember9",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember10",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember11",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember12",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember13",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember14",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember15",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember16",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember17",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember18",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember19",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember20",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember21",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember22",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember23",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember24",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember25",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember26",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember27",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember28",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember29",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember30",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember31",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember32",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember33",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember34",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember35",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember36",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember37",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember38",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember39",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember40",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember41",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember42",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember43",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember44",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember45",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember46",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember47",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember48",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember49",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember50",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember51",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember52",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember53",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember54",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember55",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember56",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember57",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember58",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember59",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember60",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember61",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember62",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember63",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember64",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember65",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember66",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember67",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember68",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember69",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember70",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember71",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember72",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember73",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember74",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember75",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember76",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember77",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember78",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember79",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember80",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember81",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember82",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember83",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember84",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember85",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember86",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember87",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember88",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember89",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember90",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember91",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember92",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember93",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember94",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember95",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember96",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember97",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember98",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember99",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember100",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember101",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember102",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember103",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember104",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember105",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember106",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember107",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember108",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember109",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember110",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember111",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember112",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember113",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember114",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember115",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember116",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember117",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember118",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember119",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember120",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember121",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember122",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember123",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember124",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember125",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember126",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember127",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember128",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember129",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember130",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember131",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember132",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember133",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember134",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember135",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember136",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember137",
    "IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember138",
]


class SearchUserSearchParams(TypedDict, total=False):
    query: Required[Union[str, SequenceNotStr[str], None]]
    """Full-text search query across user fields.

    Searches: login, displayName, bio, company, location, emails, resolvedCountry,
    resolvedState, resolvedCity (with login weighted 2x). Supports: string (single
    query), string[] (RRF fusion), null (filter-only)
    """

    after: str
    """Cursor for pagination (from previous response pageInfo.endCursor)"""

    enable_pagination: Annotated[bool, PropertyInfo(alias="enablePagination")]
    """Enable cursor-based pagination to fetch results across multiple requests"""

    filters: Filters
    """Optional filters for users.

    Supports fields like login, company, location, resolvedCountry, resolvedState,
    resolvedCity. Operators: Eq, NotEq, In, NotIn, Lt, Lte, Gt, Gte.
    """

    first: int
    """Alias for maxResults (takes precedence if both provided)"""

    include_attributes: Annotated[IncludeAttributes, PropertyInfo(alias="includeAttributes")]
    """
    Optional graph relationships to include (followers, following, stars, owns,
    contributes)
    """

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
    """Maximum number of results to return (default: 100, max: 1000)"""


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


class IncludeAttributesContributesFiltersEq(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersNotEq(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersIn(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersNotIn(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersLt(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersLte(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersGt(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersGte(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersNotGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersIGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersNotIGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersRegex(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersContainsAllTokens(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember139FilterUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


IncludeAttributesContributesFiltersUnionMember139Filter: TypeAlias = Union[
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember0,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember1,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember2,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember3,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember4,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember5,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember6,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember7,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember8,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember9,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember10,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember11,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember12,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember13,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember14,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember15,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember16,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember17,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember18,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember19,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember20,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember21,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember22,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember23,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember24,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember25,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember26,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember27,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember28,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember29,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember30,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember31,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember32,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember33,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember34,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember35,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember36,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember37,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember38,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember39,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember40,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember41,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember42,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember43,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember44,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember45,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember46,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember47,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember48,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember49,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember50,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember51,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember52,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember53,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember54,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember55,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember56,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember57,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember58,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember59,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember60,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember61,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember62,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember63,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember64,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember65,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember66,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember67,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember68,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember69,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember70,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember71,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember72,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember73,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember74,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember75,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember76,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember77,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember78,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember79,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember80,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember81,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember82,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember83,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember84,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember85,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember86,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember87,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember88,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember89,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember90,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember91,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember92,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember93,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember94,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember95,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember96,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember97,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember98,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember99,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember100,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember101,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember102,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember103,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember104,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember105,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember106,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember107,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember108,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember109,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember110,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember111,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember112,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember113,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember114,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember115,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember116,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember117,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember118,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember119,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember120,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember121,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember122,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember123,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember124,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember125,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember126,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember127,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember128,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember129,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember130,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember131,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember132,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember133,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember134,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember135,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember136,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember137,
    IncludeAttributesContributesFiltersUnionMember139FilterUnionMember138,
]


class IncludeAttributesContributesFiltersUnionMember139(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesContributesFiltersUnionMember139Filter]]

    op: Required[Literal["And", "Or"]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139Filter: TypeAlias = Union[
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember0,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember1,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember2,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember3,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember4,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember5,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember6,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember7,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember8,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember9,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember10,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember11,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember12,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember13,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember14,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember15,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember16,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember17,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember18,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember19,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember20,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember21,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember22,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember23,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember24,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember25,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember26,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember27,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember28,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember29,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember30,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember31,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember32,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember33,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember34,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember35,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember36,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember37,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember38,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember39,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember40,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember41,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember42,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember43,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember44,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember45,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember46,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember47,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember48,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember49,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember50,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember51,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember52,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember53,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember54,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember55,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember56,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember57,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember58,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember59,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember60,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember61,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember62,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember63,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember64,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember65,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember66,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember67,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember68,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember69,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember70,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember71,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember72,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember73,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember74,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember75,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember76,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember77,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember78,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember79,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember80,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember81,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember82,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember83,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember84,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember85,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember86,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember87,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember88,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember89,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember90,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember91,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember92,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember93,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember94,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember95,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember96,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember97,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember98,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember99,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember100,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember101,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember102,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember103,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember104,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember105,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember106,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember107,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember108,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember109,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember110,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember111,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember112,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember113,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember114,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember115,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember116,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember117,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember118,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember119,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember120,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember121,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember122,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember123,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember124,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember125,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember126,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember127,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember128,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember129,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember130,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember131,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember132,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember133,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember134,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember135,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember136,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember137,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139FilterUnionMember138,
]


class IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139Filter]]

    op: Required[Literal["And", "Or"]]


IncludeAttributesContributesFiltersUnionMember140Filter: TypeAlias = Union[
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember0,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember1,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember2,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember3,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember4,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember5,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember6,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember7,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember8,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember9,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember10,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember11,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember12,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember13,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember14,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember15,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember16,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember17,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember18,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember19,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember20,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember21,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember22,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember23,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember24,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember25,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember26,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember27,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember28,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember29,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember30,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember31,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember32,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember33,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember34,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember35,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember36,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember37,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember38,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember39,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember40,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember41,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember42,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember43,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember44,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember45,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember46,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember47,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember48,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember49,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember50,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember51,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember52,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember53,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember54,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember55,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember56,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember57,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember58,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember59,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember60,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember61,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember62,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember63,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember64,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember65,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember66,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember67,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember68,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember69,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember70,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember71,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember72,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember73,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember74,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember75,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember76,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember77,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember78,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember79,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember80,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember81,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember82,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember83,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember84,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember85,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember86,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember87,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember88,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember89,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember90,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember91,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember92,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember93,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember94,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember95,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember96,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember97,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember98,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember99,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember100,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember101,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember102,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember103,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember104,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember105,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember106,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember107,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember108,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember109,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember110,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember111,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember112,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember113,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember114,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember115,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember116,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember117,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember118,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember119,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember120,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember121,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember122,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember123,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember124,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember125,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember126,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember127,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember128,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember129,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember130,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember131,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember132,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember133,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember134,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember135,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember136,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember137,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember138,
    IncludeAttributesContributesFiltersUnionMember140FilterUnionMember139,
]


class IncludeAttributesContributesFiltersUnionMember140(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesContributesFiltersUnionMember140Filter]]

    op: Required[Literal["And", "Or"]]


IncludeAttributesContributesFilters: TypeAlias = Union[
    IncludeAttributesContributesFiltersEq,
    IncludeAttributesContributesFiltersNotEq,
    IncludeAttributesContributesFiltersIn,
    IncludeAttributesContributesFiltersNotIn,
    IncludeAttributesContributesFiltersLt,
    IncludeAttributesContributesFiltersLte,
    IncludeAttributesContributesFiltersGt,
    IncludeAttributesContributesFiltersGte,
    IncludeAttributesContributesFiltersGlob,
    IncludeAttributesContributesFiltersNotGlob,
    IncludeAttributesContributesFiltersIGlob,
    IncludeAttributesContributesFiltersNotIGlob,
    IncludeAttributesContributesFiltersRegex,
    IncludeAttributesContributesFiltersEq,
    IncludeAttributesContributesFiltersNotEq,
    IncludeAttributesContributesFiltersIn,
    IncludeAttributesContributesFiltersNotIn,
    IncludeAttributesContributesFiltersLt,
    IncludeAttributesContributesFiltersLte,
    IncludeAttributesContributesFiltersGt,
    IncludeAttributesContributesFiltersGte,
    IncludeAttributesContributesFiltersGlob,
    IncludeAttributesContributesFiltersNotGlob,
    IncludeAttributesContributesFiltersIGlob,
    IncludeAttributesContributesFiltersNotIGlob,
    IncludeAttributesContributesFiltersRegex,
    IncludeAttributesContributesFiltersContainsAllTokens,
    IncludeAttributesContributesFiltersEq,
    IncludeAttributesContributesFiltersNotEq,
    IncludeAttributesContributesFiltersIn,
    IncludeAttributesContributesFiltersNotIn,
    IncludeAttributesContributesFiltersLt,
    IncludeAttributesContributesFiltersLte,
    IncludeAttributesContributesFiltersGt,
    IncludeAttributesContributesFiltersGte,
    IncludeAttributesContributesFiltersGlob,
    IncludeAttributesContributesFiltersNotGlob,
    IncludeAttributesContributesFiltersIGlob,
    IncludeAttributesContributesFiltersNotIGlob,
    IncludeAttributesContributesFiltersRegex,
    IncludeAttributesContributesFiltersContainsAllTokens,
    IncludeAttributesContributesFiltersEq,
    IncludeAttributesContributesFiltersNotEq,
    IncludeAttributesContributesFiltersIn,
    IncludeAttributesContributesFiltersNotIn,
    IncludeAttributesContributesFiltersLt,
    IncludeAttributesContributesFiltersLte,
    IncludeAttributesContributesFiltersGt,
    IncludeAttributesContributesFiltersGte,
    IncludeAttributesContributesFiltersGlob,
    IncludeAttributesContributesFiltersNotGlob,
    IncludeAttributesContributesFiltersIGlob,
    IncludeAttributesContributesFiltersNotIGlob,
    IncludeAttributesContributesFiltersRegex,
    IncludeAttributesContributesFiltersContainsAllTokens,
    IncludeAttributesContributesFiltersEq,
    IncludeAttributesContributesFiltersNotEq,
    IncludeAttributesContributesFiltersIn,
    IncludeAttributesContributesFiltersNotIn,
    IncludeAttributesContributesFiltersLt,
    IncludeAttributesContributesFiltersLte,
    IncludeAttributesContributesFiltersGt,
    IncludeAttributesContributesFiltersGte,
    IncludeAttributesContributesFiltersGlob,
    IncludeAttributesContributesFiltersNotGlob,
    IncludeAttributesContributesFiltersIGlob,
    IncludeAttributesContributesFiltersNotIGlob,
    IncludeAttributesContributesFiltersRegex,
    IncludeAttributesContributesFiltersContainsAllTokens,
    IncludeAttributesContributesFiltersEq,
    IncludeAttributesContributesFiltersNotEq,
    IncludeAttributesContributesFiltersIn,
    IncludeAttributesContributesFiltersNotIn,
    IncludeAttributesContributesFiltersLt,
    IncludeAttributesContributesFiltersLte,
    IncludeAttributesContributesFiltersGt,
    IncludeAttributesContributesFiltersGte,
    IncludeAttributesContributesFiltersGlob,
    IncludeAttributesContributesFiltersNotGlob,
    IncludeAttributesContributesFiltersIGlob,
    IncludeAttributesContributesFiltersNotIGlob,
    IncludeAttributesContributesFiltersRegex,
    IncludeAttributesContributesFiltersContainsAllTokens,
    IncludeAttributesContributesFiltersEq,
    IncludeAttributesContributesFiltersNotEq,
    IncludeAttributesContributesFiltersIn,
    IncludeAttributesContributesFiltersNotIn,
    IncludeAttributesContributesFiltersLt,
    IncludeAttributesContributesFiltersLte,
    IncludeAttributesContributesFiltersGt,
    IncludeAttributesContributesFiltersGte,
    IncludeAttributesContributesFiltersGlob,
    IncludeAttributesContributesFiltersNotGlob,
    IncludeAttributesContributesFiltersIGlob,
    IncludeAttributesContributesFiltersNotIGlob,
    IncludeAttributesContributesFiltersRegex,
    IncludeAttributesContributesFiltersContainsAllTokens,
    IncludeAttributesContributesFiltersEq,
    IncludeAttributesContributesFiltersNotEq,
    IncludeAttributesContributesFiltersIn,
    IncludeAttributesContributesFiltersNotIn,
    IncludeAttributesContributesFiltersLt,
    IncludeAttributesContributesFiltersLte,
    IncludeAttributesContributesFiltersGt,
    IncludeAttributesContributesFiltersGte,
    IncludeAttributesContributesFiltersGlob,
    IncludeAttributesContributesFiltersNotGlob,
    IncludeAttributesContributesFiltersIGlob,
    IncludeAttributesContributesFiltersNotIGlob,
    IncludeAttributesContributesFiltersRegex,
    IncludeAttributesContributesFiltersContainsAllTokens,
    IncludeAttributesContributesFiltersEq,
    IncludeAttributesContributesFiltersNotEq,
    IncludeAttributesContributesFiltersIn,
    IncludeAttributesContributesFiltersNotIn,
    IncludeAttributesContributesFiltersLt,
    IncludeAttributesContributesFiltersLte,
    IncludeAttributesContributesFiltersGt,
    IncludeAttributesContributesFiltersGte,
    IncludeAttributesContributesFiltersGlob,
    IncludeAttributesContributesFiltersNotGlob,
    IncludeAttributesContributesFiltersIGlob,
    IncludeAttributesContributesFiltersNotIGlob,
    IncludeAttributesContributesFiltersRegex,
    IncludeAttributesContributesFiltersContainsAllTokens,
    IncludeAttributesContributesFiltersEq,
    IncludeAttributesContributesFiltersNotEq,
    IncludeAttributesContributesFiltersIn,
    IncludeAttributesContributesFiltersNotIn,
    IncludeAttributesContributesFiltersLt,
    IncludeAttributesContributesFiltersLte,
    IncludeAttributesContributesFiltersGt,
    IncludeAttributesContributesFiltersGte,
    IncludeAttributesContributesFiltersGlob,
    IncludeAttributesContributesFiltersNotGlob,
    IncludeAttributesContributesFiltersIGlob,
    IncludeAttributesContributesFiltersNotIGlob,
    IncludeAttributesContributesFiltersRegex,
    IncludeAttributesContributesFiltersContainsAllTokens,
    IncludeAttributesContributesFiltersUnionMember139,
    IncludeAttributesContributesFiltersUnionMember140,
]


class IncludeAttributesContributes(TypedDict, total=False):
    """Include contributed repositories with cursor pagination"""

    first: Required[int]
    """Number of items to return (max: 100)"""

    after: str
    """Cursor for pagination (opaque base64-encoded)"""

    filters: IncludeAttributesContributesFilters
    """Optional filters for users.

    Supports fields like login, company, location, resolvedCountry, resolvedState,
    resolvedCity. Operators: Eq, NotEq, In, NotIn, Lt, Lte, Gt, Gte.
    """


class IncludeAttributesFollowersFiltersEq(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersNotEq(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersIn(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersNotIn(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersLt(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersLte(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersGt(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersGte(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersNotGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersIGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersNotIGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersRegex(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersContainsAllTokens(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


IncludeAttributesFollowersFiltersUnionMember139Filter: TypeAlias = Union[
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember0,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember1,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember2,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember3,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember4,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember5,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember6,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember7,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember8,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember9,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember10,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember11,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember12,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember13,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember14,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember15,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember16,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember17,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember18,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember19,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember20,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember21,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember22,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember23,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember24,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember25,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember26,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember27,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember28,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember29,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember30,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember31,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember32,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember33,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember34,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember35,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember36,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember37,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember38,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember39,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember40,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember41,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember42,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember43,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember44,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember45,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember46,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember47,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember48,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember49,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember50,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember51,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember52,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember53,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember54,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember55,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember56,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember57,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember58,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember59,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember60,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember61,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember62,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember63,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember64,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember65,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember66,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember67,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember68,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember69,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember70,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember71,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember72,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember73,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember74,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember75,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember76,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember77,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember78,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember79,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember80,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember81,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember82,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember83,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember84,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember85,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember86,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember87,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember88,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember89,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember90,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember91,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember92,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember93,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember94,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember95,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember96,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember97,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember98,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember99,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember100,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember101,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember102,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember103,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember104,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember105,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember106,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember107,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember108,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember109,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember110,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember111,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember112,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember113,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember114,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember115,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember116,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember117,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember118,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember119,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember120,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember121,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember122,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember123,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember124,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember125,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember126,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember127,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember128,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember129,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember130,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember131,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember132,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember133,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember134,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember135,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember136,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember137,
    IncludeAttributesFollowersFiltersUnionMember139FilterUnionMember138,
]


class IncludeAttributesFollowersFiltersUnionMember139(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesFollowersFiltersUnionMember139Filter]]

    op: Required[Literal["And", "Or"]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139Filter: TypeAlias = Union[
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember0,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember1,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember2,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember3,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember4,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember5,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember6,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember7,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember8,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember9,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember10,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember11,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember12,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember13,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember14,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember15,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember16,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember17,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember18,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember19,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember20,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember21,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember22,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember23,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember24,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember25,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember26,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember27,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember28,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember29,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember30,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember31,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember32,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember33,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember34,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember35,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember36,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember37,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember38,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember39,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember40,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember41,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember42,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember43,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember44,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember45,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember46,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember47,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember48,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember49,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember50,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember51,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember52,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember53,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember54,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember55,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember56,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember57,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember58,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember59,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember60,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember61,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember62,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember63,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember64,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember65,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember66,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember67,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember68,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember69,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember70,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember71,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember72,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember73,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember74,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember75,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember76,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember77,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember78,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember79,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember80,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember81,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember82,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember83,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember84,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember85,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember86,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember87,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember88,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember89,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember90,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember91,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember92,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember93,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember94,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember95,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember96,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember97,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember98,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember99,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember100,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember101,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember102,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember103,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember104,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember105,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember106,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember107,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember108,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember109,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember110,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember111,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember112,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember113,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember114,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember115,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember116,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember117,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember118,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember119,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember120,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember121,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember122,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember123,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember124,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember125,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember126,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember127,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember128,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember129,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember130,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember131,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember132,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember133,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember134,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember135,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember136,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember137,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139FilterUnionMember138,
]


class IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139Filter]]

    op: Required[Literal["And", "Or"]]


IncludeAttributesFollowersFiltersUnionMember140Filter: TypeAlias = Union[
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember0,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember1,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember2,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember3,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember4,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember5,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember6,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember7,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember8,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember9,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember10,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember11,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember12,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember13,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember14,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember15,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember16,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember17,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember18,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember19,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember20,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember21,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember22,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember23,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember24,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember25,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember26,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember27,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember28,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember29,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember30,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember31,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember32,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember33,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember34,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember35,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember36,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember37,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember38,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember39,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember40,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember41,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember42,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember43,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember44,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember45,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember46,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember47,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember48,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember49,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember50,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember51,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember52,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember53,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember54,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember55,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember56,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember57,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember58,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember59,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember60,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember61,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember62,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember63,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember64,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember65,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember66,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember67,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember68,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember69,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember70,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember71,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember72,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember73,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember74,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember75,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember76,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember77,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember78,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember79,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember80,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember81,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember82,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember83,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember84,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember85,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember86,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember87,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember88,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember89,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember90,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember91,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember92,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember93,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember94,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember95,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember96,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember97,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember98,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember99,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember100,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember101,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember102,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember103,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember104,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember105,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember106,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember107,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember108,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember109,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember110,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember111,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember112,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember113,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember114,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember115,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember116,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember117,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember118,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember119,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember120,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember121,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember122,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember123,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember124,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember125,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember126,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember127,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember128,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember129,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember130,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember131,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember132,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember133,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember134,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember135,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember136,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember137,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember138,
    IncludeAttributesFollowersFiltersUnionMember140FilterUnionMember139,
]


class IncludeAttributesFollowersFiltersUnionMember140(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesFollowersFiltersUnionMember140Filter]]

    op: Required[Literal["And", "Or"]]


IncludeAttributesFollowersFilters: TypeAlias = Union[
    IncludeAttributesFollowersFiltersEq,
    IncludeAttributesFollowersFiltersNotEq,
    IncludeAttributesFollowersFiltersIn,
    IncludeAttributesFollowersFiltersNotIn,
    IncludeAttributesFollowersFiltersLt,
    IncludeAttributesFollowersFiltersLte,
    IncludeAttributesFollowersFiltersGt,
    IncludeAttributesFollowersFiltersGte,
    IncludeAttributesFollowersFiltersGlob,
    IncludeAttributesFollowersFiltersNotGlob,
    IncludeAttributesFollowersFiltersIGlob,
    IncludeAttributesFollowersFiltersNotIGlob,
    IncludeAttributesFollowersFiltersRegex,
    IncludeAttributesFollowersFiltersEq,
    IncludeAttributesFollowersFiltersNotEq,
    IncludeAttributesFollowersFiltersIn,
    IncludeAttributesFollowersFiltersNotIn,
    IncludeAttributesFollowersFiltersLt,
    IncludeAttributesFollowersFiltersLte,
    IncludeAttributesFollowersFiltersGt,
    IncludeAttributesFollowersFiltersGte,
    IncludeAttributesFollowersFiltersGlob,
    IncludeAttributesFollowersFiltersNotGlob,
    IncludeAttributesFollowersFiltersIGlob,
    IncludeAttributesFollowersFiltersNotIGlob,
    IncludeAttributesFollowersFiltersRegex,
    IncludeAttributesFollowersFiltersContainsAllTokens,
    IncludeAttributesFollowersFiltersEq,
    IncludeAttributesFollowersFiltersNotEq,
    IncludeAttributesFollowersFiltersIn,
    IncludeAttributesFollowersFiltersNotIn,
    IncludeAttributesFollowersFiltersLt,
    IncludeAttributesFollowersFiltersLte,
    IncludeAttributesFollowersFiltersGt,
    IncludeAttributesFollowersFiltersGte,
    IncludeAttributesFollowersFiltersGlob,
    IncludeAttributesFollowersFiltersNotGlob,
    IncludeAttributesFollowersFiltersIGlob,
    IncludeAttributesFollowersFiltersNotIGlob,
    IncludeAttributesFollowersFiltersRegex,
    IncludeAttributesFollowersFiltersContainsAllTokens,
    IncludeAttributesFollowersFiltersEq,
    IncludeAttributesFollowersFiltersNotEq,
    IncludeAttributesFollowersFiltersIn,
    IncludeAttributesFollowersFiltersNotIn,
    IncludeAttributesFollowersFiltersLt,
    IncludeAttributesFollowersFiltersLte,
    IncludeAttributesFollowersFiltersGt,
    IncludeAttributesFollowersFiltersGte,
    IncludeAttributesFollowersFiltersGlob,
    IncludeAttributesFollowersFiltersNotGlob,
    IncludeAttributesFollowersFiltersIGlob,
    IncludeAttributesFollowersFiltersNotIGlob,
    IncludeAttributesFollowersFiltersRegex,
    IncludeAttributesFollowersFiltersContainsAllTokens,
    IncludeAttributesFollowersFiltersEq,
    IncludeAttributesFollowersFiltersNotEq,
    IncludeAttributesFollowersFiltersIn,
    IncludeAttributesFollowersFiltersNotIn,
    IncludeAttributesFollowersFiltersLt,
    IncludeAttributesFollowersFiltersLte,
    IncludeAttributesFollowersFiltersGt,
    IncludeAttributesFollowersFiltersGte,
    IncludeAttributesFollowersFiltersGlob,
    IncludeAttributesFollowersFiltersNotGlob,
    IncludeAttributesFollowersFiltersIGlob,
    IncludeAttributesFollowersFiltersNotIGlob,
    IncludeAttributesFollowersFiltersRegex,
    IncludeAttributesFollowersFiltersContainsAllTokens,
    IncludeAttributesFollowersFiltersEq,
    IncludeAttributesFollowersFiltersNotEq,
    IncludeAttributesFollowersFiltersIn,
    IncludeAttributesFollowersFiltersNotIn,
    IncludeAttributesFollowersFiltersLt,
    IncludeAttributesFollowersFiltersLte,
    IncludeAttributesFollowersFiltersGt,
    IncludeAttributesFollowersFiltersGte,
    IncludeAttributesFollowersFiltersGlob,
    IncludeAttributesFollowersFiltersNotGlob,
    IncludeAttributesFollowersFiltersIGlob,
    IncludeAttributesFollowersFiltersNotIGlob,
    IncludeAttributesFollowersFiltersRegex,
    IncludeAttributesFollowersFiltersContainsAllTokens,
    IncludeAttributesFollowersFiltersEq,
    IncludeAttributesFollowersFiltersNotEq,
    IncludeAttributesFollowersFiltersIn,
    IncludeAttributesFollowersFiltersNotIn,
    IncludeAttributesFollowersFiltersLt,
    IncludeAttributesFollowersFiltersLte,
    IncludeAttributesFollowersFiltersGt,
    IncludeAttributesFollowersFiltersGte,
    IncludeAttributesFollowersFiltersGlob,
    IncludeAttributesFollowersFiltersNotGlob,
    IncludeAttributesFollowersFiltersIGlob,
    IncludeAttributesFollowersFiltersNotIGlob,
    IncludeAttributesFollowersFiltersRegex,
    IncludeAttributesFollowersFiltersContainsAllTokens,
    IncludeAttributesFollowersFiltersEq,
    IncludeAttributesFollowersFiltersNotEq,
    IncludeAttributesFollowersFiltersIn,
    IncludeAttributesFollowersFiltersNotIn,
    IncludeAttributesFollowersFiltersLt,
    IncludeAttributesFollowersFiltersLte,
    IncludeAttributesFollowersFiltersGt,
    IncludeAttributesFollowersFiltersGte,
    IncludeAttributesFollowersFiltersGlob,
    IncludeAttributesFollowersFiltersNotGlob,
    IncludeAttributesFollowersFiltersIGlob,
    IncludeAttributesFollowersFiltersNotIGlob,
    IncludeAttributesFollowersFiltersRegex,
    IncludeAttributesFollowersFiltersContainsAllTokens,
    IncludeAttributesFollowersFiltersEq,
    IncludeAttributesFollowersFiltersNotEq,
    IncludeAttributesFollowersFiltersIn,
    IncludeAttributesFollowersFiltersNotIn,
    IncludeAttributesFollowersFiltersLt,
    IncludeAttributesFollowersFiltersLte,
    IncludeAttributesFollowersFiltersGt,
    IncludeAttributesFollowersFiltersGte,
    IncludeAttributesFollowersFiltersGlob,
    IncludeAttributesFollowersFiltersNotGlob,
    IncludeAttributesFollowersFiltersIGlob,
    IncludeAttributesFollowersFiltersNotIGlob,
    IncludeAttributesFollowersFiltersRegex,
    IncludeAttributesFollowersFiltersContainsAllTokens,
    IncludeAttributesFollowersFiltersEq,
    IncludeAttributesFollowersFiltersNotEq,
    IncludeAttributesFollowersFiltersIn,
    IncludeAttributesFollowersFiltersNotIn,
    IncludeAttributesFollowersFiltersLt,
    IncludeAttributesFollowersFiltersLte,
    IncludeAttributesFollowersFiltersGt,
    IncludeAttributesFollowersFiltersGte,
    IncludeAttributesFollowersFiltersGlob,
    IncludeAttributesFollowersFiltersNotGlob,
    IncludeAttributesFollowersFiltersIGlob,
    IncludeAttributesFollowersFiltersNotIGlob,
    IncludeAttributesFollowersFiltersRegex,
    IncludeAttributesFollowersFiltersContainsAllTokens,
    IncludeAttributesFollowersFiltersUnionMember139,
    IncludeAttributesFollowersFiltersUnionMember140,
]


class IncludeAttributesFollowers(TypedDict, total=False):
    """Include followers with cursor pagination"""

    first: Required[int]
    """Number of items to return (max: 100)"""

    after: str
    """Cursor for pagination (opaque base64-encoded)"""

    filters: IncludeAttributesFollowersFilters
    """Optional filters for users.

    Supports fields like login, company, location, resolvedCountry, resolvedState,
    resolvedCity. Operators: Eq, NotEq, In, NotIn, Lt, Lte, Gt, Gte.
    """


class IncludeAttributesFollowingFiltersEq(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersNotEq(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersIn(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersNotIn(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersLt(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersLte(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersGt(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersGte(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersNotGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersIGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersNotIGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersRegex(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersContainsAllTokens(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


IncludeAttributesFollowingFiltersUnionMember139Filter: TypeAlias = Union[
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember0,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember1,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember2,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember3,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember4,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember5,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember6,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember7,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember8,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember9,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember10,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember11,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember12,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember13,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember14,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember15,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember16,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember17,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember18,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember19,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember20,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember21,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember22,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember23,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember24,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember25,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember26,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember27,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember28,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember29,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember30,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember31,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember32,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember33,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember34,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember35,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember36,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember37,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember38,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember39,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember40,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember41,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember42,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember43,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember44,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember45,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember46,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember47,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember48,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember49,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember50,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember51,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember52,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember53,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember54,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember55,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember56,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember57,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember58,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember59,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember60,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember61,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember62,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember63,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember64,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember65,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember66,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember67,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember68,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember69,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember70,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember71,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember72,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember73,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember74,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember75,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember76,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember77,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember78,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember79,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember80,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember81,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember82,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember83,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember84,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember85,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember86,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember87,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember88,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember89,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember90,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember91,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember92,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember93,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember94,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember95,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember96,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember97,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember98,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember99,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember100,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember101,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember102,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember103,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember104,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember105,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember106,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember107,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember108,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember109,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember110,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember111,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember112,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember113,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember114,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember115,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember116,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember117,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember118,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember119,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember120,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember121,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember122,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember123,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember124,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember125,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember126,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember127,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember128,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember129,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember130,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember131,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember132,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember133,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember134,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember135,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember136,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember137,
    IncludeAttributesFollowingFiltersUnionMember139FilterUnionMember138,
]


class IncludeAttributesFollowingFiltersUnionMember139(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesFollowingFiltersUnionMember139Filter]]

    op: Required[Literal["And", "Or"]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139Filter: TypeAlias = Union[
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember0,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember1,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember2,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember3,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember4,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember5,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember6,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember7,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember8,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember9,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember10,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember11,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember12,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember13,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember14,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember15,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember16,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember17,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember18,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember19,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember20,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember21,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember22,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember23,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember24,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember25,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember26,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember27,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember28,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember29,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember30,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember31,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember32,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember33,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember34,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember35,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember36,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember37,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember38,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember39,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember40,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember41,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember42,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember43,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember44,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember45,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember46,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember47,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember48,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember49,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember50,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember51,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember52,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember53,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember54,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember55,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember56,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember57,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember58,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember59,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember60,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember61,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember62,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember63,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember64,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember65,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember66,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember67,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember68,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember69,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember70,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember71,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember72,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember73,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember74,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember75,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember76,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember77,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember78,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember79,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember80,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember81,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember82,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember83,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember84,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember85,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember86,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember87,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember88,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember89,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember90,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember91,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember92,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember93,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember94,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember95,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember96,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember97,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember98,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember99,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember100,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember101,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember102,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember103,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember104,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember105,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember106,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember107,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember108,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember109,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember110,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember111,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember112,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember113,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember114,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember115,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember116,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember117,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember118,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember119,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember120,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember121,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember122,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember123,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember124,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember125,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember126,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember127,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember128,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember129,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember130,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember131,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember132,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember133,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember134,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember135,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember136,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember137,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139FilterUnionMember138,
]


class IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139Filter]]

    op: Required[Literal["And", "Or"]]


IncludeAttributesFollowingFiltersUnionMember140Filter: TypeAlias = Union[
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember0,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember1,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember2,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember3,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember4,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember5,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember6,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember7,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember8,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember9,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember10,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember11,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember12,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember13,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember14,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember15,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember16,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember17,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember18,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember19,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember20,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember21,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember22,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember23,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember24,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember25,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember26,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember27,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember28,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember29,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember30,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember31,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember32,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember33,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember34,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember35,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember36,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember37,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember38,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember39,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember40,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember41,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember42,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember43,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember44,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember45,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember46,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember47,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember48,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember49,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember50,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember51,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember52,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember53,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember54,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember55,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember56,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember57,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember58,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember59,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember60,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember61,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember62,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember63,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember64,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember65,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember66,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember67,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember68,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember69,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember70,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember71,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember72,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember73,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember74,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember75,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember76,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember77,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember78,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember79,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember80,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember81,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember82,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember83,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember84,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember85,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember86,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember87,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember88,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember89,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember90,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember91,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember92,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember93,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember94,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember95,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember96,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember97,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember98,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember99,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember100,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember101,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember102,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember103,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember104,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember105,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember106,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember107,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember108,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember109,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember110,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember111,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember112,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember113,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember114,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember115,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember116,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember117,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember118,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember119,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember120,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember121,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember122,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember123,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember124,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember125,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember126,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember127,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember128,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember129,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember130,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember131,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember132,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember133,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember134,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember135,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember136,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember137,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember138,
    IncludeAttributesFollowingFiltersUnionMember140FilterUnionMember139,
]


class IncludeAttributesFollowingFiltersUnionMember140(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesFollowingFiltersUnionMember140Filter]]

    op: Required[Literal["And", "Or"]]


IncludeAttributesFollowingFilters: TypeAlias = Union[
    IncludeAttributesFollowingFiltersEq,
    IncludeAttributesFollowingFiltersNotEq,
    IncludeAttributesFollowingFiltersIn,
    IncludeAttributesFollowingFiltersNotIn,
    IncludeAttributesFollowingFiltersLt,
    IncludeAttributesFollowingFiltersLte,
    IncludeAttributesFollowingFiltersGt,
    IncludeAttributesFollowingFiltersGte,
    IncludeAttributesFollowingFiltersGlob,
    IncludeAttributesFollowingFiltersNotGlob,
    IncludeAttributesFollowingFiltersIGlob,
    IncludeAttributesFollowingFiltersNotIGlob,
    IncludeAttributesFollowingFiltersRegex,
    IncludeAttributesFollowingFiltersEq,
    IncludeAttributesFollowingFiltersNotEq,
    IncludeAttributesFollowingFiltersIn,
    IncludeAttributesFollowingFiltersNotIn,
    IncludeAttributesFollowingFiltersLt,
    IncludeAttributesFollowingFiltersLte,
    IncludeAttributesFollowingFiltersGt,
    IncludeAttributesFollowingFiltersGte,
    IncludeAttributesFollowingFiltersGlob,
    IncludeAttributesFollowingFiltersNotGlob,
    IncludeAttributesFollowingFiltersIGlob,
    IncludeAttributesFollowingFiltersNotIGlob,
    IncludeAttributesFollowingFiltersRegex,
    IncludeAttributesFollowingFiltersContainsAllTokens,
    IncludeAttributesFollowingFiltersEq,
    IncludeAttributesFollowingFiltersNotEq,
    IncludeAttributesFollowingFiltersIn,
    IncludeAttributesFollowingFiltersNotIn,
    IncludeAttributesFollowingFiltersLt,
    IncludeAttributesFollowingFiltersLte,
    IncludeAttributesFollowingFiltersGt,
    IncludeAttributesFollowingFiltersGte,
    IncludeAttributesFollowingFiltersGlob,
    IncludeAttributesFollowingFiltersNotGlob,
    IncludeAttributesFollowingFiltersIGlob,
    IncludeAttributesFollowingFiltersNotIGlob,
    IncludeAttributesFollowingFiltersRegex,
    IncludeAttributesFollowingFiltersContainsAllTokens,
    IncludeAttributesFollowingFiltersEq,
    IncludeAttributesFollowingFiltersNotEq,
    IncludeAttributesFollowingFiltersIn,
    IncludeAttributesFollowingFiltersNotIn,
    IncludeAttributesFollowingFiltersLt,
    IncludeAttributesFollowingFiltersLte,
    IncludeAttributesFollowingFiltersGt,
    IncludeAttributesFollowingFiltersGte,
    IncludeAttributesFollowingFiltersGlob,
    IncludeAttributesFollowingFiltersNotGlob,
    IncludeAttributesFollowingFiltersIGlob,
    IncludeAttributesFollowingFiltersNotIGlob,
    IncludeAttributesFollowingFiltersRegex,
    IncludeAttributesFollowingFiltersContainsAllTokens,
    IncludeAttributesFollowingFiltersEq,
    IncludeAttributesFollowingFiltersNotEq,
    IncludeAttributesFollowingFiltersIn,
    IncludeAttributesFollowingFiltersNotIn,
    IncludeAttributesFollowingFiltersLt,
    IncludeAttributesFollowingFiltersLte,
    IncludeAttributesFollowingFiltersGt,
    IncludeAttributesFollowingFiltersGte,
    IncludeAttributesFollowingFiltersGlob,
    IncludeAttributesFollowingFiltersNotGlob,
    IncludeAttributesFollowingFiltersIGlob,
    IncludeAttributesFollowingFiltersNotIGlob,
    IncludeAttributesFollowingFiltersRegex,
    IncludeAttributesFollowingFiltersContainsAllTokens,
    IncludeAttributesFollowingFiltersEq,
    IncludeAttributesFollowingFiltersNotEq,
    IncludeAttributesFollowingFiltersIn,
    IncludeAttributesFollowingFiltersNotIn,
    IncludeAttributesFollowingFiltersLt,
    IncludeAttributesFollowingFiltersLte,
    IncludeAttributesFollowingFiltersGt,
    IncludeAttributesFollowingFiltersGte,
    IncludeAttributesFollowingFiltersGlob,
    IncludeAttributesFollowingFiltersNotGlob,
    IncludeAttributesFollowingFiltersIGlob,
    IncludeAttributesFollowingFiltersNotIGlob,
    IncludeAttributesFollowingFiltersRegex,
    IncludeAttributesFollowingFiltersContainsAllTokens,
    IncludeAttributesFollowingFiltersEq,
    IncludeAttributesFollowingFiltersNotEq,
    IncludeAttributesFollowingFiltersIn,
    IncludeAttributesFollowingFiltersNotIn,
    IncludeAttributesFollowingFiltersLt,
    IncludeAttributesFollowingFiltersLte,
    IncludeAttributesFollowingFiltersGt,
    IncludeAttributesFollowingFiltersGte,
    IncludeAttributesFollowingFiltersGlob,
    IncludeAttributesFollowingFiltersNotGlob,
    IncludeAttributesFollowingFiltersIGlob,
    IncludeAttributesFollowingFiltersNotIGlob,
    IncludeAttributesFollowingFiltersRegex,
    IncludeAttributesFollowingFiltersContainsAllTokens,
    IncludeAttributesFollowingFiltersEq,
    IncludeAttributesFollowingFiltersNotEq,
    IncludeAttributesFollowingFiltersIn,
    IncludeAttributesFollowingFiltersNotIn,
    IncludeAttributesFollowingFiltersLt,
    IncludeAttributesFollowingFiltersLte,
    IncludeAttributesFollowingFiltersGt,
    IncludeAttributesFollowingFiltersGte,
    IncludeAttributesFollowingFiltersGlob,
    IncludeAttributesFollowingFiltersNotGlob,
    IncludeAttributesFollowingFiltersIGlob,
    IncludeAttributesFollowingFiltersNotIGlob,
    IncludeAttributesFollowingFiltersRegex,
    IncludeAttributesFollowingFiltersContainsAllTokens,
    IncludeAttributesFollowingFiltersEq,
    IncludeAttributesFollowingFiltersNotEq,
    IncludeAttributesFollowingFiltersIn,
    IncludeAttributesFollowingFiltersNotIn,
    IncludeAttributesFollowingFiltersLt,
    IncludeAttributesFollowingFiltersLte,
    IncludeAttributesFollowingFiltersGt,
    IncludeAttributesFollowingFiltersGte,
    IncludeAttributesFollowingFiltersGlob,
    IncludeAttributesFollowingFiltersNotGlob,
    IncludeAttributesFollowingFiltersIGlob,
    IncludeAttributesFollowingFiltersNotIGlob,
    IncludeAttributesFollowingFiltersRegex,
    IncludeAttributesFollowingFiltersContainsAllTokens,
    IncludeAttributesFollowingFiltersEq,
    IncludeAttributesFollowingFiltersNotEq,
    IncludeAttributesFollowingFiltersIn,
    IncludeAttributesFollowingFiltersNotIn,
    IncludeAttributesFollowingFiltersLt,
    IncludeAttributesFollowingFiltersLte,
    IncludeAttributesFollowingFiltersGt,
    IncludeAttributesFollowingFiltersGte,
    IncludeAttributesFollowingFiltersGlob,
    IncludeAttributesFollowingFiltersNotGlob,
    IncludeAttributesFollowingFiltersIGlob,
    IncludeAttributesFollowingFiltersNotIGlob,
    IncludeAttributesFollowingFiltersRegex,
    IncludeAttributesFollowingFiltersContainsAllTokens,
    IncludeAttributesFollowingFiltersUnionMember139,
    IncludeAttributesFollowingFiltersUnionMember140,
]


class IncludeAttributesFollowing(TypedDict, total=False):
    """Include users this user follows with cursor pagination"""

    first: Required[int]
    """Number of items to return (max: 100)"""

    after: str
    """Cursor for pagination (opaque base64-encoded)"""

    filters: IncludeAttributesFollowingFilters
    """Optional filters for users.

    Supports fields like login, company, location, resolvedCountry, resolvedState,
    resolvedCity. Operators: Eq, NotEq, In, NotIn, Lt, Lte, Gt, Gte.
    """


class IncludeAttributesOwnsFiltersEq(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersNotEq(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersIn(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersNotIn(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersLt(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersLte(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersGt(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersGte(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersNotGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersIGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersNotIGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersRegex(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersContainsAllTokens(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


IncludeAttributesOwnsFiltersUnionMember139Filter: TypeAlias = Union[
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember0,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember1,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember2,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember3,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember4,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember5,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember6,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember7,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember8,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember9,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember10,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember11,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember12,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember13,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember14,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember15,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember16,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember17,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember18,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember19,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember20,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember21,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember22,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember23,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember24,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember25,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember26,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember27,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember28,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember29,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember30,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember31,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember32,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember33,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember34,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember35,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember36,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember37,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember38,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember39,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember40,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember41,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember42,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember43,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember44,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember45,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember46,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember47,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember48,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember49,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember50,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember51,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember52,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember53,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember54,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember55,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember56,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember57,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember58,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember59,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember60,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember61,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember62,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember63,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember64,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember65,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember66,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember67,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember68,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember69,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember70,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember71,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember72,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember73,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember74,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember75,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember76,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember77,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember78,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember79,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember80,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember81,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember82,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember83,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember84,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember85,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember86,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember87,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember88,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember89,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember90,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember91,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember92,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember93,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember94,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember95,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember96,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember97,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember98,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember99,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember100,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember101,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember102,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember103,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember104,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember105,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember106,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember107,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember108,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember109,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember110,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember111,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember112,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember113,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember114,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember115,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember116,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember117,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember118,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember119,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember120,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember121,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember122,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember123,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember124,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember125,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember126,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember127,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember128,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember129,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember130,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember131,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember132,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember133,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember134,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember135,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember136,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember137,
    IncludeAttributesOwnsFiltersUnionMember139FilterUnionMember138,
]


class IncludeAttributesOwnsFiltersUnionMember139(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesOwnsFiltersUnionMember139Filter]]

    op: Required[Literal["And", "Or"]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139Filter: TypeAlias = Union[
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember0,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember1,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember2,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember3,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember4,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember5,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember6,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember7,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember8,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember9,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember10,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember11,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember12,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember13,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember14,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember15,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember16,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember17,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember18,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember19,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember20,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember21,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember22,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember23,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember24,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember25,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember26,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember27,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember28,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember29,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember30,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember31,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember32,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember33,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember34,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember35,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember36,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember37,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember38,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember39,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember40,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember41,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember42,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember43,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember44,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember45,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember46,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember47,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember48,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember49,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember50,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember51,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember52,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember53,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember54,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember55,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember56,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember57,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember58,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember59,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember60,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember61,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember62,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember63,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember64,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember65,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember66,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember67,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember68,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember69,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember70,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember71,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember72,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember73,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember74,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember75,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember76,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember77,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember78,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember79,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember80,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember81,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember82,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember83,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember84,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember85,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember86,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember87,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember88,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember89,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember90,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember91,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember92,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember93,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember94,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember95,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember96,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember97,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember98,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember99,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember100,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember101,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember102,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember103,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember104,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember105,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember106,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember107,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember108,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember109,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember110,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember111,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember112,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember113,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember114,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember115,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember116,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember117,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember118,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember119,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember120,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember121,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember122,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember123,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember124,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember125,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember126,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember127,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember128,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember129,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember130,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember131,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember132,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember133,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember134,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember135,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember136,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember137,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139FilterUnionMember138,
]


class IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139Filter]]

    op: Required[Literal["And", "Or"]]


IncludeAttributesOwnsFiltersUnionMember140Filter: TypeAlias = Union[
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember0,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember1,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember2,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember3,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember4,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember5,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember6,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember7,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember8,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember9,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember10,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember11,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember12,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember13,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember14,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember15,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember16,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember17,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember18,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember19,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember20,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember21,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember22,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember23,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember24,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember25,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember26,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember27,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember28,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember29,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember30,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember31,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember32,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember33,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember34,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember35,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember36,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember37,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember38,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember39,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember40,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember41,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember42,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember43,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember44,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember45,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember46,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember47,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember48,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember49,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember50,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember51,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember52,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember53,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember54,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember55,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember56,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember57,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember58,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember59,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember60,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember61,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember62,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember63,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember64,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember65,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember66,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember67,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember68,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember69,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember70,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember71,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember72,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember73,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember74,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember75,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember76,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember77,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember78,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember79,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember80,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember81,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember82,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember83,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember84,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember85,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember86,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember87,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember88,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember89,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember90,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember91,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember92,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember93,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember94,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember95,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember96,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember97,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember98,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember99,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember100,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember101,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember102,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember103,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember104,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember105,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember106,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember107,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember108,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember109,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember110,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember111,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember112,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember113,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember114,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember115,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember116,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember117,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember118,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember119,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember120,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember121,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember122,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember123,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember124,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember125,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember126,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember127,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember128,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember129,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember130,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember131,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember132,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember133,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember134,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember135,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember136,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember137,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember138,
    IncludeAttributesOwnsFiltersUnionMember140FilterUnionMember139,
]


class IncludeAttributesOwnsFiltersUnionMember140(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesOwnsFiltersUnionMember140Filter]]

    op: Required[Literal["And", "Or"]]


IncludeAttributesOwnsFilters: TypeAlias = Union[
    IncludeAttributesOwnsFiltersEq,
    IncludeAttributesOwnsFiltersNotEq,
    IncludeAttributesOwnsFiltersIn,
    IncludeAttributesOwnsFiltersNotIn,
    IncludeAttributesOwnsFiltersLt,
    IncludeAttributesOwnsFiltersLte,
    IncludeAttributesOwnsFiltersGt,
    IncludeAttributesOwnsFiltersGte,
    IncludeAttributesOwnsFiltersGlob,
    IncludeAttributesOwnsFiltersNotGlob,
    IncludeAttributesOwnsFiltersIGlob,
    IncludeAttributesOwnsFiltersNotIGlob,
    IncludeAttributesOwnsFiltersRegex,
    IncludeAttributesOwnsFiltersEq,
    IncludeAttributesOwnsFiltersNotEq,
    IncludeAttributesOwnsFiltersIn,
    IncludeAttributesOwnsFiltersNotIn,
    IncludeAttributesOwnsFiltersLt,
    IncludeAttributesOwnsFiltersLte,
    IncludeAttributesOwnsFiltersGt,
    IncludeAttributesOwnsFiltersGte,
    IncludeAttributesOwnsFiltersGlob,
    IncludeAttributesOwnsFiltersNotGlob,
    IncludeAttributesOwnsFiltersIGlob,
    IncludeAttributesOwnsFiltersNotIGlob,
    IncludeAttributesOwnsFiltersRegex,
    IncludeAttributesOwnsFiltersContainsAllTokens,
    IncludeAttributesOwnsFiltersEq,
    IncludeAttributesOwnsFiltersNotEq,
    IncludeAttributesOwnsFiltersIn,
    IncludeAttributesOwnsFiltersNotIn,
    IncludeAttributesOwnsFiltersLt,
    IncludeAttributesOwnsFiltersLte,
    IncludeAttributesOwnsFiltersGt,
    IncludeAttributesOwnsFiltersGte,
    IncludeAttributesOwnsFiltersGlob,
    IncludeAttributesOwnsFiltersNotGlob,
    IncludeAttributesOwnsFiltersIGlob,
    IncludeAttributesOwnsFiltersNotIGlob,
    IncludeAttributesOwnsFiltersRegex,
    IncludeAttributesOwnsFiltersContainsAllTokens,
    IncludeAttributesOwnsFiltersEq,
    IncludeAttributesOwnsFiltersNotEq,
    IncludeAttributesOwnsFiltersIn,
    IncludeAttributesOwnsFiltersNotIn,
    IncludeAttributesOwnsFiltersLt,
    IncludeAttributesOwnsFiltersLte,
    IncludeAttributesOwnsFiltersGt,
    IncludeAttributesOwnsFiltersGte,
    IncludeAttributesOwnsFiltersGlob,
    IncludeAttributesOwnsFiltersNotGlob,
    IncludeAttributesOwnsFiltersIGlob,
    IncludeAttributesOwnsFiltersNotIGlob,
    IncludeAttributesOwnsFiltersRegex,
    IncludeAttributesOwnsFiltersContainsAllTokens,
    IncludeAttributesOwnsFiltersEq,
    IncludeAttributesOwnsFiltersNotEq,
    IncludeAttributesOwnsFiltersIn,
    IncludeAttributesOwnsFiltersNotIn,
    IncludeAttributesOwnsFiltersLt,
    IncludeAttributesOwnsFiltersLte,
    IncludeAttributesOwnsFiltersGt,
    IncludeAttributesOwnsFiltersGte,
    IncludeAttributesOwnsFiltersGlob,
    IncludeAttributesOwnsFiltersNotGlob,
    IncludeAttributesOwnsFiltersIGlob,
    IncludeAttributesOwnsFiltersNotIGlob,
    IncludeAttributesOwnsFiltersRegex,
    IncludeAttributesOwnsFiltersContainsAllTokens,
    IncludeAttributesOwnsFiltersEq,
    IncludeAttributesOwnsFiltersNotEq,
    IncludeAttributesOwnsFiltersIn,
    IncludeAttributesOwnsFiltersNotIn,
    IncludeAttributesOwnsFiltersLt,
    IncludeAttributesOwnsFiltersLte,
    IncludeAttributesOwnsFiltersGt,
    IncludeAttributesOwnsFiltersGte,
    IncludeAttributesOwnsFiltersGlob,
    IncludeAttributesOwnsFiltersNotGlob,
    IncludeAttributesOwnsFiltersIGlob,
    IncludeAttributesOwnsFiltersNotIGlob,
    IncludeAttributesOwnsFiltersRegex,
    IncludeAttributesOwnsFiltersContainsAllTokens,
    IncludeAttributesOwnsFiltersEq,
    IncludeAttributesOwnsFiltersNotEq,
    IncludeAttributesOwnsFiltersIn,
    IncludeAttributesOwnsFiltersNotIn,
    IncludeAttributesOwnsFiltersLt,
    IncludeAttributesOwnsFiltersLte,
    IncludeAttributesOwnsFiltersGt,
    IncludeAttributesOwnsFiltersGte,
    IncludeAttributesOwnsFiltersGlob,
    IncludeAttributesOwnsFiltersNotGlob,
    IncludeAttributesOwnsFiltersIGlob,
    IncludeAttributesOwnsFiltersNotIGlob,
    IncludeAttributesOwnsFiltersRegex,
    IncludeAttributesOwnsFiltersContainsAllTokens,
    IncludeAttributesOwnsFiltersEq,
    IncludeAttributesOwnsFiltersNotEq,
    IncludeAttributesOwnsFiltersIn,
    IncludeAttributesOwnsFiltersNotIn,
    IncludeAttributesOwnsFiltersLt,
    IncludeAttributesOwnsFiltersLte,
    IncludeAttributesOwnsFiltersGt,
    IncludeAttributesOwnsFiltersGte,
    IncludeAttributesOwnsFiltersGlob,
    IncludeAttributesOwnsFiltersNotGlob,
    IncludeAttributesOwnsFiltersIGlob,
    IncludeAttributesOwnsFiltersNotIGlob,
    IncludeAttributesOwnsFiltersRegex,
    IncludeAttributesOwnsFiltersContainsAllTokens,
    IncludeAttributesOwnsFiltersEq,
    IncludeAttributesOwnsFiltersNotEq,
    IncludeAttributesOwnsFiltersIn,
    IncludeAttributesOwnsFiltersNotIn,
    IncludeAttributesOwnsFiltersLt,
    IncludeAttributesOwnsFiltersLte,
    IncludeAttributesOwnsFiltersGt,
    IncludeAttributesOwnsFiltersGte,
    IncludeAttributesOwnsFiltersGlob,
    IncludeAttributesOwnsFiltersNotGlob,
    IncludeAttributesOwnsFiltersIGlob,
    IncludeAttributesOwnsFiltersNotIGlob,
    IncludeAttributesOwnsFiltersRegex,
    IncludeAttributesOwnsFiltersContainsAllTokens,
    IncludeAttributesOwnsFiltersEq,
    IncludeAttributesOwnsFiltersNotEq,
    IncludeAttributesOwnsFiltersIn,
    IncludeAttributesOwnsFiltersNotIn,
    IncludeAttributesOwnsFiltersLt,
    IncludeAttributesOwnsFiltersLte,
    IncludeAttributesOwnsFiltersGt,
    IncludeAttributesOwnsFiltersGte,
    IncludeAttributesOwnsFiltersGlob,
    IncludeAttributesOwnsFiltersNotGlob,
    IncludeAttributesOwnsFiltersIGlob,
    IncludeAttributesOwnsFiltersNotIGlob,
    IncludeAttributesOwnsFiltersRegex,
    IncludeAttributesOwnsFiltersContainsAllTokens,
    IncludeAttributesOwnsFiltersUnionMember139,
    IncludeAttributesOwnsFiltersUnionMember140,
]


class IncludeAttributesOwns(TypedDict, total=False):
    """Include owned repositories with cursor pagination"""

    first: Required[int]
    """Number of items to return (max: 100)"""

    after: str
    """Cursor for pagination (opaque base64-encoded)"""

    filters: IncludeAttributesOwnsFilters
    """Optional filters for users.

    Supports fields like login, company, location, resolvedCountry, resolvedState,
    resolvedCity. Operators: Eq, NotEq, In, NotIn, Lt, Lte, Gt, Gte.
    """


class IncludeAttributesStarsFiltersEq(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersNotEq(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersIn(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersNotIn(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersLt(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersLte(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersGt(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersGte(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersNotGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersIGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersNotIGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersRegex(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersContainsAllTokens(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember139FilterUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


IncludeAttributesStarsFiltersUnionMember139Filter: TypeAlias = Union[
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember0,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember1,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember2,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember3,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember4,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember5,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember6,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember7,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember8,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember9,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember10,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember11,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember12,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember13,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember14,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember15,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember16,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember17,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember18,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember19,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember20,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember21,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember22,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember23,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember24,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember25,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember26,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember27,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember28,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember29,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember30,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember31,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember32,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember33,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember34,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember35,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember36,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember37,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember38,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember39,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember40,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember41,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember42,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember43,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember44,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember45,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember46,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember47,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember48,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember49,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember50,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember51,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember52,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember53,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember54,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember55,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember56,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember57,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember58,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember59,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember60,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember61,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember62,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember63,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember64,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember65,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember66,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember67,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember68,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember69,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember70,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember71,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember72,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember73,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember74,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember75,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember76,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember77,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember78,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember79,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember80,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember81,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember82,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember83,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember84,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember85,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember86,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember87,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember88,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember89,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember90,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember91,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember92,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember93,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember94,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember95,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember96,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember97,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember98,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember99,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember100,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember101,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember102,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember103,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember104,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember105,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember106,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember107,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember108,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember109,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember110,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember111,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember112,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember113,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember114,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember115,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember116,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember117,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember118,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember119,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember120,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember121,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember122,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember123,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember124,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember125,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember126,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember127,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember128,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember129,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember130,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember131,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember132,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember133,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember134,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember135,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember136,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember137,
    IncludeAttributesStarsFiltersUnionMember139FilterUnionMember138,
]


class IncludeAttributesStarsFiltersUnionMember139(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesStarsFiltersUnionMember139Filter]]

    op: Required[Literal["And", "Or"]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139Filter: TypeAlias = Union[
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember0,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember1,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember2,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember3,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember4,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember5,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember6,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember7,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember8,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember9,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember10,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember11,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember12,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember13,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember14,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember15,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember16,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember17,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember18,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember19,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember20,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember21,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember22,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember23,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember24,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember25,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember26,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember27,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember28,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember29,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember30,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember31,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember32,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember33,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember34,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember35,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember36,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember37,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember38,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember39,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember40,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember41,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember42,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember43,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember44,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember45,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember46,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember47,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember48,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember49,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember50,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember51,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember52,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember53,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember54,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember55,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember56,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember57,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember58,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember59,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember60,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember61,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember62,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember63,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember64,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember65,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember66,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember67,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember68,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember69,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember70,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember71,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember72,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember73,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember74,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember75,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember76,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember77,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember78,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember79,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember80,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember81,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember82,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember83,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember84,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember85,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember86,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember87,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember88,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember89,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember90,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember91,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember92,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember93,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember94,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember95,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember96,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember97,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember98,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember99,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember100,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember101,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember102,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember103,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember104,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember105,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember106,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember107,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember108,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember109,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember110,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember111,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember112,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember113,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember114,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember115,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember116,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember117,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember118,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember119,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember120,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember121,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember122,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember123,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember124,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember125,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember126,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember127,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember128,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember129,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember130,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember131,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember132,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember133,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember134,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember135,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember136,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember137,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139FilterUnionMember138,
]


class IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139Filter]]

    op: Required[Literal["And", "Or"]]


IncludeAttributesStarsFiltersUnionMember140Filter: TypeAlias = Union[
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember0,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember1,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember2,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember3,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember4,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember5,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember6,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember7,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember8,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember9,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember10,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember11,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember12,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember13,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember14,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember15,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember16,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember17,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember18,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember19,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember20,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember21,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember22,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember23,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember24,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember25,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember26,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember27,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember28,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember29,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember30,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember31,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember32,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember33,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember34,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember35,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember36,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember37,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember38,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember39,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember40,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember41,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember42,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember43,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember44,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember45,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember46,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember47,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember48,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember49,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember50,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember51,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember52,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember53,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember54,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember55,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember56,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember57,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember58,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember59,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember60,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember61,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember62,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember63,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember64,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember65,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember66,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember67,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember68,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember69,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember70,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember71,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember72,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember73,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember74,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember75,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember76,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember77,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember78,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember79,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember80,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember81,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember82,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember83,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember84,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember85,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember86,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember87,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember88,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember89,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember90,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember91,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember92,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember93,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember94,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember95,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember96,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember97,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember98,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember99,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember100,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember101,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember102,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember103,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember104,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember105,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember106,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember107,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember108,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember109,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember110,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember111,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember112,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember113,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember114,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember115,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember116,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember117,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember118,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember119,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember120,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember121,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember122,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember123,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember124,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember125,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember126,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember127,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember128,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember129,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember130,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember131,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember132,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember133,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember134,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember135,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember136,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember137,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember138,
    IncludeAttributesStarsFiltersUnionMember140FilterUnionMember139,
]


class IncludeAttributesStarsFiltersUnionMember140(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesStarsFiltersUnionMember140Filter]]

    op: Required[Literal["And", "Or"]]


IncludeAttributesStarsFilters: TypeAlias = Union[
    IncludeAttributesStarsFiltersEq,
    IncludeAttributesStarsFiltersNotEq,
    IncludeAttributesStarsFiltersIn,
    IncludeAttributesStarsFiltersNotIn,
    IncludeAttributesStarsFiltersLt,
    IncludeAttributesStarsFiltersLte,
    IncludeAttributesStarsFiltersGt,
    IncludeAttributesStarsFiltersGte,
    IncludeAttributesStarsFiltersGlob,
    IncludeAttributesStarsFiltersNotGlob,
    IncludeAttributesStarsFiltersIGlob,
    IncludeAttributesStarsFiltersNotIGlob,
    IncludeAttributesStarsFiltersRegex,
    IncludeAttributesStarsFiltersEq,
    IncludeAttributesStarsFiltersNotEq,
    IncludeAttributesStarsFiltersIn,
    IncludeAttributesStarsFiltersNotIn,
    IncludeAttributesStarsFiltersLt,
    IncludeAttributesStarsFiltersLte,
    IncludeAttributesStarsFiltersGt,
    IncludeAttributesStarsFiltersGte,
    IncludeAttributesStarsFiltersGlob,
    IncludeAttributesStarsFiltersNotGlob,
    IncludeAttributesStarsFiltersIGlob,
    IncludeAttributesStarsFiltersNotIGlob,
    IncludeAttributesStarsFiltersRegex,
    IncludeAttributesStarsFiltersContainsAllTokens,
    IncludeAttributesStarsFiltersEq,
    IncludeAttributesStarsFiltersNotEq,
    IncludeAttributesStarsFiltersIn,
    IncludeAttributesStarsFiltersNotIn,
    IncludeAttributesStarsFiltersLt,
    IncludeAttributesStarsFiltersLte,
    IncludeAttributesStarsFiltersGt,
    IncludeAttributesStarsFiltersGte,
    IncludeAttributesStarsFiltersGlob,
    IncludeAttributesStarsFiltersNotGlob,
    IncludeAttributesStarsFiltersIGlob,
    IncludeAttributesStarsFiltersNotIGlob,
    IncludeAttributesStarsFiltersRegex,
    IncludeAttributesStarsFiltersContainsAllTokens,
    IncludeAttributesStarsFiltersEq,
    IncludeAttributesStarsFiltersNotEq,
    IncludeAttributesStarsFiltersIn,
    IncludeAttributesStarsFiltersNotIn,
    IncludeAttributesStarsFiltersLt,
    IncludeAttributesStarsFiltersLte,
    IncludeAttributesStarsFiltersGt,
    IncludeAttributesStarsFiltersGte,
    IncludeAttributesStarsFiltersGlob,
    IncludeAttributesStarsFiltersNotGlob,
    IncludeAttributesStarsFiltersIGlob,
    IncludeAttributesStarsFiltersNotIGlob,
    IncludeAttributesStarsFiltersRegex,
    IncludeAttributesStarsFiltersContainsAllTokens,
    IncludeAttributesStarsFiltersEq,
    IncludeAttributesStarsFiltersNotEq,
    IncludeAttributesStarsFiltersIn,
    IncludeAttributesStarsFiltersNotIn,
    IncludeAttributesStarsFiltersLt,
    IncludeAttributesStarsFiltersLte,
    IncludeAttributesStarsFiltersGt,
    IncludeAttributesStarsFiltersGte,
    IncludeAttributesStarsFiltersGlob,
    IncludeAttributesStarsFiltersNotGlob,
    IncludeAttributesStarsFiltersIGlob,
    IncludeAttributesStarsFiltersNotIGlob,
    IncludeAttributesStarsFiltersRegex,
    IncludeAttributesStarsFiltersContainsAllTokens,
    IncludeAttributesStarsFiltersEq,
    IncludeAttributesStarsFiltersNotEq,
    IncludeAttributesStarsFiltersIn,
    IncludeAttributesStarsFiltersNotIn,
    IncludeAttributesStarsFiltersLt,
    IncludeAttributesStarsFiltersLte,
    IncludeAttributesStarsFiltersGt,
    IncludeAttributesStarsFiltersGte,
    IncludeAttributesStarsFiltersGlob,
    IncludeAttributesStarsFiltersNotGlob,
    IncludeAttributesStarsFiltersIGlob,
    IncludeAttributesStarsFiltersNotIGlob,
    IncludeAttributesStarsFiltersRegex,
    IncludeAttributesStarsFiltersContainsAllTokens,
    IncludeAttributesStarsFiltersEq,
    IncludeAttributesStarsFiltersNotEq,
    IncludeAttributesStarsFiltersIn,
    IncludeAttributesStarsFiltersNotIn,
    IncludeAttributesStarsFiltersLt,
    IncludeAttributesStarsFiltersLte,
    IncludeAttributesStarsFiltersGt,
    IncludeAttributesStarsFiltersGte,
    IncludeAttributesStarsFiltersGlob,
    IncludeAttributesStarsFiltersNotGlob,
    IncludeAttributesStarsFiltersIGlob,
    IncludeAttributesStarsFiltersNotIGlob,
    IncludeAttributesStarsFiltersRegex,
    IncludeAttributesStarsFiltersContainsAllTokens,
    IncludeAttributesStarsFiltersEq,
    IncludeAttributesStarsFiltersNotEq,
    IncludeAttributesStarsFiltersIn,
    IncludeAttributesStarsFiltersNotIn,
    IncludeAttributesStarsFiltersLt,
    IncludeAttributesStarsFiltersLte,
    IncludeAttributesStarsFiltersGt,
    IncludeAttributesStarsFiltersGte,
    IncludeAttributesStarsFiltersGlob,
    IncludeAttributesStarsFiltersNotGlob,
    IncludeAttributesStarsFiltersIGlob,
    IncludeAttributesStarsFiltersNotIGlob,
    IncludeAttributesStarsFiltersRegex,
    IncludeAttributesStarsFiltersContainsAllTokens,
    IncludeAttributesStarsFiltersEq,
    IncludeAttributesStarsFiltersNotEq,
    IncludeAttributesStarsFiltersIn,
    IncludeAttributesStarsFiltersNotIn,
    IncludeAttributesStarsFiltersLt,
    IncludeAttributesStarsFiltersLte,
    IncludeAttributesStarsFiltersGt,
    IncludeAttributesStarsFiltersGte,
    IncludeAttributesStarsFiltersGlob,
    IncludeAttributesStarsFiltersNotGlob,
    IncludeAttributesStarsFiltersIGlob,
    IncludeAttributesStarsFiltersNotIGlob,
    IncludeAttributesStarsFiltersRegex,
    IncludeAttributesStarsFiltersContainsAllTokens,
    IncludeAttributesStarsFiltersEq,
    IncludeAttributesStarsFiltersNotEq,
    IncludeAttributesStarsFiltersIn,
    IncludeAttributesStarsFiltersNotIn,
    IncludeAttributesStarsFiltersLt,
    IncludeAttributesStarsFiltersLte,
    IncludeAttributesStarsFiltersGt,
    IncludeAttributesStarsFiltersGte,
    IncludeAttributesStarsFiltersGlob,
    IncludeAttributesStarsFiltersNotGlob,
    IncludeAttributesStarsFiltersIGlob,
    IncludeAttributesStarsFiltersNotIGlob,
    IncludeAttributesStarsFiltersRegex,
    IncludeAttributesStarsFiltersContainsAllTokens,
    IncludeAttributesStarsFiltersUnionMember139,
    IncludeAttributesStarsFiltersUnionMember140,
]


class IncludeAttributesStars(TypedDict, total=False):
    """Include starred repositories with cursor pagination"""

    first: Required[int]
    """Number of items to return (max: 100)"""

    after: str
    """Cursor for pagination (opaque base64-encoded)"""

    filters: IncludeAttributesStarsFilters
    """Optional filters for users.

    Supports fields like login, company, location, resolvedCountry, resolvedState,
    resolvedCity. Operators: Eq, NotEq, In, NotIn, Lt, Lte, Gt, Gte.
    """


class IncludeAttributes(TypedDict, total=False):
    """
    Optional graph relationships to include (followers, following, stars, owns, contributes)
    """

    contributes: IncludeAttributesContributes
    """Include contributed repositories with cursor pagination"""

    devrank: bool
    """Include devrank data for the user"""

    followers: IncludeAttributesFollowers
    """Include followers with cursor pagination"""

    following: IncludeAttributesFollowing
    """Include users this user follows with cursor pagination"""

    owns: IncludeAttributesOwns
    """Include owned repositories with cursor pagination"""

    stars: IncludeAttributesStars
    """Include starred repositories with cursor pagination"""
