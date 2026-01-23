# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "RawRepoRetrieveParams",
    "IncludeAttributes",
    "IncludeAttributesContributors",
    "IncludeAttributesContributorsFilters",
    "IncludeAttributesContributorsFiltersEq",
    "IncludeAttributesContributorsFiltersNotEq",
    "IncludeAttributesContributorsFiltersIn",
    "IncludeAttributesContributorsFiltersNotIn",
    "IncludeAttributesContributorsFiltersLt",
    "IncludeAttributesContributorsFiltersLte",
    "IncludeAttributesContributorsFiltersGt",
    "IncludeAttributesContributorsFiltersGte",
    "IncludeAttributesContributorsFiltersGlob",
    "IncludeAttributesContributorsFiltersNotGlob",
    "IncludeAttributesContributorsFiltersIGlob",
    "IncludeAttributesContributorsFiltersNotIGlob",
    "IncludeAttributesContributorsFiltersRegex",
    "IncludeAttributesContributorsFiltersContainsAllTokens",
    "IncludeAttributesContributorsFiltersUnionMember139",
    "IncludeAttributesContributorsFiltersUnionMember139Filter",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember0",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember1",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember2",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember3",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember4",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember5",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember6",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember7",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember8",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember9",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember10",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember11",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember12",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember13",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember14",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember15",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember16",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember17",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember18",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember19",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember20",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember21",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember22",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember23",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember24",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember25",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember26",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember27",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember28",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember29",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember30",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember31",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember32",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember33",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember34",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember35",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember36",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember37",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember38",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember39",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember40",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember41",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember42",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember43",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember44",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember45",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember46",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember47",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember48",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember49",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember50",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember51",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember52",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember53",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember54",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember55",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember56",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember57",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember58",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember59",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember60",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember61",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember62",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember63",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember64",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember65",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember66",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember67",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember68",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember69",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember70",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember71",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember72",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember73",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember74",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember75",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember76",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember77",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember78",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember79",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember80",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember81",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember82",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember83",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember84",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember85",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember86",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember87",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember88",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember89",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember90",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember91",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember92",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember93",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember94",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember95",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember96",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember97",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember98",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember99",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember100",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember101",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember102",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember103",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember104",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember105",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember106",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember107",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember108",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember109",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember110",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember111",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember112",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember113",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember114",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember115",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember116",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember117",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember118",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember119",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember120",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember121",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember122",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember123",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember124",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember125",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember126",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember127",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember128",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember129",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember130",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember131",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember132",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember133",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember134",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember135",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember136",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember137",
    "IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember138",
    "IncludeAttributesContributorsFiltersUnionMember140",
    "IncludeAttributesContributorsFiltersUnionMember140Filter",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember0",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember1",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember2",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember3",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember4",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember5",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember6",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember7",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember8",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember9",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember10",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember11",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember12",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember13",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember14",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember15",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember16",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember17",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember18",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember19",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember20",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember21",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember22",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember23",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember24",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember25",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember26",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember27",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember28",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember29",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember30",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember31",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember32",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember33",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember34",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember35",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember36",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember37",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember38",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember39",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember40",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember41",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember42",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember43",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember44",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember45",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember46",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember47",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember48",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember49",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember50",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember51",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember52",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember53",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember54",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember55",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember56",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember57",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember58",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember59",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember60",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember61",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember62",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember63",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember64",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember65",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember66",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember67",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember68",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember69",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember70",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember71",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember72",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember73",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember74",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember75",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember76",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember77",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember78",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember79",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember80",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember81",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember82",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember83",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember84",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember85",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember86",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember87",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember88",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember89",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember90",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember91",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember92",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember93",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember94",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember95",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember96",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember97",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember98",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember99",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember100",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember101",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember102",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember103",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember104",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember105",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember106",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember107",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember108",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember109",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember110",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember111",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember112",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember113",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember114",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember115",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember116",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember117",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember118",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember119",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember120",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember121",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember122",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember123",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember124",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember125",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember126",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember127",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember128",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember129",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember130",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember131",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember132",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember133",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember134",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember135",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember136",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember137",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember138",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139Filter",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember0",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember1",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember2",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember3",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember4",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember5",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember6",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember7",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember8",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember9",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember10",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember11",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember12",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember13",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember14",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember15",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember16",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember17",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember18",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember19",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember20",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember21",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember22",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember23",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember24",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember25",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember26",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember27",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember28",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember29",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember30",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember31",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember32",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember33",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember34",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember35",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember36",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember37",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember38",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember39",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember40",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember41",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember42",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember43",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember44",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember45",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember46",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember47",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember48",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember49",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember50",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember51",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember52",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember53",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember54",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember55",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember56",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember57",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember58",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember59",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember60",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember61",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember62",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember63",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember64",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember65",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember66",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember67",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember68",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember69",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember70",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember71",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember72",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember73",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember74",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember75",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember76",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember77",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember78",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember79",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember80",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember81",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember82",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember83",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember84",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember85",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember86",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember87",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember88",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember89",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember90",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember91",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember92",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember93",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember94",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember95",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember96",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember97",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember98",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember99",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember100",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember101",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember102",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember103",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember104",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember105",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember106",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember107",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember108",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember109",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember110",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember111",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember112",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember113",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember114",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember115",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember116",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember117",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember118",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember119",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember120",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember121",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember122",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember123",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember124",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember125",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember126",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember127",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember128",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember129",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember130",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember131",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember132",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember133",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember134",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember135",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember136",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember137",
    "IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember138",
    "IncludeAttributesStarrers",
    "IncludeAttributesStarrersFilters",
    "IncludeAttributesStarrersFiltersEq",
    "IncludeAttributesStarrersFiltersNotEq",
    "IncludeAttributesStarrersFiltersIn",
    "IncludeAttributesStarrersFiltersNotIn",
    "IncludeAttributesStarrersFiltersLt",
    "IncludeAttributesStarrersFiltersLte",
    "IncludeAttributesStarrersFiltersGt",
    "IncludeAttributesStarrersFiltersGte",
    "IncludeAttributesStarrersFiltersGlob",
    "IncludeAttributesStarrersFiltersNotGlob",
    "IncludeAttributesStarrersFiltersIGlob",
    "IncludeAttributesStarrersFiltersNotIGlob",
    "IncludeAttributesStarrersFiltersRegex",
    "IncludeAttributesStarrersFiltersContainsAllTokens",
    "IncludeAttributesStarrersFiltersUnionMember139",
    "IncludeAttributesStarrersFiltersUnionMember139Filter",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember0",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember1",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember2",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember3",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember4",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember5",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember6",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember7",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember8",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember9",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember10",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember11",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember12",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember13",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember14",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember15",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember16",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember17",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember18",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember19",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember20",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember21",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember22",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember23",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember24",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember25",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember26",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember27",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember28",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember29",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember30",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember31",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember32",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember33",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember34",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember35",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember36",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember37",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember38",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember39",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember40",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember41",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember42",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember43",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember44",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember45",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember46",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember47",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember48",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember49",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember50",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember51",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember52",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember53",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember54",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember55",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember56",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember57",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember58",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember59",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember60",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember61",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember62",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember63",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember64",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember65",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember66",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember67",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember68",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember69",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember70",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember71",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember72",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember73",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember74",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember75",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember76",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember77",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember78",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember79",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember80",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember81",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember82",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember83",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember84",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember85",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember86",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember87",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember88",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember89",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember90",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember91",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember92",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember93",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember94",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember95",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember96",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember97",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember98",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember99",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember100",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember101",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember102",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember103",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember104",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember105",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember106",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember107",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember108",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember109",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember110",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember111",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember112",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember113",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember114",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember115",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember116",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember117",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember118",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember119",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember120",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember121",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember122",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember123",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember124",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember125",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember126",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember127",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember128",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember129",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember130",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember131",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember132",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember133",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember134",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember135",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember136",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember137",
    "IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember138",
    "IncludeAttributesStarrersFiltersUnionMember140",
    "IncludeAttributesStarrersFiltersUnionMember140Filter",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember0",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember1",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember2",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember3",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember4",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember5",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember6",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember7",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember8",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember9",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember10",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember11",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember12",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember13",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember14",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember15",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember16",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember17",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember18",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember19",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember20",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember21",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember22",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember23",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember24",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember25",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember26",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember27",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember28",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember29",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember30",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember31",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember32",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember33",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember34",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember35",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember36",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember37",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember38",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember39",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember40",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember41",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember42",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember43",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember44",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember45",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember46",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember47",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember48",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember49",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember50",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember51",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember52",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember53",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember54",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember55",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember56",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember57",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember58",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember59",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember60",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember61",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember62",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember63",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember64",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember65",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember66",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember67",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember68",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember69",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember70",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember71",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember72",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember73",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember74",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember75",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember76",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember77",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember78",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember79",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember80",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember81",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember82",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember83",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember84",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember85",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember86",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember87",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember88",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember89",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember90",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember91",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember92",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember93",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember94",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember95",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember96",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember97",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember98",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember99",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember100",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember101",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember102",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember103",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember104",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember105",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember106",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember107",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember108",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember109",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember110",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember111",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember112",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember113",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember114",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember115",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember116",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember117",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember118",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember119",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember120",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember121",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember122",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember123",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember124",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember125",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember126",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember127",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember128",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember129",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember130",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember131",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember132",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember133",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember134",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember135",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember136",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember137",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember138",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139Filter",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember0",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember1",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember2",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember3",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember4",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember5",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember6",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember7",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember8",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember9",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember10",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember11",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember12",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember13",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember14",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember15",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember16",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember17",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember18",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember19",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember20",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember21",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember22",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember23",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember24",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember25",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember26",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember27",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember28",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember29",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember30",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember31",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember32",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember33",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember34",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember35",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember36",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember37",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember38",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember39",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember40",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember41",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember42",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember43",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember44",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember45",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember46",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember47",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember48",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember49",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember50",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember51",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember52",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember53",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember54",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember55",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember56",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember57",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember58",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember59",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember60",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember61",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember62",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember63",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember64",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember65",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember66",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember67",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember68",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember69",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember70",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember71",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember72",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember73",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember74",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember75",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember76",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember77",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember78",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember79",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember80",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember81",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember82",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember83",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember84",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember85",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember86",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember87",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember88",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember89",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember90",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember91",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember92",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember93",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember94",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember95",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember96",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember97",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember98",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember99",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember100",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember101",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember102",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember103",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember104",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember105",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember106",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember107",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember108",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember109",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember110",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember111",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember112",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember113",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember114",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember115",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember116",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember117",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember118",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember119",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember120",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember121",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember122",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember123",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember124",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember125",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember126",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember127",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember128",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember129",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember130",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember131",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember132",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember133",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember134",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember135",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember136",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember137",
    "IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember138",
]


class RawRepoRetrieveParams(TypedDict, total=False):
    github_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="githubIds")]]
    """Array of GitHub node IDs (1-100)"""

    include_attributes: Annotated[IncludeAttributes, PropertyInfo(alias="includeAttributes")]
    """Optional graph relationships to include (owner, contributors, starrers)"""


class IncludeAttributesContributorsFiltersEq(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersNotEq(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersIn(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersNotIn(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersLt(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersLte(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersGt(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersGte(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersNotGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersIGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersNotIGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersRegex(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersContainsAllTokens(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


IncludeAttributesContributorsFiltersUnionMember139Filter: TypeAlias = Union[
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember0,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember1,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember2,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember3,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember4,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember5,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember6,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember7,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember8,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember9,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember10,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember11,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember12,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember13,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember14,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember15,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember16,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember17,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember18,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember19,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember20,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember21,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember22,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember23,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember24,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember25,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember26,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember27,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember28,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember29,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember30,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember31,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember32,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember33,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember34,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember35,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember36,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember37,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember38,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember39,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember40,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember41,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember42,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember43,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember44,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember45,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember46,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember47,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember48,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember49,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember50,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember51,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember52,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember53,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember54,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember55,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember56,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember57,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember58,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember59,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember60,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember61,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember62,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember63,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember64,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember65,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember66,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember67,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember68,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember69,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember70,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember71,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember72,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember73,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember74,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember75,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember76,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember77,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember78,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember79,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember80,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember81,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember82,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember83,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember84,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember85,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember86,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember87,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember88,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember89,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember90,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember91,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember92,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember93,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember94,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember95,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember96,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember97,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember98,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember99,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember100,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember101,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember102,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember103,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember104,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember105,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember106,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember107,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember108,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember109,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember110,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember111,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember112,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember113,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember114,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember115,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember116,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember117,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember118,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember119,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember120,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember121,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember122,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember123,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember124,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember125,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember126,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember127,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember128,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember129,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember130,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember131,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember132,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember133,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember134,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember135,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember136,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember137,
    IncludeAttributesContributorsFiltersUnionMember139FilterUnionMember138,
]


class IncludeAttributesContributorsFiltersUnionMember139(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesContributorsFiltersUnionMember139Filter]]

    op: Required[Literal["And", "Or"]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember100(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember101(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember102(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember103(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember104(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember105(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember106(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember107(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember108(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember109(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember110(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember111(
    TypedDict, total=False
):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember112(
    TypedDict, total=False
):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember113(
    TypedDict, total=False
):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember114(
    TypedDict, total=False
):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember115(
    TypedDict, total=False
):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember116(
    TypedDict, total=False
):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember117(
    TypedDict, total=False
):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember118(
    TypedDict, total=False
):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember119(
    TypedDict, total=False
):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember120(
    TypedDict, total=False
):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember121(
    TypedDict, total=False
):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember122(
    TypedDict, total=False
):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember123(
    TypedDict, total=False
):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember124(
    TypedDict, total=False
):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember125(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember126(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember127(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember128(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember129(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember130(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember131(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember132(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember133(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember134(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember135(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember136(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember137(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember138(
    TypedDict, total=False
):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139Filter: TypeAlias = Union[
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember0,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember1,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember2,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember3,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember4,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember5,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember6,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember7,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember8,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember9,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember10,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember11,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember12,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember13,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember14,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember15,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember16,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember17,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember18,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember19,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember20,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember21,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember22,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember23,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember24,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember25,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember26,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember27,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember28,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember29,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember30,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember31,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember32,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember33,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember34,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember35,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember36,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember37,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember38,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember39,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember40,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember41,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember42,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember43,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember44,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember45,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember46,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember47,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember48,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember49,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember50,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember51,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember52,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember53,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember54,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember55,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember56,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember57,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember58,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember59,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember60,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember61,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember62,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember63,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember64,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember65,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember66,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember67,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember68,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember69,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember70,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember71,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember72,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember73,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember74,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember75,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember76,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember77,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember78,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember79,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember80,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember81,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember82,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember83,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember84,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember85,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember86,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember87,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember88,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember89,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember90,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember91,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember92,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember93,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember94,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember95,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember96,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember97,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember98,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember99,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember100,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember101,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember102,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember103,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember104,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember105,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember106,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember107,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember108,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember109,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember110,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember111,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember112,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember113,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember114,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember115,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember116,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember117,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember118,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember119,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember120,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember121,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember122,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember123,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember124,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember125,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember126,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember127,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember128,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember129,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember130,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember131,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember132,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember133,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember134,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember135,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember136,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember137,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139FilterUnionMember138,
]


class IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139Filter]]

    op: Required[Literal["And", "Or"]]


IncludeAttributesContributorsFiltersUnionMember140Filter: TypeAlias = Union[
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember0,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember1,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember2,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember3,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember4,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember5,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember6,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember7,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember8,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember9,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember10,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember11,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember12,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember13,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember14,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember15,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember16,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember17,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember18,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember19,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember20,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember21,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember22,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember23,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember24,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember25,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember26,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember27,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember28,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember29,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember30,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember31,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember32,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember33,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember34,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember35,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember36,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember37,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember38,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember39,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember40,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember41,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember42,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember43,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember44,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember45,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember46,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember47,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember48,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember49,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember50,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember51,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember52,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember53,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember54,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember55,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember56,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember57,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember58,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember59,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember60,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember61,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember62,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember63,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember64,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember65,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember66,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember67,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember68,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember69,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember70,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember71,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember72,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember73,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember74,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember75,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember76,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember77,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember78,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember79,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember80,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember81,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember82,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember83,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember84,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember85,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember86,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember87,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember88,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember89,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember90,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember91,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember92,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember93,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember94,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember95,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember96,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember97,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember98,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember99,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember100,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember101,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember102,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember103,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember104,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember105,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember106,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember107,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember108,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember109,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember110,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember111,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember112,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember113,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember114,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember115,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember116,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember117,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember118,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember119,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember120,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember121,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember122,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember123,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember124,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember125,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember126,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember127,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember128,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember129,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember130,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember131,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember132,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember133,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember134,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember135,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember136,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember137,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember138,
    IncludeAttributesContributorsFiltersUnionMember140FilterUnionMember139,
]


class IncludeAttributesContributorsFiltersUnionMember140(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesContributorsFiltersUnionMember140Filter]]

    op: Required[Literal["And", "Or"]]


IncludeAttributesContributorsFilters: TypeAlias = Union[
    IncludeAttributesContributorsFiltersEq,
    IncludeAttributesContributorsFiltersNotEq,
    IncludeAttributesContributorsFiltersIn,
    IncludeAttributesContributorsFiltersNotIn,
    IncludeAttributesContributorsFiltersLt,
    IncludeAttributesContributorsFiltersLte,
    IncludeAttributesContributorsFiltersGt,
    IncludeAttributesContributorsFiltersGte,
    IncludeAttributesContributorsFiltersGlob,
    IncludeAttributesContributorsFiltersNotGlob,
    IncludeAttributesContributorsFiltersIGlob,
    IncludeAttributesContributorsFiltersNotIGlob,
    IncludeAttributesContributorsFiltersRegex,
    IncludeAttributesContributorsFiltersEq,
    IncludeAttributesContributorsFiltersNotEq,
    IncludeAttributesContributorsFiltersIn,
    IncludeAttributesContributorsFiltersNotIn,
    IncludeAttributesContributorsFiltersLt,
    IncludeAttributesContributorsFiltersLte,
    IncludeAttributesContributorsFiltersGt,
    IncludeAttributesContributorsFiltersGte,
    IncludeAttributesContributorsFiltersGlob,
    IncludeAttributesContributorsFiltersNotGlob,
    IncludeAttributesContributorsFiltersIGlob,
    IncludeAttributesContributorsFiltersNotIGlob,
    IncludeAttributesContributorsFiltersRegex,
    IncludeAttributesContributorsFiltersContainsAllTokens,
    IncludeAttributesContributorsFiltersEq,
    IncludeAttributesContributorsFiltersNotEq,
    IncludeAttributesContributorsFiltersIn,
    IncludeAttributesContributorsFiltersNotIn,
    IncludeAttributesContributorsFiltersLt,
    IncludeAttributesContributorsFiltersLte,
    IncludeAttributesContributorsFiltersGt,
    IncludeAttributesContributorsFiltersGte,
    IncludeAttributesContributorsFiltersGlob,
    IncludeAttributesContributorsFiltersNotGlob,
    IncludeAttributesContributorsFiltersIGlob,
    IncludeAttributesContributorsFiltersNotIGlob,
    IncludeAttributesContributorsFiltersRegex,
    IncludeAttributesContributorsFiltersContainsAllTokens,
    IncludeAttributesContributorsFiltersEq,
    IncludeAttributesContributorsFiltersNotEq,
    IncludeAttributesContributorsFiltersIn,
    IncludeAttributesContributorsFiltersNotIn,
    IncludeAttributesContributorsFiltersLt,
    IncludeAttributesContributorsFiltersLte,
    IncludeAttributesContributorsFiltersGt,
    IncludeAttributesContributorsFiltersGte,
    IncludeAttributesContributorsFiltersGlob,
    IncludeAttributesContributorsFiltersNotGlob,
    IncludeAttributesContributorsFiltersIGlob,
    IncludeAttributesContributorsFiltersNotIGlob,
    IncludeAttributesContributorsFiltersRegex,
    IncludeAttributesContributorsFiltersContainsAllTokens,
    IncludeAttributesContributorsFiltersEq,
    IncludeAttributesContributorsFiltersNotEq,
    IncludeAttributesContributorsFiltersIn,
    IncludeAttributesContributorsFiltersNotIn,
    IncludeAttributesContributorsFiltersLt,
    IncludeAttributesContributorsFiltersLte,
    IncludeAttributesContributorsFiltersGt,
    IncludeAttributesContributorsFiltersGte,
    IncludeAttributesContributorsFiltersGlob,
    IncludeAttributesContributorsFiltersNotGlob,
    IncludeAttributesContributorsFiltersIGlob,
    IncludeAttributesContributorsFiltersNotIGlob,
    IncludeAttributesContributorsFiltersRegex,
    IncludeAttributesContributorsFiltersContainsAllTokens,
    IncludeAttributesContributorsFiltersEq,
    IncludeAttributesContributorsFiltersNotEq,
    IncludeAttributesContributorsFiltersIn,
    IncludeAttributesContributorsFiltersNotIn,
    IncludeAttributesContributorsFiltersLt,
    IncludeAttributesContributorsFiltersLte,
    IncludeAttributesContributorsFiltersGt,
    IncludeAttributesContributorsFiltersGte,
    IncludeAttributesContributorsFiltersGlob,
    IncludeAttributesContributorsFiltersNotGlob,
    IncludeAttributesContributorsFiltersIGlob,
    IncludeAttributesContributorsFiltersNotIGlob,
    IncludeAttributesContributorsFiltersRegex,
    IncludeAttributesContributorsFiltersContainsAllTokens,
    IncludeAttributesContributorsFiltersEq,
    IncludeAttributesContributorsFiltersNotEq,
    IncludeAttributesContributorsFiltersIn,
    IncludeAttributesContributorsFiltersNotIn,
    IncludeAttributesContributorsFiltersLt,
    IncludeAttributesContributorsFiltersLte,
    IncludeAttributesContributorsFiltersGt,
    IncludeAttributesContributorsFiltersGte,
    IncludeAttributesContributorsFiltersGlob,
    IncludeAttributesContributorsFiltersNotGlob,
    IncludeAttributesContributorsFiltersIGlob,
    IncludeAttributesContributorsFiltersNotIGlob,
    IncludeAttributesContributorsFiltersRegex,
    IncludeAttributesContributorsFiltersContainsAllTokens,
    IncludeAttributesContributorsFiltersEq,
    IncludeAttributesContributorsFiltersNotEq,
    IncludeAttributesContributorsFiltersIn,
    IncludeAttributesContributorsFiltersNotIn,
    IncludeAttributesContributorsFiltersLt,
    IncludeAttributesContributorsFiltersLte,
    IncludeAttributesContributorsFiltersGt,
    IncludeAttributesContributorsFiltersGte,
    IncludeAttributesContributorsFiltersGlob,
    IncludeAttributesContributorsFiltersNotGlob,
    IncludeAttributesContributorsFiltersIGlob,
    IncludeAttributesContributorsFiltersNotIGlob,
    IncludeAttributesContributorsFiltersRegex,
    IncludeAttributesContributorsFiltersContainsAllTokens,
    IncludeAttributesContributorsFiltersEq,
    IncludeAttributesContributorsFiltersNotEq,
    IncludeAttributesContributorsFiltersIn,
    IncludeAttributesContributorsFiltersNotIn,
    IncludeAttributesContributorsFiltersLt,
    IncludeAttributesContributorsFiltersLte,
    IncludeAttributesContributorsFiltersGt,
    IncludeAttributesContributorsFiltersGte,
    IncludeAttributesContributorsFiltersGlob,
    IncludeAttributesContributorsFiltersNotGlob,
    IncludeAttributesContributorsFiltersIGlob,
    IncludeAttributesContributorsFiltersNotIGlob,
    IncludeAttributesContributorsFiltersRegex,
    IncludeAttributesContributorsFiltersContainsAllTokens,
    IncludeAttributesContributorsFiltersEq,
    IncludeAttributesContributorsFiltersNotEq,
    IncludeAttributesContributorsFiltersIn,
    IncludeAttributesContributorsFiltersNotIn,
    IncludeAttributesContributorsFiltersLt,
    IncludeAttributesContributorsFiltersLte,
    IncludeAttributesContributorsFiltersGt,
    IncludeAttributesContributorsFiltersGte,
    IncludeAttributesContributorsFiltersGlob,
    IncludeAttributesContributorsFiltersNotGlob,
    IncludeAttributesContributorsFiltersIGlob,
    IncludeAttributesContributorsFiltersNotIGlob,
    IncludeAttributesContributorsFiltersRegex,
    IncludeAttributesContributorsFiltersContainsAllTokens,
    IncludeAttributesContributorsFiltersUnionMember139,
    IncludeAttributesContributorsFiltersUnionMember140,
]


class IncludeAttributesContributors(TypedDict, total=False):
    """Include repository contributors with cursor pagination"""

    first: Required[int]
    """Number of items to return (max: 100)"""

    after: str
    """Cursor for pagination (opaque base64-encoded)"""

    filters: IncludeAttributesContributorsFilters
    """Optional filters for users.

    Supports fields like login, company, location, resolvedCountry, resolvedState,
    resolvedCity. Operators: Eq, NotEq, In, NotIn, Lt, Lte, Gt, Gte.
    """


class IncludeAttributesStarrersFiltersEq(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersNotEq(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersIn(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersNotIn(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersLt(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersLte(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersGt(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersGte(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersNotGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersIGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersNotIGlob(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersRegex(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersContainsAllTokens(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


IncludeAttributesStarrersFiltersUnionMember139Filter: TypeAlias = Union[
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember0,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember1,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember2,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember3,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember4,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember5,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember6,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember7,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember8,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember9,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember10,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember11,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember12,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember13,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember14,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember15,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember16,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember17,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember18,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember19,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember20,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember21,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember22,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember23,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember24,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember25,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember26,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember27,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember28,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember29,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember30,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember31,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember32,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember33,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember34,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember35,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember36,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember37,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember38,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember39,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember40,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember41,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember42,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember43,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember44,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember45,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember46,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember47,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember48,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember49,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember50,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember51,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember52,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember53,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember54,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember55,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember56,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember57,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember58,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember59,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember60,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember61,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember62,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember63,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember64,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember65,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember66,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember67,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember68,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember69,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember70,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember71,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember72,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember73,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember74,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember75,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember76,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember77,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember78,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember79,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember80,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember81,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember82,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember83,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember84,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember85,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember86,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember87,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember88,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember89,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember90,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember91,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember92,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember93,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember94,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember95,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember96,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember97,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember98,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember99,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember100,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember101,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember102,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember103,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember104,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember105,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember106,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember107,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember108,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember109,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember110,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember111,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember112,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember113,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember114,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember115,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember116,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember117,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember118,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember119,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember120,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember121,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember122,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember123,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember124,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember125,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember126,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember127,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember128,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember129,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember130,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember131,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember132,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember133,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember134,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember135,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember136,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember137,
    IncludeAttributesStarrersFiltersUnionMember139FilterUnionMember138,
]


class IncludeAttributesStarrersFiltersUnionMember139(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesStarrersFiltersUnionMember139Filter]]

    op: Required[Literal["And", "Or"]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139Filter: TypeAlias = Union[
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember0,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember1,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember2,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember3,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember4,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember5,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember6,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember7,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember8,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember9,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember10,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember11,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember12,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember13,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember14,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember15,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember16,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember17,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember18,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember19,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember20,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember21,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember22,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember23,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember24,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember25,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember26,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember27,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember28,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember29,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember30,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember31,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember32,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember33,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember34,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember35,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember36,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember37,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember38,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember39,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember40,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember41,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember42,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember43,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember44,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember45,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember46,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember47,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember48,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember49,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember50,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember51,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember52,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember53,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember54,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember55,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember56,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember57,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember58,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember59,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember60,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember61,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember62,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember63,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember64,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember65,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember66,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember67,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember68,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember69,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember70,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember71,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember72,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember73,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember74,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember75,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember76,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember77,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember78,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember79,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember80,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember81,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember82,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember83,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember84,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember85,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember86,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember87,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember88,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember89,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember90,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember91,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember92,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember93,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember94,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember95,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember96,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember97,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember98,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember99,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember100,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember101,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember102,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember103,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember104,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember105,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember106,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember107,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember108,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember109,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember110,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember111,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember112,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember113,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember114,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember115,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember116,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember117,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember118,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember119,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember120,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember121,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember122,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember123,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember124,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember125,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember126,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember127,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember128,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember129,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember130,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember131,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember132,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember133,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember134,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember135,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember136,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember137,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139FilterUnionMember138,
]


class IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139Filter]]

    op: Required[Literal["And", "Or"]]


IncludeAttributesStarrersFiltersUnionMember140Filter: TypeAlias = Union[
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember0,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember1,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember2,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember3,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember4,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember5,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember6,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember7,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember8,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember9,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember10,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember11,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember12,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember13,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember14,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember15,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember16,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember17,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember18,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember19,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember20,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember21,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember22,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember23,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember24,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember25,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember26,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember27,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember28,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember29,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember30,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember31,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember32,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember33,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember34,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember35,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember36,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember37,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember38,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember39,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember40,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember41,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember42,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember43,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember44,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember45,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember46,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember47,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember48,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember49,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember50,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember51,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember52,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember53,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember54,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember55,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember56,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember57,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember58,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember59,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember60,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember61,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember62,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember63,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember64,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember65,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember66,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember67,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember68,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember69,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember70,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember71,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember72,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember73,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember74,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember75,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember76,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember77,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember78,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember79,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember80,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember81,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember82,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember83,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember84,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember85,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember86,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember87,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember88,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember89,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember90,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember91,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember92,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember93,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember94,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember95,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember96,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember97,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember98,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember99,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember100,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember101,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember102,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember103,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember104,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember105,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember106,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember107,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember108,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember109,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember110,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember111,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember112,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember113,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember114,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember115,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember116,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember117,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember118,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember119,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember120,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember121,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember122,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember123,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember124,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember125,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember126,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember127,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember128,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember129,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember130,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember131,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember132,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember133,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember134,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember135,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember136,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember137,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember138,
    IncludeAttributesStarrersFiltersUnionMember140FilterUnionMember139,
]


class IncludeAttributesStarrersFiltersUnionMember140(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesStarrersFiltersUnionMember140Filter]]

    op: Required[Literal["And", "Or"]]


IncludeAttributesStarrersFilters: TypeAlias = Union[
    IncludeAttributesStarrersFiltersEq,
    IncludeAttributesStarrersFiltersNotEq,
    IncludeAttributesStarrersFiltersIn,
    IncludeAttributesStarrersFiltersNotIn,
    IncludeAttributesStarrersFiltersLt,
    IncludeAttributesStarrersFiltersLte,
    IncludeAttributesStarrersFiltersGt,
    IncludeAttributesStarrersFiltersGte,
    IncludeAttributesStarrersFiltersGlob,
    IncludeAttributesStarrersFiltersNotGlob,
    IncludeAttributesStarrersFiltersIGlob,
    IncludeAttributesStarrersFiltersNotIGlob,
    IncludeAttributesStarrersFiltersRegex,
    IncludeAttributesStarrersFiltersEq,
    IncludeAttributesStarrersFiltersNotEq,
    IncludeAttributesStarrersFiltersIn,
    IncludeAttributesStarrersFiltersNotIn,
    IncludeAttributesStarrersFiltersLt,
    IncludeAttributesStarrersFiltersLte,
    IncludeAttributesStarrersFiltersGt,
    IncludeAttributesStarrersFiltersGte,
    IncludeAttributesStarrersFiltersGlob,
    IncludeAttributesStarrersFiltersNotGlob,
    IncludeAttributesStarrersFiltersIGlob,
    IncludeAttributesStarrersFiltersNotIGlob,
    IncludeAttributesStarrersFiltersRegex,
    IncludeAttributesStarrersFiltersContainsAllTokens,
    IncludeAttributesStarrersFiltersEq,
    IncludeAttributesStarrersFiltersNotEq,
    IncludeAttributesStarrersFiltersIn,
    IncludeAttributesStarrersFiltersNotIn,
    IncludeAttributesStarrersFiltersLt,
    IncludeAttributesStarrersFiltersLte,
    IncludeAttributesStarrersFiltersGt,
    IncludeAttributesStarrersFiltersGte,
    IncludeAttributesStarrersFiltersGlob,
    IncludeAttributesStarrersFiltersNotGlob,
    IncludeAttributesStarrersFiltersIGlob,
    IncludeAttributesStarrersFiltersNotIGlob,
    IncludeAttributesStarrersFiltersRegex,
    IncludeAttributesStarrersFiltersContainsAllTokens,
    IncludeAttributesStarrersFiltersEq,
    IncludeAttributesStarrersFiltersNotEq,
    IncludeAttributesStarrersFiltersIn,
    IncludeAttributesStarrersFiltersNotIn,
    IncludeAttributesStarrersFiltersLt,
    IncludeAttributesStarrersFiltersLte,
    IncludeAttributesStarrersFiltersGt,
    IncludeAttributesStarrersFiltersGte,
    IncludeAttributesStarrersFiltersGlob,
    IncludeAttributesStarrersFiltersNotGlob,
    IncludeAttributesStarrersFiltersIGlob,
    IncludeAttributesStarrersFiltersNotIGlob,
    IncludeAttributesStarrersFiltersRegex,
    IncludeAttributesStarrersFiltersContainsAllTokens,
    IncludeAttributesStarrersFiltersEq,
    IncludeAttributesStarrersFiltersNotEq,
    IncludeAttributesStarrersFiltersIn,
    IncludeAttributesStarrersFiltersNotIn,
    IncludeAttributesStarrersFiltersLt,
    IncludeAttributesStarrersFiltersLte,
    IncludeAttributesStarrersFiltersGt,
    IncludeAttributesStarrersFiltersGte,
    IncludeAttributesStarrersFiltersGlob,
    IncludeAttributesStarrersFiltersNotGlob,
    IncludeAttributesStarrersFiltersIGlob,
    IncludeAttributesStarrersFiltersNotIGlob,
    IncludeAttributesStarrersFiltersRegex,
    IncludeAttributesStarrersFiltersContainsAllTokens,
    IncludeAttributesStarrersFiltersEq,
    IncludeAttributesStarrersFiltersNotEq,
    IncludeAttributesStarrersFiltersIn,
    IncludeAttributesStarrersFiltersNotIn,
    IncludeAttributesStarrersFiltersLt,
    IncludeAttributesStarrersFiltersLte,
    IncludeAttributesStarrersFiltersGt,
    IncludeAttributesStarrersFiltersGte,
    IncludeAttributesStarrersFiltersGlob,
    IncludeAttributesStarrersFiltersNotGlob,
    IncludeAttributesStarrersFiltersIGlob,
    IncludeAttributesStarrersFiltersNotIGlob,
    IncludeAttributesStarrersFiltersRegex,
    IncludeAttributesStarrersFiltersContainsAllTokens,
    IncludeAttributesStarrersFiltersEq,
    IncludeAttributesStarrersFiltersNotEq,
    IncludeAttributesStarrersFiltersIn,
    IncludeAttributesStarrersFiltersNotIn,
    IncludeAttributesStarrersFiltersLt,
    IncludeAttributesStarrersFiltersLte,
    IncludeAttributesStarrersFiltersGt,
    IncludeAttributesStarrersFiltersGte,
    IncludeAttributesStarrersFiltersGlob,
    IncludeAttributesStarrersFiltersNotGlob,
    IncludeAttributesStarrersFiltersIGlob,
    IncludeAttributesStarrersFiltersNotIGlob,
    IncludeAttributesStarrersFiltersRegex,
    IncludeAttributesStarrersFiltersContainsAllTokens,
    IncludeAttributesStarrersFiltersEq,
    IncludeAttributesStarrersFiltersNotEq,
    IncludeAttributesStarrersFiltersIn,
    IncludeAttributesStarrersFiltersNotIn,
    IncludeAttributesStarrersFiltersLt,
    IncludeAttributesStarrersFiltersLte,
    IncludeAttributesStarrersFiltersGt,
    IncludeAttributesStarrersFiltersGte,
    IncludeAttributesStarrersFiltersGlob,
    IncludeAttributesStarrersFiltersNotGlob,
    IncludeAttributesStarrersFiltersIGlob,
    IncludeAttributesStarrersFiltersNotIGlob,
    IncludeAttributesStarrersFiltersRegex,
    IncludeAttributesStarrersFiltersContainsAllTokens,
    IncludeAttributesStarrersFiltersEq,
    IncludeAttributesStarrersFiltersNotEq,
    IncludeAttributesStarrersFiltersIn,
    IncludeAttributesStarrersFiltersNotIn,
    IncludeAttributesStarrersFiltersLt,
    IncludeAttributesStarrersFiltersLte,
    IncludeAttributesStarrersFiltersGt,
    IncludeAttributesStarrersFiltersGte,
    IncludeAttributesStarrersFiltersGlob,
    IncludeAttributesStarrersFiltersNotGlob,
    IncludeAttributesStarrersFiltersIGlob,
    IncludeAttributesStarrersFiltersNotIGlob,
    IncludeAttributesStarrersFiltersRegex,
    IncludeAttributesStarrersFiltersContainsAllTokens,
    IncludeAttributesStarrersFiltersEq,
    IncludeAttributesStarrersFiltersNotEq,
    IncludeAttributesStarrersFiltersIn,
    IncludeAttributesStarrersFiltersNotIn,
    IncludeAttributesStarrersFiltersLt,
    IncludeAttributesStarrersFiltersLte,
    IncludeAttributesStarrersFiltersGt,
    IncludeAttributesStarrersFiltersGte,
    IncludeAttributesStarrersFiltersGlob,
    IncludeAttributesStarrersFiltersNotGlob,
    IncludeAttributesStarrersFiltersIGlob,
    IncludeAttributesStarrersFiltersNotIGlob,
    IncludeAttributesStarrersFiltersRegex,
    IncludeAttributesStarrersFiltersContainsAllTokens,
    IncludeAttributesStarrersFiltersUnionMember139,
    IncludeAttributesStarrersFiltersUnionMember140,
]


class IncludeAttributesStarrers(TypedDict, total=False):
    """Include users who starred the repository with cursor pagination"""

    first: Required[int]
    """Number of items to return (max: 100)"""

    after: str
    """Cursor for pagination (opaque base64-encoded)"""

    filters: IncludeAttributesStarrersFilters
    """Optional filters for users.

    Supports fields like login, company, location, resolvedCountry, resolvedState,
    resolvedCity. Operators: Eq, NotEq, In, NotIn, Lt, Lte, Gt, Gte.
    """


class IncludeAttributes(TypedDict, total=False):
    """Optional graph relationships to include (owner, contributors, starrers)"""

    contributors: IncludeAttributesContributors
    """Include repository contributors with cursor pagination"""

    owner: bool
    """Include repository owner information"""

    owner_devrank: Annotated[bool, PropertyInfo(alias="ownerDevrank")]
    """Include devrank data for the repository owner"""

    starrers: IncludeAttributesStarrers
    """Include users who starred the repository with cursor pagination"""
