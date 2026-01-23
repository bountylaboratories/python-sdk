# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "RawRepoCountParams",
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
]


class RawRepoCountParams(TypedDict, total=False):
    filters: Required[Filters]
    """Filters to apply (required)"""


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
