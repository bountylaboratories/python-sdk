# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "SearchRepoSearchParams",
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
    "FiltersContains",
    "FiltersNotContains",
    "FiltersContainsAny",
    "FiltersNotContainsAny",
    "FiltersAnyLt",
    "FiltersAnyLte",
    "FiltersAnyGt",
    "FiltersAnyGte",
    "FiltersUnionMember107",
    "FiltersUnionMember107Filter",
    "FiltersUnionMember107FilterUnionMember0",
    "FiltersUnionMember107FilterUnionMember1",
    "FiltersUnionMember107FilterUnionMember2",
    "FiltersUnionMember107FilterUnionMember3",
    "FiltersUnionMember107FilterUnionMember4",
    "FiltersUnionMember107FilterUnionMember5",
    "FiltersUnionMember107FilterUnionMember6",
    "FiltersUnionMember107FilterUnionMember7",
    "FiltersUnionMember107FilterUnionMember8",
    "FiltersUnionMember107FilterUnionMember9",
    "FiltersUnionMember107FilterUnionMember10",
    "FiltersUnionMember107FilterUnionMember11",
    "FiltersUnionMember107FilterUnionMember12",
    "FiltersUnionMember107FilterUnionMember13",
    "FiltersUnionMember107FilterUnionMember14",
    "FiltersUnionMember107FilterUnionMember15",
    "FiltersUnionMember107FilterUnionMember16",
    "FiltersUnionMember107FilterUnionMember17",
    "FiltersUnionMember107FilterUnionMember18",
    "FiltersUnionMember107FilterUnionMember19",
    "FiltersUnionMember107FilterUnionMember20",
    "FiltersUnionMember107FilterUnionMember21",
    "FiltersUnionMember107FilterUnionMember22",
    "FiltersUnionMember107FilterUnionMember23",
    "FiltersUnionMember107FilterUnionMember24",
    "FiltersUnionMember107FilterUnionMember25",
    "FiltersUnionMember107FilterUnionMember26",
    "FiltersUnionMember107FilterUnionMember27",
    "FiltersUnionMember107FilterUnionMember28",
    "FiltersUnionMember107FilterUnionMember29",
    "FiltersUnionMember107FilterUnionMember30",
    "FiltersUnionMember107FilterUnionMember31",
    "FiltersUnionMember107FilterUnionMember32",
    "FiltersUnionMember107FilterUnionMember33",
    "FiltersUnionMember107FilterUnionMember34",
    "FiltersUnionMember107FilterUnionMember35",
    "FiltersUnionMember107FilterUnionMember36",
    "FiltersUnionMember107FilterUnionMember37",
    "FiltersUnionMember107FilterUnionMember38",
    "FiltersUnionMember107FilterUnionMember39",
    "FiltersUnionMember107FilterUnionMember40",
    "FiltersUnionMember107FilterUnionMember41",
    "FiltersUnionMember107FilterUnionMember42",
    "FiltersUnionMember107FilterUnionMember43",
    "FiltersUnionMember107FilterUnionMember44",
    "FiltersUnionMember107FilterUnionMember45",
    "FiltersUnionMember107FilterUnionMember46",
    "FiltersUnionMember107FilterUnionMember47",
    "FiltersUnionMember107FilterUnionMember48",
    "FiltersUnionMember107FilterUnionMember49",
    "FiltersUnionMember107FilterUnionMember50",
    "FiltersUnionMember107FilterUnionMember51",
    "FiltersUnionMember107FilterUnionMember52",
    "FiltersUnionMember107FilterUnionMember53",
    "FiltersUnionMember107FilterUnionMember54",
    "FiltersUnionMember107FilterUnionMember55",
    "FiltersUnionMember107FilterUnionMember56",
    "FiltersUnionMember107FilterUnionMember57",
    "FiltersUnionMember107FilterUnionMember58",
    "FiltersUnionMember107FilterUnionMember59",
    "FiltersUnionMember107FilterUnionMember60",
    "FiltersUnionMember107FilterUnionMember61",
    "FiltersUnionMember107FilterUnionMember62",
    "FiltersUnionMember107FilterUnionMember63",
    "FiltersUnionMember107FilterUnionMember64",
    "FiltersUnionMember107FilterUnionMember65",
    "FiltersUnionMember107FilterUnionMember66",
    "FiltersUnionMember107FilterUnionMember67",
    "FiltersUnionMember107FilterUnionMember68",
    "FiltersUnionMember107FilterUnionMember69",
    "FiltersUnionMember107FilterUnionMember70",
    "FiltersUnionMember107FilterUnionMember71",
    "FiltersUnionMember107FilterUnionMember72",
    "FiltersUnionMember107FilterUnionMember73",
    "FiltersUnionMember107FilterUnionMember74",
    "FiltersUnionMember107FilterUnionMember75",
    "FiltersUnionMember107FilterUnionMember76",
    "FiltersUnionMember107FilterUnionMember77",
    "FiltersUnionMember107FilterUnionMember78",
    "FiltersUnionMember107FilterUnionMember79",
    "FiltersUnionMember107FilterUnionMember80",
    "FiltersUnionMember107FilterUnionMember81",
    "FiltersUnionMember107FilterUnionMember82",
    "FiltersUnionMember107FilterUnionMember83",
    "FiltersUnionMember107FilterUnionMember84",
    "FiltersUnionMember107FilterUnionMember85",
    "FiltersUnionMember107FilterUnionMember86",
    "FiltersUnionMember107FilterUnionMember87",
    "FiltersUnionMember107FilterUnionMember88",
    "FiltersUnionMember107FilterUnionMember89",
    "FiltersUnionMember107FilterUnionMember90",
    "FiltersUnionMember107FilterUnionMember91",
    "FiltersUnionMember107FilterUnionMember92",
    "FiltersUnionMember107FilterUnionMember93",
    "FiltersUnionMember107FilterUnionMember94",
    "FiltersUnionMember107FilterUnionMember95",
    "FiltersUnionMember107FilterUnionMember96",
    "FiltersUnionMember107FilterUnionMember97",
    "FiltersUnionMember107FilterUnionMember98",
    "FiltersUnionMember107FilterUnionMember99",
    "FiltersUnionMember107FilterUnionMember100",
    "FiltersUnionMember107FilterUnionMember101",
    "FiltersUnionMember107FilterUnionMember102",
    "FiltersUnionMember107FilterUnionMember103",
    "FiltersUnionMember107FilterUnionMember104",
    "FiltersUnionMember107FilterUnionMember105",
    "FiltersUnionMember107FilterUnionMember106",
    "FiltersUnionMember108",
    "FiltersUnionMember108Filter",
    "FiltersUnionMember108FilterUnionMember0",
    "FiltersUnionMember108FilterUnionMember1",
    "FiltersUnionMember108FilterUnionMember2",
    "FiltersUnionMember108FilterUnionMember3",
    "FiltersUnionMember108FilterUnionMember4",
    "FiltersUnionMember108FilterUnionMember5",
    "FiltersUnionMember108FilterUnionMember6",
    "FiltersUnionMember108FilterUnionMember7",
    "FiltersUnionMember108FilterUnionMember8",
    "FiltersUnionMember108FilterUnionMember9",
    "FiltersUnionMember108FilterUnionMember10",
    "FiltersUnionMember108FilterUnionMember11",
    "FiltersUnionMember108FilterUnionMember12",
    "FiltersUnionMember108FilterUnionMember13",
    "FiltersUnionMember108FilterUnionMember14",
    "FiltersUnionMember108FilterUnionMember15",
    "FiltersUnionMember108FilterUnionMember16",
    "FiltersUnionMember108FilterUnionMember17",
    "FiltersUnionMember108FilterUnionMember18",
    "FiltersUnionMember108FilterUnionMember19",
    "FiltersUnionMember108FilterUnionMember20",
    "FiltersUnionMember108FilterUnionMember21",
    "FiltersUnionMember108FilterUnionMember22",
    "FiltersUnionMember108FilterUnionMember23",
    "FiltersUnionMember108FilterUnionMember24",
    "FiltersUnionMember108FilterUnionMember25",
    "FiltersUnionMember108FilterUnionMember26",
    "FiltersUnionMember108FilterUnionMember27",
    "FiltersUnionMember108FilterUnionMember28",
    "FiltersUnionMember108FilterUnionMember29",
    "FiltersUnionMember108FilterUnionMember30",
    "FiltersUnionMember108FilterUnionMember31",
    "FiltersUnionMember108FilterUnionMember32",
    "FiltersUnionMember108FilterUnionMember33",
    "FiltersUnionMember108FilterUnionMember34",
    "FiltersUnionMember108FilterUnionMember35",
    "FiltersUnionMember108FilterUnionMember36",
    "FiltersUnionMember108FilterUnionMember37",
    "FiltersUnionMember108FilterUnionMember38",
    "FiltersUnionMember108FilterUnionMember39",
    "FiltersUnionMember108FilterUnionMember40",
    "FiltersUnionMember108FilterUnionMember41",
    "FiltersUnionMember108FilterUnionMember42",
    "FiltersUnionMember108FilterUnionMember43",
    "FiltersUnionMember108FilterUnionMember44",
    "FiltersUnionMember108FilterUnionMember45",
    "FiltersUnionMember108FilterUnionMember46",
    "FiltersUnionMember108FilterUnionMember47",
    "FiltersUnionMember108FilterUnionMember48",
    "FiltersUnionMember108FilterUnionMember49",
    "FiltersUnionMember108FilterUnionMember50",
    "FiltersUnionMember108FilterUnionMember51",
    "FiltersUnionMember108FilterUnionMember52",
    "FiltersUnionMember108FilterUnionMember53",
    "FiltersUnionMember108FilterUnionMember54",
    "FiltersUnionMember108FilterUnionMember55",
    "FiltersUnionMember108FilterUnionMember56",
    "FiltersUnionMember108FilterUnionMember57",
    "FiltersUnionMember108FilterUnionMember58",
    "FiltersUnionMember108FilterUnionMember59",
    "FiltersUnionMember108FilterUnionMember60",
    "FiltersUnionMember108FilterUnionMember61",
    "FiltersUnionMember108FilterUnionMember62",
    "FiltersUnionMember108FilterUnionMember63",
    "FiltersUnionMember108FilterUnionMember64",
    "FiltersUnionMember108FilterUnionMember65",
    "FiltersUnionMember108FilterUnionMember66",
    "FiltersUnionMember108FilterUnionMember67",
    "FiltersUnionMember108FilterUnionMember68",
    "FiltersUnionMember108FilterUnionMember69",
    "FiltersUnionMember108FilterUnionMember70",
    "FiltersUnionMember108FilterUnionMember71",
    "FiltersUnionMember108FilterUnionMember72",
    "FiltersUnionMember108FilterUnionMember73",
    "FiltersUnionMember108FilterUnionMember74",
    "FiltersUnionMember108FilterUnionMember75",
    "FiltersUnionMember108FilterUnionMember76",
    "FiltersUnionMember108FilterUnionMember77",
    "FiltersUnionMember108FilterUnionMember78",
    "FiltersUnionMember108FilterUnionMember79",
    "FiltersUnionMember108FilterUnionMember80",
    "FiltersUnionMember108FilterUnionMember81",
    "FiltersUnionMember108FilterUnionMember82",
    "FiltersUnionMember108FilterUnionMember83",
    "FiltersUnionMember108FilterUnionMember84",
    "FiltersUnionMember108FilterUnionMember85",
    "FiltersUnionMember108FilterUnionMember86",
    "FiltersUnionMember108FilterUnionMember87",
    "FiltersUnionMember108FilterUnionMember88",
    "FiltersUnionMember108FilterUnionMember89",
    "FiltersUnionMember108FilterUnionMember90",
    "FiltersUnionMember108FilterUnionMember91",
    "FiltersUnionMember108FilterUnionMember92",
    "FiltersUnionMember108FilterUnionMember93",
    "FiltersUnionMember108FilterUnionMember94",
    "FiltersUnionMember108FilterUnionMember95",
    "FiltersUnionMember108FilterUnionMember96",
    "FiltersUnionMember108FilterUnionMember97",
    "FiltersUnionMember108FilterUnionMember98",
    "FiltersUnionMember108FilterUnionMember99",
    "FiltersUnionMember108FilterUnionMember100",
    "FiltersUnionMember108FilterUnionMember101",
    "FiltersUnionMember108FilterUnionMember102",
    "FiltersUnionMember108FilterUnionMember103",
    "FiltersUnionMember108FilterUnionMember104",
    "FiltersUnionMember108FilterUnionMember105",
    "FiltersUnionMember108FilterUnionMember106",
    "FiltersUnionMember108FilterUnionMember107",
    "FiltersUnionMember108FilterUnionMember107Filter",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember0",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember1",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember2",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember3",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember4",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember5",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember6",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember7",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember8",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember9",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember10",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember11",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember12",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember13",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember14",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember15",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember16",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember17",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember18",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember19",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember20",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember21",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember22",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember23",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember24",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember25",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember26",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember27",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember28",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember29",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember30",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember31",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember32",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember33",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember34",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember35",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember36",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember37",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember38",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember39",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember40",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember41",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember42",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember43",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember44",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember45",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember46",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember47",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember48",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember49",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember50",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember51",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember52",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember53",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember54",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember55",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember56",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember57",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember58",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember59",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember60",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember61",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember62",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember63",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember64",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember65",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember66",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember67",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember68",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember69",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember70",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember71",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember72",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember73",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember74",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember75",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember76",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember77",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember78",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember79",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember80",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember81",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember82",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember83",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember84",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember85",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember86",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember87",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember88",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember89",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember90",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember91",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember92",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember93",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember94",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember95",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember96",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember97",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember98",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember99",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember100",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember101",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember102",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember103",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember104",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember105",
    "FiltersUnionMember108FilterUnionMember107FilterUnionMember106",
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
    "RankBy",
    "RankByAttr",
    "RankByConst",
    "RankBySum",
    "RankBySumExpr",
    "RankBySumExprUnionMember0",
    "RankBySumExprUnionMember1",
    "RankBySumExprUnionMember2",
    "RankBySumExprUnionMember2Expr",
    "RankBySumExprUnionMember2ExprUnionMember0",
    "RankBySumExprUnionMember2ExprUnionMember1",
    "RankBySumExprUnionMember2ExprUnionMember2",
    "RankBySumExprUnionMember2ExprUnionMember2Expr",
    "RankBySumExprUnionMember2ExprUnionMember2ExprUnionMember0",
    "RankBySumExprUnionMember2ExprUnionMember2ExprUnionMember1",
    "RankBySumExprUnionMember2ExprUnionMember3",
    "RankBySumExprUnionMember2ExprUnionMember3Expr",
    "RankBySumExprUnionMember2ExprUnionMember3ExprUnionMember0",
    "RankBySumExprUnionMember2ExprUnionMember3ExprUnionMember1",
    "RankBySumExprUnionMember2ExprUnionMember4",
    "RankBySumExprUnionMember2ExprUnionMember4Expr",
    "RankBySumExprUnionMember2ExprUnionMember4ExprUnionMember0",
    "RankBySumExprUnionMember2ExprUnionMember4ExprUnionMember1",
    "RankBySumExprUnionMember2ExprUnionMember5",
    "RankBySumExprUnionMember2ExprUnionMember5Expr",
    "RankBySumExprUnionMember2ExprUnionMember5ExprUnionMember0",
    "RankBySumExprUnionMember2ExprUnionMember5ExprUnionMember1",
    "RankBySumExprUnionMember2ExprUnionMember6",
    "RankBySumExprUnionMember2ExprUnionMember6Expr",
    "RankBySumExprUnionMember2ExprUnionMember6ExprUnionMember0",
    "RankBySumExprUnionMember2ExprUnionMember6ExprUnionMember1",
    "RankBySumExprUnionMember2ExprUnionMember7",
    "RankBySumExprUnionMember2ExprUnionMember7Expr",
    "RankBySumExprUnionMember2ExprUnionMember7ExprUnionMember0",
    "RankBySumExprUnionMember2ExprUnionMember7ExprUnionMember1",
    "RankBySumExprUnionMember3",
    "RankBySumExprUnionMember3Expr",
    "RankBySumExprUnionMember3ExprUnionMember0",
    "RankBySumExprUnionMember3ExprUnionMember1",
    "RankBySumExprUnionMember3ExprUnionMember2",
    "RankBySumExprUnionMember3ExprUnionMember2Expr",
    "RankBySumExprUnionMember3ExprUnionMember2ExprUnionMember0",
    "RankBySumExprUnionMember3ExprUnionMember2ExprUnionMember1",
    "RankBySumExprUnionMember3ExprUnionMember3",
    "RankBySumExprUnionMember3ExprUnionMember3Expr",
    "RankBySumExprUnionMember3ExprUnionMember3ExprUnionMember0",
    "RankBySumExprUnionMember3ExprUnionMember3ExprUnionMember1",
    "RankBySumExprUnionMember3ExprUnionMember4",
    "RankBySumExprUnionMember3ExprUnionMember4Expr",
    "RankBySumExprUnionMember3ExprUnionMember4ExprUnionMember0",
    "RankBySumExprUnionMember3ExprUnionMember4ExprUnionMember1",
    "RankBySumExprUnionMember3ExprUnionMember5",
    "RankBySumExprUnionMember3ExprUnionMember5Expr",
    "RankBySumExprUnionMember3ExprUnionMember5ExprUnionMember0",
    "RankBySumExprUnionMember3ExprUnionMember5ExprUnionMember1",
    "RankBySumExprUnionMember3ExprUnionMember6",
    "RankBySumExprUnionMember3ExprUnionMember6Expr",
    "RankBySumExprUnionMember3ExprUnionMember6ExprUnionMember0",
    "RankBySumExprUnionMember3ExprUnionMember6ExprUnionMember1",
    "RankBySumExprUnionMember3ExprUnionMember7",
    "RankBySumExprUnionMember3ExprUnionMember7Expr",
    "RankBySumExprUnionMember3ExprUnionMember7ExprUnionMember0",
    "RankBySumExprUnionMember3ExprUnionMember7ExprUnionMember1",
    "RankBySumExprUnionMember4",
    "RankBySumExprUnionMember4Expr",
    "RankBySumExprUnionMember4ExprUnionMember0",
    "RankBySumExprUnionMember4ExprUnionMember1",
    "RankBySumExprUnionMember4ExprUnionMember2",
    "RankBySumExprUnionMember4ExprUnionMember2Expr",
    "RankBySumExprUnionMember4ExprUnionMember2ExprUnionMember0",
    "RankBySumExprUnionMember4ExprUnionMember2ExprUnionMember1",
    "RankBySumExprUnionMember4ExprUnionMember3",
    "RankBySumExprUnionMember4ExprUnionMember3Expr",
    "RankBySumExprUnionMember4ExprUnionMember3ExprUnionMember0",
    "RankBySumExprUnionMember4ExprUnionMember3ExprUnionMember1",
    "RankBySumExprUnionMember4ExprUnionMember4",
    "RankBySumExprUnionMember4ExprUnionMember4Expr",
    "RankBySumExprUnionMember4ExprUnionMember4ExprUnionMember0",
    "RankBySumExprUnionMember4ExprUnionMember4ExprUnionMember1",
    "RankBySumExprUnionMember4ExprUnionMember5",
    "RankBySumExprUnionMember4ExprUnionMember5Expr",
    "RankBySumExprUnionMember4ExprUnionMember5ExprUnionMember0",
    "RankBySumExprUnionMember4ExprUnionMember5ExprUnionMember1",
    "RankBySumExprUnionMember4ExprUnionMember6",
    "RankBySumExprUnionMember4ExprUnionMember6Expr",
    "RankBySumExprUnionMember4ExprUnionMember6ExprUnionMember0",
    "RankBySumExprUnionMember4ExprUnionMember6ExprUnionMember1",
    "RankBySumExprUnionMember4ExprUnionMember7",
    "RankBySumExprUnionMember4ExprUnionMember7Expr",
    "RankBySumExprUnionMember4ExprUnionMember7ExprUnionMember0",
    "RankBySumExprUnionMember4ExprUnionMember7ExprUnionMember1",
    "RankBySumExprUnionMember5",
    "RankBySumExprUnionMember5Expr",
    "RankBySumExprUnionMember5ExprUnionMember0",
    "RankBySumExprUnionMember5ExprUnionMember1",
    "RankBySumExprUnionMember5ExprUnionMember2",
    "RankBySumExprUnionMember5ExprUnionMember2Expr",
    "RankBySumExprUnionMember5ExprUnionMember2ExprUnionMember0",
    "RankBySumExprUnionMember5ExprUnionMember2ExprUnionMember1",
    "RankBySumExprUnionMember5ExprUnionMember3",
    "RankBySumExprUnionMember5ExprUnionMember3Expr",
    "RankBySumExprUnionMember5ExprUnionMember3ExprUnionMember0",
    "RankBySumExprUnionMember5ExprUnionMember3ExprUnionMember1",
    "RankBySumExprUnionMember5ExprUnionMember4",
    "RankBySumExprUnionMember5ExprUnionMember4Expr",
    "RankBySumExprUnionMember5ExprUnionMember4ExprUnionMember0",
    "RankBySumExprUnionMember5ExprUnionMember4ExprUnionMember1",
    "RankBySumExprUnionMember5ExprUnionMember5",
    "RankBySumExprUnionMember5ExprUnionMember5Expr",
    "RankBySumExprUnionMember5ExprUnionMember5ExprUnionMember0",
    "RankBySumExprUnionMember5ExprUnionMember5ExprUnionMember1",
    "RankBySumExprUnionMember5ExprUnionMember6",
    "RankBySumExprUnionMember5ExprUnionMember6Expr",
    "RankBySumExprUnionMember5ExprUnionMember6ExprUnionMember0",
    "RankBySumExprUnionMember5ExprUnionMember6ExprUnionMember1",
    "RankBySumExprUnionMember5ExprUnionMember7",
    "RankBySumExprUnionMember5ExprUnionMember7Expr",
    "RankBySumExprUnionMember5ExprUnionMember7ExprUnionMember0",
    "RankBySumExprUnionMember5ExprUnionMember7ExprUnionMember1",
    "RankBySumExprUnionMember6",
    "RankBySumExprUnionMember6Expr",
    "RankBySumExprUnionMember6ExprUnionMember0",
    "RankBySumExprUnionMember6ExprUnionMember1",
    "RankBySumExprUnionMember6ExprUnionMember2",
    "RankBySumExprUnionMember6ExprUnionMember2Expr",
    "RankBySumExprUnionMember6ExprUnionMember2ExprUnionMember0",
    "RankBySumExprUnionMember6ExprUnionMember2ExprUnionMember1",
    "RankBySumExprUnionMember6ExprUnionMember3",
    "RankBySumExprUnionMember6ExprUnionMember3Expr",
    "RankBySumExprUnionMember6ExprUnionMember3ExprUnionMember0",
    "RankBySumExprUnionMember6ExprUnionMember3ExprUnionMember1",
    "RankBySumExprUnionMember6ExprUnionMember4",
    "RankBySumExprUnionMember6ExprUnionMember4Expr",
    "RankBySumExprUnionMember6ExprUnionMember4ExprUnionMember0",
    "RankBySumExprUnionMember6ExprUnionMember4ExprUnionMember1",
    "RankBySumExprUnionMember6ExprUnionMember5",
    "RankBySumExprUnionMember6ExprUnionMember5Expr",
    "RankBySumExprUnionMember6ExprUnionMember5ExprUnionMember0",
    "RankBySumExprUnionMember6ExprUnionMember5ExprUnionMember1",
    "RankBySumExprUnionMember6ExprUnionMember6",
    "RankBySumExprUnionMember6ExprUnionMember6Expr",
    "RankBySumExprUnionMember6ExprUnionMember6ExprUnionMember0",
    "RankBySumExprUnionMember6ExprUnionMember6ExprUnionMember1",
    "RankBySumExprUnionMember6ExprUnionMember7",
    "RankBySumExprUnionMember6ExprUnionMember7Expr",
    "RankBySumExprUnionMember6ExprUnionMember7ExprUnionMember0",
    "RankBySumExprUnionMember6ExprUnionMember7ExprUnionMember1",
    "RankBySumExprUnionMember7",
    "RankBySumExprUnionMember7Expr",
    "RankBySumExprUnionMember7ExprUnionMember0",
    "RankBySumExprUnionMember7ExprUnionMember1",
    "RankBySumExprUnionMember7ExprUnionMember2",
    "RankBySumExprUnionMember7ExprUnionMember2Expr",
    "RankBySumExprUnionMember7ExprUnionMember2ExprUnionMember0",
    "RankBySumExprUnionMember7ExprUnionMember2ExprUnionMember1",
    "RankBySumExprUnionMember7ExprUnionMember3",
    "RankBySumExprUnionMember7ExprUnionMember3Expr",
    "RankBySumExprUnionMember7ExprUnionMember3ExprUnionMember0",
    "RankBySumExprUnionMember7ExprUnionMember3ExprUnionMember1",
    "RankBySumExprUnionMember7ExprUnionMember4",
    "RankBySumExprUnionMember7ExprUnionMember4Expr",
    "RankBySumExprUnionMember7ExprUnionMember4ExprUnionMember0",
    "RankBySumExprUnionMember7ExprUnionMember4ExprUnionMember1",
    "RankBySumExprUnionMember7ExprUnionMember5",
    "RankBySumExprUnionMember7ExprUnionMember5Expr",
    "RankBySumExprUnionMember7ExprUnionMember5ExprUnionMember0",
    "RankBySumExprUnionMember7ExprUnionMember5ExprUnionMember1",
    "RankBySumExprUnionMember7ExprUnionMember6",
    "RankBySumExprUnionMember7ExprUnionMember6Expr",
    "RankBySumExprUnionMember7ExprUnionMember6ExprUnionMember0",
    "RankBySumExprUnionMember7ExprUnionMember6ExprUnionMember1",
    "RankBySumExprUnionMember7ExprUnionMember7",
    "RankBySumExprUnionMember7ExprUnionMember7Expr",
    "RankBySumExprUnionMember7ExprUnionMember7ExprUnionMember0",
    "RankBySumExprUnionMember7ExprUnionMember7ExprUnionMember1",
    "RankByMult",
    "RankByMultExpr",
    "RankByMultExprUnionMember0",
    "RankByMultExprUnionMember1",
    "RankByMultExprUnionMember2",
    "RankByMultExprUnionMember2Expr",
    "RankByMultExprUnionMember2ExprUnionMember0",
    "RankByMultExprUnionMember2ExprUnionMember1",
    "RankByMultExprUnionMember2ExprUnionMember2",
    "RankByMultExprUnionMember2ExprUnionMember2Expr",
    "RankByMultExprUnionMember2ExprUnionMember2ExprUnionMember0",
    "RankByMultExprUnionMember2ExprUnionMember2ExprUnionMember1",
    "RankByMultExprUnionMember2ExprUnionMember3",
    "RankByMultExprUnionMember2ExprUnionMember3Expr",
    "RankByMultExprUnionMember2ExprUnionMember3ExprUnionMember0",
    "RankByMultExprUnionMember2ExprUnionMember3ExprUnionMember1",
    "RankByMultExprUnionMember2ExprUnionMember4",
    "RankByMultExprUnionMember2ExprUnionMember4Expr",
    "RankByMultExprUnionMember2ExprUnionMember4ExprUnionMember0",
    "RankByMultExprUnionMember2ExprUnionMember4ExprUnionMember1",
    "RankByMultExprUnionMember2ExprUnionMember5",
    "RankByMultExprUnionMember2ExprUnionMember5Expr",
    "RankByMultExprUnionMember2ExprUnionMember5ExprUnionMember0",
    "RankByMultExprUnionMember2ExprUnionMember5ExprUnionMember1",
    "RankByMultExprUnionMember2ExprUnionMember6",
    "RankByMultExprUnionMember2ExprUnionMember6Expr",
    "RankByMultExprUnionMember2ExprUnionMember6ExprUnionMember0",
    "RankByMultExprUnionMember2ExprUnionMember6ExprUnionMember1",
    "RankByMultExprUnionMember2ExprUnionMember7",
    "RankByMultExprUnionMember2ExprUnionMember7Expr",
    "RankByMultExprUnionMember2ExprUnionMember7ExprUnionMember0",
    "RankByMultExprUnionMember2ExprUnionMember7ExprUnionMember1",
    "RankByMultExprUnionMember3",
    "RankByMultExprUnionMember3Expr",
    "RankByMultExprUnionMember3ExprUnionMember0",
    "RankByMultExprUnionMember3ExprUnionMember1",
    "RankByMultExprUnionMember3ExprUnionMember2",
    "RankByMultExprUnionMember3ExprUnionMember2Expr",
    "RankByMultExprUnionMember3ExprUnionMember2ExprUnionMember0",
    "RankByMultExprUnionMember3ExprUnionMember2ExprUnionMember1",
    "RankByMultExprUnionMember3ExprUnionMember3",
    "RankByMultExprUnionMember3ExprUnionMember3Expr",
    "RankByMultExprUnionMember3ExprUnionMember3ExprUnionMember0",
    "RankByMultExprUnionMember3ExprUnionMember3ExprUnionMember1",
    "RankByMultExprUnionMember3ExprUnionMember4",
    "RankByMultExprUnionMember3ExprUnionMember4Expr",
    "RankByMultExprUnionMember3ExprUnionMember4ExprUnionMember0",
    "RankByMultExprUnionMember3ExprUnionMember4ExprUnionMember1",
    "RankByMultExprUnionMember3ExprUnionMember5",
    "RankByMultExprUnionMember3ExprUnionMember5Expr",
    "RankByMultExprUnionMember3ExprUnionMember5ExprUnionMember0",
    "RankByMultExprUnionMember3ExprUnionMember5ExprUnionMember1",
    "RankByMultExprUnionMember3ExprUnionMember6",
    "RankByMultExprUnionMember3ExprUnionMember6Expr",
    "RankByMultExprUnionMember3ExprUnionMember6ExprUnionMember0",
    "RankByMultExprUnionMember3ExprUnionMember6ExprUnionMember1",
    "RankByMultExprUnionMember3ExprUnionMember7",
    "RankByMultExprUnionMember3ExprUnionMember7Expr",
    "RankByMultExprUnionMember3ExprUnionMember7ExprUnionMember0",
    "RankByMultExprUnionMember3ExprUnionMember7ExprUnionMember1",
    "RankByMultExprUnionMember4",
    "RankByMultExprUnionMember4Expr",
    "RankByMultExprUnionMember4ExprUnionMember0",
    "RankByMultExprUnionMember4ExprUnionMember1",
    "RankByMultExprUnionMember4ExprUnionMember2",
    "RankByMultExprUnionMember4ExprUnionMember2Expr",
    "RankByMultExprUnionMember4ExprUnionMember2ExprUnionMember0",
    "RankByMultExprUnionMember4ExprUnionMember2ExprUnionMember1",
    "RankByMultExprUnionMember4ExprUnionMember3",
    "RankByMultExprUnionMember4ExprUnionMember3Expr",
    "RankByMultExprUnionMember4ExprUnionMember3ExprUnionMember0",
    "RankByMultExprUnionMember4ExprUnionMember3ExprUnionMember1",
    "RankByMultExprUnionMember4ExprUnionMember4",
    "RankByMultExprUnionMember4ExprUnionMember4Expr",
    "RankByMultExprUnionMember4ExprUnionMember4ExprUnionMember0",
    "RankByMultExprUnionMember4ExprUnionMember4ExprUnionMember1",
    "RankByMultExprUnionMember4ExprUnionMember5",
    "RankByMultExprUnionMember4ExprUnionMember5Expr",
    "RankByMultExprUnionMember4ExprUnionMember5ExprUnionMember0",
    "RankByMultExprUnionMember4ExprUnionMember5ExprUnionMember1",
    "RankByMultExprUnionMember4ExprUnionMember6",
    "RankByMultExprUnionMember4ExprUnionMember6Expr",
    "RankByMultExprUnionMember4ExprUnionMember6ExprUnionMember0",
    "RankByMultExprUnionMember4ExprUnionMember6ExprUnionMember1",
    "RankByMultExprUnionMember4ExprUnionMember7",
    "RankByMultExprUnionMember4ExprUnionMember7Expr",
    "RankByMultExprUnionMember4ExprUnionMember7ExprUnionMember0",
    "RankByMultExprUnionMember4ExprUnionMember7ExprUnionMember1",
    "RankByMultExprUnionMember5",
    "RankByMultExprUnionMember5Expr",
    "RankByMultExprUnionMember5ExprUnionMember0",
    "RankByMultExprUnionMember5ExprUnionMember1",
    "RankByMultExprUnionMember5ExprUnionMember2",
    "RankByMultExprUnionMember5ExprUnionMember2Expr",
    "RankByMultExprUnionMember5ExprUnionMember2ExprUnionMember0",
    "RankByMultExprUnionMember5ExprUnionMember2ExprUnionMember1",
    "RankByMultExprUnionMember5ExprUnionMember3",
    "RankByMultExprUnionMember5ExprUnionMember3Expr",
    "RankByMultExprUnionMember5ExprUnionMember3ExprUnionMember0",
    "RankByMultExprUnionMember5ExprUnionMember3ExprUnionMember1",
    "RankByMultExprUnionMember5ExprUnionMember4",
    "RankByMultExprUnionMember5ExprUnionMember4Expr",
    "RankByMultExprUnionMember5ExprUnionMember4ExprUnionMember0",
    "RankByMultExprUnionMember5ExprUnionMember4ExprUnionMember1",
    "RankByMultExprUnionMember5ExprUnionMember5",
    "RankByMultExprUnionMember5ExprUnionMember5Expr",
    "RankByMultExprUnionMember5ExprUnionMember5ExprUnionMember0",
    "RankByMultExprUnionMember5ExprUnionMember5ExprUnionMember1",
    "RankByMultExprUnionMember5ExprUnionMember6",
    "RankByMultExprUnionMember5ExprUnionMember6Expr",
    "RankByMultExprUnionMember5ExprUnionMember6ExprUnionMember0",
    "RankByMultExprUnionMember5ExprUnionMember6ExprUnionMember1",
    "RankByMultExprUnionMember5ExprUnionMember7",
    "RankByMultExprUnionMember5ExprUnionMember7Expr",
    "RankByMultExprUnionMember5ExprUnionMember7ExprUnionMember0",
    "RankByMultExprUnionMember5ExprUnionMember7ExprUnionMember1",
    "RankByMultExprUnionMember6",
    "RankByMultExprUnionMember6Expr",
    "RankByMultExprUnionMember6ExprUnionMember0",
    "RankByMultExprUnionMember6ExprUnionMember1",
    "RankByMultExprUnionMember6ExprUnionMember2",
    "RankByMultExprUnionMember6ExprUnionMember2Expr",
    "RankByMultExprUnionMember6ExprUnionMember2ExprUnionMember0",
    "RankByMultExprUnionMember6ExprUnionMember2ExprUnionMember1",
    "RankByMultExprUnionMember6ExprUnionMember3",
    "RankByMultExprUnionMember6ExprUnionMember3Expr",
    "RankByMultExprUnionMember6ExprUnionMember3ExprUnionMember0",
    "RankByMultExprUnionMember6ExprUnionMember3ExprUnionMember1",
    "RankByMultExprUnionMember6ExprUnionMember4",
    "RankByMultExprUnionMember6ExprUnionMember4Expr",
    "RankByMultExprUnionMember6ExprUnionMember4ExprUnionMember0",
    "RankByMultExprUnionMember6ExprUnionMember4ExprUnionMember1",
    "RankByMultExprUnionMember6ExprUnionMember5",
    "RankByMultExprUnionMember6ExprUnionMember5Expr",
    "RankByMultExprUnionMember6ExprUnionMember5ExprUnionMember0",
    "RankByMultExprUnionMember6ExprUnionMember5ExprUnionMember1",
    "RankByMultExprUnionMember6ExprUnionMember6",
    "RankByMultExprUnionMember6ExprUnionMember6Expr",
    "RankByMultExprUnionMember6ExprUnionMember6ExprUnionMember0",
    "RankByMultExprUnionMember6ExprUnionMember6ExprUnionMember1",
    "RankByMultExprUnionMember6ExprUnionMember7",
    "RankByMultExprUnionMember6ExprUnionMember7Expr",
    "RankByMultExprUnionMember6ExprUnionMember7ExprUnionMember0",
    "RankByMultExprUnionMember6ExprUnionMember7ExprUnionMember1",
    "RankByMultExprUnionMember7",
    "RankByMultExprUnionMember7Expr",
    "RankByMultExprUnionMember7ExprUnionMember0",
    "RankByMultExprUnionMember7ExprUnionMember1",
    "RankByMultExprUnionMember7ExprUnionMember2",
    "RankByMultExprUnionMember7ExprUnionMember2Expr",
    "RankByMultExprUnionMember7ExprUnionMember2ExprUnionMember0",
    "RankByMultExprUnionMember7ExprUnionMember2ExprUnionMember1",
    "RankByMultExprUnionMember7ExprUnionMember3",
    "RankByMultExprUnionMember7ExprUnionMember3Expr",
    "RankByMultExprUnionMember7ExprUnionMember3ExprUnionMember0",
    "RankByMultExprUnionMember7ExprUnionMember3ExprUnionMember1",
    "RankByMultExprUnionMember7ExprUnionMember4",
    "RankByMultExprUnionMember7ExprUnionMember4Expr",
    "RankByMultExprUnionMember7ExprUnionMember4ExprUnionMember0",
    "RankByMultExprUnionMember7ExprUnionMember4ExprUnionMember1",
    "RankByMultExprUnionMember7ExprUnionMember5",
    "RankByMultExprUnionMember7ExprUnionMember5Expr",
    "RankByMultExprUnionMember7ExprUnionMember5ExprUnionMember0",
    "RankByMultExprUnionMember7ExprUnionMember5ExprUnionMember1",
    "RankByMultExprUnionMember7ExprUnionMember6",
    "RankByMultExprUnionMember7ExprUnionMember6Expr",
    "RankByMultExprUnionMember7ExprUnionMember6ExprUnionMember0",
    "RankByMultExprUnionMember7ExprUnionMember6ExprUnionMember1",
    "RankByMultExprUnionMember7ExprUnionMember7",
    "RankByMultExprUnionMember7ExprUnionMember7Expr",
    "RankByMultExprUnionMember7ExprUnionMember7ExprUnionMember0",
    "RankByMultExprUnionMember7ExprUnionMember7ExprUnionMember1",
    "RankByDiv",
    "RankByDivExpr",
    "RankByDivExprUnionMember0",
    "RankByDivExprUnionMember1",
    "RankByDivExprUnionMember2",
    "RankByDivExprUnionMember2Expr",
    "RankByDivExprUnionMember2ExprUnionMember0",
    "RankByDivExprUnionMember2ExprUnionMember1",
    "RankByDivExprUnionMember2ExprUnionMember2",
    "RankByDivExprUnionMember2ExprUnionMember2Expr",
    "RankByDivExprUnionMember2ExprUnionMember2ExprUnionMember0",
    "RankByDivExprUnionMember2ExprUnionMember2ExprUnionMember1",
    "RankByDivExprUnionMember2ExprUnionMember3",
    "RankByDivExprUnionMember2ExprUnionMember3Expr",
    "RankByDivExprUnionMember2ExprUnionMember3ExprUnionMember0",
    "RankByDivExprUnionMember2ExprUnionMember3ExprUnionMember1",
    "RankByDivExprUnionMember2ExprUnionMember4",
    "RankByDivExprUnionMember2ExprUnionMember4Expr",
    "RankByDivExprUnionMember2ExprUnionMember4ExprUnionMember0",
    "RankByDivExprUnionMember2ExprUnionMember4ExprUnionMember1",
    "RankByDivExprUnionMember2ExprUnionMember5",
    "RankByDivExprUnionMember2ExprUnionMember5Expr",
    "RankByDivExprUnionMember2ExprUnionMember5ExprUnionMember0",
    "RankByDivExprUnionMember2ExprUnionMember5ExprUnionMember1",
    "RankByDivExprUnionMember2ExprUnionMember6",
    "RankByDivExprUnionMember2ExprUnionMember6Expr",
    "RankByDivExprUnionMember2ExprUnionMember6ExprUnionMember0",
    "RankByDivExprUnionMember2ExprUnionMember6ExprUnionMember1",
    "RankByDivExprUnionMember2ExprUnionMember7",
    "RankByDivExprUnionMember2ExprUnionMember7Expr",
    "RankByDivExprUnionMember2ExprUnionMember7ExprUnionMember0",
    "RankByDivExprUnionMember2ExprUnionMember7ExprUnionMember1",
    "RankByDivExprUnionMember3",
    "RankByDivExprUnionMember3Expr",
    "RankByDivExprUnionMember3ExprUnionMember0",
    "RankByDivExprUnionMember3ExprUnionMember1",
    "RankByDivExprUnionMember3ExprUnionMember2",
    "RankByDivExprUnionMember3ExprUnionMember2Expr",
    "RankByDivExprUnionMember3ExprUnionMember2ExprUnionMember0",
    "RankByDivExprUnionMember3ExprUnionMember2ExprUnionMember1",
    "RankByDivExprUnionMember3ExprUnionMember3",
    "RankByDivExprUnionMember3ExprUnionMember3Expr",
    "RankByDivExprUnionMember3ExprUnionMember3ExprUnionMember0",
    "RankByDivExprUnionMember3ExprUnionMember3ExprUnionMember1",
    "RankByDivExprUnionMember3ExprUnionMember4",
    "RankByDivExprUnionMember3ExprUnionMember4Expr",
    "RankByDivExprUnionMember3ExprUnionMember4ExprUnionMember0",
    "RankByDivExprUnionMember3ExprUnionMember4ExprUnionMember1",
    "RankByDivExprUnionMember3ExprUnionMember5",
    "RankByDivExprUnionMember3ExprUnionMember5Expr",
    "RankByDivExprUnionMember3ExprUnionMember5ExprUnionMember0",
    "RankByDivExprUnionMember3ExprUnionMember5ExprUnionMember1",
    "RankByDivExprUnionMember3ExprUnionMember6",
    "RankByDivExprUnionMember3ExprUnionMember6Expr",
    "RankByDivExprUnionMember3ExprUnionMember6ExprUnionMember0",
    "RankByDivExprUnionMember3ExprUnionMember6ExprUnionMember1",
    "RankByDivExprUnionMember3ExprUnionMember7",
    "RankByDivExprUnionMember3ExprUnionMember7Expr",
    "RankByDivExprUnionMember3ExprUnionMember7ExprUnionMember0",
    "RankByDivExprUnionMember3ExprUnionMember7ExprUnionMember1",
    "RankByDivExprUnionMember4",
    "RankByDivExprUnionMember4Expr",
    "RankByDivExprUnionMember4ExprUnionMember0",
    "RankByDivExprUnionMember4ExprUnionMember1",
    "RankByDivExprUnionMember4ExprUnionMember2",
    "RankByDivExprUnionMember4ExprUnionMember2Expr",
    "RankByDivExprUnionMember4ExprUnionMember2ExprUnionMember0",
    "RankByDivExprUnionMember4ExprUnionMember2ExprUnionMember1",
    "RankByDivExprUnionMember4ExprUnionMember3",
    "RankByDivExprUnionMember4ExprUnionMember3Expr",
    "RankByDivExprUnionMember4ExprUnionMember3ExprUnionMember0",
    "RankByDivExprUnionMember4ExprUnionMember3ExprUnionMember1",
    "RankByDivExprUnionMember4ExprUnionMember4",
    "RankByDivExprUnionMember4ExprUnionMember4Expr",
    "RankByDivExprUnionMember4ExprUnionMember4ExprUnionMember0",
    "RankByDivExprUnionMember4ExprUnionMember4ExprUnionMember1",
    "RankByDivExprUnionMember4ExprUnionMember5",
    "RankByDivExprUnionMember4ExprUnionMember5Expr",
    "RankByDivExprUnionMember4ExprUnionMember5ExprUnionMember0",
    "RankByDivExprUnionMember4ExprUnionMember5ExprUnionMember1",
    "RankByDivExprUnionMember4ExprUnionMember6",
    "RankByDivExprUnionMember4ExprUnionMember6Expr",
    "RankByDivExprUnionMember4ExprUnionMember6ExprUnionMember0",
    "RankByDivExprUnionMember4ExprUnionMember6ExprUnionMember1",
    "RankByDivExprUnionMember4ExprUnionMember7",
    "RankByDivExprUnionMember4ExprUnionMember7Expr",
    "RankByDivExprUnionMember4ExprUnionMember7ExprUnionMember0",
    "RankByDivExprUnionMember4ExprUnionMember7ExprUnionMember1",
    "RankByDivExprUnionMember5",
    "RankByDivExprUnionMember5Expr",
    "RankByDivExprUnionMember5ExprUnionMember0",
    "RankByDivExprUnionMember5ExprUnionMember1",
    "RankByDivExprUnionMember5ExprUnionMember2",
    "RankByDivExprUnionMember5ExprUnionMember2Expr",
    "RankByDivExprUnionMember5ExprUnionMember2ExprUnionMember0",
    "RankByDivExprUnionMember5ExprUnionMember2ExprUnionMember1",
    "RankByDivExprUnionMember5ExprUnionMember3",
    "RankByDivExprUnionMember5ExprUnionMember3Expr",
    "RankByDivExprUnionMember5ExprUnionMember3ExprUnionMember0",
    "RankByDivExprUnionMember5ExprUnionMember3ExprUnionMember1",
    "RankByDivExprUnionMember5ExprUnionMember4",
    "RankByDivExprUnionMember5ExprUnionMember4Expr",
    "RankByDivExprUnionMember5ExprUnionMember4ExprUnionMember0",
    "RankByDivExprUnionMember5ExprUnionMember4ExprUnionMember1",
    "RankByDivExprUnionMember5ExprUnionMember5",
    "RankByDivExprUnionMember5ExprUnionMember5Expr",
    "RankByDivExprUnionMember5ExprUnionMember5ExprUnionMember0",
    "RankByDivExprUnionMember5ExprUnionMember5ExprUnionMember1",
    "RankByDivExprUnionMember5ExprUnionMember6",
    "RankByDivExprUnionMember5ExprUnionMember6Expr",
    "RankByDivExprUnionMember5ExprUnionMember6ExprUnionMember0",
    "RankByDivExprUnionMember5ExprUnionMember6ExprUnionMember1",
    "RankByDivExprUnionMember5ExprUnionMember7",
    "RankByDivExprUnionMember5ExprUnionMember7Expr",
    "RankByDivExprUnionMember5ExprUnionMember7ExprUnionMember0",
    "RankByDivExprUnionMember5ExprUnionMember7ExprUnionMember1",
    "RankByDivExprUnionMember6",
    "RankByDivExprUnionMember6Expr",
    "RankByDivExprUnionMember6ExprUnionMember0",
    "RankByDivExprUnionMember6ExprUnionMember1",
    "RankByDivExprUnionMember6ExprUnionMember2",
    "RankByDivExprUnionMember6ExprUnionMember2Expr",
    "RankByDivExprUnionMember6ExprUnionMember2ExprUnionMember0",
    "RankByDivExprUnionMember6ExprUnionMember2ExprUnionMember1",
    "RankByDivExprUnionMember6ExprUnionMember3",
    "RankByDivExprUnionMember6ExprUnionMember3Expr",
    "RankByDivExprUnionMember6ExprUnionMember3ExprUnionMember0",
    "RankByDivExprUnionMember6ExprUnionMember3ExprUnionMember1",
    "RankByDivExprUnionMember6ExprUnionMember4",
    "RankByDivExprUnionMember6ExprUnionMember4Expr",
    "RankByDivExprUnionMember6ExprUnionMember4ExprUnionMember0",
    "RankByDivExprUnionMember6ExprUnionMember4ExprUnionMember1",
    "RankByDivExprUnionMember6ExprUnionMember5",
    "RankByDivExprUnionMember6ExprUnionMember5Expr",
    "RankByDivExprUnionMember6ExprUnionMember5ExprUnionMember0",
    "RankByDivExprUnionMember6ExprUnionMember5ExprUnionMember1",
    "RankByDivExprUnionMember6ExprUnionMember6",
    "RankByDivExprUnionMember6ExprUnionMember6Expr",
    "RankByDivExprUnionMember6ExprUnionMember6ExprUnionMember0",
    "RankByDivExprUnionMember6ExprUnionMember6ExprUnionMember1",
    "RankByDivExprUnionMember6ExprUnionMember7",
    "RankByDivExprUnionMember6ExprUnionMember7Expr",
    "RankByDivExprUnionMember6ExprUnionMember7ExprUnionMember0",
    "RankByDivExprUnionMember6ExprUnionMember7ExprUnionMember1",
    "RankByDivExprUnionMember7",
    "RankByDivExprUnionMember7Expr",
    "RankByDivExprUnionMember7ExprUnionMember0",
    "RankByDivExprUnionMember7ExprUnionMember1",
    "RankByDivExprUnionMember7ExprUnionMember2",
    "RankByDivExprUnionMember7ExprUnionMember2Expr",
    "RankByDivExprUnionMember7ExprUnionMember2ExprUnionMember0",
    "RankByDivExprUnionMember7ExprUnionMember2ExprUnionMember1",
    "RankByDivExprUnionMember7ExprUnionMember3",
    "RankByDivExprUnionMember7ExprUnionMember3Expr",
    "RankByDivExprUnionMember7ExprUnionMember3ExprUnionMember0",
    "RankByDivExprUnionMember7ExprUnionMember3ExprUnionMember1",
    "RankByDivExprUnionMember7ExprUnionMember4",
    "RankByDivExprUnionMember7ExprUnionMember4Expr",
    "RankByDivExprUnionMember7ExprUnionMember4ExprUnionMember0",
    "RankByDivExprUnionMember7ExprUnionMember4ExprUnionMember1",
    "RankByDivExprUnionMember7ExprUnionMember5",
    "RankByDivExprUnionMember7ExprUnionMember5Expr",
    "RankByDivExprUnionMember7ExprUnionMember5ExprUnionMember0",
    "RankByDivExprUnionMember7ExprUnionMember5ExprUnionMember1",
    "RankByDivExprUnionMember7ExprUnionMember6",
    "RankByDivExprUnionMember7ExprUnionMember6Expr",
    "RankByDivExprUnionMember7ExprUnionMember6ExprUnionMember0",
    "RankByDivExprUnionMember7ExprUnionMember6ExprUnionMember1",
    "RankByDivExprUnionMember7ExprUnionMember7",
    "RankByDivExprUnionMember7ExprUnionMember7Expr",
    "RankByDivExprUnionMember7ExprUnionMember7ExprUnionMember0",
    "RankByDivExprUnionMember7ExprUnionMember7ExprUnionMember1",
    "RankByMax",
    "RankByMaxExpr",
    "RankByMaxExprUnionMember0",
    "RankByMaxExprUnionMember1",
    "RankByMaxExprUnionMember2",
    "RankByMaxExprUnionMember2Expr",
    "RankByMaxExprUnionMember2ExprUnionMember0",
    "RankByMaxExprUnionMember2ExprUnionMember1",
    "RankByMaxExprUnionMember2ExprUnionMember2",
    "RankByMaxExprUnionMember2ExprUnionMember2Expr",
    "RankByMaxExprUnionMember2ExprUnionMember2ExprUnionMember0",
    "RankByMaxExprUnionMember2ExprUnionMember2ExprUnionMember1",
    "RankByMaxExprUnionMember2ExprUnionMember3",
    "RankByMaxExprUnionMember2ExprUnionMember3Expr",
    "RankByMaxExprUnionMember2ExprUnionMember3ExprUnionMember0",
    "RankByMaxExprUnionMember2ExprUnionMember3ExprUnionMember1",
    "RankByMaxExprUnionMember2ExprUnionMember4",
    "RankByMaxExprUnionMember2ExprUnionMember4Expr",
    "RankByMaxExprUnionMember2ExprUnionMember4ExprUnionMember0",
    "RankByMaxExprUnionMember2ExprUnionMember4ExprUnionMember1",
    "RankByMaxExprUnionMember2ExprUnionMember5",
    "RankByMaxExprUnionMember2ExprUnionMember5Expr",
    "RankByMaxExprUnionMember2ExprUnionMember5ExprUnionMember0",
    "RankByMaxExprUnionMember2ExprUnionMember5ExprUnionMember1",
    "RankByMaxExprUnionMember2ExprUnionMember6",
    "RankByMaxExprUnionMember2ExprUnionMember6Expr",
    "RankByMaxExprUnionMember2ExprUnionMember6ExprUnionMember0",
    "RankByMaxExprUnionMember2ExprUnionMember6ExprUnionMember1",
    "RankByMaxExprUnionMember2ExprUnionMember7",
    "RankByMaxExprUnionMember2ExprUnionMember7Expr",
    "RankByMaxExprUnionMember2ExprUnionMember7ExprUnionMember0",
    "RankByMaxExprUnionMember2ExprUnionMember7ExprUnionMember1",
    "RankByMaxExprUnionMember3",
    "RankByMaxExprUnionMember3Expr",
    "RankByMaxExprUnionMember3ExprUnionMember0",
    "RankByMaxExprUnionMember3ExprUnionMember1",
    "RankByMaxExprUnionMember3ExprUnionMember2",
    "RankByMaxExprUnionMember3ExprUnionMember2Expr",
    "RankByMaxExprUnionMember3ExprUnionMember2ExprUnionMember0",
    "RankByMaxExprUnionMember3ExprUnionMember2ExprUnionMember1",
    "RankByMaxExprUnionMember3ExprUnionMember3",
    "RankByMaxExprUnionMember3ExprUnionMember3Expr",
    "RankByMaxExprUnionMember3ExprUnionMember3ExprUnionMember0",
    "RankByMaxExprUnionMember3ExprUnionMember3ExprUnionMember1",
    "RankByMaxExprUnionMember3ExprUnionMember4",
    "RankByMaxExprUnionMember3ExprUnionMember4Expr",
    "RankByMaxExprUnionMember3ExprUnionMember4ExprUnionMember0",
    "RankByMaxExprUnionMember3ExprUnionMember4ExprUnionMember1",
    "RankByMaxExprUnionMember3ExprUnionMember5",
    "RankByMaxExprUnionMember3ExprUnionMember5Expr",
    "RankByMaxExprUnionMember3ExprUnionMember5ExprUnionMember0",
    "RankByMaxExprUnionMember3ExprUnionMember5ExprUnionMember1",
    "RankByMaxExprUnionMember3ExprUnionMember6",
    "RankByMaxExprUnionMember3ExprUnionMember6Expr",
    "RankByMaxExprUnionMember3ExprUnionMember6ExprUnionMember0",
    "RankByMaxExprUnionMember3ExprUnionMember6ExprUnionMember1",
    "RankByMaxExprUnionMember3ExprUnionMember7",
    "RankByMaxExprUnionMember3ExprUnionMember7Expr",
    "RankByMaxExprUnionMember3ExprUnionMember7ExprUnionMember0",
    "RankByMaxExprUnionMember3ExprUnionMember7ExprUnionMember1",
    "RankByMaxExprUnionMember4",
    "RankByMaxExprUnionMember4Expr",
    "RankByMaxExprUnionMember4ExprUnionMember0",
    "RankByMaxExprUnionMember4ExprUnionMember1",
    "RankByMaxExprUnionMember4ExprUnionMember2",
    "RankByMaxExprUnionMember4ExprUnionMember2Expr",
    "RankByMaxExprUnionMember4ExprUnionMember2ExprUnionMember0",
    "RankByMaxExprUnionMember4ExprUnionMember2ExprUnionMember1",
    "RankByMaxExprUnionMember4ExprUnionMember3",
    "RankByMaxExprUnionMember4ExprUnionMember3Expr",
    "RankByMaxExprUnionMember4ExprUnionMember3ExprUnionMember0",
    "RankByMaxExprUnionMember4ExprUnionMember3ExprUnionMember1",
    "RankByMaxExprUnionMember4ExprUnionMember4",
    "RankByMaxExprUnionMember4ExprUnionMember4Expr",
    "RankByMaxExprUnionMember4ExprUnionMember4ExprUnionMember0",
    "RankByMaxExprUnionMember4ExprUnionMember4ExprUnionMember1",
    "RankByMaxExprUnionMember4ExprUnionMember5",
    "RankByMaxExprUnionMember4ExprUnionMember5Expr",
    "RankByMaxExprUnionMember4ExprUnionMember5ExprUnionMember0",
    "RankByMaxExprUnionMember4ExprUnionMember5ExprUnionMember1",
    "RankByMaxExprUnionMember4ExprUnionMember6",
    "RankByMaxExprUnionMember4ExprUnionMember6Expr",
    "RankByMaxExprUnionMember4ExprUnionMember6ExprUnionMember0",
    "RankByMaxExprUnionMember4ExprUnionMember6ExprUnionMember1",
    "RankByMaxExprUnionMember4ExprUnionMember7",
    "RankByMaxExprUnionMember4ExprUnionMember7Expr",
    "RankByMaxExprUnionMember4ExprUnionMember7ExprUnionMember0",
    "RankByMaxExprUnionMember4ExprUnionMember7ExprUnionMember1",
    "RankByMaxExprUnionMember5",
    "RankByMaxExprUnionMember5Expr",
    "RankByMaxExprUnionMember5ExprUnionMember0",
    "RankByMaxExprUnionMember5ExprUnionMember1",
    "RankByMaxExprUnionMember5ExprUnionMember2",
    "RankByMaxExprUnionMember5ExprUnionMember2Expr",
    "RankByMaxExprUnionMember5ExprUnionMember2ExprUnionMember0",
    "RankByMaxExprUnionMember5ExprUnionMember2ExprUnionMember1",
    "RankByMaxExprUnionMember5ExprUnionMember3",
    "RankByMaxExprUnionMember5ExprUnionMember3Expr",
    "RankByMaxExprUnionMember5ExprUnionMember3ExprUnionMember0",
    "RankByMaxExprUnionMember5ExprUnionMember3ExprUnionMember1",
    "RankByMaxExprUnionMember5ExprUnionMember4",
    "RankByMaxExprUnionMember5ExprUnionMember4Expr",
    "RankByMaxExprUnionMember5ExprUnionMember4ExprUnionMember0",
    "RankByMaxExprUnionMember5ExprUnionMember4ExprUnionMember1",
    "RankByMaxExprUnionMember5ExprUnionMember5",
    "RankByMaxExprUnionMember5ExprUnionMember5Expr",
    "RankByMaxExprUnionMember5ExprUnionMember5ExprUnionMember0",
    "RankByMaxExprUnionMember5ExprUnionMember5ExprUnionMember1",
    "RankByMaxExprUnionMember5ExprUnionMember6",
    "RankByMaxExprUnionMember5ExprUnionMember6Expr",
    "RankByMaxExprUnionMember5ExprUnionMember6ExprUnionMember0",
    "RankByMaxExprUnionMember5ExprUnionMember6ExprUnionMember1",
    "RankByMaxExprUnionMember5ExprUnionMember7",
    "RankByMaxExprUnionMember5ExprUnionMember7Expr",
    "RankByMaxExprUnionMember5ExprUnionMember7ExprUnionMember0",
    "RankByMaxExprUnionMember5ExprUnionMember7ExprUnionMember1",
    "RankByMaxExprUnionMember6",
    "RankByMaxExprUnionMember6Expr",
    "RankByMaxExprUnionMember6ExprUnionMember0",
    "RankByMaxExprUnionMember6ExprUnionMember1",
    "RankByMaxExprUnionMember6ExprUnionMember2",
    "RankByMaxExprUnionMember6ExprUnionMember2Expr",
    "RankByMaxExprUnionMember6ExprUnionMember2ExprUnionMember0",
    "RankByMaxExprUnionMember6ExprUnionMember2ExprUnionMember1",
    "RankByMaxExprUnionMember6ExprUnionMember3",
    "RankByMaxExprUnionMember6ExprUnionMember3Expr",
    "RankByMaxExprUnionMember6ExprUnionMember3ExprUnionMember0",
    "RankByMaxExprUnionMember6ExprUnionMember3ExprUnionMember1",
    "RankByMaxExprUnionMember6ExprUnionMember4",
    "RankByMaxExprUnionMember6ExprUnionMember4Expr",
    "RankByMaxExprUnionMember6ExprUnionMember4ExprUnionMember0",
    "RankByMaxExprUnionMember6ExprUnionMember4ExprUnionMember1",
    "RankByMaxExprUnionMember6ExprUnionMember5",
    "RankByMaxExprUnionMember6ExprUnionMember5Expr",
    "RankByMaxExprUnionMember6ExprUnionMember5ExprUnionMember0",
    "RankByMaxExprUnionMember6ExprUnionMember5ExprUnionMember1",
    "RankByMaxExprUnionMember6ExprUnionMember6",
    "RankByMaxExprUnionMember6ExprUnionMember6Expr",
    "RankByMaxExprUnionMember6ExprUnionMember6ExprUnionMember0",
    "RankByMaxExprUnionMember6ExprUnionMember6ExprUnionMember1",
    "RankByMaxExprUnionMember6ExprUnionMember7",
    "RankByMaxExprUnionMember6ExprUnionMember7Expr",
    "RankByMaxExprUnionMember6ExprUnionMember7ExprUnionMember0",
    "RankByMaxExprUnionMember6ExprUnionMember7ExprUnionMember1",
    "RankByMaxExprUnionMember7",
    "RankByMaxExprUnionMember7Expr",
    "RankByMaxExprUnionMember7ExprUnionMember0",
    "RankByMaxExprUnionMember7ExprUnionMember1",
    "RankByMaxExprUnionMember7ExprUnionMember2",
    "RankByMaxExprUnionMember7ExprUnionMember2Expr",
    "RankByMaxExprUnionMember7ExprUnionMember2ExprUnionMember0",
    "RankByMaxExprUnionMember7ExprUnionMember2ExprUnionMember1",
    "RankByMaxExprUnionMember7ExprUnionMember3",
    "RankByMaxExprUnionMember7ExprUnionMember3Expr",
    "RankByMaxExprUnionMember7ExprUnionMember3ExprUnionMember0",
    "RankByMaxExprUnionMember7ExprUnionMember3ExprUnionMember1",
    "RankByMaxExprUnionMember7ExprUnionMember4",
    "RankByMaxExprUnionMember7ExprUnionMember4Expr",
    "RankByMaxExprUnionMember7ExprUnionMember4ExprUnionMember0",
    "RankByMaxExprUnionMember7ExprUnionMember4ExprUnionMember1",
    "RankByMaxExprUnionMember7ExprUnionMember5",
    "RankByMaxExprUnionMember7ExprUnionMember5Expr",
    "RankByMaxExprUnionMember7ExprUnionMember5ExprUnionMember0",
    "RankByMaxExprUnionMember7ExprUnionMember5ExprUnionMember1",
    "RankByMaxExprUnionMember7ExprUnionMember6",
    "RankByMaxExprUnionMember7ExprUnionMember6Expr",
    "RankByMaxExprUnionMember7ExprUnionMember6ExprUnionMember0",
    "RankByMaxExprUnionMember7ExprUnionMember6ExprUnionMember1",
    "RankByMaxExprUnionMember7ExprUnionMember7",
    "RankByMaxExprUnionMember7ExprUnionMember7Expr",
    "RankByMaxExprUnionMember7ExprUnionMember7ExprUnionMember0",
    "RankByMaxExprUnionMember7ExprUnionMember7ExprUnionMember1",
    "RankByMin",
    "RankByMinExpr",
    "RankByMinExprUnionMember0",
    "RankByMinExprUnionMember1",
    "RankByMinExprUnionMember2",
    "RankByMinExprUnionMember2Expr",
    "RankByMinExprUnionMember2ExprUnionMember0",
    "RankByMinExprUnionMember2ExprUnionMember1",
    "RankByMinExprUnionMember2ExprUnionMember2",
    "RankByMinExprUnionMember2ExprUnionMember2Expr",
    "RankByMinExprUnionMember2ExprUnionMember2ExprUnionMember0",
    "RankByMinExprUnionMember2ExprUnionMember2ExprUnionMember1",
    "RankByMinExprUnionMember2ExprUnionMember3",
    "RankByMinExprUnionMember2ExprUnionMember3Expr",
    "RankByMinExprUnionMember2ExprUnionMember3ExprUnionMember0",
    "RankByMinExprUnionMember2ExprUnionMember3ExprUnionMember1",
    "RankByMinExprUnionMember2ExprUnionMember4",
    "RankByMinExprUnionMember2ExprUnionMember4Expr",
    "RankByMinExprUnionMember2ExprUnionMember4ExprUnionMember0",
    "RankByMinExprUnionMember2ExprUnionMember4ExprUnionMember1",
    "RankByMinExprUnionMember2ExprUnionMember5",
    "RankByMinExprUnionMember2ExprUnionMember5Expr",
    "RankByMinExprUnionMember2ExprUnionMember5ExprUnionMember0",
    "RankByMinExprUnionMember2ExprUnionMember5ExprUnionMember1",
    "RankByMinExprUnionMember2ExprUnionMember6",
    "RankByMinExprUnionMember2ExprUnionMember6Expr",
    "RankByMinExprUnionMember2ExprUnionMember6ExprUnionMember0",
    "RankByMinExprUnionMember2ExprUnionMember6ExprUnionMember1",
    "RankByMinExprUnionMember2ExprUnionMember7",
    "RankByMinExprUnionMember2ExprUnionMember7Expr",
    "RankByMinExprUnionMember2ExprUnionMember7ExprUnionMember0",
    "RankByMinExprUnionMember2ExprUnionMember7ExprUnionMember1",
    "RankByMinExprUnionMember3",
    "RankByMinExprUnionMember3Expr",
    "RankByMinExprUnionMember3ExprUnionMember0",
    "RankByMinExprUnionMember3ExprUnionMember1",
    "RankByMinExprUnionMember3ExprUnionMember2",
    "RankByMinExprUnionMember3ExprUnionMember2Expr",
    "RankByMinExprUnionMember3ExprUnionMember2ExprUnionMember0",
    "RankByMinExprUnionMember3ExprUnionMember2ExprUnionMember1",
    "RankByMinExprUnionMember3ExprUnionMember3",
    "RankByMinExprUnionMember3ExprUnionMember3Expr",
    "RankByMinExprUnionMember3ExprUnionMember3ExprUnionMember0",
    "RankByMinExprUnionMember3ExprUnionMember3ExprUnionMember1",
    "RankByMinExprUnionMember3ExprUnionMember4",
    "RankByMinExprUnionMember3ExprUnionMember4Expr",
    "RankByMinExprUnionMember3ExprUnionMember4ExprUnionMember0",
    "RankByMinExprUnionMember3ExprUnionMember4ExprUnionMember1",
    "RankByMinExprUnionMember3ExprUnionMember5",
    "RankByMinExprUnionMember3ExprUnionMember5Expr",
    "RankByMinExprUnionMember3ExprUnionMember5ExprUnionMember0",
    "RankByMinExprUnionMember3ExprUnionMember5ExprUnionMember1",
    "RankByMinExprUnionMember3ExprUnionMember6",
    "RankByMinExprUnionMember3ExprUnionMember6Expr",
    "RankByMinExprUnionMember3ExprUnionMember6ExprUnionMember0",
    "RankByMinExprUnionMember3ExprUnionMember6ExprUnionMember1",
    "RankByMinExprUnionMember3ExprUnionMember7",
    "RankByMinExprUnionMember3ExprUnionMember7Expr",
    "RankByMinExprUnionMember3ExprUnionMember7ExprUnionMember0",
    "RankByMinExprUnionMember3ExprUnionMember7ExprUnionMember1",
    "RankByMinExprUnionMember4",
    "RankByMinExprUnionMember4Expr",
    "RankByMinExprUnionMember4ExprUnionMember0",
    "RankByMinExprUnionMember4ExprUnionMember1",
    "RankByMinExprUnionMember4ExprUnionMember2",
    "RankByMinExprUnionMember4ExprUnionMember2Expr",
    "RankByMinExprUnionMember4ExprUnionMember2ExprUnionMember0",
    "RankByMinExprUnionMember4ExprUnionMember2ExprUnionMember1",
    "RankByMinExprUnionMember4ExprUnionMember3",
    "RankByMinExprUnionMember4ExprUnionMember3Expr",
    "RankByMinExprUnionMember4ExprUnionMember3ExprUnionMember0",
    "RankByMinExprUnionMember4ExprUnionMember3ExprUnionMember1",
    "RankByMinExprUnionMember4ExprUnionMember4",
    "RankByMinExprUnionMember4ExprUnionMember4Expr",
    "RankByMinExprUnionMember4ExprUnionMember4ExprUnionMember0",
    "RankByMinExprUnionMember4ExprUnionMember4ExprUnionMember1",
    "RankByMinExprUnionMember4ExprUnionMember5",
    "RankByMinExprUnionMember4ExprUnionMember5Expr",
    "RankByMinExprUnionMember4ExprUnionMember5ExprUnionMember0",
    "RankByMinExprUnionMember4ExprUnionMember5ExprUnionMember1",
    "RankByMinExprUnionMember4ExprUnionMember6",
    "RankByMinExprUnionMember4ExprUnionMember6Expr",
    "RankByMinExprUnionMember4ExprUnionMember6ExprUnionMember0",
    "RankByMinExprUnionMember4ExprUnionMember6ExprUnionMember1",
    "RankByMinExprUnionMember4ExprUnionMember7",
    "RankByMinExprUnionMember4ExprUnionMember7Expr",
    "RankByMinExprUnionMember4ExprUnionMember7ExprUnionMember0",
    "RankByMinExprUnionMember4ExprUnionMember7ExprUnionMember1",
    "RankByMinExprUnionMember5",
    "RankByMinExprUnionMember5Expr",
    "RankByMinExprUnionMember5ExprUnionMember0",
    "RankByMinExprUnionMember5ExprUnionMember1",
    "RankByMinExprUnionMember5ExprUnionMember2",
    "RankByMinExprUnionMember5ExprUnionMember2Expr",
    "RankByMinExprUnionMember5ExprUnionMember2ExprUnionMember0",
    "RankByMinExprUnionMember5ExprUnionMember2ExprUnionMember1",
    "RankByMinExprUnionMember5ExprUnionMember3",
    "RankByMinExprUnionMember5ExprUnionMember3Expr",
    "RankByMinExprUnionMember5ExprUnionMember3ExprUnionMember0",
    "RankByMinExprUnionMember5ExprUnionMember3ExprUnionMember1",
    "RankByMinExprUnionMember5ExprUnionMember4",
    "RankByMinExprUnionMember5ExprUnionMember4Expr",
    "RankByMinExprUnionMember5ExprUnionMember4ExprUnionMember0",
    "RankByMinExprUnionMember5ExprUnionMember4ExprUnionMember1",
    "RankByMinExprUnionMember5ExprUnionMember5",
    "RankByMinExprUnionMember5ExprUnionMember5Expr",
    "RankByMinExprUnionMember5ExprUnionMember5ExprUnionMember0",
    "RankByMinExprUnionMember5ExprUnionMember5ExprUnionMember1",
    "RankByMinExprUnionMember5ExprUnionMember6",
    "RankByMinExprUnionMember5ExprUnionMember6Expr",
    "RankByMinExprUnionMember5ExprUnionMember6ExprUnionMember0",
    "RankByMinExprUnionMember5ExprUnionMember6ExprUnionMember1",
    "RankByMinExprUnionMember5ExprUnionMember7",
    "RankByMinExprUnionMember5ExprUnionMember7Expr",
    "RankByMinExprUnionMember5ExprUnionMember7ExprUnionMember0",
    "RankByMinExprUnionMember5ExprUnionMember7ExprUnionMember1",
    "RankByMinExprUnionMember6",
    "RankByMinExprUnionMember6Expr",
    "RankByMinExprUnionMember6ExprUnionMember0",
    "RankByMinExprUnionMember6ExprUnionMember1",
    "RankByMinExprUnionMember6ExprUnionMember2",
    "RankByMinExprUnionMember6ExprUnionMember2Expr",
    "RankByMinExprUnionMember6ExprUnionMember2ExprUnionMember0",
    "RankByMinExprUnionMember6ExprUnionMember2ExprUnionMember1",
    "RankByMinExprUnionMember6ExprUnionMember3",
    "RankByMinExprUnionMember6ExprUnionMember3Expr",
    "RankByMinExprUnionMember6ExprUnionMember3ExprUnionMember0",
    "RankByMinExprUnionMember6ExprUnionMember3ExprUnionMember1",
    "RankByMinExprUnionMember6ExprUnionMember4",
    "RankByMinExprUnionMember6ExprUnionMember4Expr",
    "RankByMinExprUnionMember6ExprUnionMember4ExprUnionMember0",
    "RankByMinExprUnionMember6ExprUnionMember4ExprUnionMember1",
    "RankByMinExprUnionMember6ExprUnionMember5",
    "RankByMinExprUnionMember6ExprUnionMember5Expr",
    "RankByMinExprUnionMember6ExprUnionMember5ExprUnionMember0",
    "RankByMinExprUnionMember6ExprUnionMember5ExprUnionMember1",
    "RankByMinExprUnionMember6ExprUnionMember6",
    "RankByMinExprUnionMember6ExprUnionMember6Expr",
    "RankByMinExprUnionMember6ExprUnionMember6ExprUnionMember0",
    "RankByMinExprUnionMember6ExprUnionMember6ExprUnionMember1",
    "RankByMinExprUnionMember6ExprUnionMember7",
    "RankByMinExprUnionMember6ExprUnionMember7Expr",
    "RankByMinExprUnionMember6ExprUnionMember7ExprUnionMember0",
    "RankByMinExprUnionMember6ExprUnionMember7ExprUnionMember1",
    "RankByMinExprUnionMember7",
    "RankByMinExprUnionMember7Expr",
    "RankByMinExprUnionMember7ExprUnionMember0",
    "RankByMinExprUnionMember7ExprUnionMember1",
    "RankByMinExprUnionMember7ExprUnionMember2",
    "RankByMinExprUnionMember7ExprUnionMember2Expr",
    "RankByMinExprUnionMember7ExprUnionMember2ExprUnionMember0",
    "RankByMinExprUnionMember7ExprUnionMember2ExprUnionMember1",
    "RankByMinExprUnionMember7ExprUnionMember3",
    "RankByMinExprUnionMember7ExprUnionMember3Expr",
    "RankByMinExprUnionMember7ExprUnionMember3ExprUnionMember0",
    "RankByMinExprUnionMember7ExprUnionMember3ExprUnionMember1",
    "RankByMinExprUnionMember7ExprUnionMember4",
    "RankByMinExprUnionMember7ExprUnionMember4Expr",
    "RankByMinExprUnionMember7ExprUnionMember4ExprUnionMember0",
    "RankByMinExprUnionMember7ExprUnionMember4ExprUnionMember1",
    "RankByMinExprUnionMember7ExprUnionMember5",
    "RankByMinExprUnionMember7ExprUnionMember5Expr",
    "RankByMinExprUnionMember7ExprUnionMember5ExprUnionMember0",
    "RankByMinExprUnionMember7ExprUnionMember5ExprUnionMember1",
    "RankByMinExprUnionMember7ExprUnionMember6",
    "RankByMinExprUnionMember7ExprUnionMember6Expr",
    "RankByMinExprUnionMember7ExprUnionMember6ExprUnionMember0",
    "RankByMinExprUnionMember7ExprUnionMember6ExprUnionMember1",
    "RankByMinExprUnionMember7ExprUnionMember7",
    "RankByMinExprUnionMember7ExprUnionMember7Expr",
    "RankByMinExprUnionMember7ExprUnionMember7ExprUnionMember0",
    "RankByMinExprUnionMember7ExprUnionMember7ExprUnionMember1",
    "RankByLog",
    "RankByLogExpr",
    "RankByLogExprUnionMember0",
    "RankByLogExprUnionMember1",
    "RankByLogExprUnionMember2",
    "RankByLogExprUnionMember2Expr",
    "RankByLogExprUnionMember2ExprUnionMember0",
    "RankByLogExprUnionMember2ExprUnionMember1",
    "RankByLogExprUnionMember2ExprUnionMember2",
    "RankByLogExprUnionMember2ExprUnionMember2Expr",
    "RankByLogExprUnionMember2ExprUnionMember2ExprUnionMember0",
    "RankByLogExprUnionMember2ExprUnionMember2ExprUnionMember1",
    "RankByLogExprUnionMember2ExprUnionMember3",
    "RankByLogExprUnionMember2ExprUnionMember3Expr",
    "RankByLogExprUnionMember2ExprUnionMember3ExprUnionMember0",
    "RankByLogExprUnionMember2ExprUnionMember3ExprUnionMember1",
    "RankByLogExprUnionMember2ExprUnionMember4",
    "RankByLogExprUnionMember2ExprUnionMember4Expr",
    "RankByLogExprUnionMember2ExprUnionMember4ExprUnionMember0",
    "RankByLogExprUnionMember2ExprUnionMember4ExprUnionMember1",
    "RankByLogExprUnionMember2ExprUnionMember5",
    "RankByLogExprUnionMember2ExprUnionMember5Expr",
    "RankByLogExprUnionMember2ExprUnionMember5ExprUnionMember0",
    "RankByLogExprUnionMember2ExprUnionMember5ExprUnionMember1",
    "RankByLogExprUnionMember2ExprUnionMember6",
    "RankByLogExprUnionMember2ExprUnionMember6Expr",
    "RankByLogExprUnionMember2ExprUnionMember6ExprUnionMember0",
    "RankByLogExprUnionMember2ExprUnionMember6ExprUnionMember1",
    "RankByLogExprUnionMember2ExprUnionMember7",
    "RankByLogExprUnionMember2ExprUnionMember7Expr",
    "RankByLogExprUnionMember2ExprUnionMember7ExprUnionMember0",
    "RankByLogExprUnionMember2ExprUnionMember7ExprUnionMember1",
    "RankByLogExprUnionMember3",
    "RankByLogExprUnionMember3Expr",
    "RankByLogExprUnionMember3ExprUnionMember0",
    "RankByLogExprUnionMember3ExprUnionMember1",
    "RankByLogExprUnionMember3ExprUnionMember2",
    "RankByLogExprUnionMember3ExprUnionMember2Expr",
    "RankByLogExprUnionMember3ExprUnionMember2ExprUnionMember0",
    "RankByLogExprUnionMember3ExprUnionMember2ExprUnionMember1",
    "RankByLogExprUnionMember3ExprUnionMember3",
    "RankByLogExprUnionMember3ExprUnionMember3Expr",
    "RankByLogExprUnionMember3ExprUnionMember3ExprUnionMember0",
    "RankByLogExprUnionMember3ExprUnionMember3ExprUnionMember1",
    "RankByLogExprUnionMember3ExprUnionMember4",
    "RankByLogExprUnionMember3ExprUnionMember4Expr",
    "RankByLogExprUnionMember3ExprUnionMember4ExprUnionMember0",
    "RankByLogExprUnionMember3ExprUnionMember4ExprUnionMember1",
    "RankByLogExprUnionMember3ExprUnionMember5",
    "RankByLogExprUnionMember3ExprUnionMember5Expr",
    "RankByLogExprUnionMember3ExprUnionMember5ExprUnionMember0",
    "RankByLogExprUnionMember3ExprUnionMember5ExprUnionMember1",
    "RankByLogExprUnionMember3ExprUnionMember6",
    "RankByLogExprUnionMember3ExprUnionMember6Expr",
    "RankByLogExprUnionMember3ExprUnionMember6ExprUnionMember0",
    "RankByLogExprUnionMember3ExprUnionMember6ExprUnionMember1",
    "RankByLogExprUnionMember3ExprUnionMember7",
    "RankByLogExprUnionMember3ExprUnionMember7Expr",
    "RankByLogExprUnionMember3ExprUnionMember7ExprUnionMember0",
    "RankByLogExprUnionMember3ExprUnionMember7ExprUnionMember1",
    "RankByLogExprUnionMember4",
    "RankByLogExprUnionMember4Expr",
    "RankByLogExprUnionMember4ExprUnionMember0",
    "RankByLogExprUnionMember4ExprUnionMember1",
    "RankByLogExprUnionMember4ExprUnionMember2",
    "RankByLogExprUnionMember4ExprUnionMember2Expr",
    "RankByLogExprUnionMember4ExprUnionMember2ExprUnionMember0",
    "RankByLogExprUnionMember4ExprUnionMember2ExprUnionMember1",
    "RankByLogExprUnionMember4ExprUnionMember3",
    "RankByLogExprUnionMember4ExprUnionMember3Expr",
    "RankByLogExprUnionMember4ExprUnionMember3ExprUnionMember0",
    "RankByLogExprUnionMember4ExprUnionMember3ExprUnionMember1",
    "RankByLogExprUnionMember4ExprUnionMember4",
    "RankByLogExprUnionMember4ExprUnionMember4Expr",
    "RankByLogExprUnionMember4ExprUnionMember4ExprUnionMember0",
    "RankByLogExprUnionMember4ExprUnionMember4ExprUnionMember1",
    "RankByLogExprUnionMember4ExprUnionMember5",
    "RankByLogExprUnionMember4ExprUnionMember5Expr",
    "RankByLogExprUnionMember4ExprUnionMember5ExprUnionMember0",
    "RankByLogExprUnionMember4ExprUnionMember5ExprUnionMember1",
    "RankByLogExprUnionMember4ExprUnionMember6",
    "RankByLogExprUnionMember4ExprUnionMember6Expr",
    "RankByLogExprUnionMember4ExprUnionMember6ExprUnionMember0",
    "RankByLogExprUnionMember4ExprUnionMember6ExprUnionMember1",
    "RankByLogExprUnionMember4ExprUnionMember7",
    "RankByLogExprUnionMember4ExprUnionMember7Expr",
    "RankByLogExprUnionMember4ExprUnionMember7ExprUnionMember0",
    "RankByLogExprUnionMember4ExprUnionMember7ExprUnionMember1",
    "RankByLogExprUnionMember5",
    "RankByLogExprUnionMember5Expr",
    "RankByLogExprUnionMember5ExprUnionMember0",
    "RankByLogExprUnionMember5ExprUnionMember1",
    "RankByLogExprUnionMember5ExprUnionMember2",
    "RankByLogExprUnionMember5ExprUnionMember2Expr",
    "RankByLogExprUnionMember5ExprUnionMember2ExprUnionMember0",
    "RankByLogExprUnionMember5ExprUnionMember2ExprUnionMember1",
    "RankByLogExprUnionMember5ExprUnionMember3",
    "RankByLogExprUnionMember5ExprUnionMember3Expr",
    "RankByLogExprUnionMember5ExprUnionMember3ExprUnionMember0",
    "RankByLogExprUnionMember5ExprUnionMember3ExprUnionMember1",
    "RankByLogExprUnionMember5ExprUnionMember4",
    "RankByLogExprUnionMember5ExprUnionMember4Expr",
    "RankByLogExprUnionMember5ExprUnionMember4ExprUnionMember0",
    "RankByLogExprUnionMember5ExprUnionMember4ExprUnionMember1",
    "RankByLogExprUnionMember5ExprUnionMember5",
    "RankByLogExprUnionMember5ExprUnionMember5Expr",
    "RankByLogExprUnionMember5ExprUnionMember5ExprUnionMember0",
    "RankByLogExprUnionMember5ExprUnionMember5ExprUnionMember1",
    "RankByLogExprUnionMember5ExprUnionMember6",
    "RankByLogExprUnionMember5ExprUnionMember6Expr",
    "RankByLogExprUnionMember5ExprUnionMember6ExprUnionMember0",
    "RankByLogExprUnionMember5ExprUnionMember6ExprUnionMember1",
    "RankByLogExprUnionMember5ExprUnionMember7",
    "RankByLogExprUnionMember5ExprUnionMember7Expr",
    "RankByLogExprUnionMember5ExprUnionMember7ExprUnionMember0",
    "RankByLogExprUnionMember5ExprUnionMember7ExprUnionMember1",
    "RankByLogExprUnionMember6",
    "RankByLogExprUnionMember6Expr",
    "RankByLogExprUnionMember6ExprUnionMember0",
    "RankByLogExprUnionMember6ExprUnionMember1",
    "RankByLogExprUnionMember6ExprUnionMember2",
    "RankByLogExprUnionMember6ExprUnionMember2Expr",
    "RankByLogExprUnionMember6ExprUnionMember2ExprUnionMember0",
    "RankByLogExprUnionMember6ExprUnionMember2ExprUnionMember1",
    "RankByLogExprUnionMember6ExprUnionMember3",
    "RankByLogExprUnionMember6ExprUnionMember3Expr",
    "RankByLogExprUnionMember6ExprUnionMember3ExprUnionMember0",
    "RankByLogExprUnionMember6ExprUnionMember3ExprUnionMember1",
    "RankByLogExprUnionMember6ExprUnionMember4",
    "RankByLogExprUnionMember6ExprUnionMember4Expr",
    "RankByLogExprUnionMember6ExprUnionMember4ExprUnionMember0",
    "RankByLogExprUnionMember6ExprUnionMember4ExprUnionMember1",
    "RankByLogExprUnionMember6ExprUnionMember5",
    "RankByLogExprUnionMember6ExprUnionMember5Expr",
    "RankByLogExprUnionMember6ExprUnionMember5ExprUnionMember0",
    "RankByLogExprUnionMember6ExprUnionMember5ExprUnionMember1",
    "RankByLogExprUnionMember6ExprUnionMember6",
    "RankByLogExprUnionMember6ExprUnionMember6Expr",
    "RankByLogExprUnionMember6ExprUnionMember6ExprUnionMember0",
    "RankByLogExprUnionMember6ExprUnionMember6ExprUnionMember1",
    "RankByLogExprUnionMember6ExprUnionMember7",
    "RankByLogExprUnionMember6ExprUnionMember7Expr",
    "RankByLogExprUnionMember6ExprUnionMember7ExprUnionMember0",
    "RankByLogExprUnionMember6ExprUnionMember7ExprUnionMember1",
    "RankByLogExprUnionMember7",
    "RankByLogExprUnionMember7Expr",
    "RankByLogExprUnionMember7ExprUnionMember0",
    "RankByLogExprUnionMember7ExprUnionMember1",
    "RankByLogExprUnionMember7ExprUnionMember2",
    "RankByLogExprUnionMember7ExprUnionMember2Expr",
    "RankByLogExprUnionMember7ExprUnionMember2ExprUnionMember0",
    "RankByLogExprUnionMember7ExprUnionMember2ExprUnionMember1",
    "RankByLogExprUnionMember7ExprUnionMember3",
    "RankByLogExprUnionMember7ExprUnionMember3Expr",
    "RankByLogExprUnionMember7ExprUnionMember3ExprUnionMember0",
    "RankByLogExprUnionMember7ExprUnionMember3ExprUnionMember1",
    "RankByLogExprUnionMember7ExprUnionMember4",
    "RankByLogExprUnionMember7ExprUnionMember4Expr",
    "RankByLogExprUnionMember7ExprUnionMember4ExprUnionMember0",
    "RankByLogExprUnionMember7ExprUnionMember4ExprUnionMember1",
    "RankByLogExprUnionMember7ExprUnionMember5",
    "RankByLogExprUnionMember7ExprUnionMember5Expr",
    "RankByLogExprUnionMember7ExprUnionMember5ExprUnionMember0",
    "RankByLogExprUnionMember7ExprUnionMember5ExprUnionMember1",
    "RankByLogExprUnionMember7ExprUnionMember6",
    "RankByLogExprUnionMember7ExprUnionMember6Expr",
    "RankByLogExprUnionMember7ExprUnionMember6ExprUnionMember0",
    "RankByLogExprUnionMember7ExprUnionMember6ExprUnionMember1",
    "RankByLogExprUnionMember7ExprUnionMember7",
    "RankByLogExprUnionMember7ExprUnionMember7Expr",
    "RankByLogExprUnionMember7ExprUnionMember7ExprUnionMember0",
    "RankByLogExprUnionMember7ExprUnionMember7ExprUnionMember1",
]


class SearchRepoSearchParams(TypedDict, total=False):
    query: Required[Union[str, SequenceNotStr[str], None]]
    """
    Search query for semantic search across repository README and description using
    vector embeddings. Supports: string (single query), string[] (RRF fusion), null
    (filter-only)
    """

    after: str
    """Cursor for pagination (from previous response pageInfo.endCursor)"""

    enable_pagination: Annotated[bool, PropertyInfo(alias="enablePagination")]
    """Enable cursor-based pagination to fetch results across multiple requests"""

    filters: Filters
    """Filters to apply (required)"""

    first: int
    """Alias for maxResults (takes precedence if both provided)"""

    include_attributes: Annotated[IncludeAttributes, PropertyInfo(alias="includeAttributes")]
    """Optional graph relationships to include (owner, contributors, starrers)"""

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
    """Maximum number of results to return (default: 100, max: 1000)"""

    rank_by: Annotated[RankBy, PropertyInfo(alias="rankBy")]
    """Custom ranking formula (AST expression).

    If not provided, uses default log-normalized 70/20/10 formula (70% semantic
    similarity, 20% popularity, 10% activity).
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
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersContains(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["Contains"]]

    value: Required[str]


class FiltersNotContains(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["NotContains"]]

    value: Required[str]


class FiltersContainsAny(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["ContainsAny"]]

    value: Required[SequenceNotStr[str]]


class FiltersNotContainsAny(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["NotContainsAny"]]

    value: Required[SequenceNotStr[str]]


class FiltersAnyLt(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["AnyLt"]]

    value: Required[str]


class FiltersAnyLte(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["AnyLte"]]

    value: Required[str]


class FiltersAnyGt(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["AnyGt"]]

    value: Required[str]


class FiltersAnyGte(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["AnyGte"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember107FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember107FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember107FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember107FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember107FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember107FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember107FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember107FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["Eq"]]

    value: Required[float]


class FiltersUnionMember107FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["NotEq"]]

    value: Required[float]


class FiltersUnionMember107FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["In"]]

    value: Required[Iterable[float]]


class FiltersUnionMember107FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["NotIn"]]

    value: Required[Iterable[float]]


class FiltersUnionMember107FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["Lt"]]

    value: Required[float]


class FiltersUnionMember107FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["Lte"]]

    value: Required[float]


class FiltersUnionMember107FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["Gt"]]

    value: Required[float]


class FiltersUnionMember107FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["Gte"]]

    value: Required[float]


class FiltersUnionMember107FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember107FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember107FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["Eq"]]

    value: Required[float]


class FiltersUnionMember107FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["NotEq"]]

    value: Required[float]


class FiltersUnionMember107FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["In"]]

    value: Required[Iterable[float]]


class FiltersUnionMember107FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["NotIn"]]

    value: Required[Iterable[float]]


class FiltersUnionMember107FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["Lt"]]

    value: Required[float]


class FiltersUnionMember107FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["Lte"]]

    value: Required[float]


class FiltersUnionMember107FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["Gt"]]

    value: Required[float]


class FiltersUnionMember107FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["Gte"]]

    value: Required[float]


class FiltersUnionMember107FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["Eq"]]

    value: Required[float]


class FiltersUnionMember107FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["NotEq"]]

    value: Required[float]


class FiltersUnionMember107FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["In"]]

    value: Required[Iterable[float]]


class FiltersUnionMember107FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["NotIn"]]

    value: Required[Iterable[float]]


class FiltersUnionMember107FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["Lt"]]

    value: Required[float]


class FiltersUnionMember107FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["Lte"]]

    value: Required[float]


class FiltersUnionMember107FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["Gt"]]

    value: Required[float]


class FiltersUnionMember107FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["Gte"]]

    value: Required[float]


class FiltersUnionMember107FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["Eq"]]

    value: Required[float]


class FiltersUnionMember107FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["NotEq"]]

    value: Required[float]


class FiltersUnionMember107FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["In"]]

    value: Required[Iterable[float]]


class FiltersUnionMember107FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["NotIn"]]

    value: Required[Iterable[float]]


class FiltersUnionMember107FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["Lt"]]

    value: Required[float]


class FiltersUnionMember107FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["Lte"]]

    value: Required[float]


class FiltersUnionMember107FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["Gt"]]

    value: Required[float]


class FiltersUnionMember107FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["Gte"]]

    value: Required[float]


class FiltersUnionMember107FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["Contains"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["NotContains"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["ContainsAny"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember107FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["NotContainsAny"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember107FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["AnyLt"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["AnyLte"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["AnyGt"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["AnyGte"]]

    value: Required[str]


class FiltersUnionMember107FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


FiltersUnionMember107Filter: TypeAlias = Union[
    FiltersUnionMember107FilterUnionMember0,
    FiltersUnionMember107FilterUnionMember1,
    FiltersUnionMember107FilterUnionMember2,
    FiltersUnionMember107FilterUnionMember3,
    FiltersUnionMember107FilterUnionMember4,
    FiltersUnionMember107FilterUnionMember5,
    FiltersUnionMember107FilterUnionMember6,
    FiltersUnionMember107FilterUnionMember7,
    FiltersUnionMember107FilterUnionMember8,
    FiltersUnionMember107FilterUnionMember9,
    FiltersUnionMember107FilterUnionMember10,
    FiltersUnionMember107FilterUnionMember11,
    FiltersUnionMember107FilterUnionMember12,
    FiltersUnionMember107FilterUnionMember13,
    FiltersUnionMember107FilterUnionMember14,
    FiltersUnionMember107FilterUnionMember15,
    FiltersUnionMember107FilterUnionMember16,
    FiltersUnionMember107FilterUnionMember17,
    FiltersUnionMember107FilterUnionMember18,
    FiltersUnionMember107FilterUnionMember19,
    FiltersUnionMember107FilterUnionMember20,
    FiltersUnionMember107FilterUnionMember21,
    FiltersUnionMember107FilterUnionMember22,
    FiltersUnionMember107FilterUnionMember23,
    FiltersUnionMember107FilterUnionMember24,
    FiltersUnionMember107FilterUnionMember25,
    FiltersUnionMember107FilterUnionMember26,
    FiltersUnionMember107FilterUnionMember27,
    FiltersUnionMember107FilterUnionMember28,
    FiltersUnionMember107FilterUnionMember29,
    FiltersUnionMember107FilterUnionMember30,
    FiltersUnionMember107FilterUnionMember31,
    FiltersUnionMember107FilterUnionMember32,
    FiltersUnionMember107FilterUnionMember33,
    FiltersUnionMember107FilterUnionMember34,
    FiltersUnionMember107FilterUnionMember35,
    FiltersUnionMember107FilterUnionMember36,
    FiltersUnionMember107FilterUnionMember37,
    FiltersUnionMember107FilterUnionMember38,
    FiltersUnionMember107FilterUnionMember39,
    FiltersUnionMember107FilterUnionMember40,
    FiltersUnionMember107FilterUnionMember41,
    FiltersUnionMember107FilterUnionMember42,
    FiltersUnionMember107FilterUnionMember43,
    FiltersUnionMember107FilterUnionMember44,
    FiltersUnionMember107FilterUnionMember45,
    FiltersUnionMember107FilterUnionMember46,
    FiltersUnionMember107FilterUnionMember47,
    FiltersUnionMember107FilterUnionMember48,
    FiltersUnionMember107FilterUnionMember49,
    FiltersUnionMember107FilterUnionMember50,
    FiltersUnionMember107FilterUnionMember51,
    FiltersUnionMember107FilterUnionMember52,
    FiltersUnionMember107FilterUnionMember53,
    FiltersUnionMember107FilterUnionMember54,
    FiltersUnionMember107FilterUnionMember55,
    FiltersUnionMember107FilterUnionMember56,
    FiltersUnionMember107FilterUnionMember57,
    FiltersUnionMember107FilterUnionMember58,
    FiltersUnionMember107FilterUnionMember59,
    FiltersUnionMember107FilterUnionMember60,
    FiltersUnionMember107FilterUnionMember61,
    FiltersUnionMember107FilterUnionMember62,
    FiltersUnionMember107FilterUnionMember63,
    FiltersUnionMember107FilterUnionMember64,
    FiltersUnionMember107FilterUnionMember65,
    FiltersUnionMember107FilterUnionMember66,
    FiltersUnionMember107FilterUnionMember67,
    FiltersUnionMember107FilterUnionMember68,
    FiltersUnionMember107FilterUnionMember69,
    FiltersUnionMember107FilterUnionMember70,
    FiltersUnionMember107FilterUnionMember71,
    FiltersUnionMember107FilterUnionMember72,
    FiltersUnionMember107FilterUnionMember73,
    FiltersUnionMember107FilterUnionMember74,
    FiltersUnionMember107FilterUnionMember75,
    FiltersUnionMember107FilterUnionMember76,
    FiltersUnionMember107FilterUnionMember77,
    FiltersUnionMember107FilterUnionMember78,
    FiltersUnionMember107FilterUnionMember79,
    FiltersUnionMember107FilterUnionMember80,
    FiltersUnionMember107FilterUnionMember81,
    FiltersUnionMember107FilterUnionMember82,
    FiltersUnionMember107FilterUnionMember83,
    FiltersUnionMember107FilterUnionMember84,
    FiltersUnionMember107FilterUnionMember85,
    FiltersUnionMember107FilterUnionMember86,
    FiltersUnionMember107FilterUnionMember87,
    FiltersUnionMember107FilterUnionMember88,
    FiltersUnionMember107FilterUnionMember89,
    FiltersUnionMember107FilterUnionMember90,
    FiltersUnionMember107FilterUnionMember91,
    FiltersUnionMember107FilterUnionMember92,
    FiltersUnionMember107FilterUnionMember93,
    FiltersUnionMember107FilterUnionMember94,
    FiltersUnionMember107FilterUnionMember95,
    FiltersUnionMember107FilterUnionMember96,
    FiltersUnionMember107FilterUnionMember97,
    FiltersUnionMember107FilterUnionMember98,
    FiltersUnionMember107FilterUnionMember99,
    FiltersUnionMember107FilterUnionMember100,
    FiltersUnionMember107FilterUnionMember101,
    FiltersUnionMember107FilterUnionMember102,
    FiltersUnionMember107FilterUnionMember103,
    FiltersUnionMember107FilterUnionMember104,
    FiltersUnionMember107FilterUnionMember105,
    FiltersUnionMember107FilterUnionMember106,
]


class FiltersUnionMember107(TypedDict, total=False):
    filters: Required[Iterable[FiltersUnionMember107Filter]]

    op: Required[Literal["And", "Or"]]


class FiltersUnionMember108FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember108FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember108FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember108FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember108FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember108FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember108FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember108FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember108FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["Eq"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["NotEq"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["In"]]

    value: Required[Iterable[float]]


class FiltersUnionMember108FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["NotIn"]]

    value: Required[Iterable[float]]


class FiltersUnionMember108FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["Lt"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["Lte"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["Gt"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["Gte"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember108FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember108FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["Eq"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["NotEq"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["In"]]

    value: Required[Iterable[float]]


class FiltersUnionMember108FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["NotIn"]]

    value: Required[Iterable[float]]


class FiltersUnionMember108FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["Lt"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["Lte"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["Gt"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["Gte"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["Eq"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["NotEq"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["In"]]

    value: Required[Iterable[float]]


class FiltersUnionMember108FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["NotIn"]]

    value: Required[Iterable[float]]


class FiltersUnionMember108FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["Lt"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["Lte"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["Gt"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["Gte"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["Eq"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["NotEq"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["In"]]

    value: Required[Iterable[float]]


class FiltersUnionMember108FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["NotIn"]]

    value: Required[Iterable[float]]


class FiltersUnionMember108FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["Lt"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["Lte"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["Gt"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["Gte"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["Contains"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["NotContains"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["ContainsAny"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember108FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["NotContainsAny"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember108FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["AnyLt"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["AnyLte"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["AnyGt"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["AnyGte"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember13(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember14(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember15(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember16(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember17(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember18(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember19(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember20(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember21(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember22(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember23(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember24(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember25(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember26(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember27(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember28(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember29(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember30(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember31(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember32(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember33(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember34(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember35(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember36(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember37(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember38(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember39(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember40(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember41(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember42(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember43(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember44(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember45(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember46(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember47(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember48(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember49(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember50(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember51(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember52(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember53(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["Eq"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember54(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["NotEq"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember55(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["In"]]

    value: Required[Iterable[float]]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember56(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["NotIn"]]

    value: Required[Iterable[float]]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember57(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["Lt"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember58(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["Lte"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember59(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["Gt"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember60(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["Gte"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember61(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember62(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember63(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember64(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember65(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember66(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember67(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember68(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember69(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember70(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember71(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember72(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember73(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember74(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["Eq"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember75(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["NotEq"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember76(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["In"]]

    value: Required[Iterable[float]]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember77(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["NotIn"]]

    value: Required[Iterable[float]]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember78(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["Lt"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember79(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["Lte"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember80(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["Gt"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember81(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["Gte"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember82(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["Eq"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember83(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["NotEq"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember84(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["In"]]

    value: Required[Iterable[float]]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember85(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["NotIn"]]

    value: Required[Iterable[float]]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember86(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["Lt"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember87(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["Lte"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember88(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["Gt"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember89(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["Gte"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember90(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["Eq"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember91(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["NotEq"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember92(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["In"]]

    value: Required[Iterable[float]]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember93(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["NotIn"]]

    value: Required[Iterable[float]]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember94(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["Lt"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember95(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["Lte"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember96(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["Gt"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember97(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["Gte"]]

    value: Required[float]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember98(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["Contains"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember99(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["NotContains"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember100(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["ContainsAny"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember101(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["NotContainsAny"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember102(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["AnyLt"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember103(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["AnyLte"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember104(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["AnyGt"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember105(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["AnyGte"]]

    value: Required[str]


class FiltersUnionMember108FilterUnionMember107FilterUnionMember106(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


FiltersUnionMember108FilterUnionMember107Filter: TypeAlias = Union[
    FiltersUnionMember108FilterUnionMember107FilterUnionMember0,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember1,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember2,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember3,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember4,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember5,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember6,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember7,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember8,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember9,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember10,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember11,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember12,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember13,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember14,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember15,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember16,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember17,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember18,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember19,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember20,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember21,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember22,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember23,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember24,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember25,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember26,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember27,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember28,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember29,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember30,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember31,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember32,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember33,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember34,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember35,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember36,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember37,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember38,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember39,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember40,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember41,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember42,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember43,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember44,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember45,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember46,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember47,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember48,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember49,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember50,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember51,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember52,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember53,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember54,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember55,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember56,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember57,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember58,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember59,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember60,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember61,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember62,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember63,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember64,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember65,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember66,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember67,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember68,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember69,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember70,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember71,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember72,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember73,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember74,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember75,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember76,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember77,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember78,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember79,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember80,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember81,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember82,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember83,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember84,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember85,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember86,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember87,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember88,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember89,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember90,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember91,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember92,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember93,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember94,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember95,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember96,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember97,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember98,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember99,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember100,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember101,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember102,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember103,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember104,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember105,
    FiltersUnionMember108FilterUnionMember107FilterUnionMember106,
]


class FiltersUnionMember108FilterUnionMember107(TypedDict, total=False):
    filters: Required[Iterable[FiltersUnionMember108FilterUnionMember107Filter]]

    op: Required[Literal["And", "Or"]]


FiltersUnionMember108Filter: TypeAlias = Union[
    FiltersUnionMember108FilterUnionMember0,
    FiltersUnionMember108FilterUnionMember1,
    FiltersUnionMember108FilterUnionMember2,
    FiltersUnionMember108FilterUnionMember3,
    FiltersUnionMember108FilterUnionMember4,
    FiltersUnionMember108FilterUnionMember5,
    FiltersUnionMember108FilterUnionMember6,
    FiltersUnionMember108FilterUnionMember7,
    FiltersUnionMember108FilterUnionMember8,
    FiltersUnionMember108FilterUnionMember9,
    FiltersUnionMember108FilterUnionMember10,
    FiltersUnionMember108FilterUnionMember11,
    FiltersUnionMember108FilterUnionMember12,
    FiltersUnionMember108FilterUnionMember13,
    FiltersUnionMember108FilterUnionMember14,
    FiltersUnionMember108FilterUnionMember15,
    FiltersUnionMember108FilterUnionMember16,
    FiltersUnionMember108FilterUnionMember17,
    FiltersUnionMember108FilterUnionMember18,
    FiltersUnionMember108FilterUnionMember19,
    FiltersUnionMember108FilterUnionMember20,
    FiltersUnionMember108FilterUnionMember21,
    FiltersUnionMember108FilterUnionMember22,
    FiltersUnionMember108FilterUnionMember23,
    FiltersUnionMember108FilterUnionMember24,
    FiltersUnionMember108FilterUnionMember25,
    FiltersUnionMember108FilterUnionMember26,
    FiltersUnionMember108FilterUnionMember27,
    FiltersUnionMember108FilterUnionMember28,
    FiltersUnionMember108FilterUnionMember29,
    FiltersUnionMember108FilterUnionMember30,
    FiltersUnionMember108FilterUnionMember31,
    FiltersUnionMember108FilterUnionMember32,
    FiltersUnionMember108FilterUnionMember33,
    FiltersUnionMember108FilterUnionMember34,
    FiltersUnionMember108FilterUnionMember35,
    FiltersUnionMember108FilterUnionMember36,
    FiltersUnionMember108FilterUnionMember37,
    FiltersUnionMember108FilterUnionMember38,
    FiltersUnionMember108FilterUnionMember39,
    FiltersUnionMember108FilterUnionMember40,
    FiltersUnionMember108FilterUnionMember41,
    FiltersUnionMember108FilterUnionMember42,
    FiltersUnionMember108FilterUnionMember43,
    FiltersUnionMember108FilterUnionMember44,
    FiltersUnionMember108FilterUnionMember45,
    FiltersUnionMember108FilterUnionMember46,
    FiltersUnionMember108FilterUnionMember47,
    FiltersUnionMember108FilterUnionMember48,
    FiltersUnionMember108FilterUnionMember49,
    FiltersUnionMember108FilterUnionMember50,
    FiltersUnionMember108FilterUnionMember51,
    FiltersUnionMember108FilterUnionMember52,
    FiltersUnionMember108FilterUnionMember53,
    FiltersUnionMember108FilterUnionMember54,
    FiltersUnionMember108FilterUnionMember55,
    FiltersUnionMember108FilterUnionMember56,
    FiltersUnionMember108FilterUnionMember57,
    FiltersUnionMember108FilterUnionMember58,
    FiltersUnionMember108FilterUnionMember59,
    FiltersUnionMember108FilterUnionMember60,
    FiltersUnionMember108FilterUnionMember61,
    FiltersUnionMember108FilterUnionMember62,
    FiltersUnionMember108FilterUnionMember63,
    FiltersUnionMember108FilterUnionMember64,
    FiltersUnionMember108FilterUnionMember65,
    FiltersUnionMember108FilterUnionMember66,
    FiltersUnionMember108FilterUnionMember67,
    FiltersUnionMember108FilterUnionMember68,
    FiltersUnionMember108FilterUnionMember69,
    FiltersUnionMember108FilterUnionMember70,
    FiltersUnionMember108FilterUnionMember71,
    FiltersUnionMember108FilterUnionMember72,
    FiltersUnionMember108FilterUnionMember73,
    FiltersUnionMember108FilterUnionMember74,
    FiltersUnionMember108FilterUnionMember75,
    FiltersUnionMember108FilterUnionMember76,
    FiltersUnionMember108FilterUnionMember77,
    FiltersUnionMember108FilterUnionMember78,
    FiltersUnionMember108FilterUnionMember79,
    FiltersUnionMember108FilterUnionMember80,
    FiltersUnionMember108FilterUnionMember81,
    FiltersUnionMember108FilterUnionMember82,
    FiltersUnionMember108FilterUnionMember83,
    FiltersUnionMember108FilterUnionMember84,
    FiltersUnionMember108FilterUnionMember85,
    FiltersUnionMember108FilterUnionMember86,
    FiltersUnionMember108FilterUnionMember87,
    FiltersUnionMember108FilterUnionMember88,
    FiltersUnionMember108FilterUnionMember89,
    FiltersUnionMember108FilterUnionMember90,
    FiltersUnionMember108FilterUnionMember91,
    FiltersUnionMember108FilterUnionMember92,
    FiltersUnionMember108FilterUnionMember93,
    FiltersUnionMember108FilterUnionMember94,
    FiltersUnionMember108FilterUnionMember95,
    FiltersUnionMember108FilterUnionMember96,
    FiltersUnionMember108FilterUnionMember97,
    FiltersUnionMember108FilterUnionMember98,
    FiltersUnionMember108FilterUnionMember99,
    FiltersUnionMember108FilterUnionMember100,
    FiltersUnionMember108FilterUnionMember101,
    FiltersUnionMember108FilterUnionMember102,
    FiltersUnionMember108FilterUnionMember103,
    FiltersUnionMember108FilterUnionMember104,
    FiltersUnionMember108FilterUnionMember105,
    FiltersUnionMember108FilterUnionMember106,
    FiltersUnionMember108FilterUnionMember107,
]


class FiltersUnionMember108(TypedDict, total=False):
    filters: Required[Iterable[FiltersUnionMember108Filter]]

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
    FiltersEq,
    FiltersNotEq,
    FiltersIn,
    FiltersNotIn,
    FiltersLt,
    FiltersLte,
    FiltersGt,
    FiltersGte,
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
    FiltersEq,
    FiltersNotEq,
    FiltersIn,
    FiltersNotIn,
    FiltersLt,
    FiltersLte,
    FiltersGt,
    FiltersGte,
    FiltersEq,
    FiltersNotEq,
    FiltersIn,
    FiltersNotIn,
    FiltersLt,
    FiltersLte,
    FiltersGt,
    FiltersGte,
    FiltersContains,
    FiltersNotContains,
    FiltersContainsAny,
    FiltersNotContainsAny,
    FiltersAnyLt,
    FiltersAnyLte,
    FiltersAnyGt,
    FiltersAnyGte,
    FiltersContainsAllTokens,
    FiltersUnionMember107,
    FiltersUnionMember108,
]


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


class RankByAttr(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByConst(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankBySumExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankBySumExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankBySumExprUnionMember2ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember2ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember2ExprUnionMember2Expr: TypeAlias = Union[
    RankBySumExprUnionMember2ExprUnionMember2ExprUnionMember0, RankBySumExprUnionMember2ExprUnionMember2ExprUnionMember1
]


class RankBySumExprUnionMember2ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember2ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankBySumExprUnionMember2ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember2ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember2ExprUnionMember3Expr: TypeAlias = Union[
    RankBySumExprUnionMember2ExprUnionMember3ExprUnionMember0, RankBySumExprUnionMember2ExprUnionMember3ExprUnionMember1
]


class RankBySumExprUnionMember2ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember2ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankBySumExprUnionMember2ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember2ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember2ExprUnionMember4Expr: TypeAlias = Union[
    RankBySumExprUnionMember2ExprUnionMember4ExprUnionMember0, RankBySumExprUnionMember2ExprUnionMember4ExprUnionMember1
]


class RankBySumExprUnionMember2ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember2ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankBySumExprUnionMember2ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember2ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember2ExprUnionMember5Expr: TypeAlias = Union[
    RankBySumExprUnionMember2ExprUnionMember5ExprUnionMember0, RankBySumExprUnionMember2ExprUnionMember5ExprUnionMember1
]


class RankBySumExprUnionMember2ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember2ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankBySumExprUnionMember2ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember2ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember2ExprUnionMember6Expr: TypeAlias = Union[
    RankBySumExprUnionMember2ExprUnionMember6ExprUnionMember0, RankBySumExprUnionMember2ExprUnionMember6ExprUnionMember1
]


class RankBySumExprUnionMember2ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember2ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankBySumExprUnionMember2ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember2ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember2ExprUnionMember7Expr: TypeAlias = Union[
    RankBySumExprUnionMember2ExprUnionMember7ExprUnionMember0, RankBySumExprUnionMember2ExprUnionMember7ExprUnionMember1
]


class RankBySumExprUnionMember2ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankBySumExprUnionMember2ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankBySumExprUnionMember2Expr: TypeAlias = Union[
    RankBySumExprUnionMember2ExprUnionMember0,
    RankBySumExprUnionMember2ExprUnionMember1,
    RankBySumExprUnionMember2ExprUnionMember2,
    RankBySumExprUnionMember2ExprUnionMember3,
    RankBySumExprUnionMember2ExprUnionMember4,
    RankBySumExprUnionMember2ExprUnionMember5,
    RankBySumExprUnionMember2ExprUnionMember6,
    RankBySumExprUnionMember2ExprUnionMember7,
]


class RankBySumExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankBySumExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankBySumExprUnionMember3ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember3ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember3ExprUnionMember2Expr: TypeAlias = Union[
    RankBySumExprUnionMember3ExprUnionMember2ExprUnionMember0, RankBySumExprUnionMember3ExprUnionMember2ExprUnionMember1
]


class RankBySumExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember3ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankBySumExprUnionMember3ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember3ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember3ExprUnionMember3Expr: TypeAlias = Union[
    RankBySumExprUnionMember3ExprUnionMember3ExprUnionMember0, RankBySumExprUnionMember3ExprUnionMember3ExprUnionMember1
]


class RankBySumExprUnionMember3ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember3ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankBySumExprUnionMember3ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember3ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember3ExprUnionMember4Expr: TypeAlias = Union[
    RankBySumExprUnionMember3ExprUnionMember4ExprUnionMember0, RankBySumExprUnionMember3ExprUnionMember4ExprUnionMember1
]


class RankBySumExprUnionMember3ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember3ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankBySumExprUnionMember3ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember3ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember3ExprUnionMember5Expr: TypeAlias = Union[
    RankBySumExprUnionMember3ExprUnionMember5ExprUnionMember0, RankBySumExprUnionMember3ExprUnionMember5ExprUnionMember1
]


class RankBySumExprUnionMember3ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember3ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankBySumExprUnionMember3ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember3ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember3ExprUnionMember6Expr: TypeAlias = Union[
    RankBySumExprUnionMember3ExprUnionMember6ExprUnionMember0, RankBySumExprUnionMember3ExprUnionMember6ExprUnionMember1
]


class RankBySumExprUnionMember3ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember3ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankBySumExprUnionMember3ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember3ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember3ExprUnionMember7Expr: TypeAlias = Union[
    RankBySumExprUnionMember3ExprUnionMember7ExprUnionMember0, RankBySumExprUnionMember3ExprUnionMember7ExprUnionMember1
]


class RankBySumExprUnionMember3ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankBySumExprUnionMember3ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankBySumExprUnionMember3Expr: TypeAlias = Union[
    RankBySumExprUnionMember3ExprUnionMember0,
    RankBySumExprUnionMember3ExprUnionMember1,
    RankBySumExprUnionMember3ExprUnionMember2,
    RankBySumExprUnionMember3ExprUnionMember3,
    RankBySumExprUnionMember3ExprUnionMember4,
    RankBySumExprUnionMember3ExprUnionMember5,
    RankBySumExprUnionMember3ExprUnionMember6,
    RankBySumExprUnionMember3ExprUnionMember7,
]


class RankBySumExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankBySumExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankBySumExprUnionMember4ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember4ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember4ExprUnionMember2Expr: TypeAlias = Union[
    RankBySumExprUnionMember4ExprUnionMember2ExprUnionMember0, RankBySumExprUnionMember4ExprUnionMember2ExprUnionMember1
]


class RankBySumExprUnionMember4ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember4ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankBySumExprUnionMember4ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember4ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember4ExprUnionMember3Expr: TypeAlias = Union[
    RankBySumExprUnionMember4ExprUnionMember3ExprUnionMember0, RankBySumExprUnionMember4ExprUnionMember3ExprUnionMember1
]


class RankBySumExprUnionMember4ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember4ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankBySumExprUnionMember4ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember4ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember4ExprUnionMember4Expr: TypeAlias = Union[
    RankBySumExprUnionMember4ExprUnionMember4ExprUnionMember0, RankBySumExprUnionMember4ExprUnionMember4ExprUnionMember1
]


class RankBySumExprUnionMember4ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember4ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankBySumExprUnionMember4ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember4ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember4ExprUnionMember5Expr: TypeAlias = Union[
    RankBySumExprUnionMember4ExprUnionMember5ExprUnionMember0, RankBySumExprUnionMember4ExprUnionMember5ExprUnionMember1
]


class RankBySumExprUnionMember4ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember4ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankBySumExprUnionMember4ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember4ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember4ExprUnionMember6Expr: TypeAlias = Union[
    RankBySumExprUnionMember4ExprUnionMember6ExprUnionMember0, RankBySumExprUnionMember4ExprUnionMember6ExprUnionMember1
]


class RankBySumExprUnionMember4ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember4ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankBySumExprUnionMember4ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember4ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember4ExprUnionMember7Expr: TypeAlias = Union[
    RankBySumExprUnionMember4ExprUnionMember7ExprUnionMember0, RankBySumExprUnionMember4ExprUnionMember7ExprUnionMember1
]


class RankBySumExprUnionMember4ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankBySumExprUnionMember4ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankBySumExprUnionMember4Expr: TypeAlias = Union[
    RankBySumExprUnionMember4ExprUnionMember0,
    RankBySumExprUnionMember4ExprUnionMember1,
    RankBySumExprUnionMember4ExprUnionMember2,
    RankBySumExprUnionMember4ExprUnionMember3,
    RankBySumExprUnionMember4ExprUnionMember4,
    RankBySumExprUnionMember4ExprUnionMember5,
    RankBySumExprUnionMember4ExprUnionMember6,
    RankBySumExprUnionMember4ExprUnionMember7,
]


class RankBySumExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankBySumExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankBySumExprUnionMember5ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember5ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember5ExprUnionMember2Expr: TypeAlias = Union[
    RankBySumExprUnionMember5ExprUnionMember2ExprUnionMember0, RankBySumExprUnionMember5ExprUnionMember2ExprUnionMember1
]


class RankBySumExprUnionMember5ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember5ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankBySumExprUnionMember5ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember5ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember5ExprUnionMember3Expr: TypeAlias = Union[
    RankBySumExprUnionMember5ExprUnionMember3ExprUnionMember0, RankBySumExprUnionMember5ExprUnionMember3ExprUnionMember1
]


class RankBySumExprUnionMember5ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember5ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankBySumExprUnionMember5ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember5ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember5ExprUnionMember4Expr: TypeAlias = Union[
    RankBySumExprUnionMember5ExprUnionMember4ExprUnionMember0, RankBySumExprUnionMember5ExprUnionMember4ExprUnionMember1
]


class RankBySumExprUnionMember5ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember5ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankBySumExprUnionMember5ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember5ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember5ExprUnionMember5Expr: TypeAlias = Union[
    RankBySumExprUnionMember5ExprUnionMember5ExprUnionMember0, RankBySumExprUnionMember5ExprUnionMember5ExprUnionMember1
]


class RankBySumExprUnionMember5ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember5ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankBySumExprUnionMember5ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember5ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember5ExprUnionMember6Expr: TypeAlias = Union[
    RankBySumExprUnionMember5ExprUnionMember6ExprUnionMember0, RankBySumExprUnionMember5ExprUnionMember6ExprUnionMember1
]


class RankBySumExprUnionMember5ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember5ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankBySumExprUnionMember5ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember5ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember5ExprUnionMember7Expr: TypeAlias = Union[
    RankBySumExprUnionMember5ExprUnionMember7ExprUnionMember0, RankBySumExprUnionMember5ExprUnionMember7ExprUnionMember1
]


class RankBySumExprUnionMember5ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankBySumExprUnionMember5ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankBySumExprUnionMember5Expr: TypeAlias = Union[
    RankBySumExprUnionMember5ExprUnionMember0,
    RankBySumExprUnionMember5ExprUnionMember1,
    RankBySumExprUnionMember5ExprUnionMember2,
    RankBySumExprUnionMember5ExprUnionMember3,
    RankBySumExprUnionMember5ExprUnionMember4,
    RankBySumExprUnionMember5ExprUnionMember5,
    RankBySumExprUnionMember5ExprUnionMember6,
    RankBySumExprUnionMember5ExprUnionMember7,
]


class RankBySumExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankBySumExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankBySumExprUnionMember6ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember6ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember6ExprUnionMember2Expr: TypeAlias = Union[
    RankBySumExprUnionMember6ExprUnionMember2ExprUnionMember0, RankBySumExprUnionMember6ExprUnionMember2ExprUnionMember1
]


class RankBySumExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember6ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankBySumExprUnionMember6ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember6ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember6ExprUnionMember3Expr: TypeAlias = Union[
    RankBySumExprUnionMember6ExprUnionMember3ExprUnionMember0, RankBySumExprUnionMember6ExprUnionMember3ExprUnionMember1
]


class RankBySumExprUnionMember6ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember6ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankBySumExprUnionMember6ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember6ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember6ExprUnionMember4Expr: TypeAlias = Union[
    RankBySumExprUnionMember6ExprUnionMember4ExprUnionMember0, RankBySumExprUnionMember6ExprUnionMember4ExprUnionMember1
]


class RankBySumExprUnionMember6ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember6ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankBySumExprUnionMember6ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember6ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember6ExprUnionMember5Expr: TypeAlias = Union[
    RankBySumExprUnionMember6ExprUnionMember5ExprUnionMember0, RankBySumExprUnionMember6ExprUnionMember5ExprUnionMember1
]


class RankBySumExprUnionMember6ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember6ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankBySumExprUnionMember6ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember6ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember6ExprUnionMember6Expr: TypeAlias = Union[
    RankBySumExprUnionMember6ExprUnionMember6ExprUnionMember0, RankBySumExprUnionMember6ExprUnionMember6ExprUnionMember1
]


class RankBySumExprUnionMember6ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember6ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankBySumExprUnionMember6ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember6ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember6ExprUnionMember7Expr: TypeAlias = Union[
    RankBySumExprUnionMember6ExprUnionMember7ExprUnionMember0, RankBySumExprUnionMember6ExprUnionMember7ExprUnionMember1
]


class RankBySumExprUnionMember6ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankBySumExprUnionMember6ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankBySumExprUnionMember6Expr: TypeAlias = Union[
    RankBySumExprUnionMember6ExprUnionMember0,
    RankBySumExprUnionMember6ExprUnionMember1,
    RankBySumExprUnionMember6ExprUnionMember2,
    RankBySumExprUnionMember6ExprUnionMember3,
    RankBySumExprUnionMember6ExprUnionMember4,
    RankBySumExprUnionMember6ExprUnionMember5,
    RankBySumExprUnionMember6ExprUnionMember6,
    RankBySumExprUnionMember6ExprUnionMember7,
]


class RankBySumExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankBySumExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankBySumExprUnionMember7ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember7ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember7ExprUnionMember2Expr: TypeAlias = Union[
    RankBySumExprUnionMember7ExprUnionMember2ExprUnionMember0, RankBySumExprUnionMember7ExprUnionMember2ExprUnionMember1
]


class RankBySumExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember7ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankBySumExprUnionMember7ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember7ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember7ExprUnionMember3Expr: TypeAlias = Union[
    RankBySumExprUnionMember7ExprUnionMember3ExprUnionMember0, RankBySumExprUnionMember7ExprUnionMember3ExprUnionMember1
]


class RankBySumExprUnionMember7ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember7ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankBySumExprUnionMember7ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember7ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember7ExprUnionMember4Expr: TypeAlias = Union[
    RankBySumExprUnionMember7ExprUnionMember4ExprUnionMember0, RankBySumExprUnionMember7ExprUnionMember4ExprUnionMember1
]


class RankBySumExprUnionMember7ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember7ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankBySumExprUnionMember7ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember7ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember7ExprUnionMember5Expr: TypeAlias = Union[
    RankBySumExprUnionMember7ExprUnionMember5ExprUnionMember0, RankBySumExprUnionMember7ExprUnionMember5ExprUnionMember1
]


class RankBySumExprUnionMember7ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember7ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankBySumExprUnionMember7ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember7ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember7ExprUnionMember6Expr: TypeAlias = Union[
    RankBySumExprUnionMember7ExprUnionMember6ExprUnionMember0, RankBySumExprUnionMember7ExprUnionMember6ExprUnionMember1
]


class RankBySumExprUnionMember7ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember7ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankBySumExprUnionMember7ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember7ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember7ExprUnionMember7Expr: TypeAlias = Union[
    RankBySumExprUnionMember7ExprUnionMember7ExprUnionMember0, RankBySumExprUnionMember7ExprUnionMember7ExprUnionMember1
]


class RankBySumExprUnionMember7ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankBySumExprUnionMember7ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankBySumExprUnionMember7Expr: TypeAlias = Union[
    RankBySumExprUnionMember7ExprUnionMember0,
    RankBySumExprUnionMember7ExprUnionMember1,
    RankBySumExprUnionMember7ExprUnionMember2,
    RankBySumExprUnionMember7ExprUnionMember3,
    RankBySumExprUnionMember7ExprUnionMember4,
    RankBySumExprUnionMember7ExprUnionMember5,
    RankBySumExprUnionMember7ExprUnionMember6,
    RankBySumExprUnionMember7ExprUnionMember7,
]


class RankBySumExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankBySumExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankBySumExpr: TypeAlias = Union[
    RankBySumExprUnionMember0,
    RankBySumExprUnionMember1,
    RankBySumExprUnionMember2,
    RankBySumExprUnionMember3,
    RankBySumExprUnionMember4,
    RankBySumExprUnionMember5,
    RankBySumExprUnionMember6,
    RankBySumExprUnionMember7,
]


class RankBySum(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExpr]]

    type: Required[Literal["Sum"]]


class RankByMultExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByMultExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByMultExprUnionMember2ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember2ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember2ExprUnionMember2Expr: TypeAlias = Union[
    RankByMultExprUnionMember2ExprUnionMember2ExprUnionMember0,
    RankByMultExprUnionMember2ExprUnionMember2ExprUnionMember1,
]


class RankByMultExprUnionMember2ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember2ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMultExprUnionMember2ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember2ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember2ExprUnionMember3Expr: TypeAlias = Union[
    RankByMultExprUnionMember2ExprUnionMember3ExprUnionMember0,
    RankByMultExprUnionMember2ExprUnionMember3ExprUnionMember1,
]


class RankByMultExprUnionMember2ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember2ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByMultExprUnionMember2ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember2ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember2ExprUnionMember4Expr: TypeAlias = Union[
    RankByMultExprUnionMember2ExprUnionMember4ExprUnionMember0,
    RankByMultExprUnionMember2ExprUnionMember4ExprUnionMember1,
]


class RankByMultExprUnionMember2ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember2ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByMultExprUnionMember2ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember2ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember2ExprUnionMember5Expr: TypeAlias = Union[
    RankByMultExprUnionMember2ExprUnionMember5ExprUnionMember0,
    RankByMultExprUnionMember2ExprUnionMember5ExprUnionMember1,
]


class RankByMultExprUnionMember2ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember2ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByMultExprUnionMember2ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember2ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember2ExprUnionMember6Expr: TypeAlias = Union[
    RankByMultExprUnionMember2ExprUnionMember6ExprUnionMember0,
    RankByMultExprUnionMember2ExprUnionMember6ExprUnionMember1,
]


class RankByMultExprUnionMember2ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember2ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByMultExprUnionMember2ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember2ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember2ExprUnionMember7Expr: TypeAlias = Union[
    RankByMultExprUnionMember2ExprUnionMember7ExprUnionMember0,
    RankByMultExprUnionMember2ExprUnionMember7ExprUnionMember1,
]


class RankByMultExprUnionMember2ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMultExprUnionMember2ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByMultExprUnionMember2Expr: TypeAlias = Union[
    RankByMultExprUnionMember2ExprUnionMember0,
    RankByMultExprUnionMember2ExprUnionMember1,
    RankByMultExprUnionMember2ExprUnionMember2,
    RankByMultExprUnionMember2ExprUnionMember3,
    RankByMultExprUnionMember2ExprUnionMember4,
    RankByMultExprUnionMember2ExprUnionMember5,
    RankByMultExprUnionMember2ExprUnionMember6,
    RankByMultExprUnionMember2ExprUnionMember7,
]


class RankByMultExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMultExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByMultExprUnionMember3ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember3ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember3ExprUnionMember2Expr: TypeAlias = Union[
    RankByMultExprUnionMember3ExprUnionMember2ExprUnionMember0,
    RankByMultExprUnionMember3ExprUnionMember2ExprUnionMember1,
]


class RankByMultExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember3ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMultExprUnionMember3ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember3ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember3ExprUnionMember3Expr: TypeAlias = Union[
    RankByMultExprUnionMember3ExprUnionMember3ExprUnionMember0,
    RankByMultExprUnionMember3ExprUnionMember3ExprUnionMember1,
]


class RankByMultExprUnionMember3ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember3ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByMultExprUnionMember3ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember3ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember3ExprUnionMember4Expr: TypeAlias = Union[
    RankByMultExprUnionMember3ExprUnionMember4ExprUnionMember0,
    RankByMultExprUnionMember3ExprUnionMember4ExprUnionMember1,
]


class RankByMultExprUnionMember3ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember3ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByMultExprUnionMember3ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember3ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember3ExprUnionMember5Expr: TypeAlias = Union[
    RankByMultExprUnionMember3ExprUnionMember5ExprUnionMember0,
    RankByMultExprUnionMember3ExprUnionMember5ExprUnionMember1,
]


class RankByMultExprUnionMember3ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember3ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByMultExprUnionMember3ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember3ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember3ExprUnionMember6Expr: TypeAlias = Union[
    RankByMultExprUnionMember3ExprUnionMember6ExprUnionMember0,
    RankByMultExprUnionMember3ExprUnionMember6ExprUnionMember1,
]


class RankByMultExprUnionMember3ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember3ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByMultExprUnionMember3ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember3ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember3ExprUnionMember7Expr: TypeAlias = Union[
    RankByMultExprUnionMember3ExprUnionMember7ExprUnionMember0,
    RankByMultExprUnionMember3ExprUnionMember7ExprUnionMember1,
]


class RankByMultExprUnionMember3ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMultExprUnionMember3ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByMultExprUnionMember3Expr: TypeAlias = Union[
    RankByMultExprUnionMember3ExprUnionMember0,
    RankByMultExprUnionMember3ExprUnionMember1,
    RankByMultExprUnionMember3ExprUnionMember2,
    RankByMultExprUnionMember3ExprUnionMember3,
    RankByMultExprUnionMember3ExprUnionMember4,
    RankByMultExprUnionMember3ExprUnionMember5,
    RankByMultExprUnionMember3ExprUnionMember6,
    RankByMultExprUnionMember3ExprUnionMember7,
]


class RankByMultExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByMultExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByMultExprUnionMember4ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember4ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember4ExprUnionMember2Expr: TypeAlias = Union[
    RankByMultExprUnionMember4ExprUnionMember2ExprUnionMember0,
    RankByMultExprUnionMember4ExprUnionMember2ExprUnionMember1,
]


class RankByMultExprUnionMember4ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember4ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMultExprUnionMember4ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember4ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember4ExprUnionMember3Expr: TypeAlias = Union[
    RankByMultExprUnionMember4ExprUnionMember3ExprUnionMember0,
    RankByMultExprUnionMember4ExprUnionMember3ExprUnionMember1,
]


class RankByMultExprUnionMember4ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember4ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByMultExprUnionMember4ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember4ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember4ExprUnionMember4Expr: TypeAlias = Union[
    RankByMultExprUnionMember4ExprUnionMember4ExprUnionMember0,
    RankByMultExprUnionMember4ExprUnionMember4ExprUnionMember1,
]


class RankByMultExprUnionMember4ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember4ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByMultExprUnionMember4ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember4ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember4ExprUnionMember5Expr: TypeAlias = Union[
    RankByMultExprUnionMember4ExprUnionMember5ExprUnionMember0,
    RankByMultExprUnionMember4ExprUnionMember5ExprUnionMember1,
]


class RankByMultExprUnionMember4ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember4ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByMultExprUnionMember4ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember4ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember4ExprUnionMember6Expr: TypeAlias = Union[
    RankByMultExprUnionMember4ExprUnionMember6ExprUnionMember0,
    RankByMultExprUnionMember4ExprUnionMember6ExprUnionMember1,
]


class RankByMultExprUnionMember4ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember4ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByMultExprUnionMember4ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember4ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember4ExprUnionMember7Expr: TypeAlias = Union[
    RankByMultExprUnionMember4ExprUnionMember7ExprUnionMember0,
    RankByMultExprUnionMember4ExprUnionMember7ExprUnionMember1,
]


class RankByMultExprUnionMember4ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMultExprUnionMember4ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByMultExprUnionMember4Expr: TypeAlias = Union[
    RankByMultExprUnionMember4ExprUnionMember0,
    RankByMultExprUnionMember4ExprUnionMember1,
    RankByMultExprUnionMember4ExprUnionMember2,
    RankByMultExprUnionMember4ExprUnionMember3,
    RankByMultExprUnionMember4ExprUnionMember4,
    RankByMultExprUnionMember4ExprUnionMember5,
    RankByMultExprUnionMember4ExprUnionMember6,
    RankByMultExprUnionMember4ExprUnionMember7,
]


class RankByMultExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByMultExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByMultExprUnionMember5ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember5ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember5ExprUnionMember2Expr: TypeAlias = Union[
    RankByMultExprUnionMember5ExprUnionMember2ExprUnionMember0,
    RankByMultExprUnionMember5ExprUnionMember2ExprUnionMember1,
]


class RankByMultExprUnionMember5ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember5ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMultExprUnionMember5ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember5ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember5ExprUnionMember3Expr: TypeAlias = Union[
    RankByMultExprUnionMember5ExprUnionMember3ExprUnionMember0,
    RankByMultExprUnionMember5ExprUnionMember3ExprUnionMember1,
]


class RankByMultExprUnionMember5ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember5ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByMultExprUnionMember5ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember5ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember5ExprUnionMember4Expr: TypeAlias = Union[
    RankByMultExprUnionMember5ExprUnionMember4ExprUnionMember0,
    RankByMultExprUnionMember5ExprUnionMember4ExprUnionMember1,
]


class RankByMultExprUnionMember5ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember5ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByMultExprUnionMember5ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember5ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember5ExprUnionMember5Expr: TypeAlias = Union[
    RankByMultExprUnionMember5ExprUnionMember5ExprUnionMember0,
    RankByMultExprUnionMember5ExprUnionMember5ExprUnionMember1,
]


class RankByMultExprUnionMember5ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember5ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByMultExprUnionMember5ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember5ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember5ExprUnionMember6Expr: TypeAlias = Union[
    RankByMultExprUnionMember5ExprUnionMember6ExprUnionMember0,
    RankByMultExprUnionMember5ExprUnionMember6ExprUnionMember1,
]


class RankByMultExprUnionMember5ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember5ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByMultExprUnionMember5ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember5ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember5ExprUnionMember7Expr: TypeAlias = Union[
    RankByMultExprUnionMember5ExprUnionMember7ExprUnionMember0,
    RankByMultExprUnionMember5ExprUnionMember7ExprUnionMember1,
]


class RankByMultExprUnionMember5ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMultExprUnionMember5ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByMultExprUnionMember5Expr: TypeAlias = Union[
    RankByMultExprUnionMember5ExprUnionMember0,
    RankByMultExprUnionMember5ExprUnionMember1,
    RankByMultExprUnionMember5ExprUnionMember2,
    RankByMultExprUnionMember5ExprUnionMember3,
    RankByMultExprUnionMember5ExprUnionMember4,
    RankByMultExprUnionMember5ExprUnionMember5,
    RankByMultExprUnionMember5ExprUnionMember6,
    RankByMultExprUnionMember5ExprUnionMember7,
]


class RankByMultExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByMultExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByMultExprUnionMember6ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember6ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember6ExprUnionMember2Expr: TypeAlias = Union[
    RankByMultExprUnionMember6ExprUnionMember2ExprUnionMember0,
    RankByMultExprUnionMember6ExprUnionMember2ExprUnionMember1,
]


class RankByMultExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember6ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMultExprUnionMember6ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember6ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember6ExprUnionMember3Expr: TypeAlias = Union[
    RankByMultExprUnionMember6ExprUnionMember3ExprUnionMember0,
    RankByMultExprUnionMember6ExprUnionMember3ExprUnionMember1,
]


class RankByMultExprUnionMember6ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember6ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByMultExprUnionMember6ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember6ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember6ExprUnionMember4Expr: TypeAlias = Union[
    RankByMultExprUnionMember6ExprUnionMember4ExprUnionMember0,
    RankByMultExprUnionMember6ExprUnionMember4ExprUnionMember1,
]


class RankByMultExprUnionMember6ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember6ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByMultExprUnionMember6ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember6ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember6ExprUnionMember5Expr: TypeAlias = Union[
    RankByMultExprUnionMember6ExprUnionMember5ExprUnionMember0,
    RankByMultExprUnionMember6ExprUnionMember5ExprUnionMember1,
]


class RankByMultExprUnionMember6ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember6ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByMultExprUnionMember6ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember6ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember6ExprUnionMember6Expr: TypeAlias = Union[
    RankByMultExprUnionMember6ExprUnionMember6ExprUnionMember0,
    RankByMultExprUnionMember6ExprUnionMember6ExprUnionMember1,
]


class RankByMultExprUnionMember6ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember6ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByMultExprUnionMember6ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember6ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember6ExprUnionMember7Expr: TypeAlias = Union[
    RankByMultExprUnionMember6ExprUnionMember7ExprUnionMember0,
    RankByMultExprUnionMember6ExprUnionMember7ExprUnionMember1,
]


class RankByMultExprUnionMember6ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMultExprUnionMember6ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByMultExprUnionMember6Expr: TypeAlias = Union[
    RankByMultExprUnionMember6ExprUnionMember0,
    RankByMultExprUnionMember6ExprUnionMember1,
    RankByMultExprUnionMember6ExprUnionMember2,
    RankByMultExprUnionMember6ExprUnionMember3,
    RankByMultExprUnionMember6ExprUnionMember4,
    RankByMultExprUnionMember6ExprUnionMember5,
    RankByMultExprUnionMember6ExprUnionMember6,
    RankByMultExprUnionMember6ExprUnionMember7,
]


class RankByMultExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByMultExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByMultExprUnionMember7ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember7ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember7ExprUnionMember2Expr: TypeAlias = Union[
    RankByMultExprUnionMember7ExprUnionMember2ExprUnionMember0,
    RankByMultExprUnionMember7ExprUnionMember2ExprUnionMember1,
]


class RankByMultExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember7ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMultExprUnionMember7ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember7ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember7ExprUnionMember3Expr: TypeAlias = Union[
    RankByMultExprUnionMember7ExprUnionMember3ExprUnionMember0,
    RankByMultExprUnionMember7ExprUnionMember3ExprUnionMember1,
]


class RankByMultExprUnionMember7ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember7ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByMultExprUnionMember7ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember7ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember7ExprUnionMember4Expr: TypeAlias = Union[
    RankByMultExprUnionMember7ExprUnionMember4ExprUnionMember0,
    RankByMultExprUnionMember7ExprUnionMember4ExprUnionMember1,
]


class RankByMultExprUnionMember7ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember7ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByMultExprUnionMember7ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember7ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember7ExprUnionMember5Expr: TypeAlias = Union[
    RankByMultExprUnionMember7ExprUnionMember5ExprUnionMember0,
    RankByMultExprUnionMember7ExprUnionMember5ExprUnionMember1,
]


class RankByMultExprUnionMember7ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember7ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByMultExprUnionMember7ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember7ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember7ExprUnionMember6Expr: TypeAlias = Union[
    RankByMultExprUnionMember7ExprUnionMember6ExprUnionMember0,
    RankByMultExprUnionMember7ExprUnionMember6ExprUnionMember1,
]


class RankByMultExprUnionMember7ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExprUnionMember7ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByMultExprUnionMember7ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMultExprUnionMember7ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMultExprUnionMember7ExprUnionMember7Expr: TypeAlias = Union[
    RankByMultExprUnionMember7ExprUnionMember7ExprUnionMember0,
    RankByMultExprUnionMember7ExprUnionMember7ExprUnionMember1,
]


class RankByMultExprUnionMember7ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMultExprUnionMember7ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByMultExprUnionMember7Expr: TypeAlias = Union[
    RankByMultExprUnionMember7ExprUnionMember0,
    RankByMultExprUnionMember7ExprUnionMember1,
    RankByMultExprUnionMember7ExprUnionMember2,
    RankByMultExprUnionMember7ExprUnionMember3,
    RankByMultExprUnionMember7ExprUnionMember4,
    RankByMultExprUnionMember7ExprUnionMember5,
    RankByMultExprUnionMember7ExprUnionMember6,
    RankByMultExprUnionMember7ExprUnionMember7,
]


class RankByMultExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMultExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByMultExpr: TypeAlias = Union[
    RankByMultExprUnionMember0,
    RankByMultExprUnionMember1,
    RankByMultExprUnionMember2,
    RankByMultExprUnionMember3,
    RankByMultExprUnionMember4,
    RankByMultExprUnionMember5,
    RankByMultExprUnionMember6,
    RankByMultExprUnionMember7,
]


class RankByMult(TypedDict, total=False):
    exprs: Required[Iterable[RankByMultExpr]]

    type: Required[Literal["Mult"]]


class RankByDivExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByDivExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByDivExprUnionMember2ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember2ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember2ExprUnionMember2Expr: TypeAlias = Union[
    RankByDivExprUnionMember2ExprUnionMember2ExprUnionMember0, RankByDivExprUnionMember2ExprUnionMember2ExprUnionMember1
]


class RankByDivExprUnionMember2ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember2ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByDivExprUnionMember2ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember2ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember2ExprUnionMember3Expr: TypeAlias = Union[
    RankByDivExprUnionMember2ExprUnionMember3ExprUnionMember0, RankByDivExprUnionMember2ExprUnionMember3ExprUnionMember1
]


class RankByDivExprUnionMember2ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember2ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByDivExprUnionMember2ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember2ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember2ExprUnionMember4Expr: TypeAlias = Union[
    RankByDivExprUnionMember2ExprUnionMember4ExprUnionMember0, RankByDivExprUnionMember2ExprUnionMember4ExprUnionMember1
]


class RankByDivExprUnionMember2ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember2ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByDivExprUnionMember2ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember2ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember2ExprUnionMember5Expr: TypeAlias = Union[
    RankByDivExprUnionMember2ExprUnionMember5ExprUnionMember0, RankByDivExprUnionMember2ExprUnionMember5ExprUnionMember1
]


class RankByDivExprUnionMember2ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember2ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByDivExprUnionMember2ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember2ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember2ExprUnionMember6Expr: TypeAlias = Union[
    RankByDivExprUnionMember2ExprUnionMember6ExprUnionMember0, RankByDivExprUnionMember2ExprUnionMember6ExprUnionMember1
]


class RankByDivExprUnionMember2ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember2ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByDivExprUnionMember2ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember2ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember2ExprUnionMember7Expr: TypeAlias = Union[
    RankByDivExprUnionMember2ExprUnionMember7ExprUnionMember0, RankByDivExprUnionMember2ExprUnionMember7ExprUnionMember1
]


class RankByDivExprUnionMember2ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByDivExprUnionMember2ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByDivExprUnionMember2Expr: TypeAlias = Union[
    RankByDivExprUnionMember2ExprUnionMember0,
    RankByDivExprUnionMember2ExprUnionMember1,
    RankByDivExprUnionMember2ExprUnionMember2,
    RankByDivExprUnionMember2ExprUnionMember3,
    RankByDivExprUnionMember2ExprUnionMember4,
    RankByDivExprUnionMember2ExprUnionMember5,
    RankByDivExprUnionMember2ExprUnionMember6,
    RankByDivExprUnionMember2ExprUnionMember7,
]


class RankByDivExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByDivExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByDivExprUnionMember3ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember3ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember3ExprUnionMember2Expr: TypeAlias = Union[
    RankByDivExprUnionMember3ExprUnionMember2ExprUnionMember0, RankByDivExprUnionMember3ExprUnionMember2ExprUnionMember1
]


class RankByDivExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember3ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByDivExprUnionMember3ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember3ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember3ExprUnionMember3Expr: TypeAlias = Union[
    RankByDivExprUnionMember3ExprUnionMember3ExprUnionMember0, RankByDivExprUnionMember3ExprUnionMember3ExprUnionMember1
]


class RankByDivExprUnionMember3ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember3ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByDivExprUnionMember3ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember3ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember3ExprUnionMember4Expr: TypeAlias = Union[
    RankByDivExprUnionMember3ExprUnionMember4ExprUnionMember0, RankByDivExprUnionMember3ExprUnionMember4ExprUnionMember1
]


class RankByDivExprUnionMember3ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember3ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByDivExprUnionMember3ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember3ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember3ExprUnionMember5Expr: TypeAlias = Union[
    RankByDivExprUnionMember3ExprUnionMember5ExprUnionMember0, RankByDivExprUnionMember3ExprUnionMember5ExprUnionMember1
]


class RankByDivExprUnionMember3ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember3ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByDivExprUnionMember3ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember3ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember3ExprUnionMember6Expr: TypeAlias = Union[
    RankByDivExprUnionMember3ExprUnionMember6ExprUnionMember0, RankByDivExprUnionMember3ExprUnionMember6ExprUnionMember1
]


class RankByDivExprUnionMember3ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember3ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByDivExprUnionMember3ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember3ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember3ExprUnionMember7Expr: TypeAlias = Union[
    RankByDivExprUnionMember3ExprUnionMember7ExprUnionMember0, RankByDivExprUnionMember3ExprUnionMember7ExprUnionMember1
]


class RankByDivExprUnionMember3ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByDivExprUnionMember3ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByDivExprUnionMember3Expr: TypeAlias = Union[
    RankByDivExprUnionMember3ExprUnionMember0,
    RankByDivExprUnionMember3ExprUnionMember1,
    RankByDivExprUnionMember3ExprUnionMember2,
    RankByDivExprUnionMember3ExprUnionMember3,
    RankByDivExprUnionMember3ExprUnionMember4,
    RankByDivExprUnionMember3ExprUnionMember5,
    RankByDivExprUnionMember3ExprUnionMember6,
    RankByDivExprUnionMember3ExprUnionMember7,
]


class RankByDivExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByDivExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByDivExprUnionMember4ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember4ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember4ExprUnionMember2Expr: TypeAlias = Union[
    RankByDivExprUnionMember4ExprUnionMember2ExprUnionMember0, RankByDivExprUnionMember4ExprUnionMember2ExprUnionMember1
]


class RankByDivExprUnionMember4ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember4ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByDivExprUnionMember4ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember4ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember4ExprUnionMember3Expr: TypeAlias = Union[
    RankByDivExprUnionMember4ExprUnionMember3ExprUnionMember0, RankByDivExprUnionMember4ExprUnionMember3ExprUnionMember1
]


class RankByDivExprUnionMember4ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember4ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByDivExprUnionMember4ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember4ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember4ExprUnionMember4Expr: TypeAlias = Union[
    RankByDivExprUnionMember4ExprUnionMember4ExprUnionMember0, RankByDivExprUnionMember4ExprUnionMember4ExprUnionMember1
]


class RankByDivExprUnionMember4ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember4ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByDivExprUnionMember4ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember4ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember4ExprUnionMember5Expr: TypeAlias = Union[
    RankByDivExprUnionMember4ExprUnionMember5ExprUnionMember0, RankByDivExprUnionMember4ExprUnionMember5ExprUnionMember1
]


class RankByDivExprUnionMember4ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember4ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByDivExprUnionMember4ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember4ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember4ExprUnionMember6Expr: TypeAlias = Union[
    RankByDivExprUnionMember4ExprUnionMember6ExprUnionMember0, RankByDivExprUnionMember4ExprUnionMember6ExprUnionMember1
]


class RankByDivExprUnionMember4ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember4ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByDivExprUnionMember4ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember4ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember4ExprUnionMember7Expr: TypeAlias = Union[
    RankByDivExprUnionMember4ExprUnionMember7ExprUnionMember0, RankByDivExprUnionMember4ExprUnionMember7ExprUnionMember1
]


class RankByDivExprUnionMember4ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByDivExprUnionMember4ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByDivExprUnionMember4Expr: TypeAlias = Union[
    RankByDivExprUnionMember4ExprUnionMember0,
    RankByDivExprUnionMember4ExprUnionMember1,
    RankByDivExprUnionMember4ExprUnionMember2,
    RankByDivExprUnionMember4ExprUnionMember3,
    RankByDivExprUnionMember4ExprUnionMember4,
    RankByDivExprUnionMember4ExprUnionMember5,
    RankByDivExprUnionMember4ExprUnionMember6,
    RankByDivExprUnionMember4ExprUnionMember7,
]


class RankByDivExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByDivExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByDivExprUnionMember5ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember5ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember5ExprUnionMember2Expr: TypeAlias = Union[
    RankByDivExprUnionMember5ExprUnionMember2ExprUnionMember0, RankByDivExprUnionMember5ExprUnionMember2ExprUnionMember1
]


class RankByDivExprUnionMember5ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember5ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByDivExprUnionMember5ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember5ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember5ExprUnionMember3Expr: TypeAlias = Union[
    RankByDivExprUnionMember5ExprUnionMember3ExprUnionMember0, RankByDivExprUnionMember5ExprUnionMember3ExprUnionMember1
]


class RankByDivExprUnionMember5ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember5ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByDivExprUnionMember5ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember5ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember5ExprUnionMember4Expr: TypeAlias = Union[
    RankByDivExprUnionMember5ExprUnionMember4ExprUnionMember0, RankByDivExprUnionMember5ExprUnionMember4ExprUnionMember1
]


class RankByDivExprUnionMember5ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember5ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByDivExprUnionMember5ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember5ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember5ExprUnionMember5Expr: TypeAlias = Union[
    RankByDivExprUnionMember5ExprUnionMember5ExprUnionMember0, RankByDivExprUnionMember5ExprUnionMember5ExprUnionMember1
]


class RankByDivExprUnionMember5ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember5ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByDivExprUnionMember5ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember5ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember5ExprUnionMember6Expr: TypeAlias = Union[
    RankByDivExprUnionMember5ExprUnionMember6ExprUnionMember0, RankByDivExprUnionMember5ExprUnionMember6ExprUnionMember1
]


class RankByDivExprUnionMember5ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember5ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByDivExprUnionMember5ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember5ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember5ExprUnionMember7Expr: TypeAlias = Union[
    RankByDivExprUnionMember5ExprUnionMember7ExprUnionMember0, RankByDivExprUnionMember5ExprUnionMember7ExprUnionMember1
]


class RankByDivExprUnionMember5ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByDivExprUnionMember5ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByDivExprUnionMember5Expr: TypeAlias = Union[
    RankByDivExprUnionMember5ExprUnionMember0,
    RankByDivExprUnionMember5ExprUnionMember1,
    RankByDivExprUnionMember5ExprUnionMember2,
    RankByDivExprUnionMember5ExprUnionMember3,
    RankByDivExprUnionMember5ExprUnionMember4,
    RankByDivExprUnionMember5ExprUnionMember5,
    RankByDivExprUnionMember5ExprUnionMember6,
    RankByDivExprUnionMember5ExprUnionMember7,
]


class RankByDivExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByDivExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByDivExprUnionMember6ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember6ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember6ExprUnionMember2Expr: TypeAlias = Union[
    RankByDivExprUnionMember6ExprUnionMember2ExprUnionMember0, RankByDivExprUnionMember6ExprUnionMember2ExprUnionMember1
]


class RankByDivExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember6ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByDivExprUnionMember6ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember6ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember6ExprUnionMember3Expr: TypeAlias = Union[
    RankByDivExprUnionMember6ExprUnionMember3ExprUnionMember0, RankByDivExprUnionMember6ExprUnionMember3ExprUnionMember1
]


class RankByDivExprUnionMember6ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember6ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByDivExprUnionMember6ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember6ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember6ExprUnionMember4Expr: TypeAlias = Union[
    RankByDivExprUnionMember6ExprUnionMember4ExprUnionMember0, RankByDivExprUnionMember6ExprUnionMember4ExprUnionMember1
]


class RankByDivExprUnionMember6ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember6ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByDivExprUnionMember6ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember6ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember6ExprUnionMember5Expr: TypeAlias = Union[
    RankByDivExprUnionMember6ExprUnionMember5ExprUnionMember0, RankByDivExprUnionMember6ExprUnionMember5ExprUnionMember1
]


class RankByDivExprUnionMember6ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember6ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByDivExprUnionMember6ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember6ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember6ExprUnionMember6Expr: TypeAlias = Union[
    RankByDivExprUnionMember6ExprUnionMember6ExprUnionMember0, RankByDivExprUnionMember6ExprUnionMember6ExprUnionMember1
]


class RankByDivExprUnionMember6ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember6ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByDivExprUnionMember6ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember6ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember6ExprUnionMember7Expr: TypeAlias = Union[
    RankByDivExprUnionMember6ExprUnionMember7ExprUnionMember0, RankByDivExprUnionMember6ExprUnionMember7ExprUnionMember1
]


class RankByDivExprUnionMember6ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByDivExprUnionMember6ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByDivExprUnionMember6Expr: TypeAlias = Union[
    RankByDivExprUnionMember6ExprUnionMember0,
    RankByDivExprUnionMember6ExprUnionMember1,
    RankByDivExprUnionMember6ExprUnionMember2,
    RankByDivExprUnionMember6ExprUnionMember3,
    RankByDivExprUnionMember6ExprUnionMember4,
    RankByDivExprUnionMember6ExprUnionMember5,
    RankByDivExprUnionMember6ExprUnionMember6,
    RankByDivExprUnionMember6ExprUnionMember7,
]


class RankByDivExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByDivExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByDivExprUnionMember7ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember7ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember7ExprUnionMember2Expr: TypeAlias = Union[
    RankByDivExprUnionMember7ExprUnionMember2ExprUnionMember0, RankByDivExprUnionMember7ExprUnionMember2ExprUnionMember1
]


class RankByDivExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember7ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByDivExprUnionMember7ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember7ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember7ExprUnionMember3Expr: TypeAlias = Union[
    RankByDivExprUnionMember7ExprUnionMember3ExprUnionMember0, RankByDivExprUnionMember7ExprUnionMember3ExprUnionMember1
]


class RankByDivExprUnionMember7ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember7ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByDivExprUnionMember7ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember7ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember7ExprUnionMember4Expr: TypeAlias = Union[
    RankByDivExprUnionMember7ExprUnionMember4ExprUnionMember0, RankByDivExprUnionMember7ExprUnionMember4ExprUnionMember1
]


class RankByDivExprUnionMember7ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember7ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByDivExprUnionMember7ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember7ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember7ExprUnionMember5Expr: TypeAlias = Union[
    RankByDivExprUnionMember7ExprUnionMember5ExprUnionMember0, RankByDivExprUnionMember7ExprUnionMember5ExprUnionMember1
]


class RankByDivExprUnionMember7ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember7ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByDivExprUnionMember7ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember7ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember7ExprUnionMember6Expr: TypeAlias = Union[
    RankByDivExprUnionMember7ExprUnionMember6ExprUnionMember0, RankByDivExprUnionMember7ExprUnionMember6ExprUnionMember1
]


class RankByDivExprUnionMember7ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExprUnionMember7ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByDivExprUnionMember7ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByDivExprUnionMember7ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByDivExprUnionMember7ExprUnionMember7Expr: TypeAlias = Union[
    RankByDivExprUnionMember7ExprUnionMember7ExprUnionMember0, RankByDivExprUnionMember7ExprUnionMember7ExprUnionMember1
]


class RankByDivExprUnionMember7ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByDivExprUnionMember7ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByDivExprUnionMember7Expr: TypeAlias = Union[
    RankByDivExprUnionMember7ExprUnionMember0,
    RankByDivExprUnionMember7ExprUnionMember1,
    RankByDivExprUnionMember7ExprUnionMember2,
    RankByDivExprUnionMember7ExprUnionMember3,
    RankByDivExprUnionMember7ExprUnionMember4,
    RankByDivExprUnionMember7ExprUnionMember5,
    RankByDivExprUnionMember7ExprUnionMember6,
    RankByDivExprUnionMember7ExprUnionMember7,
]


class RankByDivExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByDivExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByDivExpr: TypeAlias = Union[
    RankByDivExprUnionMember0,
    RankByDivExprUnionMember1,
    RankByDivExprUnionMember2,
    RankByDivExprUnionMember3,
    RankByDivExprUnionMember4,
    RankByDivExprUnionMember5,
    RankByDivExprUnionMember6,
    RankByDivExprUnionMember7,
]


class RankByDiv(TypedDict, total=False):
    exprs: Required[Iterable[RankByDivExpr]]

    type: Required[Literal["Div"]]


class RankByMaxExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByMaxExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByMaxExprUnionMember2ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember2ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember2ExprUnionMember2Expr: TypeAlias = Union[
    RankByMaxExprUnionMember2ExprUnionMember2ExprUnionMember0, RankByMaxExprUnionMember2ExprUnionMember2ExprUnionMember1
]


class RankByMaxExprUnionMember2ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember2ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMaxExprUnionMember2ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember2ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember2ExprUnionMember3Expr: TypeAlias = Union[
    RankByMaxExprUnionMember2ExprUnionMember3ExprUnionMember0, RankByMaxExprUnionMember2ExprUnionMember3ExprUnionMember1
]


class RankByMaxExprUnionMember2ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember2ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByMaxExprUnionMember2ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember2ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember2ExprUnionMember4Expr: TypeAlias = Union[
    RankByMaxExprUnionMember2ExprUnionMember4ExprUnionMember0, RankByMaxExprUnionMember2ExprUnionMember4ExprUnionMember1
]


class RankByMaxExprUnionMember2ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember2ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByMaxExprUnionMember2ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember2ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember2ExprUnionMember5Expr: TypeAlias = Union[
    RankByMaxExprUnionMember2ExprUnionMember5ExprUnionMember0, RankByMaxExprUnionMember2ExprUnionMember5ExprUnionMember1
]


class RankByMaxExprUnionMember2ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember2ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByMaxExprUnionMember2ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember2ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember2ExprUnionMember6Expr: TypeAlias = Union[
    RankByMaxExprUnionMember2ExprUnionMember6ExprUnionMember0, RankByMaxExprUnionMember2ExprUnionMember6ExprUnionMember1
]


class RankByMaxExprUnionMember2ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember2ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByMaxExprUnionMember2ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember2ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember2ExprUnionMember7Expr: TypeAlias = Union[
    RankByMaxExprUnionMember2ExprUnionMember7ExprUnionMember0, RankByMaxExprUnionMember2ExprUnionMember7ExprUnionMember1
]


class RankByMaxExprUnionMember2ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMaxExprUnionMember2ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByMaxExprUnionMember2Expr: TypeAlias = Union[
    RankByMaxExprUnionMember2ExprUnionMember0,
    RankByMaxExprUnionMember2ExprUnionMember1,
    RankByMaxExprUnionMember2ExprUnionMember2,
    RankByMaxExprUnionMember2ExprUnionMember3,
    RankByMaxExprUnionMember2ExprUnionMember4,
    RankByMaxExprUnionMember2ExprUnionMember5,
    RankByMaxExprUnionMember2ExprUnionMember6,
    RankByMaxExprUnionMember2ExprUnionMember7,
]


class RankByMaxExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMaxExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByMaxExprUnionMember3ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember3ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember3ExprUnionMember2Expr: TypeAlias = Union[
    RankByMaxExprUnionMember3ExprUnionMember2ExprUnionMember0, RankByMaxExprUnionMember3ExprUnionMember2ExprUnionMember1
]


class RankByMaxExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember3ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMaxExprUnionMember3ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember3ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember3ExprUnionMember3Expr: TypeAlias = Union[
    RankByMaxExprUnionMember3ExprUnionMember3ExprUnionMember0, RankByMaxExprUnionMember3ExprUnionMember3ExprUnionMember1
]


class RankByMaxExprUnionMember3ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember3ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByMaxExprUnionMember3ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember3ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember3ExprUnionMember4Expr: TypeAlias = Union[
    RankByMaxExprUnionMember3ExprUnionMember4ExprUnionMember0, RankByMaxExprUnionMember3ExprUnionMember4ExprUnionMember1
]


class RankByMaxExprUnionMember3ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember3ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByMaxExprUnionMember3ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember3ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember3ExprUnionMember5Expr: TypeAlias = Union[
    RankByMaxExprUnionMember3ExprUnionMember5ExprUnionMember0, RankByMaxExprUnionMember3ExprUnionMember5ExprUnionMember1
]


class RankByMaxExprUnionMember3ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember3ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByMaxExprUnionMember3ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember3ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember3ExprUnionMember6Expr: TypeAlias = Union[
    RankByMaxExprUnionMember3ExprUnionMember6ExprUnionMember0, RankByMaxExprUnionMember3ExprUnionMember6ExprUnionMember1
]


class RankByMaxExprUnionMember3ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember3ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByMaxExprUnionMember3ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember3ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember3ExprUnionMember7Expr: TypeAlias = Union[
    RankByMaxExprUnionMember3ExprUnionMember7ExprUnionMember0, RankByMaxExprUnionMember3ExprUnionMember7ExprUnionMember1
]


class RankByMaxExprUnionMember3ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMaxExprUnionMember3ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByMaxExprUnionMember3Expr: TypeAlias = Union[
    RankByMaxExprUnionMember3ExprUnionMember0,
    RankByMaxExprUnionMember3ExprUnionMember1,
    RankByMaxExprUnionMember3ExprUnionMember2,
    RankByMaxExprUnionMember3ExprUnionMember3,
    RankByMaxExprUnionMember3ExprUnionMember4,
    RankByMaxExprUnionMember3ExprUnionMember5,
    RankByMaxExprUnionMember3ExprUnionMember6,
    RankByMaxExprUnionMember3ExprUnionMember7,
]


class RankByMaxExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByMaxExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByMaxExprUnionMember4ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember4ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember4ExprUnionMember2Expr: TypeAlias = Union[
    RankByMaxExprUnionMember4ExprUnionMember2ExprUnionMember0, RankByMaxExprUnionMember4ExprUnionMember2ExprUnionMember1
]


class RankByMaxExprUnionMember4ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember4ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMaxExprUnionMember4ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember4ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember4ExprUnionMember3Expr: TypeAlias = Union[
    RankByMaxExprUnionMember4ExprUnionMember3ExprUnionMember0, RankByMaxExprUnionMember4ExprUnionMember3ExprUnionMember1
]


class RankByMaxExprUnionMember4ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember4ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByMaxExprUnionMember4ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember4ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember4ExprUnionMember4Expr: TypeAlias = Union[
    RankByMaxExprUnionMember4ExprUnionMember4ExprUnionMember0, RankByMaxExprUnionMember4ExprUnionMember4ExprUnionMember1
]


class RankByMaxExprUnionMember4ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember4ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByMaxExprUnionMember4ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember4ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember4ExprUnionMember5Expr: TypeAlias = Union[
    RankByMaxExprUnionMember4ExprUnionMember5ExprUnionMember0, RankByMaxExprUnionMember4ExprUnionMember5ExprUnionMember1
]


class RankByMaxExprUnionMember4ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember4ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByMaxExprUnionMember4ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember4ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember4ExprUnionMember6Expr: TypeAlias = Union[
    RankByMaxExprUnionMember4ExprUnionMember6ExprUnionMember0, RankByMaxExprUnionMember4ExprUnionMember6ExprUnionMember1
]


class RankByMaxExprUnionMember4ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember4ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByMaxExprUnionMember4ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember4ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember4ExprUnionMember7Expr: TypeAlias = Union[
    RankByMaxExprUnionMember4ExprUnionMember7ExprUnionMember0, RankByMaxExprUnionMember4ExprUnionMember7ExprUnionMember1
]


class RankByMaxExprUnionMember4ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMaxExprUnionMember4ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByMaxExprUnionMember4Expr: TypeAlias = Union[
    RankByMaxExprUnionMember4ExprUnionMember0,
    RankByMaxExprUnionMember4ExprUnionMember1,
    RankByMaxExprUnionMember4ExprUnionMember2,
    RankByMaxExprUnionMember4ExprUnionMember3,
    RankByMaxExprUnionMember4ExprUnionMember4,
    RankByMaxExprUnionMember4ExprUnionMember5,
    RankByMaxExprUnionMember4ExprUnionMember6,
    RankByMaxExprUnionMember4ExprUnionMember7,
]


class RankByMaxExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByMaxExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByMaxExprUnionMember5ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember5ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember5ExprUnionMember2Expr: TypeAlias = Union[
    RankByMaxExprUnionMember5ExprUnionMember2ExprUnionMember0, RankByMaxExprUnionMember5ExprUnionMember2ExprUnionMember1
]


class RankByMaxExprUnionMember5ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember5ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMaxExprUnionMember5ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember5ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember5ExprUnionMember3Expr: TypeAlias = Union[
    RankByMaxExprUnionMember5ExprUnionMember3ExprUnionMember0, RankByMaxExprUnionMember5ExprUnionMember3ExprUnionMember1
]


class RankByMaxExprUnionMember5ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember5ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByMaxExprUnionMember5ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember5ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember5ExprUnionMember4Expr: TypeAlias = Union[
    RankByMaxExprUnionMember5ExprUnionMember4ExprUnionMember0, RankByMaxExprUnionMember5ExprUnionMember4ExprUnionMember1
]


class RankByMaxExprUnionMember5ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember5ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByMaxExprUnionMember5ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember5ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember5ExprUnionMember5Expr: TypeAlias = Union[
    RankByMaxExprUnionMember5ExprUnionMember5ExprUnionMember0, RankByMaxExprUnionMember5ExprUnionMember5ExprUnionMember1
]


class RankByMaxExprUnionMember5ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember5ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByMaxExprUnionMember5ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember5ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember5ExprUnionMember6Expr: TypeAlias = Union[
    RankByMaxExprUnionMember5ExprUnionMember6ExprUnionMember0, RankByMaxExprUnionMember5ExprUnionMember6ExprUnionMember1
]


class RankByMaxExprUnionMember5ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember5ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByMaxExprUnionMember5ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember5ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember5ExprUnionMember7Expr: TypeAlias = Union[
    RankByMaxExprUnionMember5ExprUnionMember7ExprUnionMember0, RankByMaxExprUnionMember5ExprUnionMember7ExprUnionMember1
]


class RankByMaxExprUnionMember5ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMaxExprUnionMember5ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByMaxExprUnionMember5Expr: TypeAlias = Union[
    RankByMaxExprUnionMember5ExprUnionMember0,
    RankByMaxExprUnionMember5ExprUnionMember1,
    RankByMaxExprUnionMember5ExprUnionMember2,
    RankByMaxExprUnionMember5ExprUnionMember3,
    RankByMaxExprUnionMember5ExprUnionMember4,
    RankByMaxExprUnionMember5ExprUnionMember5,
    RankByMaxExprUnionMember5ExprUnionMember6,
    RankByMaxExprUnionMember5ExprUnionMember7,
]


class RankByMaxExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByMaxExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByMaxExprUnionMember6ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember6ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember6ExprUnionMember2Expr: TypeAlias = Union[
    RankByMaxExprUnionMember6ExprUnionMember2ExprUnionMember0, RankByMaxExprUnionMember6ExprUnionMember2ExprUnionMember1
]


class RankByMaxExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember6ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMaxExprUnionMember6ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember6ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember6ExprUnionMember3Expr: TypeAlias = Union[
    RankByMaxExprUnionMember6ExprUnionMember3ExprUnionMember0, RankByMaxExprUnionMember6ExprUnionMember3ExprUnionMember1
]


class RankByMaxExprUnionMember6ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember6ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByMaxExprUnionMember6ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember6ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember6ExprUnionMember4Expr: TypeAlias = Union[
    RankByMaxExprUnionMember6ExprUnionMember4ExprUnionMember0, RankByMaxExprUnionMember6ExprUnionMember4ExprUnionMember1
]


class RankByMaxExprUnionMember6ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember6ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByMaxExprUnionMember6ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember6ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember6ExprUnionMember5Expr: TypeAlias = Union[
    RankByMaxExprUnionMember6ExprUnionMember5ExprUnionMember0, RankByMaxExprUnionMember6ExprUnionMember5ExprUnionMember1
]


class RankByMaxExprUnionMember6ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember6ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByMaxExprUnionMember6ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember6ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember6ExprUnionMember6Expr: TypeAlias = Union[
    RankByMaxExprUnionMember6ExprUnionMember6ExprUnionMember0, RankByMaxExprUnionMember6ExprUnionMember6ExprUnionMember1
]


class RankByMaxExprUnionMember6ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember6ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByMaxExprUnionMember6ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember6ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember6ExprUnionMember7Expr: TypeAlias = Union[
    RankByMaxExprUnionMember6ExprUnionMember7ExprUnionMember0, RankByMaxExprUnionMember6ExprUnionMember7ExprUnionMember1
]


class RankByMaxExprUnionMember6ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMaxExprUnionMember6ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByMaxExprUnionMember6Expr: TypeAlias = Union[
    RankByMaxExprUnionMember6ExprUnionMember0,
    RankByMaxExprUnionMember6ExprUnionMember1,
    RankByMaxExprUnionMember6ExprUnionMember2,
    RankByMaxExprUnionMember6ExprUnionMember3,
    RankByMaxExprUnionMember6ExprUnionMember4,
    RankByMaxExprUnionMember6ExprUnionMember5,
    RankByMaxExprUnionMember6ExprUnionMember6,
    RankByMaxExprUnionMember6ExprUnionMember7,
]


class RankByMaxExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByMaxExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByMaxExprUnionMember7ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember7ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember7ExprUnionMember2Expr: TypeAlias = Union[
    RankByMaxExprUnionMember7ExprUnionMember2ExprUnionMember0, RankByMaxExprUnionMember7ExprUnionMember2ExprUnionMember1
]


class RankByMaxExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember7ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMaxExprUnionMember7ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember7ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember7ExprUnionMember3Expr: TypeAlias = Union[
    RankByMaxExprUnionMember7ExprUnionMember3ExprUnionMember0, RankByMaxExprUnionMember7ExprUnionMember3ExprUnionMember1
]


class RankByMaxExprUnionMember7ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember7ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByMaxExprUnionMember7ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember7ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember7ExprUnionMember4Expr: TypeAlias = Union[
    RankByMaxExprUnionMember7ExprUnionMember4ExprUnionMember0, RankByMaxExprUnionMember7ExprUnionMember4ExprUnionMember1
]


class RankByMaxExprUnionMember7ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember7ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByMaxExprUnionMember7ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember7ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember7ExprUnionMember5Expr: TypeAlias = Union[
    RankByMaxExprUnionMember7ExprUnionMember5ExprUnionMember0, RankByMaxExprUnionMember7ExprUnionMember5ExprUnionMember1
]


class RankByMaxExprUnionMember7ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember7ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByMaxExprUnionMember7ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember7ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember7ExprUnionMember6Expr: TypeAlias = Union[
    RankByMaxExprUnionMember7ExprUnionMember6ExprUnionMember0, RankByMaxExprUnionMember7ExprUnionMember6ExprUnionMember1
]


class RankByMaxExprUnionMember7ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember7ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByMaxExprUnionMember7ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember7ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember7ExprUnionMember7Expr: TypeAlias = Union[
    RankByMaxExprUnionMember7ExprUnionMember7ExprUnionMember0, RankByMaxExprUnionMember7ExprUnionMember7ExprUnionMember1
]


class RankByMaxExprUnionMember7ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMaxExprUnionMember7ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByMaxExprUnionMember7Expr: TypeAlias = Union[
    RankByMaxExprUnionMember7ExprUnionMember0,
    RankByMaxExprUnionMember7ExprUnionMember1,
    RankByMaxExprUnionMember7ExprUnionMember2,
    RankByMaxExprUnionMember7ExprUnionMember3,
    RankByMaxExprUnionMember7ExprUnionMember4,
    RankByMaxExprUnionMember7ExprUnionMember5,
    RankByMaxExprUnionMember7ExprUnionMember6,
    RankByMaxExprUnionMember7ExprUnionMember7,
]


class RankByMaxExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMaxExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByMaxExpr: TypeAlias = Union[
    RankByMaxExprUnionMember0,
    RankByMaxExprUnionMember1,
    RankByMaxExprUnionMember2,
    RankByMaxExprUnionMember3,
    RankByMaxExprUnionMember4,
    RankByMaxExprUnionMember5,
    RankByMaxExprUnionMember6,
    RankByMaxExprUnionMember7,
]


class RankByMax(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExpr]]

    type: Required[Literal["Max"]]


class RankByMinExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByMinExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByMinExprUnionMember2ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember2ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember2ExprUnionMember2Expr: TypeAlias = Union[
    RankByMinExprUnionMember2ExprUnionMember2ExprUnionMember0, RankByMinExprUnionMember2ExprUnionMember2ExprUnionMember1
]


class RankByMinExprUnionMember2ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember2ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMinExprUnionMember2ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember2ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember2ExprUnionMember3Expr: TypeAlias = Union[
    RankByMinExprUnionMember2ExprUnionMember3ExprUnionMember0, RankByMinExprUnionMember2ExprUnionMember3ExprUnionMember1
]


class RankByMinExprUnionMember2ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember2ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByMinExprUnionMember2ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember2ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember2ExprUnionMember4Expr: TypeAlias = Union[
    RankByMinExprUnionMember2ExprUnionMember4ExprUnionMember0, RankByMinExprUnionMember2ExprUnionMember4ExprUnionMember1
]


class RankByMinExprUnionMember2ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember2ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByMinExprUnionMember2ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember2ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember2ExprUnionMember5Expr: TypeAlias = Union[
    RankByMinExprUnionMember2ExprUnionMember5ExprUnionMember0, RankByMinExprUnionMember2ExprUnionMember5ExprUnionMember1
]


class RankByMinExprUnionMember2ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember2ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByMinExprUnionMember2ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember2ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember2ExprUnionMember6Expr: TypeAlias = Union[
    RankByMinExprUnionMember2ExprUnionMember6ExprUnionMember0, RankByMinExprUnionMember2ExprUnionMember6ExprUnionMember1
]


class RankByMinExprUnionMember2ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember2ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByMinExprUnionMember2ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember2ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember2ExprUnionMember7Expr: TypeAlias = Union[
    RankByMinExprUnionMember2ExprUnionMember7ExprUnionMember0, RankByMinExprUnionMember2ExprUnionMember7ExprUnionMember1
]


class RankByMinExprUnionMember2ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMinExprUnionMember2ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByMinExprUnionMember2Expr: TypeAlias = Union[
    RankByMinExprUnionMember2ExprUnionMember0,
    RankByMinExprUnionMember2ExprUnionMember1,
    RankByMinExprUnionMember2ExprUnionMember2,
    RankByMinExprUnionMember2ExprUnionMember3,
    RankByMinExprUnionMember2ExprUnionMember4,
    RankByMinExprUnionMember2ExprUnionMember5,
    RankByMinExprUnionMember2ExprUnionMember6,
    RankByMinExprUnionMember2ExprUnionMember7,
]


class RankByMinExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMinExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByMinExprUnionMember3ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember3ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember3ExprUnionMember2Expr: TypeAlias = Union[
    RankByMinExprUnionMember3ExprUnionMember2ExprUnionMember0, RankByMinExprUnionMember3ExprUnionMember2ExprUnionMember1
]


class RankByMinExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember3ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMinExprUnionMember3ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember3ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember3ExprUnionMember3Expr: TypeAlias = Union[
    RankByMinExprUnionMember3ExprUnionMember3ExprUnionMember0, RankByMinExprUnionMember3ExprUnionMember3ExprUnionMember1
]


class RankByMinExprUnionMember3ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember3ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByMinExprUnionMember3ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember3ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember3ExprUnionMember4Expr: TypeAlias = Union[
    RankByMinExprUnionMember3ExprUnionMember4ExprUnionMember0, RankByMinExprUnionMember3ExprUnionMember4ExprUnionMember1
]


class RankByMinExprUnionMember3ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember3ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByMinExprUnionMember3ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember3ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember3ExprUnionMember5Expr: TypeAlias = Union[
    RankByMinExprUnionMember3ExprUnionMember5ExprUnionMember0, RankByMinExprUnionMember3ExprUnionMember5ExprUnionMember1
]


class RankByMinExprUnionMember3ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember3ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByMinExprUnionMember3ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember3ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember3ExprUnionMember6Expr: TypeAlias = Union[
    RankByMinExprUnionMember3ExprUnionMember6ExprUnionMember0, RankByMinExprUnionMember3ExprUnionMember6ExprUnionMember1
]


class RankByMinExprUnionMember3ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember3ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByMinExprUnionMember3ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember3ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember3ExprUnionMember7Expr: TypeAlias = Union[
    RankByMinExprUnionMember3ExprUnionMember7ExprUnionMember0, RankByMinExprUnionMember3ExprUnionMember7ExprUnionMember1
]


class RankByMinExprUnionMember3ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMinExprUnionMember3ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByMinExprUnionMember3Expr: TypeAlias = Union[
    RankByMinExprUnionMember3ExprUnionMember0,
    RankByMinExprUnionMember3ExprUnionMember1,
    RankByMinExprUnionMember3ExprUnionMember2,
    RankByMinExprUnionMember3ExprUnionMember3,
    RankByMinExprUnionMember3ExprUnionMember4,
    RankByMinExprUnionMember3ExprUnionMember5,
    RankByMinExprUnionMember3ExprUnionMember6,
    RankByMinExprUnionMember3ExprUnionMember7,
]


class RankByMinExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByMinExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByMinExprUnionMember4ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember4ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember4ExprUnionMember2Expr: TypeAlias = Union[
    RankByMinExprUnionMember4ExprUnionMember2ExprUnionMember0, RankByMinExprUnionMember4ExprUnionMember2ExprUnionMember1
]


class RankByMinExprUnionMember4ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember4ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMinExprUnionMember4ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember4ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember4ExprUnionMember3Expr: TypeAlias = Union[
    RankByMinExprUnionMember4ExprUnionMember3ExprUnionMember0, RankByMinExprUnionMember4ExprUnionMember3ExprUnionMember1
]


class RankByMinExprUnionMember4ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember4ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByMinExprUnionMember4ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember4ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember4ExprUnionMember4Expr: TypeAlias = Union[
    RankByMinExprUnionMember4ExprUnionMember4ExprUnionMember0, RankByMinExprUnionMember4ExprUnionMember4ExprUnionMember1
]


class RankByMinExprUnionMember4ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember4ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByMinExprUnionMember4ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember4ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember4ExprUnionMember5Expr: TypeAlias = Union[
    RankByMinExprUnionMember4ExprUnionMember5ExprUnionMember0, RankByMinExprUnionMember4ExprUnionMember5ExprUnionMember1
]


class RankByMinExprUnionMember4ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember4ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByMinExprUnionMember4ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember4ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember4ExprUnionMember6Expr: TypeAlias = Union[
    RankByMinExprUnionMember4ExprUnionMember6ExprUnionMember0, RankByMinExprUnionMember4ExprUnionMember6ExprUnionMember1
]


class RankByMinExprUnionMember4ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember4ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByMinExprUnionMember4ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember4ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember4ExprUnionMember7Expr: TypeAlias = Union[
    RankByMinExprUnionMember4ExprUnionMember7ExprUnionMember0, RankByMinExprUnionMember4ExprUnionMember7ExprUnionMember1
]


class RankByMinExprUnionMember4ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMinExprUnionMember4ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByMinExprUnionMember4Expr: TypeAlias = Union[
    RankByMinExprUnionMember4ExprUnionMember0,
    RankByMinExprUnionMember4ExprUnionMember1,
    RankByMinExprUnionMember4ExprUnionMember2,
    RankByMinExprUnionMember4ExprUnionMember3,
    RankByMinExprUnionMember4ExprUnionMember4,
    RankByMinExprUnionMember4ExprUnionMember5,
    RankByMinExprUnionMember4ExprUnionMember6,
    RankByMinExprUnionMember4ExprUnionMember7,
]


class RankByMinExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByMinExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByMinExprUnionMember5ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember5ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember5ExprUnionMember2Expr: TypeAlias = Union[
    RankByMinExprUnionMember5ExprUnionMember2ExprUnionMember0, RankByMinExprUnionMember5ExprUnionMember2ExprUnionMember1
]


class RankByMinExprUnionMember5ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember5ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMinExprUnionMember5ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember5ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember5ExprUnionMember3Expr: TypeAlias = Union[
    RankByMinExprUnionMember5ExprUnionMember3ExprUnionMember0, RankByMinExprUnionMember5ExprUnionMember3ExprUnionMember1
]


class RankByMinExprUnionMember5ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember5ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByMinExprUnionMember5ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember5ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember5ExprUnionMember4Expr: TypeAlias = Union[
    RankByMinExprUnionMember5ExprUnionMember4ExprUnionMember0, RankByMinExprUnionMember5ExprUnionMember4ExprUnionMember1
]


class RankByMinExprUnionMember5ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember5ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByMinExprUnionMember5ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember5ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember5ExprUnionMember5Expr: TypeAlias = Union[
    RankByMinExprUnionMember5ExprUnionMember5ExprUnionMember0, RankByMinExprUnionMember5ExprUnionMember5ExprUnionMember1
]


class RankByMinExprUnionMember5ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember5ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByMinExprUnionMember5ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember5ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember5ExprUnionMember6Expr: TypeAlias = Union[
    RankByMinExprUnionMember5ExprUnionMember6ExprUnionMember0, RankByMinExprUnionMember5ExprUnionMember6ExprUnionMember1
]


class RankByMinExprUnionMember5ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember5ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByMinExprUnionMember5ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember5ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember5ExprUnionMember7Expr: TypeAlias = Union[
    RankByMinExprUnionMember5ExprUnionMember7ExprUnionMember0, RankByMinExprUnionMember5ExprUnionMember7ExprUnionMember1
]


class RankByMinExprUnionMember5ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMinExprUnionMember5ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByMinExprUnionMember5Expr: TypeAlias = Union[
    RankByMinExprUnionMember5ExprUnionMember0,
    RankByMinExprUnionMember5ExprUnionMember1,
    RankByMinExprUnionMember5ExprUnionMember2,
    RankByMinExprUnionMember5ExprUnionMember3,
    RankByMinExprUnionMember5ExprUnionMember4,
    RankByMinExprUnionMember5ExprUnionMember5,
    RankByMinExprUnionMember5ExprUnionMember6,
    RankByMinExprUnionMember5ExprUnionMember7,
]


class RankByMinExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByMinExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByMinExprUnionMember6ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember6ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember6ExprUnionMember2Expr: TypeAlias = Union[
    RankByMinExprUnionMember6ExprUnionMember2ExprUnionMember0, RankByMinExprUnionMember6ExprUnionMember2ExprUnionMember1
]


class RankByMinExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember6ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMinExprUnionMember6ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember6ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember6ExprUnionMember3Expr: TypeAlias = Union[
    RankByMinExprUnionMember6ExprUnionMember3ExprUnionMember0, RankByMinExprUnionMember6ExprUnionMember3ExprUnionMember1
]


class RankByMinExprUnionMember6ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember6ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByMinExprUnionMember6ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember6ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember6ExprUnionMember4Expr: TypeAlias = Union[
    RankByMinExprUnionMember6ExprUnionMember4ExprUnionMember0, RankByMinExprUnionMember6ExprUnionMember4ExprUnionMember1
]


class RankByMinExprUnionMember6ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember6ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByMinExprUnionMember6ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember6ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember6ExprUnionMember5Expr: TypeAlias = Union[
    RankByMinExprUnionMember6ExprUnionMember5ExprUnionMember0, RankByMinExprUnionMember6ExprUnionMember5ExprUnionMember1
]


class RankByMinExprUnionMember6ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember6ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByMinExprUnionMember6ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember6ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember6ExprUnionMember6Expr: TypeAlias = Union[
    RankByMinExprUnionMember6ExprUnionMember6ExprUnionMember0, RankByMinExprUnionMember6ExprUnionMember6ExprUnionMember1
]


class RankByMinExprUnionMember6ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember6ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByMinExprUnionMember6ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember6ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember6ExprUnionMember7Expr: TypeAlias = Union[
    RankByMinExprUnionMember6ExprUnionMember7ExprUnionMember0, RankByMinExprUnionMember6ExprUnionMember7ExprUnionMember1
]


class RankByMinExprUnionMember6ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMinExprUnionMember6ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByMinExprUnionMember6Expr: TypeAlias = Union[
    RankByMinExprUnionMember6ExprUnionMember0,
    RankByMinExprUnionMember6ExprUnionMember1,
    RankByMinExprUnionMember6ExprUnionMember2,
    RankByMinExprUnionMember6ExprUnionMember3,
    RankByMinExprUnionMember6ExprUnionMember4,
    RankByMinExprUnionMember6ExprUnionMember5,
    RankByMinExprUnionMember6ExprUnionMember6,
    RankByMinExprUnionMember6ExprUnionMember7,
]


class RankByMinExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByMinExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByMinExprUnionMember7ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember7ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember7ExprUnionMember2Expr: TypeAlias = Union[
    RankByMinExprUnionMember7ExprUnionMember2ExprUnionMember0, RankByMinExprUnionMember7ExprUnionMember2ExprUnionMember1
]


class RankByMinExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember7ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMinExprUnionMember7ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember7ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember7ExprUnionMember3Expr: TypeAlias = Union[
    RankByMinExprUnionMember7ExprUnionMember3ExprUnionMember0, RankByMinExprUnionMember7ExprUnionMember3ExprUnionMember1
]


class RankByMinExprUnionMember7ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember7ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByMinExprUnionMember7ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember7ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember7ExprUnionMember4Expr: TypeAlias = Union[
    RankByMinExprUnionMember7ExprUnionMember4ExprUnionMember0, RankByMinExprUnionMember7ExprUnionMember4ExprUnionMember1
]


class RankByMinExprUnionMember7ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember7ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByMinExprUnionMember7ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember7ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember7ExprUnionMember5Expr: TypeAlias = Union[
    RankByMinExprUnionMember7ExprUnionMember5ExprUnionMember0, RankByMinExprUnionMember7ExprUnionMember5ExprUnionMember1
]


class RankByMinExprUnionMember7ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember7ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByMinExprUnionMember7ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember7ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember7ExprUnionMember6Expr: TypeAlias = Union[
    RankByMinExprUnionMember7ExprUnionMember6ExprUnionMember0, RankByMinExprUnionMember7ExprUnionMember6ExprUnionMember1
]


class RankByMinExprUnionMember7ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember7ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByMinExprUnionMember7ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember7ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember7ExprUnionMember7Expr: TypeAlias = Union[
    RankByMinExprUnionMember7ExprUnionMember7ExprUnionMember0, RankByMinExprUnionMember7ExprUnionMember7ExprUnionMember1
]


class RankByMinExprUnionMember7ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMinExprUnionMember7ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByMinExprUnionMember7Expr: TypeAlias = Union[
    RankByMinExprUnionMember7ExprUnionMember0,
    RankByMinExprUnionMember7ExprUnionMember1,
    RankByMinExprUnionMember7ExprUnionMember2,
    RankByMinExprUnionMember7ExprUnionMember3,
    RankByMinExprUnionMember7ExprUnionMember4,
    RankByMinExprUnionMember7ExprUnionMember5,
    RankByMinExprUnionMember7ExprUnionMember6,
    RankByMinExprUnionMember7ExprUnionMember7,
]


class RankByMinExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMinExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByMinExpr: TypeAlias = Union[
    RankByMinExprUnionMember0,
    RankByMinExprUnionMember1,
    RankByMinExprUnionMember2,
    RankByMinExprUnionMember3,
    RankByMinExprUnionMember4,
    RankByMinExprUnionMember5,
    RankByMinExprUnionMember6,
    RankByMinExprUnionMember7,
]


class RankByMin(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExpr]]

    type: Required[Literal["Min"]]


class RankByLogExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByLogExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByLogExprUnionMember2ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember2ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember2ExprUnionMember2Expr: TypeAlias = Union[
    RankByLogExprUnionMember2ExprUnionMember2ExprUnionMember0, RankByLogExprUnionMember2ExprUnionMember2ExprUnionMember1
]


class RankByLogExprUnionMember2ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember2ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByLogExprUnionMember2ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember2ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember2ExprUnionMember3Expr: TypeAlias = Union[
    RankByLogExprUnionMember2ExprUnionMember3ExprUnionMember0, RankByLogExprUnionMember2ExprUnionMember3ExprUnionMember1
]


class RankByLogExprUnionMember2ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember2ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByLogExprUnionMember2ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember2ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember2ExprUnionMember4Expr: TypeAlias = Union[
    RankByLogExprUnionMember2ExprUnionMember4ExprUnionMember0, RankByLogExprUnionMember2ExprUnionMember4ExprUnionMember1
]


class RankByLogExprUnionMember2ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember2ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByLogExprUnionMember2ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember2ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember2ExprUnionMember5Expr: TypeAlias = Union[
    RankByLogExprUnionMember2ExprUnionMember5ExprUnionMember0, RankByLogExprUnionMember2ExprUnionMember5ExprUnionMember1
]


class RankByLogExprUnionMember2ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember2ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByLogExprUnionMember2ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember2ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember2ExprUnionMember6Expr: TypeAlias = Union[
    RankByLogExprUnionMember2ExprUnionMember6ExprUnionMember0, RankByLogExprUnionMember2ExprUnionMember6ExprUnionMember1
]


class RankByLogExprUnionMember2ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember2ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByLogExprUnionMember2ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember2ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember2ExprUnionMember7Expr: TypeAlias = Union[
    RankByLogExprUnionMember2ExprUnionMember7ExprUnionMember0, RankByLogExprUnionMember2ExprUnionMember7ExprUnionMember1
]


class RankByLogExprUnionMember2ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByLogExprUnionMember2ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByLogExprUnionMember2Expr: TypeAlias = Union[
    RankByLogExprUnionMember2ExprUnionMember0,
    RankByLogExprUnionMember2ExprUnionMember1,
    RankByLogExprUnionMember2ExprUnionMember2,
    RankByLogExprUnionMember2ExprUnionMember3,
    RankByLogExprUnionMember2ExprUnionMember4,
    RankByLogExprUnionMember2ExprUnionMember5,
    RankByLogExprUnionMember2ExprUnionMember6,
    RankByLogExprUnionMember2ExprUnionMember7,
]


class RankByLogExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByLogExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByLogExprUnionMember3ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember3ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember3ExprUnionMember2Expr: TypeAlias = Union[
    RankByLogExprUnionMember3ExprUnionMember2ExprUnionMember0, RankByLogExprUnionMember3ExprUnionMember2ExprUnionMember1
]


class RankByLogExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember3ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByLogExprUnionMember3ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember3ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember3ExprUnionMember3Expr: TypeAlias = Union[
    RankByLogExprUnionMember3ExprUnionMember3ExprUnionMember0, RankByLogExprUnionMember3ExprUnionMember3ExprUnionMember1
]


class RankByLogExprUnionMember3ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember3ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByLogExprUnionMember3ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember3ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember3ExprUnionMember4Expr: TypeAlias = Union[
    RankByLogExprUnionMember3ExprUnionMember4ExprUnionMember0, RankByLogExprUnionMember3ExprUnionMember4ExprUnionMember1
]


class RankByLogExprUnionMember3ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember3ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByLogExprUnionMember3ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember3ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember3ExprUnionMember5Expr: TypeAlias = Union[
    RankByLogExprUnionMember3ExprUnionMember5ExprUnionMember0, RankByLogExprUnionMember3ExprUnionMember5ExprUnionMember1
]


class RankByLogExprUnionMember3ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember3ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByLogExprUnionMember3ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember3ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember3ExprUnionMember6Expr: TypeAlias = Union[
    RankByLogExprUnionMember3ExprUnionMember6ExprUnionMember0, RankByLogExprUnionMember3ExprUnionMember6ExprUnionMember1
]


class RankByLogExprUnionMember3ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember3ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByLogExprUnionMember3ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember3ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember3ExprUnionMember7Expr: TypeAlias = Union[
    RankByLogExprUnionMember3ExprUnionMember7ExprUnionMember0, RankByLogExprUnionMember3ExprUnionMember7ExprUnionMember1
]


class RankByLogExprUnionMember3ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByLogExprUnionMember3ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByLogExprUnionMember3Expr: TypeAlias = Union[
    RankByLogExprUnionMember3ExprUnionMember0,
    RankByLogExprUnionMember3ExprUnionMember1,
    RankByLogExprUnionMember3ExprUnionMember2,
    RankByLogExprUnionMember3ExprUnionMember3,
    RankByLogExprUnionMember3ExprUnionMember4,
    RankByLogExprUnionMember3ExprUnionMember5,
    RankByLogExprUnionMember3ExprUnionMember6,
    RankByLogExprUnionMember3ExprUnionMember7,
]


class RankByLogExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByLogExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByLogExprUnionMember4ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember4ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember4ExprUnionMember2Expr: TypeAlias = Union[
    RankByLogExprUnionMember4ExprUnionMember2ExprUnionMember0, RankByLogExprUnionMember4ExprUnionMember2ExprUnionMember1
]


class RankByLogExprUnionMember4ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember4ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByLogExprUnionMember4ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember4ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember4ExprUnionMember3Expr: TypeAlias = Union[
    RankByLogExprUnionMember4ExprUnionMember3ExprUnionMember0, RankByLogExprUnionMember4ExprUnionMember3ExprUnionMember1
]


class RankByLogExprUnionMember4ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember4ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByLogExprUnionMember4ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember4ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember4ExprUnionMember4Expr: TypeAlias = Union[
    RankByLogExprUnionMember4ExprUnionMember4ExprUnionMember0, RankByLogExprUnionMember4ExprUnionMember4ExprUnionMember1
]


class RankByLogExprUnionMember4ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember4ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByLogExprUnionMember4ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember4ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember4ExprUnionMember5Expr: TypeAlias = Union[
    RankByLogExprUnionMember4ExprUnionMember5ExprUnionMember0, RankByLogExprUnionMember4ExprUnionMember5ExprUnionMember1
]


class RankByLogExprUnionMember4ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember4ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByLogExprUnionMember4ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember4ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember4ExprUnionMember6Expr: TypeAlias = Union[
    RankByLogExprUnionMember4ExprUnionMember6ExprUnionMember0, RankByLogExprUnionMember4ExprUnionMember6ExprUnionMember1
]


class RankByLogExprUnionMember4ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember4ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByLogExprUnionMember4ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember4ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember4ExprUnionMember7Expr: TypeAlias = Union[
    RankByLogExprUnionMember4ExprUnionMember7ExprUnionMember0, RankByLogExprUnionMember4ExprUnionMember7ExprUnionMember1
]


class RankByLogExprUnionMember4ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByLogExprUnionMember4ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByLogExprUnionMember4Expr: TypeAlias = Union[
    RankByLogExprUnionMember4ExprUnionMember0,
    RankByLogExprUnionMember4ExprUnionMember1,
    RankByLogExprUnionMember4ExprUnionMember2,
    RankByLogExprUnionMember4ExprUnionMember3,
    RankByLogExprUnionMember4ExprUnionMember4,
    RankByLogExprUnionMember4ExprUnionMember5,
    RankByLogExprUnionMember4ExprUnionMember6,
    RankByLogExprUnionMember4ExprUnionMember7,
]


class RankByLogExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByLogExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByLogExprUnionMember5ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember5ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember5ExprUnionMember2Expr: TypeAlias = Union[
    RankByLogExprUnionMember5ExprUnionMember2ExprUnionMember0, RankByLogExprUnionMember5ExprUnionMember2ExprUnionMember1
]


class RankByLogExprUnionMember5ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember5ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByLogExprUnionMember5ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember5ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember5ExprUnionMember3Expr: TypeAlias = Union[
    RankByLogExprUnionMember5ExprUnionMember3ExprUnionMember0, RankByLogExprUnionMember5ExprUnionMember3ExprUnionMember1
]


class RankByLogExprUnionMember5ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember5ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByLogExprUnionMember5ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember5ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember5ExprUnionMember4Expr: TypeAlias = Union[
    RankByLogExprUnionMember5ExprUnionMember4ExprUnionMember0, RankByLogExprUnionMember5ExprUnionMember4ExprUnionMember1
]


class RankByLogExprUnionMember5ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember5ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByLogExprUnionMember5ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember5ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember5ExprUnionMember5Expr: TypeAlias = Union[
    RankByLogExprUnionMember5ExprUnionMember5ExprUnionMember0, RankByLogExprUnionMember5ExprUnionMember5ExprUnionMember1
]


class RankByLogExprUnionMember5ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember5ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByLogExprUnionMember5ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember5ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember5ExprUnionMember6Expr: TypeAlias = Union[
    RankByLogExprUnionMember5ExprUnionMember6ExprUnionMember0, RankByLogExprUnionMember5ExprUnionMember6ExprUnionMember1
]


class RankByLogExprUnionMember5ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember5ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByLogExprUnionMember5ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember5ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember5ExprUnionMember7Expr: TypeAlias = Union[
    RankByLogExprUnionMember5ExprUnionMember7ExprUnionMember0, RankByLogExprUnionMember5ExprUnionMember7ExprUnionMember1
]


class RankByLogExprUnionMember5ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByLogExprUnionMember5ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByLogExprUnionMember5Expr: TypeAlias = Union[
    RankByLogExprUnionMember5ExprUnionMember0,
    RankByLogExprUnionMember5ExprUnionMember1,
    RankByLogExprUnionMember5ExprUnionMember2,
    RankByLogExprUnionMember5ExprUnionMember3,
    RankByLogExprUnionMember5ExprUnionMember4,
    RankByLogExprUnionMember5ExprUnionMember5,
    RankByLogExprUnionMember5ExprUnionMember6,
    RankByLogExprUnionMember5ExprUnionMember7,
]


class RankByLogExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByLogExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByLogExprUnionMember6ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember6ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember6ExprUnionMember2Expr: TypeAlias = Union[
    RankByLogExprUnionMember6ExprUnionMember2ExprUnionMember0, RankByLogExprUnionMember6ExprUnionMember2ExprUnionMember1
]


class RankByLogExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember6ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByLogExprUnionMember6ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember6ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember6ExprUnionMember3Expr: TypeAlias = Union[
    RankByLogExprUnionMember6ExprUnionMember3ExprUnionMember0, RankByLogExprUnionMember6ExprUnionMember3ExprUnionMember1
]


class RankByLogExprUnionMember6ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember6ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByLogExprUnionMember6ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember6ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember6ExprUnionMember4Expr: TypeAlias = Union[
    RankByLogExprUnionMember6ExprUnionMember4ExprUnionMember0, RankByLogExprUnionMember6ExprUnionMember4ExprUnionMember1
]


class RankByLogExprUnionMember6ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember6ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByLogExprUnionMember6ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember6ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember6ExprUnionMember5Expr: TypeAlias = Union[
    RankByLogExprUnionMember6ExprUnionMember5ExprUnionMember0, RankByLogExprUnionMember6ExprUnionMember5ExprUnionMember1
]


class RankByLogExprUnionMember6ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember6ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByLogExprUnionMember6ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember6ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember6ExprUnionMember6Expr: TypeAlias = Union[
    RankByLogExprUnionMember6ExprUnionMember6ExprUnionMember0, RankByLogExprUnionMember6ExprUnionMember6ExprUnionMember1
]


class RankByLogExprUnionMember6ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember6ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByLogExprUnionMember6ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember6ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember6ExprUnionMember7Expr: TypeAlias = Union[
    RankByLogExprUnionMember6ExprUnionMember7ExprUnionMember0, RankByLogExprUnionMember6ExprUnionMember7ExprUnionMember1
]


class RankByLogExprUnionMember6ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByLogExprUnionMember6ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByLogExprUnionMember6Expr: TypeAlias = Union[
    RankByLogExprUnionMember6ExprUnionMember0,
    RankByLogExprUnionMember6ExprUnionMember1,
    RankByLogExprUnionMember6ExprUnionMember2,
    RankByLogExprUnionMember6ExprUnionMember3,
    RankByLogExprUnionMember6ExprUnionMember4,
    RankByLogExprUnionMember6ExprUnionMember5,
    RankByLogExprUnionMember6ExprUnionMember6,
    RankByLogExprUnionMember6ExprUnionMember7,
]


class RankByLogExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByLogExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByLogExprUnionMember7ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember7ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember7ExprUnionMember2Expr: TypeAlias = Union[
    RankByLogExprUnionMember7ExprUnionMember2ExprUnionMember0, RankByLogExprUnionMember7ExprUnionMember2ExprUnionMember1
]


class RankByLogExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember7ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByLogExprUnionMember7ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember7ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember7ExprUnionMember3Expr: TypeAlias = Union[
    RankByLogExprUnionMember7ExprUnionMember3ExprUnionMember0, RankByLogExprUnionMember7ExprUnionMember3ExprUnionMember1
]


class RankByLogExprUnionMember7ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember7ExprUnionMember3Expr]]

    type: Required[Literal["Mult"]]


class RankByLogExprUnionMember7ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember7ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember7ExprUnionMember4Expr: TypeAlias = Union[
    RankByLogExprUnionMember7ExprUnionMember4ExprUnionMember0, RankByLogExprUnionMember7ExprUnionMember4ExprUnionMember1
]


class RankByLogExprUnionMember7ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember7ExprUnionMember4Expr]]

    type: Required[Literal["Div"]]


class RankByLogExprUnionMember7ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember7ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember7ExprUnionMember5Expr: TypeAlias = Union[
    RankByLogExprUnionMember7ExprUnionMember5ExprUnionMember0, RankByLogExprUnionMember7ExprUnionMember5ExprUnionMember1
]


class RankByLogExprUnionMember7ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember7ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByLogExprUnionMember7ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember7ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember7ExprUnionMember6Expr: TypeAlias = Union[
    RankByLogExprUnionMember7ExprUnionMember6ExprUnionMember0, RankByLogExprUnionMember7ExprUnionMember6ExprUnionMember1
]


class RankByLogExprUnionMember7ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember7ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByLogExprUnionMember7ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember7ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember7ExprUnionMember7Expr: TypeAlias = Union[
    RankByLogExprUnionMember7ExprUnionMember7ExprUnionMember0, RankByLogExprUnionMember7ExprUnionMember7ExprUnionMember1
]


class RankByLogExprUnionMember7ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByLogExprUnionMember7ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByLogExprUnionMember7Expr: TypeAlias = Union[
    RankByLogExprUnionMember7ExprUnionMember0,
    RankByLogExprUnionMember7ExprUnionMember1,
    RankByLogExprUnionMember7ExprUnionMember2,
    RankByLogExprUnionMember7ExprUnionMember3,
    RankByLogExprUnionMember7ExprUnionMember4,
    RankByLogExprUnionMember7ExprUnionMember5,
    RankByLogExprUnionMember7ExprUnionMember6,
    RankByLogExprUnionMember7ExprUnionMember7,
]


class RankByLogExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByLogExprUnionMember7Expr]

    type: Required[Literal["Log"]]


RankByLogExpr: TypeAlias = Union[
    RankByLogExprUnionMember0,
    RankByLogExprUnionMember1,
    RankByLogExprUnionMember2,
    RankByLogExprUnionMember3,
    RankByLogExprUnionMember4,
    RankByLogExprUnionMember5,
    RankByLogExprUnionMember6,
    RankByLogExprUnionMember7,
]


class RankByLog(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByLogExpr]

    type: Required[Literal["Log"]]


RankBy: TypeAlias = Union[RankByAttr, RankByConst, RankBySum, RankByMult, RankByDiv, RankByMax, RankByMin, RankByLog]
