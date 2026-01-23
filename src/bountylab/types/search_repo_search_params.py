# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "SearchRepoSearchParams",
    "Filters",
    "FiltersUnionMember0",
    "FiltersUnionMember1",
    "FiltersUnionMember2",
    "FiltersUnionMember3",
    "FiltersUnionMember4",
    "FiltersUnionMember5",
    "FiltersUnionMember6",
    "FiltersUnionMember7",
    "FiltersUnionMember8",
    "FiltersUnionMember9",
    "FiltersUnionMember10",
    "FiltersUnionMember11",
    "FiltersUnionMember12",
    "FiltersUnionMember13",
    "FiltersUnionMember14",
    "FiltersUnionMember15",
    "FiltersUnionMember16",
    "FiltersUnionMember17",
    "FiltersUnionMember18",
    "FiltersUnionMember19",
    "FiltersUnionMember20",
    "FiltersUnionMember21",
    "FiltersUnionMember22",
    "FiltersUnionMember23",
    "FiltersUnionMember24",
    "FiltersUnionMember25",
    "FiltersUnionMember26",
    "FiltersUnionMember27",
    "FiltersUnionMember28",
    "FiltersUnionMember29",
    "FiltersUnionMember30",
    "FiltersUnionMember31",
    "FiltersUnionMember32",
    "FiltersUnionMember33",
    "FiltersUnionMember34",
    "FiltersUnionMember35",
    "FiltersUnionMember36",
    "FiltersUnionMember37",
    "FiltersUnionMember38",
    "FiltersUnionMember39",
    "FiltersUnionMember40",
    "FiltersUnionMember41",
    "FiltersUnionMember42",
    "FiltersUnionMember43",
    "FiltersUnionMember44",
    "FiltersUnionMember45",
    "FiltersUnionMember46",
    "FiltersUnionMember47",
    "FiltersUnionMember48",
    "FiltersUnionMember49",
    "FiltersUnionMember50",
    "FiltersUnionMember51",
    "FiltersUnionMember52",
    "FiltersUnionMember53",
    "FiltersUnionMember54",
    "FiltersUnionMember55",
    "FiltersUnionMember56",
    "FiltersUnionMember57",
    "FiltersUnionMember58",
    "FiltersUnionMember59",
    "FiltersUnionMember60",
    "FiltersUnionMember61",
    "FiltersUnionMember62",
    "FiltersUnionMember63",
    "FiltersUnionMember64",
    "FiltersUnionMember65",
    "FiltersUnionMember66",
    "FiltersUnionMember67",
    "FiltersUnionMember68",
    "FiltersUnionMember69",
    "FiltersUnionMember70",
    "FiltersUnionMember71",
    "FiltersUnionMember72",
    "FiltersUnionMember73",
    "FiltersUnionMember74",
    "FiltersUnionMember75",
    "FiltersUnionMember76",
    "FiltersUnionMember77",
    "FiltersUnionMember78",
    "FiltersUnionMember79",
    "FiltersUnionMember80",
    "FiltersUnionMember81",
    "FiltersUnionMember82",
    "FiltersUnionMember83",
    "FiltersUnionMember84",
    "FiltersUnionMember85",
    "FiltersUnionMember86",
    "FiltersUnionMember87",
    "FiltersUnionMember88",
    "FiltersUnionMember89",
    "FiltersUnionMember90",
    "FiltersUnionMember91",
    "FiltersUnionMember92",
    "FiltersUnionMember93",
    "FiltersUnionMember94",
    "FiltersUnionMember95",
    "FiltersUnionMember96",
    "FiltersUnionMember97",
    "FiltersUnionMember98",
    "FiltersUnionMember99",
    "FiltersUnionMember100",
    "FiltersUnionMember101",
    "FiltersUnionMember102",
    "FiltersUnionMember103",
    "FiltersUnionMember104",
    "FiltersUnionMember105",
    "FiltersUnionMember106",
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
    "IncludeAttributesContributorsFiltersUnionMember0",
    "IncludeAttributesContributorsFiltersUnionMember1",
    "IncludeAttributesContributorsFiltersUnionMember2",
    "IncludeAttributesContributorsFiltersUnionMember3",
    "IncludeAttributesContributorsFiltersUnionMember4",
    "IncludeAttributesContributorsFiltersUnionMember5",
    "IncludeAttributesContributorsFiltersUnionMember6",
    "IncludeAttributesContributorsFiltersUnionMember7",
    "IncludeAttributesContributorsFiltersUnionMember8",
    "IncludeAttributesContributorsFiltersUnionMember9",
    "IncludeAttributesContributorsFiltersUnionMember10",
    "IncludeAttributesContributorsFiltersUnionMember11",
    "IncludeAttributesContributorsFiltersUnionMember12",
    "IncludeAttributesContributorsFiltersUnionMember13",
    "IncludeAttributesContributorsFiltersUnionMember14",
    "IncludeAttributesContributorsFiltersUnionMember15",
    "IncludeAttributesContributorsFiltersUnionMember16",
    "IncludeAttributesContributorsFiltersUnionMember17",
    "IncludeAttributesContributorsFiltersUnionMember18",
    "IncludeAttributesContributorsFiltersUnionMember19",
    "IncludeAttributesContributorsFiltersUnionMember20",
    "IncludeAttributesContributorsFiltersUnionMember21",
    "IncludeAttributesContributorsFiltersUnionMember22",
    "IncludeAttributesContributorsFiltersUnionMember23",
    "IncludeAttributesContributorsFiltersUnionMember24",
    "IncludeAttributesContributorsFiltersUnionMember25",
    "IncludeAttributesContributorsFiltersUnionMember26",
    "IncludeAttributesContributorsFiltersUnionMember27",
    "IncludeAttributesContributorsFiltersUnionMember28",
    "IncludeAttributesContributorsFiltersUnionMember29",
    "IncludeAttributesContributorsFiltersUnionMember30",
    "IncludeAttributesContributorsFiltersUnionMember31",
    "IncludeAttributesContributorsFiltersUnionMember32",
    "IncludeAttributesContributorsFiltersUnionMember33",
    "IncludeAttributesContributorsFiltersUnionMember34",
    "IncludeAttributesContributorsFiltersUnionMember35",
    "IncludeAttributesContributorsFiltersUnionMember36",
    "IncludeAttributesContributorsFiltersUnionMember37",
    "IncludeAttributesContributorsFiltersUnionMember38",
    "IncludeAttributesContributorsFiltersUnionMember39",
    "IncludeAttributesContributorsFiltersUnionMember40",
    "IncludeAttributesContributorsFiltersUnionMember41",
    "IncludeAttributesContributorsFiltersUnionMember42",
    "IncludeAttributesContributorsFiltersUnionMember43",
    "IncludeAttributesContributorsFiltersUnionMember44",
    "IncludeAttributesContributorsFiltersUnionMember45",
    "IncludeAttributesContributorsFiltersUnionMember46",
    "IncludeAttributesContributorsFiltersUnionMember47",
    "IncludeAttributesContributorsFiltersUnionMember48",
    "IncludeAttributesContributorsFiltersUnionMember49",
    "IncludeAttributesContributorsFiltersUnionMember50",
    "IncludeAttributesContributorsFiltersUnionMember51",
    "IncludeAttributesContributorsFiltersUnionMember52",
    "IncludeAttributesContributorsFiltersUnionMember53",
    "IncludeAttributesContributorsFiltersUnionMember54",
    "IncludeAttributesContributorsFiltersUnionMember55",
    "IncludeAttributesContributorsFiltersUnionMember56",
    "IncludeAttributesContributorsFiltersUnionMember57",
    "IncludeAttributesContributorsFiltersUnionMember58",
    "IncludeAttributesContributorsFiltersUnionMember59",
    "IncludeAttributesContributorsFiltersUnionMember60",
    "IncludeAttributesContributorsFiltersUnionMember61",
    "IncludeAttributesContributorsFiltersUnionMember62",
    "IncludeAttributesContributorsFiltersUnionMember63",
    "IncludeAttributesContributorsFiltersUnionMember64",
    "IncludeAttributesContributorsFiltersUnionMember65",
    "IncludeAttributesContributorsFiltersUnionMember66",
    "IncludeAttributesContributorsFiltersUnionMember67",
    "IncludeAttributesContributorsFiltersUnionMember68",
    "IncludeAttributesContributorsFiltersUnionMember69",
    "IncludeAttributesContributorsFiltersUnionMember70",
    "IncludeAttributesContributorsFiltersUnionMember71",
    "IncludeAttributesContributorsFiltersUnionMember72",
    "IncludeAttributesContributorsFiltersUnionMember73",
    "IncludeAttributesContributorsFiltersUnionMember74",
    "IncludeAttributesContributorsFiltersUnionMember75",
    "IncludeAttributesContributorsFiltersUnionMember76",
    "IncludeAttributesContributorsFiltersUnionMember77",
    "IncludeAttributesContributorsFiltersUnionMember78",
    "IncludeAttributesContributorsFiltersUnionMember79",
    "IncludeAttributesContributorsFiltersUnionMember80",
    "IncludeAttributesContributorsFiltersUnionMember81",
    "IncludeAttributesContributorsFiltersUnionMember82",
    "IncludeAttributesContributorsFiltersUnionMember83",
    "IncludeAttributesContributorsFiltersUnionMember84",
    "IncludeAttributesContributorsFiltersUnionMember85",
    "IncludeAttributesContributorsFiltersUnionMember86",
    "IncludeAttributesContributorsFiltersUnionMember87",
    "IncludeAttributesContributorsFiltersUnionMember88",
    "IncludeAttributesContributorsFiltersUnionMember89",
    "IncludeAttributesContributorsFiltersUnionMember90",
    "IncludeAttributesContributorsFiltersUnionMember91",
    "IncludeAttributesContributorsFiltersUnionMember92",
    "IncludeAttributesContributorsFiltersUnionMember93",
    "IncludeAttributesContributorsFiltersUnionMember94",
    "IncludeAttributesContributorsFiltersUnionMember95",
    "IncludeAttributesContributorsFiltersUnionMember96",
    "IncludeAttributesContributorsFiltersUnionMember97",
    "IncludeAttributesContributorsFiltersUnionMember98",
    "IncludeAttributesContributorsFiltersUnionMember99",
    "IncludeAttributesContributorsFiltersUnionMember100",
    "IncludeAttributesContributorsFiltersUnionMember101",
    "IncludeAttributesContributorsFiltersUnionMember102",
    "IncludeAttributesContributorsFiltersUnionMember103",
    "IncludeAttributesContributorsFiltersUnionMember104",
    "IncludeAttributesContributorsFiltersUnionMember105",
    "IncludeAttributesContributorsFiltersUnionMember106",
    "IncludeAttributesContributorsFiltersUnionMember107",
    "IncludeAttributesContributorsFiltersUnionMember108",
    "IncludeAttributesContributorsFiltersUnionMember109",
    "IncludeAttributesContributorsFiltersUnionMember110",
    "IncludeAttributesContributorsFiltersUnionMember111",
    "IncludeAttributesContributorsFiltersUnionMember112",
    "IncludeAttributesContributorsFiltersUnionMember113",
    "IncludeAttributesContributorsFiltersUnionMember114",
    "IncludeAttributesContributorsFiltersUnionMember115",
    "IncludeAttributesContributorsFiltersUnionMember116",
    "IncludeAttributesContributorsFiltersUnionMember117",
    "IncludeAttributesContributorsFiltersUnionMember118",
    "IncludeAttributesContributorsFiltersUnionMember119",
    "IncludeAttributesContributorsFiltersUnionMember120",
    "IncludeAttributesContributorsFiltersUnionMember121",
    "IncludeAttributesContributorsFiltersUnionMember122",
    "IncludeAttributesContributorsFiltersUnionMember123",
    "IncludeAttributesContributorsFiltersUnionMember124",
    "IncludeAttributesContributorsFiltersUnionMember125",
    "IncludeAttributesContributorsFiltersUnionMember126",
    "IncludeAttributesContributorsFiltersUnionMember127",
    "IncludeAttributesContributorsFiltersUnionMember128",
    "IncludeAttributesContributorsFiltersUnionMember129",
    "IncludeAttributesContributorsFiltersUnionMember130",
    "IncludeAttributesContributorsFiltersUnionMember131",
    "IncludeAttributesContributorsFiltersUnionMember132",
    "IncludeAttributesContributorsFiltersUnionMember133",
    "IncludeAttributesContributorsFiltersUnionMember134",
    "IncludeAttributesContributorsFiltersUnionMember135",
    "IncludeAttributesContributorsFiltersUnionMember136",
    "IncludeAttributesContributorsFiltersUnionMember137",
    "IncludeAttributesContributorsFiltersUnionMember138",
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
    "IncludeAttributesStarrersFiltersUnionMember0",
    "IncludeAttributesStarrersFiltersUnionMember1",
    "IncludeAttributesStarrersFiltersUnionMember2",
    "IncludeAttributesStarrersFiltersUnionMember3",
    "IncludeAttributesStarrersFiltersUnionMember4",
    "IncludeAttributesStarrersFiltersUnionMember5",
    "IncludeAttributesStarrersFiltersUnionMember6",
    "IncludeAttributesStarrersFiltersUnionMember7",
    "IncludeAttributesStarrersFiltersUnionMember8",
    "IncludeAttributesStarrersFiltersUnionMember9",
    "IncludeAttributesStarrersFiltersUnionMember10",
    "IncludeAttributesStarrersFiltersUnionMember11",
    "IncludeAttributesStarrersFiltersUnionMember12",
    "IncludeAttributesStarrersFiltersUnionMember13",
    "IncludeAttributesStarrersFiltersUnionMember14",
    "IncludeAttributesStarrersFiltersUnionMember15",
    "IncludeAttributesStarrersFiltersUnionMember16",
    "IncludeAttributesStarrersFiltersUnionMember17",
    "IncludeAttributesStarrersFiltersUnionMember18",
    "IncludeAttributesStarrersFiltersUnionMember19",
    "IncludeAttributesStarrersFiltersUnionMember20",
    "IncludeAttributesStarrersFiltersUnionMember21",
    "IncludeAttributesStarrersFiltersUnionMember22",
    "IncludeAttributesStarrersFiltersUnionMember23",
    "IncludeAttributesStarrersFiltersUnionMember24",
    "IncludeAttributesStarrersFiltersUnionMember25",
    "IncludeAttributesStarrersFiltersUnionMember26",
    "IncludeAttributesStarrersFiltersUnionMember27",
    "IncludeAttributesStarrersFiltersUnionMember28",
    "IncludeAttributesStarrersFiltersUnionMember29",
    "IncludeAttributesStarrersFiltersUnionMember30",
    "IncludeAttributesStarrersFiltersUnionMember31",
    "IncludeAttributesStarrersFiltersUnionMember32",
    "IncludeAttributesStarrersFiltersUnionMember33",
    "IncludeAttributesStarrersFiltersUnionMember34",
    "IncludeAttributesStarrersFiltersUnionMember35",
    "IncludeAttributesStarrersFiltersUnionMember36",
    "IncludeAttributesStarrersFiltersUnionMember37",
    "IncludeAttributesStarrersFiltersUnionMember38",
    "IncludeAttributesStarrersFiltersUnionMember39",
    "IncludeAttributesStarrersFiltersUnionMember40",
    "IncludeAttributesStarrersFiltersUnionMember41",
    "IncludeAttributesStarrersFiltersUnionMember42",
    "IncludeAttributesStarrersFiltersUnionMember43",
    "IncludeAttributesStarrersFiltersUnionMember44",
    "IncludeAttributesStarrersFiltersUnionMember45",
    "IncludeAttributesStarrersFiltersUnionMember46",
    "IncludeAttributesStarrersFiltersUnionMember47",
    "IncludeAttributesStarrersFiltersUnionMember48",
    "IncludeAttributesStarrersFiltersUnionMember49",
    "IncludeAttributesStarrersFiltersUnionMember50",
    "IncludeAttributesStarrersFiltersUnionMember51",
    "IncludeAttributesStarrersFiltersUnionMember52",
    "IncludeAttributesStarrersFiltersUnionMember53",
    "IncludeAttributesStarrersFiltersUnionMember54",
    "IncludeAttributesStarrersFiltersUnionMember55",
    "IncludeAttributesStarrersFiltersUnionMember56",
    "IncludeAttributesStarrersFiltersUnionMember57",
    "IncludeAttributesStarrersFiltersUnionMember58",
    "IncludeAttributesStarrersFiltersUnionMember59",
    "IncludeAttributesStarrersFiltersUnionMember60",
    "IncludeAttributesStarrersFiltersUnionMember61",
    "IncludeAttributesStarrersFiltersUnionMember62",
    "IncludeAttributesStarrersFiltersUnionMember63",
    "IncludeAttributesStarrersFiltersUnionMember64",
    "IncludeAttributesStarrersFiltersUnionMember65",
    "IncludeAttributesStarrersFiltersUnionMember66",
    "IncludeAttributesStarrersFiltersUnionMember67",
    "IncludeAttributesStarrersFiltersUnionMember68",
    "IncludeAttributesStarrersFiltersUnionMember69",
    "IncludeAttributesStarrersFiltersUnionMember70",
    "IncludeAttributesStarrersFiltersUnionMember71",
    "IncludeAttributesStarrersFiltersUnionMember72",
    "IncludeAttributesStarrersFiltersUnionMember73",
    "IncludeAttributesStarrersFiltersUnionMember74",
    "IncludeAttributesStarrersFiltersUnionMember75",
    "IncludeAttributesStarrersFiltersUnionMember76",
    "IncludeAttributesStarrersFiltersUnionMember77",
    "IncludeAttributesStarrersFiltersUnionMember78",
    "IncludeAttributesStarrersFiltersUnionMember79",
    "IncludeAttributesStarrersFiltersUnionMember80",
    "IncludeAttributesStarrersFiltersUnionMember81",
    "IncludeAttributesStarrersFiltersUnionMember82",
    "IncludeAttributesStarrersFiltersUnionMember83",
    "IncludeAttributesStarrersFiltersUnionMember84",
    "IncludeAttributesStarrersFiltersUnionMember85",
    "IncludeAttributesStarrersFiltersUnionMember86",
    "IncludeAttributesStarrersFiltersUnionMember87",
    "IncludeAttributesStarrersFiltersUnionMember88",
    "IncludeAttributesStarrersFiltersUnionMember89",
    "IncludeAttributesStarrersFiltersUnionMember90",
    "IncludeAttributesStarrersFiltersUnionMember91",
    "IncludeAttributesStarrersFiltersUnionMember92",
    "IncludeAttributesStarrersFiltersUnionMember93",
    "IncludeAttributesStarrersFiltersUnionMember94",
    "IncludeAttributesStarrersFiltersUnionMember95",
    "IncludeAttributesStarrersFiltersUnionMember96",
    "IncludeAttributesStarrersFiltersUnionMember97",
    "IncludeAttributesStarrersFiltersUnionMember98",
    "IncludeAttributesStarrersFiltersUnionMember99",
    "IncludeAttributesStarrersFiltersUnionMember100",
    "IncludeAttributesStarrersFiltersUnionMember101",
    "IncludeAttributesStarrersFiltersUnionMember102",
    "IncludeAttributesStarrersFiltersUnionMember103",
    "IncludeAttributesStarrersFiltersUnionMember104",
    "IncludeAttributesStarrersFiltersUnionMember105",
    "IncludeAttributesStarrersFiltersUnionMember106",
    "IncludeAttributesStarrersFiltersUnionMember107",
    "IncludeAttributesStarrersFiltersUnionMember108",
    "IncludeAttributesStarrersFiltersUnionMember109",
    "IncludeAttributesStarrersFiltersUnionMember110",
    "IncludeAttributesStarrersFiltersUnionMember111",
    "IncludeAttributesStarrersFiltersUnionMember112",
    "IncludeAttributesStarrersFiltersUnionMember113",
    "IncludeAttributesStarrersFiltersUnionMember114",
    "IncludeAttributesStarrersFiltersUnionMember115",
    "IncludeAttributesStarrersFiltersUnionMember116",
    "IncludeAttributesStarrersFiltersUnionMember117",
    "IncludeAttributesStarrersFiltersUnionMember118",
    "IncludeAttributesStarrersFiltersUnionMember119",
    "IncludeAttributesStarrersFiltersUnionMember120",
    "IncludeAttributesStarrersFiltersUnionMember121",
    "IncludeAttributesStarrersFiltersUnionMember122",
    "IncludeAttributesStarrersFiltersUnionMember123",
    "IncludeAttributesStarrersFiltersUnionMember124",
    "IncludeAttributesStarrersFiltersUnionMember125",
    "IncludeAttributesStarrersFiltersUnionMember126",
    "IncludeAttributesStarrersFiltersUnionMember127",
    "IncludeAttributesStarrersFiltersUnionMember128",
    "IncludeAttributesStarrersFiltersUnionMember129",
    "IncludeAttributesStarrersFiltersUnionMember130",
    "IncludeAttributesStarrersFiltersUnionMember131",
    "IncludeAttributesStarrersFiltersUnionMember132",
    "IncludeAttributesStarrersFiltersUnionMember133",
    "IncludeAttributesStarrersFiltersUnionMember134",
    "IncludeAttributesStarrersFiltersUnionMember135",
    "IncludeAttributesStarrersFiltersUnionMember136",
    "IncludeAttributesStarrersFiltersUnionMember137",
    "IncludeAttributesStarrersFiltersUnionMember138",
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
    "RankByUnionMember0",
    "RankByUnionMember1",
    "RankByUnionMember2",
    "RankByUnionMember2Expr",
    "RankByUnionMember2ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember2",
    "RankByUnionMember2ExprUnionMember2Expr",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember2",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember2Expr",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember3",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember3Expr",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember4",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember4Expr",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember5",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember5Expr",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember6",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember6Expr",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember7",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember7Expr",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember2ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember3",
    "RankByUnionMember2ExprUnionMember3Expr",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember2Expr",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember3",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember3Expr",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember4",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember4Expr",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember5",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember5Expr",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember6",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember6Expr",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember7",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember7Expr",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember3ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember4",
    "RankByUnionMember2ExprUnionMember4Expr",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember2",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember2Expr",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember3",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember3Expr",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember4",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember4Expr",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember5",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember5Expr",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember6",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember6Expr",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember7",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember7Expr",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember4ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember5",
    "RankByUnionMember2ExprUnionMember5Expr",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember2",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember2Expr",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember3",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember3Expr",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember4",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember4Expr",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember5",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember5Expr",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember6",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember6Expr",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember7",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember7Expr",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember5ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember6",
    "RankByUnionMember2ExprUnionMember6Expr",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember2Expr",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember3",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember3Expr",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember4",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember4Expr",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember5",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember5Expr",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember6",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember6Expr",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember7",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember7Expr",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember6ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember7",
    "RankByUnionMember2ExprUnionMember7Expr",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember2Expr",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember3",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember3Expr",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember4",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember4Expr",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember5",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember5Expr",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember6",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember6Expr",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember7",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember7Expr",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember2ExprUnionMember7ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember3",
    "RankByUnionMember3Expr",
    "RankByUnionMember3ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember2Expr",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember2Expr",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember3",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember3Expr",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember4",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember4Expr",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember5",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember5Expr",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember6",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember6Expr",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember7",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember7Expr",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember2ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember3",
    "RankByUnionMember3ExprUnionMember3Expr",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember2Expr",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember3",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember3Expr",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember4",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember4Expr",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember5",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember5Expr",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember6",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember6Expr",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember7",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember7Expr",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember4",
    "RankByUnionMember3ExprUnionMember4Expr",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember2Expr",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember3",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember3Expr",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember4",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember4Expr",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember5",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember5Expr",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember6",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember6Expr",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember7",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember7Expr",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember4ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember5",
    "RankByUnionMember3ExprUnionMember5Expr",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember2Expr",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember3",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember3Expr",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember4",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember4Expr",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember5",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember5Expr",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember6",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember6Expr",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember7",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember7Expr",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember5ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember6",
    "RankByUnionMember3ExprUnionMember6Expr",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember2Expr",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember3",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember3Expr",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember4",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember4Expr",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember5",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember5Expr",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember6",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember6Expr",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember7",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember7Expr",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember7",
    "RankByUnionMember3ExprUnionMember7Expr",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember2Expr",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember3",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember3Expr",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember4",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember4Expr",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember5",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember5Expr",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember6",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember6Expr",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember7",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember7Expr",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember4",
    "RankByUnionMember4Expr",
    "RankByUnionMember4ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember2",
    "RankByUnionMember4ExprUnionMember2Expr",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember2",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember2Expr",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember3",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember3Expr",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember4",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember4Expr",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember5",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember5Expr",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember6",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember6Expr",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember7",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember7Expr",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember2ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember3",
    "RankByUnionMember4ExprUnionMember3Expr",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember2Expr",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember3",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember3Expr",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember4",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember4Expr",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember5",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember5Expr",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember6",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember6Expr",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember7",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember7Expr",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember3ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember4",
    "RankByUnionMember4ExprUnionMember4Expr",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember2",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember2Expr",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember3",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember3Expr",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember4",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember4Expr",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember5",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember5Expr",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember6",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember6Expr",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember7",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember7Expr",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember4ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember5",
    "RankByUnionMember4ExprUnionMember5Expr",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember2",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember2Expr",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember3",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember3Expr",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember4",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember4Expr",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember5",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember5Expr",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember6",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember6Expr",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember7",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember7Expr",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember5ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember6",
    "RankByUnionMember4ExprUnionMember6Expr",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember2Expr",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember3",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember3Expr",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember4",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember4Expr",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember5",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember5Expr",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember6",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember6Expr",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember7",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember7Expr",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember6ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember7",
    "RankByUnionMember4ExprUnionMember7Expr",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember2Expr",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember3",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember3Expr",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember4",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember4Expr",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember5",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember5Expr",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember6",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember6Expr",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember7",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember7Expr",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember4ExprUnionMember7ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember5",
    "RankByUnionMember5Expr",
    "RankByUnionMember5ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember2",
    "RankByUnionMember5ExprUnionMember2Expr",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember2",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember2Expr",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember3",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember3Expr",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember4",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember4Expr",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember5",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember5Expr",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember6",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember6Expr",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember7",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember7Expr",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember2ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember3",
    "RankByUnionMember5ExprUnionMember3Expr",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember2Expr",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember3",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember3Expr",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember4",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember4Expr",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember5",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember5Expr",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember6",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember6Expr",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember7",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember7Expr",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember3ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember4",
    "RankByUnionMember5ExprUnionMember4Expr",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember2",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember2Expr",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember3",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember3Expr",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember4",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember4Expr",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember5",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember5Expr",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember6",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember6Expr",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember7",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember7Expr",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember4ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember5",
    "RankByUnionMember5ExprUnionMember5Expr",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember2",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember2Expr",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember3",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember3Expr",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember4",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember4Expr",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember5",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember5Expr",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember6",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember6Expr",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember7",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember7Expr",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember5ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember6",
    "RankByUnionMember5ExprUnionMember6Expr",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember2Expr",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember3",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember3Expr",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember4",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember4Expr",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember5",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember5Expr",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember6",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember6Expr",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember7",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember7Expr",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember6ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember7",
    "RankByUnionMember5ExprUnionMember7Expr",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember2Expr",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember3",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember3Expr",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember4",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember4Expr",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember5",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember5Expr",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember6",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember6Expr",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember7",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember7Expr",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember5ExprUnionMember7ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember6",
    "RankByUnionMember6Expr",
    "RankByUnionMember6ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember2Expr",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember2Expr",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember3",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember3Expr",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember4",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember4Expr",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember5",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember5Expr",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember6",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember6Expr",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember7",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember7Expr",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember2ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember3",
    "RankByUnionMember6ExprUnionMember3Expr",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember2Expr",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember3",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember3Expr",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember4",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember4Expr",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember5",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember5Expr",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember6",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember6Expr",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember7",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember7Expr",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember4",
    "RankByUnionMember6ExprUnionMember4Expr",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember2Expr",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember3",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember3Expr",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember4",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember4Expr",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember5",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember5Expr",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember6",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember6Expr",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember7",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember7Expr",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember4ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember5",
    "RankByUnionMember6ExprUnionMember5Expr",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember2Expr",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember3",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember3Expr",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember4",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember4Expr",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember5",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember5Expr",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember6",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember6Expr",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember7",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember7Expr",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember5ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember6",
    "RankByUnionMember6ExprUnionMember6Expr",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember2Expr",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember3",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember3Expr",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember4",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember4Expr",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember5",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember5Expr",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember6",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember6Expr",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember7",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember7Expr",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember7",
    "RankByUnionMember6ExprUnionMember7Expr",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember2Expr",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember3",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember3Expr",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember4",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember4Expr",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember5",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember5Expr",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember6",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember6Expr",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember7",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember7Expr",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember7",
    "RankByUnionMember7Expr",
    "RankByUnionMember7ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember2Expr",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember2Expr",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember3",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember3Expr",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember4",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember4Expr",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember5",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember5Expr",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember6",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember6Expr",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember7",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember7Expr",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember2ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember3",
    "RankByUnionMember7ExprUnionMember3Expr",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember2Expr",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember3",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember3Expr",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember4",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember4Expr",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember5",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember5Expr",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember6",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember6Expr",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember7",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember7Expr",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember4",
    "RankByUnionMember7ExprUnionMember4Expr",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember2Expr",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember3",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember3Expr",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember4",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember4Expr",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember5",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember5Expr",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember6",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember6Expr",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember7",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember7Expr",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember4ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember5",
    "RankByUnionMember7ExprUnionMember5Expr",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember2Expr",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember3",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember3Expr",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember4",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember4Expr",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember5",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember5Expr",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember6",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember6Expr",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember7",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember7Expr",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember5ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember6",
    "RankByUnionMember7ExprUnionMember6Expr",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember2Expr",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember3",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember3Expr",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember4",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember4Expr",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember5",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember5Expr",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember6",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember6Expr",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember7",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember7Expr",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember7",
    "RankByUnionMember7ExprUnionMember7Expr",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember2Expr",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember2ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember2ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember3",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember3Expr",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember4",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember4Expr",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember4ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember4ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember5",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember5Expr",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember5ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember5ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember6",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember6Expr",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember7",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember7Expr",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember7ExprUnionMember1",
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

    filters: Optional[Filters]
    """Optional filters for narrowing search results.

    Supports filtering on: githubId, ownerLogin, ownerLocation, name,
    stargazerCount, language, totalIssuesCount, totalIssuesOpen, totalIssuesClosed,
    lastContributorLocations.

    Filter structure:

    - Field filters: { field: "fieldName", op: "Eq"|"In"|"Gte"|"Lte", value:
      string|number|array }
    - Composite filters: { op: "And"|"Or", filters: [...] }

    Supported operators:

    - String fields: Eq (exact match), In (one of array)
    - Number fields: Eq (exact), In (one of array), Gte (>=), Lte (<=)
    - Use And/Or to combine multiple filters
    """

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


class FiltersUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember13(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember14(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember15(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember16(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember17(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember18(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember19(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember20(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember21(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember22(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember23(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember24(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember25(TypedDict, total=False):
    field: Required[Literal["ownerLogin"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember26(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember27(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember28(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember29(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember30(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember31(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember32(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember33(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember34(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember35(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember36(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember37(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember38(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember39(TypedDict, total=False):
    field: Required[Literal["ownerLocation"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class FiltersUnionMember40(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember41(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember42(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember43(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember44(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember45(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember46(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember47(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember48(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember49(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember50(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember51(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember52(TypedDict, total=False):
    field: Required[Literal["name"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember53(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["Eq"]]

    value: Required[float]


class FiltersUnionMember54(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["NotEq"]]

    value: Required[float]


class FiltersUnionMember55(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["In"]]

    value: Required[Iterable[float]]


class FiltersUnionMember56(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["NotIn"]]

    value: Required[Iterable[float]]


class FiltersUnionMember57(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["Lt"]]

    value: Required[float]


class FiltersUnionMember58(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["Lte"]]

    value: Required[float]


class FiltersUnionMember59(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["Gt"]]

    value: Required[float]


class FiltersUnionMember60(TypedDict, total=False):
    field: Required[Literal["stargazerCount"]]

    op: Required[Literal["Gte"]]

    value: Required[float]


class FiltersUnionMember61(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class FiltersUnionMember62(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class FiltersUnionMember63(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember64(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember65(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class FiltersUnionMember66(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class FiltersUnionMember67(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class FiltersUnionMember68(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class FiltersUnionMember69(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class FiltersUnionMember70(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class FiltersUnionMember71(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class FiltersUnionMember72(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class FiltersUnionMember73(TypedDict, total=False):
    field: Required[Literal["language"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class FiltersUnionMember74(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["Eq"]]

    value: Required[float]


class FiltersUnionMember75(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["NotEq"]]

    value: Required[float]


class FiltersUnionMember76(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["In"]]

    value: Required[Iterable[float]]


class FiltersUnionMember77(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["NotIn"]]

    value: Required[Iterable[float]]


class FiltersUnionMember78(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["Lt"]]

    value: Required[float]


class FiltersUnionMember79(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["Lte"]]

    value: Required[float]


class FiltersUnionMember80(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["Gt"]]

    value: Required[float]


class FiltersUnionMember81(TypedDict, total=False):
    field: Required[Literal["totalIssuesCount"]]

    op: Required[Literal["Gte"]]

    value: Required[float]


class FiltersUnionMember82(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["Eq"]]

    value: Required[float]


class FiltersUnionMember83(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["NotEq"]]

    value: Required[float]


class FiltersUnionMember84(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["In"]]

    value: Required[Iterable[float]]


class FiltersUnionMember85(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["NotIn"]]

    value: Required[Iterable[float]]


class FiltersUnionMember86(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["Lt"]]

    value: Required[float]


class FiltersUnionMember87(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["Lte"]]

    value: Required[float]


class FiltersUnionMember88(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["Gt"]]

    value: Required[float]


class FiltersUnionMember89(TypedDict, total=False):
    field: Required[Literal["totalIssuesOpen"]]

    op: Required[Literal["Gte"]]

    value: Required[float]


class FiltersUnionMember90(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["Eq"]]

    value: Required[float]


class FiltersUnionMember91(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["NotEq"]]

    value: Required[float]


class FiltersUnionMember92(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["In"]]

    value: Required[Iterable[float]]


class FiltersUnionMember93(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["NotIn"]]

    value: Required[Iterable[float]]


class FiltersUnionMember94(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["Lt"]]

    value: Required[float]


class FiltersUnionMember95(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["Lte"]]

    value: Required[float]


class FiltersUnionMember96(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["Gt"]]

    value: Required[float]


class FiltersUnionMember97(TypedDict, total=False):
    field: Required[Literal["totalIssuesClosed"]]

    op: Required[Literal["Gte"]]

    value: Required[float]


class FiltersUnionMember98(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["Contains"]]

    value: Required[str]


class FiltersUnionMember99(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["NotContains"]]

    value: Required[str]


class FiltersUnionMember100(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["ContainsAny"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember101(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["NotContainsAny"]]

    value: Required[SequenceNotStr[str]]


class FiltersUnionMember102(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["AnyLt"]]

    value: Required[str]


class FiltersUnionMember103(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["AnyLte"]]

    value: Required[str]


class FiltersUnionMember104(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["AnyGt"]]

    value: Required[str]


class FiltersUnionMember105(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["AnyGte"]]

    value: Required[str]


class FiltersUnionMember106(TypedDict, total=False):
    field: Required[Literal["lastContributorLocations"]]

    op: Required[Literal["ContainsAllTokens"]]

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
    FiltersUnionMember0,
    FiltersUnionMember1,
    FiltersUnionMember2,
    FiltersUnionMember3,
    FiltersUnionMember4,
    FiltersUnionMember5,
    FiltersUnionMember6,
    FiltersUnionMember7,
    FiltersUnionMember8,
    FiltersUnionMember9,
    FiltersUnionMember10,
    FiltersUnionMember11,
    FiltersUnionMember12,
    FiltersUnionMember13,
    FiltersUnionMember14,
    FiltersUnionMember15,
    FiltersUnionMember16,
    FiltersUnionMember17,
    FiltersUnionMember18,
    FiltersUnionMember19,
    FiltersUnionMember20,
    FiltersUnionMember21,
    FiltersUnionMember22,
    FiltersUnionMember23,
    FiltersUnionMember24,
    FiltersUnionMember25,
    FiltersUnionMember26,
    FiltersUnionMember27,
    FiltersUnionMember28,
    FiltersUnionMember29,
    FiltersUnionMember30,
    FiltersUnionMember31,
    FiltersUnionMember32,
    FiltersUnionMember33,
    FiltersUnionMember34,
    FiltersUnionMember35,
    FiltersUnionMember36,
    FiltersUnionMember37,
    FiltersUnionMember38,
    FiltersUnionMember39,
    FiltersUnionMember40,
    FiltersUnionMember41,
    FiltersUnionMember42,
    FiltersUnionMember43,
    FiltersUnionMember44,
    FiltersUnionMember45,
    FiltersUnionMember46,
    FiltersUnionMember47,
    FiltersUnionMember48,
    FiltersUnionMember49,
    FiltersUnionMember50,
    FiltersUnionMember51,
    FiltersUnionMember52,
    FiltersUnionMember53,
    FiltersUnionMember54,
    FiltersUnionMember55,
    FiltersUnionMember56,
    FiltersUnionMember57,
    FiltersUnionMember58,
    FiltersUnionMember59,
    FiltersUnionMember60,
    FiltersUnionMember61,
    FiltersUnionMember62,
    FiltersUnionMember63,
    FiltersUnionMember64,
    FiltersUnionMember65,
    FiltersUnionMember66,
    FiltersUnionMember67,
    FiltersUnionMember68,
    FiltersUnionMember69,
    FiltersUnionMember70,
    FiltersUnionMember71,
    FiltersUnionMember72,
    FiltersUnionMember73,
    FiltersUnionMember74,
    FiltersUnionMember75,
    FiltersUnionMember76,
    FiltersUnionMember77,
    FiltersUnionMember78,
    FiltersUnionMember79,
    FiltersUnionMember80,
    FiltersUnionMember81,
    FiltersUnionMember82,
    FiltersUnionMember83,
    FiltersUnionMember84,
    FiltersUnionMember85,
    FiltersUnionMember86,
    FiltersUnionMember87,
    FiltersUnionMember88,
    FiltersUnionMember89,
    FiltersUnionMember90,
    FiltersUnionMember91,
    FiltersUnionMember92,
    FiltersUnionMember93,
    FiltersUnionMember94,
    FiltersUnionMember95,
    FiltersUnionMember96,
    FiltersUnionMember97,
    FiltersUnionMember98,
    FiltersUnionMember99,
    FiltersUnionMember100,
    FiltersUnionMember101,
    FiltersUnionMember102,
    FiltersUnionMember103,
    FiltersUnionMember104,
    FiltersUnionMember105,
    FiltersUnionMember106,
    FiltersUnionMember107,
    FiltersUnionMember108,
]


class IncludeAttributesContributorsFiltersUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesContributorsFiltersUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesContributorsFiltersUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

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
    IncludeAttributesContributorsFiltersUnionMember0,
    IncludeAttributesContributorsFiltersUnionMember1,
    IncludeAttributesContributorsFiltersUnionMember2,
    IncludeAttributesContributorsFiltersUnionMember3,
    IncludeAttributesContributorsFiltersUnionMember4,
    IncludeAttributesContributorsFiltersUnionMember5,
    IncludeAttributesContributorsFiltersUnionMember6,
    IncludeAttributesContributorsFiltersUnionMember7,
    IncludeAttributesContributorsFiltersUnionMember8,
    IncludeAttributesContributorsFiltersUnionMember9,
    IncludeAttributesContributorsFiltersUnionMember10,
    IncludeAttributesContributorsFiltersUnionMember11,
    IncludeAttributesContributorsFiltersUnionMember12,
    IncludeAttributesContributorsFiltersUnionMember13,
    IncludeAttributesContributorsFiltersUnionMember14,
    IncludeAttributesContributorsFiltersUnionMember15,
    IncludeAttributesContributorsFiltersUnionMember16,
    IncludeAttributesContributorsFiltersUnionMember17,
    IncludeAttributesContributorsFiltersUnionMember18,
    IncludeAttributesContributorsFiltersUnionMember19,
    IncludeAttributesContributorsFiltersUnionMember20,
    IncludeAttributesContributorsFiltersUnionMember21,
    IncludeAttributesContributorsFiltersUnionMember22,
    IncludeAttributesContributorsFiltersUnionMember23,
    IncludeAttributesContributorsFiltersUnionMember24,
    IncludeAttributesContributorsFiltersUnionMember25,
    IncludeAttributesContributorsFiltersUnionMember26,
    IncludeAttributesContributorsFiltersUnionMember27,
    IncludeAttributesContributorsFiltersUnionMember28,
    IncludeAttributesContributorsFiltersUnionMember29,
    IncludeAttributesContributorsFiltersUnionMember30,
    IncludeAttributesContributorsFiltersUnionMember31,
    IncludeAttributesContributorsFiltersUnionMember32,
    IncludeAttributesContributorsFiltersUnionMember33,
    IncludeAttributesContributorsFiltersUnionMember34,
    IncludeAttributesContributorsFiltersUnionMember35,
    IncludeAttributesContributorsFiltersUnionMember36,
    IncludeAttributesContributorsFiltersUnionMember37,
    IncludeAttributesContributorsFiltersUnionMember38,
    IncludeAttributesContributorsFiltersUnionMember39,
    IncludeAttributesContributorsFiltersUnionMember40,
    IncludeAttributesContributorsFiltersUnionMember41,
    IncludeAttributesContributorsFiltersUnionMember42,
    IncludeAttributesContributorsFiltersUnionMember43,
    IncludeAttributesContributorsFiltersUnionMember44,
    IncludeAttributesContributorsFiltersUnionMember45,
    IncludeAttributesContributorsFiltersUnionMember46,
    IncludeAttributesContributorsFiltersUnionMember47,
    IncludeAttributesContributorsFiltersUnionMember48,
    IncludeAttributesContributorsFiltersUnionMember49,
    IncludeAttributesContributorsFiltersUnionMember50,
    IncludeAttributesContributorsFiltersUnionMember51,
    IncludeAttributesContributorsFiltersUnionMember52,
    IncludeAttributesContributorsFiltersUnionMember53,
    IncludeAttributesContributorsFiltersUnionMember54,
    IncludeAttributesContributorsFiltersUnionMember55,
    IncludeAttributesContributorsFiltersUnionMember56,
    IncludeAttributesContributorsFiltersUnionMember57,
    IncludeAttributesContributorsFiltersUnionMember58,
    IncludeAttributesContributorsFiltersUnionMember59,
    IncludeAttributesContributorsFiltersUnionMember60,
    IncludeAttributesContributorsFiltersUnionMember61,
    IncludeAttributesContributorsFiltersUnionMember62,
    IncludeAttributesContributorsFiltersUnionMember63,
    IncludeAttributesContributorsFiltersUnionMember64,
    IncludeAttributesContributorsFiltersUnionMember65,
    IncludeAttributesContributorsFiltersUnionMember66,
    IncludeAttributesContributorsFiltersUnionMember67,
    IncludeAttributesContributorsFiltersUnionMember68,
    IncludeAttributesContributorsFiltersUnionMember69,
    IncludeAttributesContributorsFiltersUnionMember70,
    IncludeAttributesContributorsFiltersUnionMember71,
    IncludeAttributesContributorsFiltersUnionMember72,
    IncludeAttributesContributorsFiltersUnionMember73,
    IncludeAttributesContributorsFiltersUnionMember74,
    IncludeAttributesContributorsFiltersUnionMember75,
    IncludeAttributesContributorsFiltersUnionMember76,
    IncludeAttributesContributorsFiltersUnionMember77,
    IncludeAttributesContributorsFiltersUnionMember78,
    IncludeAttributesContributorsFiltersUnionMember79,
    IncludeAttributesContributorsFiltersUnionMember80,
    IncludeAttributesContributorsFiltersUnionMember81,
    IncludeAttributesContributorsFiltersUnionMember82,
    IncludeAttributesContributorsFiltersUnionMember83,
    IncludeAttributesContributorsFiltersUnionMember84,
    IncludeAttributesContributorsFiltersUnionMember85,
    IncludeAttributesContributorsFiltersUnionMember86,
    IncludeAttributesContributorsFiltersUnionMember87,
    IncludeAttributesContributorsFiltersUnionMember88,
    IncludeAttributesContributorsFiltersUnionMember89,
    IncludeAttributesContributorsFiltersUnionMember90,
    IncludeAttributesContributorsFiltersUnionMember91,
    IncludeAttributesContributorsFiltersUnionMember92,
    IncludeAttributesContributorsFiltersUnionMember93,
    IncludeAttributesContributorsFiltersUnionMember94,
    IncludeAttributesContributorsFiltersUnionMember95,
    IncludeAttributesContributorsFiltersUnionMember96,
    IncludeAttributesContributorsFiltersUnionMember97,
    IncludeAttributesContributorsFiltersUnionMember98,
    IncludeAttributesContributorsFiltersUnionMember99,
    IncludeAttributesContributorsFiltersUnionMember100,
    IncludeAttributesContributorsFiltersUnionMember101,
    IncludeAttributesContributorsFiltersUnionMember102,
    IncludeAttributesContributorsFiltersUnionMember103,
    IncludeAttributesContributorsFiltersUnionMember104,
    IncludeAttributesContributorsFiltersUnionMember105,
    IncludeAttributesContributorsFiltersUnionMember106,
    IncludeAttributesContributorsFiltersUnionMember107,
    IncludeAttributesContributorsFiltersUnionMember108,
    IncludeAttributesContributorsFiltersUnionMember109,
    IncludeAttributesContributorsFiltersUnionMember110,
    IncludeAttributesContributorsFiltersUnionMember111,
    IncludeAttributesContributorsFiltersUnionMember112,
    IncludeAttributesContributorsFiltersUnionMember113,
    IncludeAttributesContributorsFiltersUnionMember114,
    IncludeAttributesContributorsFiltersUnionMember115,
    IncludeAttributesContributorsFiltersUnionMember116,
    IncludeAttributesContributorsFiltersUnionMember117,
    IncludeAttributesContributorsFiltersUnionMember118,
    IncludeAttributesContributorsFiltersUnionMember119,
    IncludeAttributesContributorsFiltersUnionMember120,
    IncludeAttributesContributorsFiltersUnionMember121,
    IncludeAttributesContributorsFiltersUnionMember122,
    IncludeAttributesContributorsFiltersUnionMember123,
    IncludeAttributesContributorsFiltersUnionMember124,
    IncludeAttributesContributorsFiltersUnionMember125,
    IncludeAttributesContributorsFiltersUnionMember126,
    IncludeAttributesContributorsFiltersUnionMember127,
    IncludeAttributesContributorsFiltersUnionMember128,
    IncludeAttributesContributorsFiltersUnionMember129,
    IncludeAttributesContributorsFiltersUnionMember130,
    IncludeAttributesContributorsFiltersUnionMember131,
    IncludeAttributesContributorsFiltersUnionMember132,
    IncludeAttributesContributorsFiltersUnionMember133,
    IncludeAttributesContributorsFiltersUnionMember134,
    IncludeAttributesContributorsFiltersUnionMember135,
    IncludeAttributesContributorsFiltersUnionMember136,
    IncludeAttributesContributorsFiltersUnionMember137,
    IncludeAttributesContributorsFiltersUnionMember138,
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


class IncludeAttributesStarrersFiltersUnionMember0(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember1(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember2(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember3(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember4(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember5(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember6(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember7(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember8(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember9(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember10(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember11(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember12(TypedDict, total=False):
    field: Required[Literal["githubId"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember13(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember14(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember15(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember16(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember17(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember18(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember19(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember20(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember21(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember22(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember23(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember24(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember25(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember26(TypedDict, total=False):
    field: Required[Literal["login"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember27(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember28(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember29(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember30(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember31(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember32(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember33(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember34(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember35(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember36(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember37(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember38(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember39(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember40(TypedDict, total=False):
    field: Required[Literal["displayName"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember41(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember42(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember43(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember44(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember45(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember46(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember47(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember48(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember49(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember50(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember51(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember52(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember53(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember54(TypedDict, total=False):
    field: Required[Literal["bio"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember55(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember56(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember57(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember58(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember59(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember60(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember61(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember62(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember63(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember64(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember65(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember66(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember67(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember68(TypedDict, total=False):
    field: Required[Literal["company"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember69(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember70(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember71(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember72(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember73(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember74(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember75(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember76(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember77(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember78(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember79(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember80(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember81(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember82(TypedDict, total=False):
    field: Required[Literal["location"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember83(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember84(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember85(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember86(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember87(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember88(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember89(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember90(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember91(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember92(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember93(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember94(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember95(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember96(TypedDict, total=False):
    field: Required[Literal["emails"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember97(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember98(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember99(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember100(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember101(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember102(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember103(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember104(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember105(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember106(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember107(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember108(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember109(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember110(TypedDict, total=False):
    field: Required[Literal["resolvedCountry"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember111(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember112(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember113(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember114(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember115(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember116(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember117(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember118(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember119(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember120(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember121(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember122(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember123(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember124(TypedDict, total=False):
    field: Required[Literal["resolvedState"]]

    op: Required[Literal["ContainsAllTokens"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember125(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Eq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember126(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotEq"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember127(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["In"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember128(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIn"]]

    value: Required[SequenceNotStr[str]]


class IncludeAttributesStarrersFiltersUnionMember129(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember130(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Lte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember131(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gt"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember132(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Gte"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember133(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Glob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember134(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember135(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["IGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember136(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["NotIGlob"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember137(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

    op: Required[Literal["Regex"]]

    value: Required[str]


class IncludeAttributesStarrersFiltersUnionMember138(TypedDict, total=False):
    field: Required[Literal["resolvedCity"]]

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
    IncludeAttributesStarrersFiltersUnionMember0,
    IncludeAttributesStarrersFiltersUnionMember1,
    IncludeAttributesStarrersFiltersUnionMember2,
    IncludeAttributesStarrersFiltersUnionMember3,
    IncludeAttributesStarrersFiltersUnionMember4,
    IncludeAttributesStarrersFiltersUnionMember5,
    IncludeAttributesStarrersFiltersUnionMember6,
    IncludeAttributesStarrersFiltersUnionMember7,
    IncludeAttributesStarrersFiltersUnionMember8,
    IncludeAttributesStarrersFiltersUnionMember9,
    IncludeAttributesStarrersFiltersUnionMember10,
    IncludeAttributesStarrersFiltersUnionMember11,
    IncludeAttributesStarrersFiltersUnionMember12,
    IncludeAttributesStarrersFiltersUnionMember13,
    IncludeAttributesStarrersFiltersUnionMember14,
    IncludeAttributesStarrersFiltersUnionMember15,
    IncludeAttributesStarrersFiltersUnionMember16,
    IncludeAttributesStarrersFiltersUnionMember17,
    IncludeAttributesStarrersFiltersUnionMember18,
    IncludeAttributesStarrersFiltersUnionMember19,
    IncludeAttributesStarrersFiltersUnionMember20,
    IncludeAttributesStarrersFiltersUnionMember21,
    IncludeAttributesStarrersFiltersUnionMember22,
    IncludeAttributesStarrersFiltersUnionMember23,
    IncludeAttributesStarrersFiltersUnionMember24,
    IncludeAttributesStarrersFiltersUnionMember25,
    IncludeAttributesStarrersFiltersUnionMember26,
    IncludeAttributesStarrersFiltersUnionMember27,
    IncludeAttributesStarrersFiltersUnionMember28,
    IncludeAttributesStarrersFiltersUnionMember29,
    IncludeAttributesStarrersFiltersUnionMember30,
    IncludeAttributesStarrersFiltersUnionMember31,
    IncludeAttributesStarrersFiltersUnionMember32,
    IncludeAttributesStarrersFiltersUnionMember33,
    IncludeAttributesStarrersFiltersUnionMember34,
    IncludeAttributesStarrersFiltersUnionMember35,
    IncludeAttributesStarrersFiltersUnionMember36,
    IncludeAttributesStarrersFiltersUnionMember37,
    IncludeAttributesStarrersFiltersUnionMember38,
    IncludeAttributesStarrersFiltersUnionMember39,
    IncludeAttributesStarrersFiltersUnionMember40,
    IncludeAttributesStarrersFiltersUnionMember41,
    IncludeAttributesStarrersFiltersUnionMember42,
    IncludeAttributesStarrersFiltersUnionMember43,
    IncludeAttributesStarrersFiltersUnionMember44,
    IncludeAttributesStarrersFiltersUnionMember45,
    IncludeAttributesStarrersFiltersUnionMember46,
    IncludeAttributesStarrersFiltersUnionMember47,
    IncludeAttributesStarrersFiltersUnionMember48,
    IncludeAttributesStarrersFiltersUnionMember49,
    IncludeAttributesStarrersFiltersUnionMember50,
    IncludeAttributesStarrersFiltersUnionMember51,
    IncludeAttributesStarrersFiltersUnionMember52,
    IncludeAttributesStarrersFiltersUnionMember53,
    IncludeAttributesStarrersFiltersUnionMember54,
    IncludeAttributesStarrersFiltersUnionMember55,
    IncludeAttributesStarrersFiltersUnionMember56,
    IncludeAttributesStarrersFiltersUnionMember57,
    IncludeAttributesStarrersFiltersUnionMember58,
    IncludeAttributesStarrersFiltersUnionMember59,
    IncludeAttributesStarrersFiltersUnionMember60,
    IncludeAttributesStarrersFiltersUnionMember61,
    IncludeAttributesStarrersFiltersUnionMember62,
    IncludeAttributesStarrersFiltersUnionMember63,
    IncludeAttributesStarrersFiltersUnionMember64,
    IncludeAttributesStarrersFiltersUnionMember65,
    IncludeAttributesStarrersFiltersUnionMember66,
    IncludeAttributesStarrersFiltersUnionMember67,
    IncludeAttributesStarrersFiltersUnionMember68,
    IncludeAttributesStarrersFiltersUnionMember69,
    IncludeAttributesStarrersFiltersUnionMember70,
    IncludeAttributesStarrersFiltersUnionMember71,
    IncludeAttributesStarrersFiltersUnionMember72,
    IncludeAttributesStarrersFiltersUnionMember73,
    IncludeAttributesStarrersFiltersUnionMember74,
    IncludeAttributesStarrersFiltersUnionMember75,
    IncludeAttributesStarrersFiltersUnionMember76,
    IncludeAttributesStarrersFiltersUnionMember77,
    IncludeAttributesStarrersFiltersUnionMember78,
    IncludeAttributesStarrersFiltersUnionMember79,
    IncludeAttributesStarrersFiltersUnionMember80,
    IncludeAttributesStarrersFiltersUnionMember81,
    IncludeAttributesStarrersFiltersUnionMember82,
    IncludeAttributesStarrersFiltersUnionMember83,
    IncludeAttributesStarrersFiltersUnionMember84,
    IncludeAttributesStarrersFiltersUnionMember85,
    IncludeAttributesStarrersFiltersUnionMember86,
    IncludeAttributesStarrersFiltersUnionMember87,
    IncludeAttributesStarrersFiltersUnionMember88,
    IncludeAttributesStarrersFiltersUnionMember89,
    IncludeAttributesStarrersFiltersUnionMember90,
    IncludeAttributesStarrersFiltersUnionMember91,
    IncludeAttributesStarrersFiltersUnionMember92,
    IncludeAttributesStarrersFiltersUnionMember93,
    IncludeAttributesStarrersFiltersUnionMember94,
    IncludeAttributesStarrersFiltersUnionMember95,
    IncludeAttributesStarrersFiltersUnionMember96,
    IncludeAttributesStarrersFiltersUnionMember97,
    IncludeAttributesStarrersFiltersUnionMember98,
    IncludeAttributesStarrersFiltersUnionMember99,
    IncludeAttributesStarrersFiltersUnionMember100,
    IncludeAttributesStarrersFiltersUnionMember101,
    IncludeAttributesStarrersFiltersUnionMember102,
    IncludeAttributesStarrersFiltersUnionMember103,
    IncludeAttributesStarrersFiltersUnionMember104,
    IncludeAttributesStarrersFiltersUnionMember105,
    IncludeAttributesStarrersFiltersUnionMember106,
    IncludeAttributesStarrersFiltersUnionMember107,
    IncludeAttributesStarrersFiltersUnionMember108,
    IncludeAttributesStarrersFiltersUnionMember109,
    IncludeAttributesStarrersFiltersUnionMember110,
    IncludeAttributesStarrersFiltersUnionMember111,
    IncludeAttributesStarrersFiltersUnionMember112,
    IncludeAttributesStarrersFiltersUnionMember113,
    IncludeAttributesStarrersFiltersUnionMember114,
    IncludeAttributesStarrersFiltersUnionMember115,
    IncludeAttributesStarrersFiltersUnionMember116,
    IncludeAttributesStarrersFiltersUnionMember117,
    IncludeAttributesStarrersFiltersUnionMember118,
    IncludeAttributesStarrersFiltersUnionMember119,
    IncludeAttributesStarrersFiltersUnionMember120,
    IncludeAttributesStarrersFiltersUnionMember121,
    IncludeAttributesStarrersFiltersUnionMember122,
    IncludeAttributesStarrersFiltersUnionMember123,
    IncludeAttributesStarrersFiltersUnionMember124,
    IncludeAttributesStarrersFiltersUnionMember125,
    IncludeAttributesStarrersFiltersUnionMember126,
    IncludeAttributesStarrersFiltersUnionMember127,
    IncludeAttributesStarrersFiltersUnionMember128,
    IncludeAttributesStarrersFiltersUnionMember129,
    IncludeAttributesStarrersFiltersUnionMember130,
    IncludeAttributesStarrersFiltersUnionMember131,
    IncludeAttributesStarrersFiltersUnionMember132,
    IncludeAttributesStarrersFiltersUnionMember133,
    IncludeAttributesStarrersFiltersUnionMember134,
    IncludeAttributesStarrersFiltersUnionMember135,
    IncludeAttributesStarrersFiltersUnionMember136,
    IncludeAttributesStarrersFiltersUnionMember137,
    IncludeAttributesStarrersFiltersUnionMember138,
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


class RankByUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember2ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember2ExprUnionMember2ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember2ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember2ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember2ExprUnionMember2ExprUnionMember0,
    RankByUnionMember2ExprUnionMember2ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember2ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember2ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember2ExprUnionMember2ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember2ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember2ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember2ExprUnionMember3ExprUnionMember0,
    RankByUnionMember2ExprUnionMember2ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember2ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember2ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember2ExprUnionMember2ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember2ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember2ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember2ExprUnionMember4ExprUnionMember0,
    RankByUnionMember2ExprUnionMember2ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember2ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember2ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember2ExprUnionMember2ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember2ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember2ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember2ExprUnionMember5ExprUnionMember0,
    RankByUnionMember2ExprUnionMember2ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember2ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember2ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember2ExprUnionMember2ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember2ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember2ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember2ExprUnionMember6ExprUnionMember0,
    RankByUnionMember2ExprUnionMember2ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember2ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember2ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember2ExprUnionMember2ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember2ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember2ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember2ExprUnionMember7ExprUnionMember0,
    RankByUnionMember2ExprUnionMember2ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember2ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember2ExprUnionMember2ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember2ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember2ExprUnionMember0,
    RankByUnionMember2ExprUnionMember2ExprUnionMember1,
    RankByUnionMember2ExprUnionMember2ExprUnionMember2,
    RankByUnionMember2ExprUnionMember2ExprUnionMember3,
    RankByUnionMember2ExprUnionMember2ExprUnionMember4,
    RankByUnionMember2ExprUnionMember2ExprUnionMember5,
    RankByUnionMember2ExprUnionMember2ExprUnionMember6,
    RankByUnionMember2ExprUnionMember2ExprUnionMember7,
]


class RankByUnionMember2ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember2ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember2ExprUnionMember3ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember3ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember3ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember3ExprUnionMember2ExprUnionMember0,
    RankByUnionMember2ExprUnionMember3ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember3ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember2ExprUnionMember3ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember3ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember3ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember3ExprUnionMember3ExprUnionMember0,
    RankByUnionMember2ExprUnionMember3ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember3ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember3ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember2ExprUnionMember3ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember3ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember3ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember3ExprUnionMember4ExprUnionMember0,
    RankByUnionMember2ExprUnionMember3ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember3ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember3ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember2ExprUnionMember3ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember3ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember3ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember3ExprUnionMember5ExprUnionMember0,
    RankByUnionMember2ExprUnionMember3ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember3ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember3ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember2ExprUnionMember3ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember3ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember3ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember3ExprUnionMember6ExprUnionMember0,
    RankByUnionMember2ExprUnionMember3ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember3ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember3ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember2ExprUnionMember3ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember3ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember3ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember3ExprUnionMember7ExprUnionMember0,
    RankByUnionMember2ExprUnionMember3ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember3ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember2ExprUnionMember3ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember2ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember3ExprUnionMember0,
    RankByUnionMember2ExprUnionMember3ExprUnionMember1,
    RankByUnionMember2ExprUnionMember3ExprUnionMember2,
    RankByUnionMember2ExprUnionMember3ExprUnionMember3,
    RankByUnionMember2ExprUnionMember3ExprUnionMember4,
    RankByUnionMember2ExprUnionMember3ExprUnionMember5,
    RankByUnionMember2ExprUnionMember3ExprUnionMember6,
    RankByUnionMember2ExprUnionMember3ExprUnionMember7,
]


class RankByUnionMember2ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember2ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember2ExprUnionMember4ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember4ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember4ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember4ExprUnionMember2ExprUnionMember0,
    RankByUnionMember2ExprUnionMember4ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember4ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember4ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember2ExprUnionMember4ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember4ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember4ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember4ExprUnionMember3ExprUnionMember0,
    RankByUnionMember2ExprUnionMember4ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember4ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember4ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember2ExprUnionMember4ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember4ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember4ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember4ExprUnionMember4ExprUnionMember0,
    RankByUnionMember2ExprUnionMember4ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember4ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember4ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember2ExprUnionMember4ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember4ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember4ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember4ExprUnionMember5ExprUnionMember0,
    RankByUnionMember2ExprUnionMember4ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember4ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember4ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember2ExprUnionMember4ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember4ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember4ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember4ExprUnionMember6ExprUnionMember0,
    RankByUnionMember2ExprUnionMember4ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember4ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember4ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember2ExprUnionMember4ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember4ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember4ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember4ExprUnionMember7ExprUnionMember0,
    RankByUnionMember2ExprUnionMember4ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember4ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember2ExprUnionMember4ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember2ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember4ExprUnionMember0,
    RankByUnionMember2ExprUnionMember4ExprUnionMember1,
    RankByUnionMember2ExprUnionMember4ExprUnionMember2,
    RankByUnionMember2ExprUnionMember4ExprUnionMember3,
    RankByUnionMember2ExprUnionMember4ExprUnionMember4,
    RankByUnionMember2ExprUnionMember4ExprUnionMember5,
    RankByUnionMember2ExprUnionMember4ExprUnionMember6,
    RankByUnionMember2ExprUnionMember4ExprUnionMember7,
]


class RankByUnionMember2ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember2ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember2ExprUnionMember5ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember5ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember5ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember5ExprUnionMember2ExprUnionMember0,
    RankByUnionMember2ExprUnionMember5ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember5ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember5ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember2ExprUnionMember5ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember5ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember5ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember5ExprUnionMember3ExprUnionMember0,
    RankByUnionMember2ExprUnionMember5ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember5ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember5ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember2ExprUnionMember5ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember5ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember5ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember5ExprUnionMember4ExprUnionMember0,
    RankByUnionMember2ExprUnionMember5ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember5ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember5ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember2ExprUnionMember5ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember5ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember5ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember5ExprUnionMember5ExprUnionMember0,
    RankByUnionMember2ExprUnionMember5ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember5ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember5ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember2ExprUnionMember5ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember5ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember5ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember5ExprUnionMember6ExprUnionMember0,
    RankByUnionMember2ExprUnionMember5ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember5ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember5ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember2ExprUnionMember5ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember5ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember5ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember5ExprUnionMember7ExprUnionMember0,
    RankByUnionMember2ExprUnionMember5ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember5ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember2ExprUnionMember5ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember2ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember5ExprUnionMember0,
    RankByUnionMember2ExprUnionMember5ExprUnionMember1,
    RankByUnionMember2ExprUnionMember5ExprUnionMember2,
    RankByUnionMember2ExprUnionMember5ExprUnionMember3,
    RankByUnionMember2ExprUnionMember5ExprUnionMember4,
    RankByUnionMember2ExprUnionMember5ExprUnionMember5,
    RankByUnionMember2ExprUnionMember5ExprUnionMember6,
    RankByUnionMember2ExprUnionMember5ExprUnionMember7,
]


class RankByUnionMember2ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember2ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember2ExprUnionMember6ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember6ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember6ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember6ExprUnionMember2ExprUnionMember0,
    RankByUnionMember2ExprUnionMember6ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember6ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember2ExprUnionMember6ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember6ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember6ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember6ExprUnionMember3ExprUnionMember0,
    RankByUnionMember2ExprUnionMember6ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember6ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember6ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember2ExprUnionMember6ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember6ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember6ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember6ExprUnionMember4ExprUnionMember0,
    RankByUnionMember2ExprUnionMember6ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember6ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember6ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember2ExprUnionMember6ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember6ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember6ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember6ExprUnionMember5ExprUnionMember0,
    RankByUnionMember2ExprUnionMember6ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember6ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember6ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember2ExprUnionMember6ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember6ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember6ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember6ExprUnionMember6ExprUnionMember0,
    RankByUnionMember2ExprUnionMember6ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember6ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember6ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember2ExprUnionMember6ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember6ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember6ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember6ExprUnionMember7ExprUnionMember0,
    RankByUnionMember2ExprUnionMember6ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember6ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember2ExprUnionMember6ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember2ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember6ExprUnionMember0,
    RankByUnionMember2ExprUnionMember6ExprUnionMember1,
    RankByUnionMember2ExprUnionMember6ExprUnionMember2,
    RankByUnionMember2ExprUnionMember6ExprUnionMember3,
    RankByUnionMember2ExprUnionMember6ExprUnionMember4,
    RankByUnionMember2ExprUnionMember6ExprUnionMember5,
    RankByUnionMember2ExprUnionMember6ExprUnionMember6,
    RankByUnionMember2ExprUnionMember6ExprUnionMember7,
]


class RankByUnionMember2ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember2ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember2ExprUnionMember7ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember7ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember7ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember7ExprUnionMember2ExprUnionMember0,
    RankByUnionMember2ExprUnionMember7ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember7ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember2ExprUnionMember7ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember7ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember7ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember7ExprUnionMember3ExprUnionMember0,
    RankByUnionMember2ExprUnionMember7ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember7ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember7ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember2ExprUnionMember7ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember7ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember7ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember7ExprUnionMember4ExprUnionMember0,
    RankByUnionMember2ExprUnionMember7ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember7ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember7ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember2ExprUnionMember7ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember7ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember7ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember7ExprUnionMember5ExprUnionMember0,
    RankByUnionMember2ExprUnionMember7ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember7ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember7ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember2ExprUnionMember7ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember7ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember7ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember7ExprUnionMember6ExprUnionMember0,
    RankByUnionMember2ExprUnionMember7ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember7ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2ExprUnionMember7ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember2ExprUnionMember7ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember2ExprUnionMember7ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember2ExprUnionMember7ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember7ExprUnionMember7ExprUnionMember0,
    RankByUnionMember2ExprUnionMember7ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember2ExprUnionMember7ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember2ExprUnionMember7ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember2ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember7ExprUnionMember0,
    RankByUnionMember2ExprUnionMember7ExprUnionMember1,
    RankByUnionMember2ExprUnionMember7ExprUnionMember2,
    RankByUnionMember2ExprUnionMember7ExprUnionMember3,
    RankByUnionMember2ExprUnionMember7ExprUnionMember4,
    RankByUnionMember2ExprUnionMember7ExprUnionMember5,
    RankByUnionMember2ExprUnionMember7ExprUnionMember6,
    RankByUnionMember2ExprUnionMember7ExprUnionMember7,
]


class RankByUnionMember2ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember2ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember2ExprUnionMember0,
    RankByUnionMember2ExprUnionMember1,
    RankByUnionMember2ExprUnionMember2,
    RankByUnionMember2ExprUnionMember3,
    RankByUnionMember2ExprUnionMember4,
    RankByUnionMember2ExprUnionMember5,
    RankByUnionMember2ExprUnionMember6,
    RankByUnionMember2ExprUnionMember7,
]


class RankByUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember2ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember2ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember2ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember2ExprUnionMember2ExprUnionMember0,
    RankByUnionMember3ExprUnionMember2ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember2ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember2ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember3ExprUnionMember2ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember2ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember2ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember2ExprUnionMember3ExprUnionMember0,
    RankByUnionMember3ExprUnionMember2ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember2ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember2ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember3ExprUnionMember2ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember2ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember2ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember2ExprUnionMember4ExprUnionMember0,
    RankByUnionMember3ExprUnionMember2ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember2ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember2ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember3ExprUnionMember2ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember2ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember2ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember2ExprUnionMember5ExprUnionMember0,
    RankByUnionMember3ExprUnionMember2ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember2ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember2ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember3ExprUnionMember2ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember2ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember2ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember2ExprUnionMember6ExprUnionMember0,
    RankByUnionMember3ExprUnionMember2ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember2ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember2ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember3ExprUnionMember2ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember2ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember2ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember2ExprUnionMember7ExprUnionMember0,
    RankByUnionMember3ExprUnionMember2ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember2ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember3ExprUnionMember2ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember3ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember2ExprUnionMember0,
    RankByUnionMember3ExprUnionMember2ExprUnionMember1,
    RankByUnionMember3ExprUnionMember2ExprUnionMember2,
    RankByUnionMember3ExprUnionMember2ExprUnionMember3,
    RankByUnionMember3ExprUnionMember2ExprUnionMember4,
    RankByUnionMember3ExprUnionMember2ExprUnionMember5,
    RankByUnionMember3ExprUnionMember2ExprUnionMember6,
    RankByUnionMember3ExprUnionMember2ExprUnionMember7,
]


class RankByUnionMember3ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember3ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember3ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember3ExprUnionMember2ExprUnionMember0,
    RankByUnionMember3ExprUnionMember3ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember3ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember3ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember3ExprUnionMember3ExprUnionMember0,
    RankByUnionMember3ExprUnionMember3ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember3ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember3ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember3ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember3ExprUnionMember4ExprUnionMember0,
    RankByUnionMember3ExprUnionMember3ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember3ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember3ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember3ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember3ExprUnionMember5ExprUnionMember0,
    RankByUnionMember3ExprUnionMember3ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember3ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember3ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember3ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember3ExprUnionMember6ExprUnionMember0,
    RankByUnionMember3ExprUnionMember3ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember3ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember3ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember3ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember3ExprUnionMember7ExprUnionMember0,
    RankByUnionMember3ExprUnionMember3ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember3ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember3ExprUnionMember3ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember3ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember3ExprUnionMember0,
    RankByUnionMember3ExprUnionMember3ExprUnionMember1,
    RankByUnionMember3ExprUnionMember3ExprUnionMember2,
    RankByUnionMember3ExprUnionMember3ExprUnionMember3,
    RankByUnionMember3ExprUnionMember3ExprUnionMember4,
    RankByUnionMember3ExprUnionMember3ExprUnionMember5,
    RankByUnionMember3ExprUnionMember3ExprUnionMember6,
    RankByUnionMember3ExprUnionMember3ExprUnionMember7,
]


class RankByUnionMember3ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember3ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember4ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember4ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember4ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember4ExprUnionMember2ExprUnionMember0,
    RankByUnionMember3ExprUnionMember4ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember4ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember4ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember3ExprUnionMember4ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember4ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember4ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember4ExprUnionMember3ExprUnionMember0,
    RankByUnionMember3ExprUnionMember4ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember4ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember4ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember3ExprUnionMember4ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember4ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember4ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember4ExprUnionMember4ExprUnionMember0,
    RankByUnionMember3ExprUnionMember4ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember4ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember4ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember3ExprUnionMember4ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember4ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember4ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember4ExprUnionMember5ExprUnionMember0,
    RankByUnionMember3ExprUnionMember4ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember4ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember4ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember3ExprUnionMember4ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember4ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember4ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember4ExprUnionMember6ExprUnionMember0,
    RankByUnionMember3ExprUnionMember4ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember4ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember4ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember3ExprUnionMember4ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember4ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember4ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember4ExprUnionMember7ExprUnionMember0,
    RankByUnionMember3ExprUnionMember4ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember4ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember3ExprUnionMember4ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember3ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember4ExprUnionMember0,
    RankByUnionMember3ExprUnionMember4ExprUnionMember1,
    RankByUnionMember3ExprUnionMember4ExprUnionMember2,
    RankByUnionMember3ExprUnionMember4ExprUnionMember3,
    RankByUnionMember3ExprUnionMember4ExprUnionMember4,
    RankByUnionMember3ExprUnionMember4ExprUnionMember5,
    RankByUnionMember3ExprUnionMember4ExprUnionMember6,
    RankByUnionMember3ExprUnionMember4ExprUnionMember7,
]


class RankByUnionMember3ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember3ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember5ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember5ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember5ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember5ExprUnionMember2ExprUnionMember0,
    RankByUnionMember3ExprUnionMember5ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember5ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember5ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember3ExprUnionMember5ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember5ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember5ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember5ExprUnionMember3ExprUnionMember0,
    RankByUnionMember3ExprUnionMember5ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember5ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember5ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember3ExprUnionMember5ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember5ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember5ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember5ExprUnionMember4ExprUnionMember0,
    RankByUnionMember3ExprUnionMember5ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember5ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember5ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember3ExprUnionMember5ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember5ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember5ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember5ExprUnionMember5ExprUnionMember0,
    RankByUnionMember3ExprUnionMember5ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember5ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember5ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember3ExprUnionMember5ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember5ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember5ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember5ExprUnionMember6ExprUnionMember0,
    RankByUnionMember3ExprUnionMember5ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember5ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember5ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember3ExprUnionMember5ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember5ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember5ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember5ExprUnionMember7ExprUnionMember0,
    RankByUnionMember3ExprUnionMember5ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember5ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember3ExprUnionMember5ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember3ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember5ExprUnionMember0,
    RankByUnionMember3ExprUnionMember5ExprUnionMember1,
    RankByUnionMember3ExprUnionMember5ExprUnionMember2,
    RankByUnionMember3ExprUnionMember5ExprUnionMember3,
    RankByUnionMember3ExprUnionMember5ExprUnionMember4,
    RankByUnionMember3ExprUnionMember5ExprUnionMember5,
    RankByUnionMember3ExprUnionMember5ExprUnionMember6,
    RankByUnionMember3ExprUnionMember5ExprUnionMember7,
]


class RankByUnionMember3ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember6ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember6ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember6ExprUnionMember2ExprUnionMember0,
    RankByUnionMember3ExprUnionMember6ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember6ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember6ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember6ExprUnionMember3ExprUnionMember0,
    RankByUnionMember3ExprUnionMember6ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember6ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember6ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember6ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember6ExprUnionMember4ExprUnionMember0,
    RankByUnionMember3ExprUnionMember6ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember6ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember6ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember6ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember6ExprUnionMember5ExprUnionMember0,
    RankByUnionMember3ExprUnionMember6ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember6ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember6ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember6ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember6ExprUnionMember6ExprUnionMember0,
    RankByUnionMember3ExprUnionMember6ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember6ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember6ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember6ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember6ExprUnionMember7ExprUnionMember0,
    RankByUnionMember3ExprUnionMember6ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember6ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember3ExprUnionMember6ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember3ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember6ExprUnionMember0,
    RankByUnionMember3ExprUnionMember6ExprUnionMember1,
    RankByUnionMember3ExprUnionMember6ExprUnionMember2,
    RankByUnionMember3ExprUnionMember6ExprUnionMember3,
    RankByUnionMember3ExprUnionMember6ExprUnionMember4,
    RankByUnionMember3ExprUnionMember6ExprUnionMember5,
    RankByUnionMember3ExprUnionMember6ExprUnionMember6,
    RankByUnionMember3ExprUnionMember6ExprUnionMember7,
]


class RankByUnionMember3ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember7ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember7ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember7ExprUnionMember2ExprUnionMember0,
    RankByUnionMember3ExprUnionMember7ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember7ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember7ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember7ExprUnionMember3ExprUnionMember0,
    RankByUnionMember3ExprUnionMember7ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember7ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember7ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember7ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember7ExprUnionMember4ExprUnionMember0,
    RankByUnionMember3ExprUnionMember7ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember7ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember7ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember7ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember7ExprUnionMember5ExprUnionMember0,
    RankByUnionMember3ExprUnionMember7ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember7ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember7ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember7ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember7ExprUnionMember6ExprUnionMember0,
    RankByUnionMember3ExprUnionMember7ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember7ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember7ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember3ExprUnionMember7ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember7ExprUnionMember7ExprUnionMember0,
    RankByUnionMember3ExprUnionMember7ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember3ExprUnionMember7ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember3ExprUnionMember7ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember3ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember7ExprUnionMember0,
    RankByUnionMember3ExprUnionMember7ExprUnionMember1,
    RankByUnionMember3ExprUnionMember7ExprUnionMember2,
    RankByUnionMember3ExprUnionMember7ExprUnionMember3,
    RankByUnionMember3ExprUnionMember7ExprUnionMember4,
    RankByUnionMember3ExprUnionMember7ExprUnionMember5,
    RankByUnionMember3ExprUnionMember7ExprUnionMember6,
    RankByUnionMember3ExprUnionMember7ExprUnionMember7,
]


class RankByUnionMember3ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember3ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember0,
    RankByUnionMember3ExprUnionMember1,
    RankByUnionMember3ExprUnionMember2,
    RankByUnionMember3ExprUnionMember3,
    RankByUnionMember3ExprUnionMember4,
    RankByUnionMember3ExprUnionMember5,
    RankByUnionMember3ExprUnionMember6,
    RankByUnionMember3ExprUnionMember7,
]


class RankByUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember4ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember4ExprUnionMember2ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember2ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember2ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember2ExprUnionMember2ExprUnionMember0,
    RankByUnionMember4ExprUnionMember2ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember2ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember2ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember4ExprUnionMember2ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember2ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember2ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember2ExprUnionMember3ExprUnionMember0,
    RankByUnionMember4ExprUnionMember2ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember2ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember2ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember4ExprUnionMember2ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember2ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember2ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember2ExprUnionMember4ExprUnionMember0,
    RankByUnionMember4ExprUnionMember2ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember2ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember2ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember4ExprUnionMember2ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember2ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember2ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember2ExprUnionMember5ExprUnionMember0,
    RankByUnionMember4ExprUnionMember2ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember2ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember2ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember4ExprUnionMember2ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember2ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember2ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember2ExprUnionMember6ExprUnionMember0,
    RankByUnionMember4ExprUnionMember2ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember2ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember2ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember4ExprUnionMember2ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember2ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember2ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember2ExprUnionMember7ExprUnionMember0,
    RankByUnionMember4ExprUnionMember2ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember2ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember4ExprUnionMember2ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember4ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember2ExprUnionMember0,
    RankByUnionMember4ExprUnionMember2ExprUnionMember1,
    RankByUnionMember4ExprUnionMember2ExprUnionMember2,
    RankByUnionMember4ExprUnionMember2ExprUnionMember3,
    RankByUnionMember4ExprUnionMember2ExprUnionMember4,
    RankByUnionMember4ExprUnionMember2ExprUnionMember5,
    RankByUnionMember4ExprUnionMember2ExprUnionMember6,
    RankByUnionMember4ExprUnionMember2ExprUnionMember7,
]


class RankByUnionMember4ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember4ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember4ExprUnionMember3ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember3ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember3ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember3ExprUnionMember2ExprUnionMember0,
    RankByUnionMember4ExprUnionMember3ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember3ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember4ExprUnionMember3ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember3ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember3ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember3ExprUnionMember3ExprUnionMember0,
    RankByUnionMember4ExprUnionMember3ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember3ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember3ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember4ExprUnionMember3ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember3ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember3ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember3ExprUnionMember4ExprUnionMember0,
    RankByUnionMember4ExprUnionMember3ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember3ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember3ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember4ExprUnionMember3ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember3ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember3ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember3ExprUnionMember5ExprUnionMember0,
    RankByUnionMember4ExprUnionMember3ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember3ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember3ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember4ExprUnionMember3ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember3ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember3ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember3ExprUnionMember6ExprUnionMember0,
    RankByUnionMember4ExprUnionMember3ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember3ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember3ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember4ExprUnionMember3ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember3ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember3ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember3ExprUnionMember7ExprUnionMember0,
    RankByUnionMember4ExprUnionMember3ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember3ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember4ExprUnionMember3ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember4ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember3ExprUnionMember0,
    RankByUnionMember4ExprUnionMember3ExprUnionMember1,
    RankByUnionMember4ExprUnionMember3ExprUnionMember2,
    RankByUnionMember4ExprUnionMember3ExprUnionMember3,
    RankByUnionMember4ExprUnionMember3ExprUnionMember4,
    RankByUnionMember4ExprUnionMember3ExprUnionMember5,
    RankByUnionMember4ExprUnionMember3ExprUnionMember6,
    RankByUnionMember4ExprUnionMember3ExprUnionMember7,
]


class RankByUnionMember4ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember4ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember4ExprUnionMember4ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember4ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember4ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember4ExprUnionMember2ExprUnionMember0,
    RankByUnionMember4ExprUnionMember4ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember4ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember4ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember4ExprUnionMember4ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember4ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember4ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember4ExprUnionMember3ExprUnionMember0,
    RankByUnionMember4ExprUnionMember4ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember4ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember4ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember4ExprUnionMember4ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember4ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember4ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember4ExprUnionMember4ExprUnionMember0,
    RankByUnionMember4ExprUnionMember4ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember4ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember4ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember4ExprUnionMember4ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember4ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember4ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember4ExprUnionMember5ExprUnionMember0,
    RankByUnionMember4ExprUnionMember4ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember4ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember4ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember4ExprUnionMember4ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember4ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember4ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember4ExprUnionMember6ExprUnionMember0,
    RankByUnionMember4ExprUnionMember4ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember4ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember4ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember4ExprUnionMember4ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember4ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember4ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember4ExprUnionMember7ExprUnionMember0,
    RankByUnionMember4ExprUnionMember4ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember4ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember4ExprUnionMember4ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember4ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember4ExprUnionMember0,
    RankByUnionMember4ExprUnionMember4ExprUnionMember1,
    RankByUnionMember4ExprUnionMember4ExprUnionMember2,
    RankByUnionMember4ExprUnionMember4ExprUnionMember3,
    RankByUnionMember4ExprUnionMember4ExprUnionMember4,
    RankByUnionMember4ExprUnionMember4ExprUnionMember5,
    RankByUnionMember4ExprUnionMember4ExprUnionMember6,
    RankByUnionMember4ExprUnionMember4ExprUnionMember7,
]


class RankByUnionMember4ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember4ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember4ExprUnionMember5ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember5ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember5ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember5ExprUnionMember2ExprUnionMember0,
    RankByUnionMember4ExprUnionMember5ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember5ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember5ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember4ExprUnionMember5ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember5ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember5ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember5ExprUnionMember3ExprUnionMember0,
    RankByUnionMember4ExprUnionMember5ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember5ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember5ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember4ExprUnionMember5ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember5ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember5ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember5ExprUnionMember4ExprUnionMember0,
    RankByUnionMember4ExprUnionMember5ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember5ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember5ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember4ExprUnionMember5ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember5ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember5ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember5ExprUnionMember5ExprUnionMember0,
    RankByUnionMember4ExprUnionMember5ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember5ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember5ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember4ExprUnionMember5ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember5ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember5ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember5ExprUnionMember6ExprUnionMember0,
    RankByUnionMember4ExprUnionMember5ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember5ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember5ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember4ExprUnionMember5ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember5ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember5ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember5ExprUnionMember7ExprUnionMember0,
    RankByUnionMember4ExprUnionMember5ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember5ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember4ExprUnionMember5ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember4ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember5ExprUnionMember0,
    RankByUnionMember4ExprUnionMember5ExprUnionMember1,
    RankByUnionMember4ExprUnionMember5ExprUnionMember2,
    RankByUnionMember4ExprUnionMember5ExprUnionMember3,
    RankByUnionMember4ExprUnionMember5ExprUnionMember4,
    RankByUnionMember4ExprUnionMember5ExprUnionMember5,
    RankByUnionMember4ExprUnionMember5ExprUnionMember6,
    RankByUnionMember4ExprUnionMember5ExprUnionMember7,
]


class RankByUnionMember4ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember4ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember4ExprUnionMember6ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember6ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember6ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember6ExprUnionMember2ExprUnionMember0,
    RankByUnionMember4ExprUnionMember6ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember6ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember4ExprUnionMember6ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember6ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember6ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember6ExprUnionMember3ExprUnionMember0,
    RankByUnionMember4ExprUnionMember6ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember6ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember6ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember4ExprUnionMember6ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember6ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember6ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember6ExprUnionMember4ExprUnionMember0,
    RankByUnionMember4ExprUnionMember6ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember6ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember6ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember4ExprUnionMember6ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember6ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember6ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember6ExprUnionMember5ExprUnionMember0,
    RankByUnionMember4ExprUnionMember6ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember6ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember6ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember4ExprUnionMember6ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember6ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember6ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember6ExprUnionMember6ExprUnionMember0,
    RankByUnionMember4ExprUnionMember6ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember6ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember6ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember4ExprUnionMember6ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember6ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember6ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember6ExprUnionMember7ExprUnionMember0,
    RankByUnionMember4ExprUnionMember6ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember6ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember4ExprUnionMember6ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember4ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember6ExprUnionMember0,
    RankByUnionMember4ExprUnionMember6ExprUnionMember1,
    RankByUnionMember4ExprUnionMember6ExprUnionMember2,
    RankByUnionMember4ExprUnionMember6ExprUnionMember3,
    RankByUnionMember4ExprUnionMember6ExprUnionMember4,
    RankByUnionMember4ExprUnionMember6ExprUnionMember5,
    RankByUnionMember4ExprUnionMember6ExprUnionMember6,
    RankByUnionMember4ExprUnionMember6ExprUnionMember7,
]


class RankByUnionMember4ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember4ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember4ExprUnionMember7ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember7ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember7ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember7ExprUnionMember2ExprUnionMember0,
    RankByUnionMember4ExprUnionMember7ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember7ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember4ExprUnionMember7ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember7ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember7ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember7ExprUnionMember3ExprUnionMember0,
    RankByUnionMember4ExprUnionMember7ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember7ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember7ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember4ExprUnionMember7ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember7ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember7ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember7ExprUnionMember4ExprUnionMember0,
    RankByUnionMember4ExprUnionMember7ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember7ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember7ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember4ExprUnionMember7ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember7ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember7ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember7ExprUnionMember5ExprUnionMember0,
    RankByUnionMember4ExprUnionMember7ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember7ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember7ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember4ExprUnionMember7ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember7ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember7ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember7ExprUnionMember6ExprUnionMember0,
    RankByUnionMember4ExprUnionMember7ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember7ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4ExprUnionMember7ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember4ExprUnionMember7ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember4ExprUnionMember7ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember4ExprUnionMember7ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember7ExprUnionMember7ExprUnionMember0,
    RankByUnionMember4ExprUnionMember7ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember4ExprUnionMember7ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember4ExprUnionMember7ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember4ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember7ExprUnionMember0,
    RankByUnionMember4ExprUnionMember7ExprUnionMember1,
    RankByUnionMember4ExprUnionMember7ExprUnionMember2,
    RankByUnionMember4ExprUnionMember7ExprUnionMember3,
    RankByUnionMember4ExprUnionMember7ExprUnionMember4,
    RankByUnionMember4ExprUnionMember7ExprUnionMember5,
    RankByUnionMember4ExprUnionMember7ExprUnionMember6,
    RankByUnionMember4ExprUnionMember7ExprUnionMember7,
]


class RankByUnionMember4ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember4ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember4ExprUnionMember0,
    RankByUnionMember4ExprUnionMember1,
    RankByUnionMember4ExprUnionMember2,
    RankByUnionMember4ExprUnionMember3,
    RankByUnionMember4ExprUnionMember4,
    RankByUnionMember4ExprUnionMember5,
    RankByUnionMember4ExprUnionMember6,
    RankByUnionMember4ExprUnionMember7,
]


class RankByUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember5ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember5ExprUnionMember2ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember2ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember2ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember2ExprUnionMember2ExprUnionMember0,
    RankByUnionMember5ExprUnionMember2ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember2ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember2ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember5ExprUnionMember2ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember2ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember2ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember2ExprUnionMember3ExprUnionMember0,
    RankByUnionMember5ExprUnionMember2ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember2ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember2ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember5ExprUnionMember2ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember2ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember2ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember2ExprUnionMember4ExprUnionMember0,
    RankByUnionMember5ExprUnionMember2ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember2ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember2ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember5ExprUnionMember2ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember2ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember2ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember2ExprUnionMember5ExprUnionMember0,
    RankByUnionMember5ExprUnionMember2ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember2ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember2ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember5ExprUnionMember2ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember2ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember2ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember2ExprUnionMember6ExprUnionMember0,
    RankByUnionMember5ExprUnionMember2ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember2ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember2ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember5ExprUnionMember2ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember2ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember2ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember2ExprUnionMember7ExprUnionMember0,
    RankByUnionMember5ExprUnionMember2ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember2ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember5ExprUnionMember2ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember5ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember2ExprUnionMember0,
    RankByUnionMember5ExprUnionMember2ExprUnionMember1,
    RankByUnionMember5ExprUnionMember2ExprUnionMember2,
    RankByUnionMember5ExprUnionMember2ExprUnionMember3,
    RankByUnionMember5ExprUnionMember2ExprUnionMember4,
    RankByUnionMember5ExprUnionMember2ExprUnionMember5,
    RankByUnionMember5ExprUnionMember2ExprUnionMember6,
    RankByUnionMember5ExprUnionMember2ExprUnionMember7,
]


class RankByUnionMember5ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember5ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember5ExprUnionMember3ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember3ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember3ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember3ExprUnionMember2ExprUnionMember0,
    RankByUnionMember5ExprUnionMember3ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember3ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember5ExprUnionMember3ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember3ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember3ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember3ExprUnionMember3ExprUnionMember0,
    RankByUnionMember5ExprUnionMember3ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember3ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember3ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember5ExprUnionMember3ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember3ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember3ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember3ExprUnionMember4ExprUnionMember0,
    RankByUnionMember5ExprUnionMember3ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember3ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember3ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember5ExprUnionMember3ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember3ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember3ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember3ExprUnionMember5ExprUnionMember0,
    RankByUnionMember5ExprUnionMember3ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember3ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember3ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember5ExprUnionMember3ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember3ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember3ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember3ExprUnionMember6ExprUnionMember0,
    RankByUnionMember5ExprUnionMember3ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember3ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember3ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember5ExprUnionMember3ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember3ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember3ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember3ExprUnionMember7ExprUnionMember0,
    RankByUnionMember5ExprUnionMember3ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember3ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember5ExprUnionMember3ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember5ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember3ExprUnionMember0,
    RankByUnionMember5ExprUnionMember3ExprUnionMember1,
    RankByUnionMember5ExprUnionMember3ExprUnionMember2,
    RankByUnionMember5ExprUnionMember3ExprUnionMember3,
    RankByUnionMember5ExprUnionMember3ExprUnionMember4,
    RankByUnionMember5ExprUnionMember3ExprUnionMember5,
    RankByUnionMember5ExprUnionMember3ExprUnionMember6,
    RankByUnionMember5ExprUnionMember3ExprUnionMember7,
]


class RankByUnionMember5ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember5ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember5ExprUnionMember4ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember4ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember4ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember4ExprUnionMember2ExprUnionMember0,
    RankByUnionMember5ExprUnionMember4ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember4ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember4ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember5ExprUnionMember4ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember4ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember4ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember4ExprUnionMember3ExprUnionMember0,
    RankByUnionMember5ExprUnionMember4ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember4ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember4ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember5ExprUnionMember4ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember4ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember4ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember4ExprUnionMember4ExprUnionMember0,
    RankByUnionMember5ExprUnionMember4ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember4ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember4ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember5ExprUnionMember4ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember4ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember4ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember4ExprUnionMember5ExprUnionMember0,
    RankByUnionMember5ExprUnionMember4ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember4ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember4ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember5ExprUnionMember4ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember4ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember4ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember4ExprUnionMember6ExprUnionMember0,
    RankByUnionMember5ExprUnionMember4ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember4ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember4ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember5ExprUnionMember4ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember4ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember4ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember4ExprUnionMember7ExprUnionMember0,
    RankByUnionMember5ExprUnionMember4ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember4ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember5ExprUnionMember4ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember5ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember4ExprUnionMember0,
    RankByUnionMember5ExprUnionMember4ExprUnionMember1,
    RankByUnionMember5ExprUnionMember4ExprUnionMember2,
    RankByUnionMember5ExprUnionMember4ExprUnionMember3,
    RankByUnionMember5ExprUnionMember4ExprUnionMember4,
    RankByUnionMember5ExprUnionMember4ExprUnionMember5,
    RankByUnionMember5ExprUnionMember4ExprUnionMember6,
    RankByUnionMember5ExprUnionMember4ExprUnionMember7,
]


class RankByUnionMember5ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember5ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember5ExprUnionMember5ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember5ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember5ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember5ExprUnionMember2ExprUnionMember0,
    RankByUnionMember5ExprUnionMember5ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember5ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember5ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember5ExprUnionMember5ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember5ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember5ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember5ExprUnionMember3ExprUnionMember0,
    RankByUnionMember5ExprUnionMember5ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember5ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember5ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember5ExprUnionMember5ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember5ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember5ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember5ExprUnionMember4ExprUnionMember0,
    RankByUnionMember5ExprUnionMember5ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember5ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember5ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember5ExprUnionMember5ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember5ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember5ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember5ExprUnionMember5ExprUnionMember0,
    RankByUnionMember5ExprUnionMember5ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember5ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember5ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember5ExprUnionMember5ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember5ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember5ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember5ExprUnionMember6ExprUnionMember0,
    RankByUnionMember5ExprUnionMember5ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember5ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember5ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember5ExprUnionMember5ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember5ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember5ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember5ExprUnionMember7ExprUnionMember0,
    RankByUnionMember5ExprUnionMember5ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember5ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember5ExprUnionMember5ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember5ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember5ExprUnionMember0,
    RankByUnionMember5ExprUnionMember5ExprUnionMember1,
    RankByUnionMember5ExprUnionMember5ExprUnionMember2,
    RankByUnionMember5ExprUnionMember5ExprUnionMember3,
    RankByUnionMember5ExprUnionMember5ExprUnionMember4,
    RankByUnionMember5ExprUnionMember5ExprUnionMember5,
    RankByUnionMember5ExprUnionMember5ExprUnionMember6,
    RankByUnionMember5ExprUnionMember5ExprUnionMember7,
]


class RankByUnionMember5ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember5ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember5ExprUnionMember6ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember6ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember6ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember6ExprUnionMember2ExprUnionMember0,
    RankByUnionMember5ExprUnionMember6ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember6ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember5ExprUnionMember6ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember6ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember6ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember6ExprUnionMember3ExprUnionMember0,
    RankByUnionMember5ExprUnionMember6ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember6ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember6ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember5ExprUnionMember6ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember6ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember6ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember6ExprUnionMember4ExprUnionMember0,
    RankByUnionMember5ExprUnionMember6ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember6ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember6ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember5ExprUnionMember6ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember6ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember6ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember6ExprUnionMember5ExprUnionMember0,
    RankByUnionMember5ExprUnionMember6ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember6ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember6ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember5ExprUnionMember6ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember6ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember6ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember6ExprUnionMember6ExprUnionMember0,
    RankByUnionMember5ExprUnionMember6ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember6ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember6ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember5ExprUnionMember6ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember6ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember6ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember6ExprUnionMember7ExprUnionMember0,
    RankByUnionMember5ExprUnionMember6ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember6ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember5ExprUnionMember6ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember5ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember6ExprUnionMember0,
    RankByUnionMember5ExprUnionMember6ExprUnionMember1,
    RankByUnionMember5ExprUnionMember6ExprUnionMember2,
    RankByUnionMember5ExprUnionMember6ExprUnionMember3,
    RankByUnionMember5ExprUnionMember6ExprUnionMember4,
    RankByUnionMember5ExprUnionMember6ExprUnionMember5,
    RankByUnionMember5ExprUnionMember6ExprUnionMember6,
    RankByUnionMember5ExprUnionMember6ExprUnionMember7,
]


class RankByUnionMember5ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember5ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember5ExprUnionMember7ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember7ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember7ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember7ExprUnionMember2ExprUnionMember0,
    RankByUnionMember5ExprUnionMember7ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember7ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember5ExprUnionMember7ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember7ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember7ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember7ExprUnionMember3ExprUnionMember0,
    RankByUnionMember5ExprUnionMember7ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember7ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember7ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember5ExprUnionMember7ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember7ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember7ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember7ExprUnionMember4ExprUnionMember0,
    RankByUnionMember5ExprUnionMember7ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember7ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember7ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember5ExprUnionMember7ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember7ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember7ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember7ExprUnionMember5ExprUnionMember0,
    RankByUnionMember5ExprUnionMember7ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember7ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember7ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember5ExprUnionMember7ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember7ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember7ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember7ExprUnionMember6ExprUnionMember0,
    RankByUnionMember5ExprUnionMember7ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember7ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5ExprUnionMember7ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember5ExprUnionMember7ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember5ExprUnionMember7ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember5ExprUnionMember7ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember7ExprUnionMember7ExprUnionMember0,
    RankByUnionMember5ExprUnionMember7ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember5ExprUnionMember7ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember5ExprUnionMember7ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember5ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember7ExprUnionMember0,
    RankByUnionMember5ExprUnionMember7ExprUnionMember1,
    RankByUnionMember5ExprUnionMember7ExprUnionMember2,
    RankByUnionMember5ExprUnionMember7ExprUnionMember3,
    RankByUnionMember5ExprUnionMember7ExprUnionMember4,
    RankByUnionMember5ExprUnionMember7ExprUnionMember5,
    RankByUnionMember5ExprUnionMember7ExprUnionMember6,
    RankByUnionMember5ExprUnionMember7ExprUnionMember7,
]


class RankByUnionMember5ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember5ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember5ExprUnionMember0,
    RankByUnionMember5ExprUnionMember1,
    RankByUnionMember5ExprUnionMember2,
    RankByUnionMember5ExprUnionMember3,
    RankByUnionMember5ExprUnionMember4,
    RankByUnionMember5ExprUnionMember5,
    RankByUnionMember5ExprUnionMember6,
    RankByUnionMember5ExprUnionMember7,
]


class RankByUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember2ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember2ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember2ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember2ExprUnionMember2ExprUnionMember0,
    RankByUnionMember6ExprUnionMember2ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember2ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember2ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember6ExprUnionMember2ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember2ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember2ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember2ExprUnionMember3ExprUnionMember0,
    RankByUnionMember6ExprUnionMember2ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember2ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember2ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember6ExprUnionMember2ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember2ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember2ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember2ExprUnionMember4ExprUnionMember0,
    RankByUnionMember6ExprUnionMember2ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember2ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember2ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember6ExprUnionMember2ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember2ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember2ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember2ExprUnionMember5ExprUnionMember0,
    RankByUnionMember6ExprUnionMember2ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember2ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember2ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember6ExprUnionMember2ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember2ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember2ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember2ExprUnionMember6ExprUnionMember0,
    RankByUnionMember6ExprUnionMember2ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember2ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember2ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember6ExprUnionMember2ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember2ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember2ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember2ExprUnionMember7ExprUnionMember0,
    RankByUnionMember6ExprUnionMember2ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember2ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember6ExprUnionMember2ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember6ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember2ExprUnionMember0,
    RankByUnionMember6ExprUnionMember2ExprUnionMember1,
    RankByUnionMember6ExprUnionMember2ExprUnionMember2,
    RankByUnionMember6ExprUnionMember2ExprUnionMember3,
    RankByUnionMember6ExprUnionMember2ExprUnionMember4,
    RankByUnionMember6ExprUnionMember2ExprUnionMember5,
    RankByUnionMember6ExprUnionMember2ExprUnionMember6,
    RankByUnionMember6ExprUnionMember2ExprUnionMember7,
]


class RankByUnionMember6ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember3ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember3ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember3ExprUnionMember2ExprUnionMember0,
    RankByUnionMember6ExprUnionMember3ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember3ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember3ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember3ExprUnionMember3ExprUnionMember0,
    RankByUnionMember6ExprUnionMember3ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember3ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember3ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember3ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember3ExprUnionMember4ExprUnionMember0,
    RankByUnionMember6ExprUnionMember3ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember3ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember3ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember3ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember3ExprUnionMember5ExprUnionMember0,
    RankByUnionMember6ExprUnionMember3ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember3ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember3ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember3ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember3ExprUnionMember6ExprUnionMember0,
    RankByUnionMember6ExprUnionMember3ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember3ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember3ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember3ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember3ExprUnionMember7ExprUnionMember0,
    RankByUnionMember6ExprUnionMember3ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember3ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember6ExprUnionMember3ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember6ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember3ExprUnionMember0,
    RankByUnionMember6ExprUnionMember3ExprUnionMember1,
    RankByUnionMember6ExprUnionMember3ExprUnionMember2,
    RankByUnionMember6ExprUnionMember3ExprUnionMember3,
    RankByUnionMember6ExprUnionMember3ExprUnionMember4,
    RankByUnionMember6ExprUnionMember3ExprUnionMember5,
    RankByUnionMember6ExprUnionMember3ExprUnionMember6,
    RankByUnionMember6ExprUnionMember3ExprUnionMember7,
]


class RankByUnionMember6ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember6ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember4ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember4ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember4ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember4ExprUnionMember2ExprUnionMember0,
    RankByUnionMember6ExprUnionMember4ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember4ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember4ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember6ExprUnionMember4ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember4ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember4ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember4ExprUnionMember3ExprUnionMember0,
    RankByUnionMember6ExprUnionMember4ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember4ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember4ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember6ExprUnionMember4ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember4ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember4ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember4ExprUnionMember4ExprUnionMember0,
    RankByUnionMember6ExprUnionMember4ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember4ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember4ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember6ExprUnionMember4ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember4ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember4ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember4ExprUnionMember5ExprUnionMember0,
    RankByUnionMember6ExprUnionMember4ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember4ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember4ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember6ExprUnionMember4ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember4ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember4ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember4ExprUnionMember6ExprUnionMember0,
    RankByUnionMember6ExprUnionMember4ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember4ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember4ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember6ExprUnionMember4ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember4ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember4ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember4ExprUnionMember7ExprUnionMember0,
    RankByUnionMember6ExprUnionMember4ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember4ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember6ExprUnionMember4ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember6ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember4ExprUnionMember0,
    RankByUnionMember6ExprUnionMember4ExprUnionMember1,
    RankByUnionMember6ExprUnionMember4ExprUnionMember2,
    RankByUnionMember6ExprUnionMember4ExprUnionMember3,
    RankByUnionMember6ExprUnionMember4ExprUnionMember4,
    RankByUnionMember6ExprUnionMember4ExprUnionMember5,
    RankByUnionMember6ExprUnionMember4ExprUnionMember6,
    RankByUnionMember6ExprUnionMember4ExprUnionMember7,
]


class RankByUnionMember6ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember6ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember5ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember5ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember5ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember5ExprUnionMember2ExprUnionMember0,
    RankByUnionMember6ExprUnionMember5ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember5ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember5ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember6ExprUnionMember5ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember5ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember5ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember5ExprUnionMember3ExprUnionMember0,
    RankByUnionMember6ExprUnionMember5ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember5ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember5ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember6ExprUnionMember5ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember5ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember5ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember5ExprUnionMember4ExprUnionMember0,
    RankByUnionMember6ExprUnionMember5ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember5ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember5ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember6ExprUnionMember5ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember5ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember5ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember5ExprUnionMember5ExprUnionMember0,
    RankByUnionMember6ExprUnionMember5ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember5ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember5ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember6ExprUnionMember5ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember5ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember5ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember5ExprUnionMember6ExprUnionMember0,
    RankByUnionMember6ExprUnionMember5ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember5ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember5ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember6ExprUnionMember5ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember5ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember5ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember5ExprUnionMember7ExprUnionMember0,
    RankByUnionMember6ExprUnionMember5ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember5ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember6ExprUnionMember5ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember6ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember5ExprUnionMember0,
    RankByUnionMember6ExprUnionMember5ExprUnionMember1,
    RankByUnionMember6ExprUnionMember5ExprUnionMember2,
    RankByUnionMember6ExprUnionMember5ExprUnionMember3,
    RankByUnionMember6ExprUnionMember5ExprUnionMember4,
    RankByUnionMember6ExprUnionMember5ExprUnionMember5,
    RankByUnionMember6ExprUnionMember5ExprUnionMember6,
    RankByUnionMember6ExprUnionMember5ExprUnionMember7,
]


class RankByUnionMember6ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember6ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember6ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember6ExprUnionMember2ExprUnionMember0,
    RankByUnionMember6ExprUnionMember6ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember6ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember6ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember6ExprUnionMember3ExprUnionMember0,
    RankByUnionMember6ExprUnionMember6ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember6ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember6ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember6ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember6ExprUnionMember4ExprUnionMember0,
    RankByUnionMember6ExprUnionMember6ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember6ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember6ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember6ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember6ExprUnionMember5ExprUnionMember0,
    RankByUnionMember6ExprUnionMember6ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember6ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember6ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember6ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember6ExprUnionMember6ExprUnionMember0,
    RankByUnionMember6ExprUnionMember6ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember6ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember6ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember6ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember6ExprUnionMember7ExprUnionMember0,
    RankByUnionMember6ExprUnionMember6ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember6ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember6ExprUnionMember6ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember6ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember6ExprUnionMember0,
    RankByUnionMember6ExprUnionMember6ExprUnionMember1,
    RankByUnionMember6ExprUnionMember6ExprUnionMember2,
    RankByUnionMember6ExprUnionMember6ExprUnionMember3,
    RankByUnionMember6ExprUnionMember6ExprUnionMember4,
    RankByUnionMember6ExprUnionMember6ExprUnionMember5,
    RankByUnionMember6ExprUnionMember6ExprUnionMember6,
    RankByUnionMember6ExprUnionMember6ExprUnionMember7,
]


class RankByUnionMember6ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember7ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember7ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember7ExprUnionMember2ExprUnionMember0,
    RankByUnionMember6ExprUnionMember7ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember7ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember7ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember7ExprUnionMember3ExprUnionMember0,
    RankByUnionMember6ExprUnionMember7ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember7ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember7ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember7ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember7ExprUnionMember4ExprUnionMember0,
    RankByUnionMember6ExprUnionMember7ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember7ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember7ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember7ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember7ExprUnionMember5ExprUnionMember0,
    RankByUnionMember6ExprUnionMember7ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember7ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember7ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember7ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember7ExprUnionMember6ExprUnionMember0,
    RankByUnionMember6ExprUnionMember7ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember7ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember7ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember6ExprUnionMember7ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember7ExprUnionMember7ExprUnionMember0,
    RankByUnionMember6ExprUnionMember7ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember6ExprUnionMember7ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember6ExprUnionMember7ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember6ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember7ExprUnionMember0,
    RankByUnionMember6ExprUnionMember7ExprUnionMember1,
    RankByUnionMember6ExprUnionMember7ExprUnionMember2,
    RankByUnionMember6ExprUnionMember7ExprUnionMember3,
    RankByUnionMember6ExprUnionMember7ExprUnionMember4,
    RankByUnionMember6ExprUnionMember7ExprUnionMember5,
    RankByUnionMember6ExprUnionMember7ExprUnionMember6,
    RankByUnionMember6ExprUnionMember7ExprUnionMember7,
]


class RankByUnionMember6ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember6ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember0,
    RankByUnionMember6ExprUnionMember1,
    RankByUnionMember6ExprUnionMember2,
    RankByUnionMember6ExprUnionMember3,
    RankByUnionMember6ExprUnionMember4,
    RankByUnionMember6ExprUnionMember5,
    RankByUnionMember6ExprUnionMember6,
    RankByUnionMember6ExprUnionMember7,
]


class RankByUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember2ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember2ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember2ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember2ExprUnionMember2ExprUnionMember0,
    RankByUnionMember7ExprUnionMember2ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember2ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember2ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember7ExprUnionMember2ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember2ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember2ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember2ExprUnionMember3ExprUnionMember0,
    RankByUnionMember7ExprUnionMember2ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember2ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember2ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember7ExprUnionMember2ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember2ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember2ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember2ExprUnionMember4ExprUnionMember0,
    RankByUnionMember7ExprUnionMember2ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember2ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember2ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember7ExprUnionMember2ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember2ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember2ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember2ExprUnionMember5ExprUnionMember0,
    RankByUnionMember7ExprUnionMember2ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember2ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember2ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember7ExprUnionMember2ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember2ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember2ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember2ExprUnionMember6ExprUnionMember0,
    RankByUnionMember7ExprUnionMember2ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember2ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember2ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember7ExprUnionMember2ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember2ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember2ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember2ExprUnionMember7ExprUnionMember0,
    RankByUnionMember7ExprUnionMember2ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember2ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember7ExprUnionMember2ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember7ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember2ExprUnionMember0,
    RankByUnionMember7ExprUnionMember2ExprUnionMember1,
    RankByUnionMember7ExprUnionMember2ExprUnionMember2,
    RankByUnionMember7ExprUnionMember2ExprUnionMember3,
    RankByUnionMember7ExprUnionMember2ExprUnionMember4,
    RankByUnionMember7ExprUnionMember2ExprUnionMember5,
    RankByUnionMember7ExprUnionMember2ExprUnionMember6,
    RankByUnionMember7ExprUnionMember2ExprUnionMember7,
]


class RankByUnionMember7ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember3ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember3ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember3ExprUnionMember2ExprUnionMember0,
    RankByUnionMember7ExprUnionMember3ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember3ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember3ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember3ExprUnionMember3ExprUnionMember0,
    RankByUnionMember7ExprUnionMember3ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember3ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember3ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember3ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember3ExprUnionMember4ExprUnionMember0,
    RankByUnionMember7ExprUnionMember3ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember3ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember3ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember3ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember3ExprUnionMember5ExprUnionMember0,
    RankByUnionMember7ExprUnionMember3ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember3ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember3ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember3ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember3ExprUnionMember6ExprUnionMember0,
    RankByUnionMember7ExprUnionMember3ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember3ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember3ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember3ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember3ExprUnionMember7ExprUnionMember0,
    RankByUnionMember7ExprUnionMember3ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember3ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember7ExprUnionMember3ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember7ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember3ExprUnionMember0,
    RankByUnionMember7ExprUnionMember3ExprUnionMember1,
    RankByUnionMember7ExprUnionMember3ExprUnionMember2,
    RankByUnionMember7ExprUnionMember3ExprUnionMember3,
    RankByUnionMember7ExprUnionMember3ExprUnionMember4,
    RankByUnionMember7ExprUnionMember3ExprUnionMember5,
    RankByUnionMember7ExprUnionMember3ExprUnionMember6,
    RankByUnionMember7ExprUnionMember3ExprUnionMember7,
]


class RankByUnionMember7ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember7ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember4ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember4ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember4ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember4ExprUnionMember2ExprUnionMember0,
    RankByUnionMember7ExprUnionMember4ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember4ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember4ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember7ExprUnionMember4ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember4ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember4ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember4ExprUnionMember3ExprUnionMember0,
    RankByUnionMember7ExprUnionMember4ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember4ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember4ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember7ExprUnionMember4ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember4ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember4ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember4ExprUnionMember4ExprUnionMember0,
    RankByUnionMember7ExprUnionMember4ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember4ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember4ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember7ExprUnionMember4ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember4ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember4ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember4ExprUnionMember5ExprUnionMember0,
    RankByUnionMember7ExprUnionMember4ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember4ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember4ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember7ExprUnionMember4ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember4ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember4ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember4ExprUnionMember6ExprUnionMember0,
    RankByUnionMember7ExprUnionMember4ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember4ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember4ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember7ExprUnionMember4ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember4ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember4ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember4ExprUnionMember7ExprUnionMember0,
    RankByUnionMember7ExprUnionMember4ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember4ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember7ExprUnionMember4ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember7ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember4ExprUnionMember0,
    RankByUnionMember7ExprUnionMember4ExprUnionMember1,
    RankByUnionMember7ExprUnionMember4ExprUnionMember2,
    RankByUnionMember7ExprUnionMember4ExprUnionMember3,
    RankByUnionMember7ExprUnionMember4ExprUnionMember4,
    RankByUnionMember7ExprUnionMember4ExprUnionMember5,
    RankByUnionMember7ExprUnionMember4ExprUnionMember6,
    RankByUnionMember7ExprUnionMember4ExprUnionMember7,
]


class RankByUnionMember7ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember7ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember5ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember5ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember5ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember5ExprUnionMember2ExprUnionMember0,
    RankByUnionMember7ExprUnionMember5ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember5ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember5ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember7ExprUnionMember5ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember5ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember5ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember5ExprUnionMember3ExprUnionMember0,
    RankByUnionMember7ExprUnionMember5ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember5ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember5ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember7ExprUnionMember5ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember5ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember5ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember5ExprUnionMember4ExprUnionMember0,
    RankByUnionMember7ExprUnionMember5ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember5ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember5ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember7ExprUnionMember5ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember5ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember5ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember5ExprUnionMember5ExprUnionMember0,
    RankByUnionMember7ExprUnionMember5ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember5ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember5ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember7ExprUnionMember5ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember5ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember5ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember5ExprUnionMember6ExprUnionMember0,
    RankByUnionMember7ExprUnionMember5ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember5ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember5ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember7ExprUnionMember5ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember5ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember5ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember5ExprUnionMember7ExprUnionMember0,
    RankByUnionMember7ExprUnionMember5ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember5ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember7ExprUnionMember5ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember7ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember5ExprUnionMember0,
    RankByUnionMember7ExprUnionMember5ExprUnionMember1,
    RankByUnionMember7ExprUnionMember5ExprUnionMember2,
    RankByUnionMember7ExprUnionMember5ExprUnionMember3,
    RankByUnionMember7ExprUnionMember5ExprUnionMember4,
    RankByUnionMember7ExprUnionMember5ExprUnionMember5,
    RankByUnionMember7ExprUnionMember5ExprUnionMember6,
    RankByUnionMember7ExprUnionMember5ExprUnionMember7,
]


class RankByUnionMember7ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember6ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember6ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember6ExprUnionMember2ExprUnionMember0,
    RankByUnionMember7ExprUnionMember6ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember6ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember6ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember6ExprUnionMember3ExprUnionMember0,
    RankByUnionMember7ExprUnionMember6ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember6ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember6ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember6ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember6ExprUnionMember4ExprUnionMember0,
    RankByUnionMember7ExprUnionMember6ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember6ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember6ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember6ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember6ExprUnionMember5ExprUnionMember0,
    RankByUnionMember7ExprUnionMember6ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember6ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember6ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember6ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember6ExprUnionMember6ExprUnionMember0,
    RankByUnionMember7ExprUnionMember6ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember6ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember6ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember6ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember6ExprUnionMember7ExprUnionMember0,
    RankByUnionMember7ExprUnionMember6ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember6ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember7ExprUnionMember6ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember7ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember6ExprUnionMember0,
    RankByUnionMember7ExprUnionMember6ExprUnionMember1,
    RankByUnionMember7ExprUnionMember6ExprUnionMember2,
    RankByUnionMember7ExprUnionMember6ExprUnionMember3,
    RankByUnionMember7ExprUnionMember6ExprUnionMember4,
    RankByUnionMember7ExprUnionMember6ExprUnionMember5,
    RankByUnionMember7ExprUnionMember6ExprUnionMember6,
    RankByUnionMember7ExprUnionMember6ExprUnionMember7,
]


class RankByUnionMember7ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember7ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember7ExprUnionMember2Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember7ExprUnionMember2ExprUnionMember0,
    RankByUnionMember7ExprUnionMember7ExprUnionMember2ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember7ExprUnionMember2Expr]]

    op: Required[Literal["Sum"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember7ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember7ExprUnionMember3ExprUnionMember0,
    RankByUnionMember7ExprUnionMember7ExprUnionMember3ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember7ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember7ExprUnionMember3Expr]]

    op: Required[Literal["Mult"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember4ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember4ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember7ExprUnionMember4Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember7ExprUnionMember4ExprUnionMember0,
    RankByUnionMember7ExprUnionMember7ExprUnionMember4ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember7ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember7ExprUnionMember4Expr]]

    op: Required[Literal["Div"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember7ExprUnionMember5Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember7ExprUnionMember5ExprUnionMember0,
    RankByUnionMember7ExprUnionMember7ExprUnionMember5ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember7ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember7ExprUnionMember5Expr]]

    op: Required[Literal["Max"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember7ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember7ExprUnionMember6ExprUnionMember0,
    RankByUnionMember7ExprUnionMember7ExprUnionMember6ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember7ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember7ExprUnionMember6Expr]]

    op: Required[Literal["Min"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    op: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    op: Required[Literal["Const"]]

    value: Required[float]


RankByUnionMember7ExprUnionMember7ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember7ExprUnionMember7ExprUnionMember0,
    RankByUnionMember7ExprUnionMember7ExprUnionMember7ExprUnionMember1,
]


class RankByUnionMember7ExprUnionMember7ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember7ExprUnionMember7ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember7ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember7ExprUnionMember0,
    RankByUnionMember7ExprUnionMember7ExprUnionMember1,
    RankByUnionMember7ExprUnionMember7ExprUnionMember2,
    RankByUnionMember7ExprUnionMember7ExprUnionMember3,
    RankByUnionMember7ExprUnionMember7ExprUnionMember4,
    RankByUnionMember7ExprUnionMember7ExprUnionMember5,
    RankByUnionMember7ExprUnionMember7ExprUnionMember6,
    RankByUnionMember7ExprUnionMember7ExprUnionMember7,
]


class RankByUnionMember7ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember7ExprUnionMember7Expr]

    op: Required[Literal["Log"]]


RankByUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember0,
    RankByUnionMember7ExprUnionMember1,
    RankByUnionMember7ExprUnionMember2,
    RankByUnionMember7ExprUnionMember3,
    RankByUnionMember7ExprUnionMember4,
    RankByUnionMember7ExprUnionMember5,
    RankByUnionMember7ExprUnionMember6,
    RankByUnionMember7ExprUnionMember7,
]


class RankByUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember7Expr]

    op: Required[Literal["Log"]]


RankBy: TypeAlias = Union[
    RankByUnionMember0,
    RankByUnionMember1,
    RankByUnionMember2,
    RankByUnionMember3,
    RankByUnionMember4,
    RankByUnionMember5,
    RankByUnionMember6,
    RankByUnionMember7,
]
