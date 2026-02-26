# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "SearchRepoSearchParams",
    "Filters",
    "FiltersUnionMember0",
    "FiltersUnionMember1",
    "FiltersUnionMember1Filter",
    "FiltersUnionMember2",
    "FiltersUnionMember2Filter",
    "FiltersUnionMember2FilterUnionMember0",
    "FiltersUnionMember2FilterUnionMember1",
    "FiltersUnionMember2FilterUnionMember1Filter",
    "IncludeAttributes",
    "IncludeAttributesContributors",
    "IncludeAttributesContributorsFilters",
    "IncludeAttributesContributorsFiltersUnionMember0",
    "IncludeAttributesContributorsFiltersUnionMember1",
    "IncludeAttributesContributorsFiltersUnionMember1Filter",
    "IncludeAttributesContributorsFiltersUnionMember2",
    "IncludeAttributesContributorsFiltersUnionMember2Filter",
    "IncludeAttributesContributorsFiltersUnionMember2FilterUnionMember0",
    "IncludeAttributesContributorsFiltersUnionMember2FilterUnionMember1",
    "IncludeAttributesContributorsFiltersUnionMember2FilterUnionMember1Filter",
    "IncludeAttributesStarrers",
    "IncludeAttributesStarrersFilters",
    "IncludeAttributesStarrersFiltersUnionMember0",
    "IncludeAttributesStarrersFiltersUnionMember1",
    "IncludeAttributesStarrersFiltersUnionMember1Filter",
    "IncludeAttributesStarrersFiltersUnionMember2",
    "IncludeAttributesStarrersFiltersUnionMember2Filter",
    "IncludeAttributesStarrersFiltersUnionMember2FilterUnionMember0",
    "IncludeAttributesStarrersFiltersUnionMember2FilterUnionMember1",
    "IncludeAttributesStarrersFiltersUnionMember2FilterUnionMember1Filter",
    "RankBy",
    "RankByUnionMember0",
    "RankByUnionMember1",
    "RankByUnionMember2",
    "RankByUnionMember3",
    "RankByUnionMember3Expr",
    "RankByUnionMember3ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember3",
    "RankByUnionMember3ExprUnionMember3Expr",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember3",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember3Expr",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember4",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember5",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember6",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember6Expr",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember7",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember7Expr",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember8",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember8Expr",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember9",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember9Expr",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember3ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember4",
    "RankByUnionMember3ExprUnionMember5",
    "RankByUnionMember3ExprUnionMember6",
    "RankByUnionMember3ExprUnionMember6Expr",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember3",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember3Expr",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember4",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember5",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember6",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember6Expr",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember7",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember7Expr",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember8",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember8Expr",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember9",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember9Expr",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember6ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember7",
    "RankByUnionMember3ExprUnionMember7Expr",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember3",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember3Expr",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember4",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember5",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember6",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember6Expr",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember7",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember7Expr",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember8",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember8Expr",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember9",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember9Expr",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember7ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember8",
    "RankByUnionMember3ExprUnionMember8Expr",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember3",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember3Expr",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember4",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember5",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember6",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember6Expr",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember7",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember7Expr",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember8",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember8Expr",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember9",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember9Expr",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember8ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember9",
    "RankByUnionMember3ExprUnionMember9Expr",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember3",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember3Expr",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember4",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember5",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember6",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember6Expr",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember7",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember7Expr",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember8",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember8Expr",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember9",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember9Expr",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember3ExprUnionMember9ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember4",
    "RankByUnionMember5",
    "RankByUnionMember6",
    "RankByUnionMember6Expr",
    "RankByUnionMember6ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember3",
    "RankByUnionMember6ExprUnionMember3Expr",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember3",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember3Expr",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember4",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember5",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember6",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember6Expr",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember7",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember7Expr",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember8",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember8Expr",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember9",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember9Expr",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember3ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember4",
    "RankByUnionMember6ExprUnionMember5",
    "RankByUnionMember6ExprUnionMember6",
    "RankByUnionMember6ExprUnionMember6Expr",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember3",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember3Expr",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember4",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember5",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember6",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember6Expr",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember7",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember7Expr",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember8",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember8Expr",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember9",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember9Expr",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember6ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember7",
    "RankByUnionMember6ExprUnionMember7Expr",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember3",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember3Expr",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember4",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember5",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember6",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember6Expr",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember7",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember7Expr",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember8",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember8Expr",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember9",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember9Expr",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember7ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember8",
    "RankByUnionMember6ExprUnionMember8Expr",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember3",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember3Expr",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember4",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember5",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember6",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember6Expr",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember7",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember7Expr",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember8",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember8Expr",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember9",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember9Expr",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember8ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember9",
    "RankByUnionMember6ExprUnionMember9Expr",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember3",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember3Expr",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember4",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember5",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember6",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember6Expr",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember7",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember7Expr",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember8",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember8Expr",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember9",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember9Expr",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember6ExprUnionMember9ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember7",
    "RankByUnionMember7Expr",
    "RankByUnionMember7ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember3",
    "RankByUnionMember7ExprUnionMember3Expr",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember3",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember3Expr",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember4",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember5",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember6",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember6Expr",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember7",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember7Expr",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember8",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember8Expr",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember9",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember9Expr",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember3ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember4",
    "RankByUnionMember7ExprUnionMember5",
    "RankByUnionMember7ExprUnionMember6",
    "RankByUnionMember7ExprUnionMember6Expr",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember3",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember3Expr",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember4",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember5",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember6",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember6Expr",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember7",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember7Expr",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember8",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember8Expr",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember9",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember9Expr",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember6ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember7",
    "RankByUnionMember7ExprUnionMember7Expr",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember3",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember3Expr",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember4",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember5",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember6",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember6Expr",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember7",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember7Expr",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember8",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember8Expr",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember9",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember9Expr",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember7ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember8",
    "RankByUnionMember7ExprUnionMember8Expr",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember3",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember3Expr",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember4",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember5",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember6",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember6Expr",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember7",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember7Expr",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember8",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember8Expr",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember9",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember9Expr",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember8ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember9",
    "RankByUnionMember7ExprUnionMember9Expr",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember3",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember3Expr",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember4",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember5",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember6",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember6Expr",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember7",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember7Expr",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember8",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember8Expr",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember9",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember9Expr",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember7ExprUnionMember9ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember8",
    "RankByUnionMember8Expr",
    "RankByUnionMember8ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember3",
    "RankByUnionMember8ExprUnionMember3Expr",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember3",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember3Expr",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember4",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember5",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember6",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember6Expr",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember7",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember7Expr",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember8",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember8Expr",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember9",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember9Expr",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember3ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember4",
    "RankByUnionMember8ExprUnionMember5",
    "RankByUnionMember8ExprUnionMember6",
    "RankByUnionMember8ExprUnionMember6Expr",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember3",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember3Expr",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember4",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember5",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember6",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember6Expr",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember7",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember7Expr",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember8",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember8Expr",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember9",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember9Expr",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember6ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember7",
    "RankByUnionMember8ExprUnionMember7Expr",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember3",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember3Expr",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember4",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember5",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember6",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember6Expr",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember7",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember7Expr",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember8",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember8Expr",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember9",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember9Expr",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember7ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember8",
    "RankByUnionMember8ExprUnionMember8Expr",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember3",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember3Expr",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember4",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember5",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember6",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember6Expr",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember7",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember7Expr",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember8",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember8Expr",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember9",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember9Expr",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember8ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember9",
    "RankByUnionMember8ExprUnionMember9Expr",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember3",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember3Expr",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember4",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember5",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember6",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember6Expr",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember7",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember7Expr",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember8",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember8Expr",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember9",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember9Expr",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember8ExprUnionMember9ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember9",
    "RankByUnionMember9Expr",
    "RankByUnionMember9ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember3",
    "RankByUnionMember9ExprUnionMember3Expr",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember3",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember3Expr",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember4",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember5",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember6",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember6Expr",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember7",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember7Expr",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember8",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember8Expr",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember9",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember9Expr",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember3ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember4",
    "RankByUnionMember9ExprUnionMember5",
    "RankByUnionMember9ExprUnionMember6",
    "RankByUnionMember9ExprUnionMember6Expr",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember3",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember3Expr",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember4",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember5",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember6",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember6Expr",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember7",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember7Expr",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember8",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember8Expr",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember9",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember9Expr",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember6ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember7",
    "RankByUnionMember9ExprUnionMember7Expr",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember3",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember3Expr",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember4",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember5",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember6",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember6Expr",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember7",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember7Expr",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember8",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember8Expr",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember9",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember9Expr",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember7ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember8",
    "RankByUnionMember9ExprUnionMember8Expr",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember3",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember3Expr",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember4",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember5",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember6",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember6Expr",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember7",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember7Expr",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember8",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember8Expr",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember9",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember9Expr",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember8ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember9",
    "RankByUnionMember9ExprUnionMember9Expr",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember3",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember3Expr",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember3ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember3ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember3ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember4",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember5",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember6",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember6Expr",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember6ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember6ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember6ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember7",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember7Expr",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember7ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember7ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember7ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember8",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember8Expr",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember8ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember8ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember8ExprUnionMember2",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember9",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember9Expr",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember9ExprUnionMember0",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember9ExprUnionMember1",
    "RankByUnionMember9ExprUnionMember9ExprUnionMember9ExprUnionMember2",
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

    apply_filters_to_include_attributes: Annotated[bool, PropertyInfo(alias="applyFiltersToIncludeAttributes")]
    """
    When true, applies the search filter to all user-returning includeAttributes
    (contributors, starrers). This filters the returned users to match the same
    criteria.
    """

    enable_pagination: Annotated[bool, PropertyInfo(alias="enablePagination")]
    """Enable cursor-based pagination to fetch results across multiple requests"""

    filters: Filters
    """Filters to apply (required)"""

    first: int
    """Alias for maxResults (takes precedence if both provided)"""

    include_attributes: Annotated[IncludeAttributes, PropertyInfo(alias="includeAttributes")]
    """Optional graph relationships and enrichment attributes"""

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
    """Maximum number of results to return (default: 100, max: 1000)"""

    rank_by: Annotated[RankBy, PropertyInfo(alias="rankBy")]
    """Custom ranking formula (AST expression).

    If not provided, uses default log-normalized 70/20/10 formula (70% semantic
    similarity, 20% popularity, 10% activity).
    """


class FiltersUnionMember0(TypedDict, total=False):
    field: Required[str]
    """Field name to filter on"""

    op: Required[
        Literal[
            "Eq",
            "NotEq",
            "In",
            "NotIn",
            "Lt",
            "Lte",
            "Gt",
            "Gte",
            "Glob",
            "NotGlob",
            "IGlob",
            "NotIGlob",
            "Regex",
            "Contains",
            "NotContains",
            "ContainsAny",
            "NotContainsAny",
            "AnyLt",
            "AnyLte",
            "AnyGt",
            "AnyGte",
            "ContainsAllTokens",
        ]
    ]
    """Filter operator"""

    value: Required[Union[str, float, bool, SequenceNotStr[str], Iterable[float]]]
    """Filter value (type depends on field and operator)"""


class FiltersUnionMember1Filter(TypedDict, total=False):
    field: Required[str]
    """Field name to filter on"""

    op: Required[
        Literal[
            "Eq",
            "NotEq",
            "In",
            "NotIn",
            "Lt",
            "Lte",
            "Gt",
            "Gte",
            "Glob",
            "NotGlob",
            "IGlob",
            "NotIGlob",
            "Regex",
            "Contains",
            "NotContains",
            "ContainsAny",
            "NotContainsAny",
            "AnyLt",
            "AnyLte",
            "AnyGt",
            "AnyGte",
            "ContainsAllTokens",
        ]
    ]
    """Filter operator"""

    value: Required[Union[str, float, bool, SequenceNotStr[str], Iterable[float]]]
    """Filter value (type depends on field and operator)"""


class FiltersUnionMember1(TypedDict, total=False):
    filters: Required[Iterable[FiltersUnionMember1Filter]]
    """Array of field filters"""

    op: Required[Literal["And", "Or"]]
    """Composite operator"""


class FiltersUnionMember2FilterUnionMember0(TypedDict, total=False):
    field: Required[str]
    """Field name to filter on"""

    op: Required[
        Literal[
            "Eq",
            "NotEq",
            "In",
            "NotIn",
            "Lt",
            "Lte",
            "Gt",
            "Gte",
            "Glob",
            "NotGlob",
            "IGlob",
            "NotIGlob",
            "Regex",
            "Contains",
            "NotContains",
            "ContainsAny",
            "NotContainsAny",
            "AnyLt",
            "AnyLte",
            "AnyGt",
            "AnyGte",
            "ContainsAllTokens",
        ]
    ]
    """Filter operator"""

    value: Required[Union[str, float, bool, SequenceNotStr[str], Iterable[float]]]
    """Filter value (type depends on field and operator)"""


class FiltersUnionMember2FilterUnionMember1Filter(TypedDict, total=False):
    field: Required[str]
    """Field name to filter on"""

    op: Required[
        Literal[
            "Eq",
            "NotEq",
            "In",
            "NotIn",
            "Lt",
            "Lte",
            "Gt",
            "Gte",
            "Glob",
            "NotGlob",
            "IGlob",
            "NotIGlob",
            "Regex",
            "Contains",
            "NotContains",
            "ContainsAny",
            "NotContainsAny",
            "AnyLt",
            "AnyLte",
            "AnyGt",
            "AnyGte",
            "ContainsAllTokens",
        ]
    ]
    """Filter operator"""

    value: Required[Union[str, float, bool, SequenceNotStr[str], Iterable[float]]]
    """Filter value (type depends on field and operator)"""


class FiltersUnionMember2FilterUnionMember1(TypedDict, total=False):
    filters: Required[Iterable[FiltersUnionMember2FilterUnionMember1Filter]]
    """Array of field filters"""

    op: Required[Literal["And", "Or"]]
    """Composite operator"""


FiltersUnionMember2Filter: TypeAlias = Union[
    FiltersUnionMember2FilterUnionMember0, FiltersUnionMember2FilterUnionMember1
]


class FiltersUnionMember2(TypedDict, total=False):
    filters: Required[Iterable[FiltersUnionMember2Filter]]
    """Array of filters"""

    op: Required[Literal["And", "Or"]]
    """Composite operator"""


Filters: TypeAlias = Union[FiltersUnionMember0, FiltersUnionMember1, FiltersUnionMember2]


class IncludeAttributesContributorsFiltersUnionMember0(TypedDict, total=False):
    field: Required[str]
    """Field name to filter on"""

    op: Required[
        Literal[
            "Eq",
            "NotEq",
            "In",
            "NotIn",
            "Lt",
            "Lte",
            "Gt",
            "Gte",
            "Glob",
            "NotGlob",
            "IGlob",
            "NotIGlob",
            "Regex",
            "Contains",
            "NotContains",
            "ContainsAny",
            "NotContainsAny",
            "AnyLt",
            "AnyLte",
            "AnyGt",
            "AnyGte",
            "ContainsAllTokens",
        ]
    ]
    """Filter operator"""

    value: Required[Union[str, float, bool, SequenceNotStr[str], Iterable[float]]]
    """Filter value (type depends on field and operator)"""


class IncludeAttributesContributorsFiltersUnionMember1Filter(TypedDict, total=False):
    field: Required[str]
    """Field name to filter on"""

    op: Required[
        Literal[
            "Eq",
            "NotEq",
            "In",
            "NotIn",
            "Lt",
            "Lte",
            "Gt",
            "Gte",
            "Glob",
            "NotGlob",
            "IGlob",
            "NotIGlob",
            "Regex",
            "Contains",
            "NotContains",
            "ContainsAny",
            "NotContainsAny",
            "AnyLt",
            "AnyLte",
            "AnyGt",
            "AnyGte",
            "ContainsAllTokens",
        ]
    ]
    """Filter operator"""

    value: Required[Union[str, float, bool, SequenceNotStr[str], Iterable[float]]]
    """Filter value (type depends on field and operator)"""


class IncludeAttributesContributorsFiltersUnionMember1(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesContributorsFiltersUnionMember1Filter]]
    """Array of field filters"""

    op: Required[Literal["And", "Or"]]
    """Composite operator"""


class IncludeAttributesContributorsFiltersUnionMember2FilterUnionMember0(TypedDict, total=False):
    field: Required[str]
    """Field name to filter on"""

    op: Required[
        Literal[
            "Eq",
            "NotEq",
            "In",
            "NotIn",
            "Lt",
            "Lte",
            "Gt",
            "Gte",
            "Glob",
            "NotGlob",
            "IGlob",
            "NotIGlob",
            "Regex",
            "Contains",
            "NotContains",
            "ContainsAny",
            "NotContainsAny",
            "AnyLt",
            "AnyLte",
            "AnyGt",
            "AnyGte",
            "ContainsAllTokens",
        ]
    ]
    """Filter operator"""

    value: Required[Union[str, float, bool, SequenceNotStr[str], Iterable[float]]]
    """Filter value (type depends on field and operator)"""


class IncludeAttributesContributorsFiltersUnionMember2FilterUnionMember1Filter(TypedDict, total=False):
    field: Required[str]
    """Field name to filter on"""

    op: Required[
        Literal[
            "Eq",
            "NotEq",
            "In",
            "NotIn",
            "Lt",
            "Lte",
            "Gt",
            "Gte",
            "Glob",
            "NotGlob",
            "IGlob",
            "NotIGlob",
            "Regex",
            "Contains",
            "NotContains",
            "ContainsAny",
            "NotContainsAny",
            "AnyLt",
            "AnyLte",
            "AnyGt",
            "AnyGte",
            "ContainsAllTokens",
        ]
    ]
    """Filter operator"""

    value: Required[Union[str, float, bool, SequenceNotStr[str], Iterable[float]]]
    """Filter value (type depends on field and operator)"""


class IncludeAttributesContributorsFiltersUnionMember2FilterUnionMember1(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesContributorsFiltersUnionMember2FilterUnionMember1Filter]]
    """Array of field filters"""

    op: Required[Literal["And", "Or"]]
    """Composite operator"""


IncludeAttributesContributorsFiltersUnionMember2Filter: TypeAlias = Union[
    IncludeAttributesContributorsFiltersUnionMember2FilterUnionMember0,
    IncludeAttributesContributorsFiltersUnionMember2FilterUnionMember1,
]


class IncludeAttributesContributorsFiltersUnionMember2(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesContributorsFiltersUnionMember2Filter]]
    """Array of filters"""

    op: Required[Literal["And", "Or"]]
    """Composite operator"""


IncludeAttributesContributorsFilters: TypeAlias = Union[
    IncludeAttributesContributorsFiltersUnionMember0,
    IncludeAttributesContributorsFiltersUnionMember1,
    IncludeAttributesContributorsFiltersUnionMember2,
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
    field: Required[str]
    """Field name to filter on"""

    op: Required[
        Literal[
            "Eq",
            "NotEq",
            "In",
            "NotIn",
            "Lt",
            "Lte",
            "Gt",
            "Gte",
            "Glob",
            "NotGlob",
            "IGlob",
            "NotIGlob",
            "Regex",
            "Contains",
            "NotContains",
            "ContainsAny",
            "NotContainsAny",
            "AnyLt",
            "AnyLte",
            "AnyGt",
            "AnyGte",
            "ContainsAllTokens",
        ]
    ]
    """Filter operator"""

    value: Required[Union[str, float, bool, SequenceNotStr[str], Iterable[float]]]
    """Filter value (type depends on field and operator)"""


class IncludeAttributesStarrersFiltersUnionMember1Filter(TypedDict, total=False):
    field: Required[str]
    """Field name to filter on"""

    op: Required[
        Literal[
            "Eq",
            "NotEq",
            "In",
            "NotIn",
            "Lt",
            "Lte",
            "Gt",
            "Gte",
            "Glob",
            "NotGlob",
            "IGlob",
            "NotIGlob",
            "Regex",
            "Contains",
            "NotContains",
            "ContainsAny",
            "NotContainsAny",
            "AnyLt",
            "AnyLte",
            "AnyGt",
            "AnyGte",
            "ContainsAllTokens",
        ]
    ]
    """Filter operator"""

    value: Required[Union[str, float, bool, SequenceNotStr[str], Iterable[float]]]
    """Filter value (type depends on field and operator)"""


class IncludeAttributesStarrersFiltersUnionMember1(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesStarrersFiltersUnionMember1Filter]]
    """Array of field filters"""

    op: Required[Literal["And", "Or"]]
    """Composite operator"""


class IncludeAttributesStarrersFiltersUnionMember2FilterUnionMember0(TypedDict, total=False):
    field: Required[str]
    """Field name to filter on"""

    op: Required[
        Literal[
            "Eq",
            "NotEq",
            "In",
            "NotIn",
            "Lt",
            "Lte",
            "Gt",
            "Gte",
            "Glob",
            "NotGlob",
            "IGlob",
            "NotIGlob",
            "Regex",
            "Contains",
            "NotContains",
            "ContainsAny",
            "NotContainsAny",
            "AnyLt",
            "AnyLte",
            "AnyGt",
            "AnyGte",
            "ContainsAllTokens",
        ]
    ]
    """Filter operator"""

    value: Required[Union[str, float, bool, SequenceNotStr[str], Iterable[float]]]
    """Filter value (type depends on field and operator)"""


class IncludeAttributesStarrersFiltersUnionMember2FilterUnionMember1Filter(TypedDict, total=False):
    field: Required[str]
    """Field name to filter on"""

    op: Required[
        Literal[
            "Eq",
            "NotEq",
            "In",
            "NotIn",
            "Lt",
            "Lte",
            "Gt",
            "Gte",
            "Glob",
            "NotGlob",
            "IGlob",
            "NotIGlob",
            "Regex",
            "Contains",
            "NotContains",
            "ContainsAny",
            "NotContainsAny",
            "AnyLt",
            "AnyLte",
            "AnyGt",
            "AnyGte",
            "ContainsAllTokens",
        ]
    ]
    """Filter operator"""

    value: Required[Union[str, float, bool, SequenceNotStr[str], Iterable[float]]]
    """Filter value (type depends on field and operator)"""


class IncludeAttributesStarrersFiltersUnionMember2FilterUnionMember1(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesStarrersFiltersUnionMember2FilterUnionMember1Filter]]
    """Array of field filters"""

    op: Required[Literal["And", "Or"]]
    """Composite operator"""


IncludeAttributesStarrersFiltersUnionMember2Filter: TypeAlias = Union[
    IncludeAttributesStarrersFiltersUnionMember2FilterUnionMember0,
    IncludeAttributesStarrersFiltersUnionMember2FilterUnionMember1,
]


class IncludeAttributesStarrersFiltersUnionMember2(TypedDict, total=False):
    filters: Required[Iterable[IncludeAttributesStarrersFiltersUnionMember2Filter]]
    """Array of filters"""

    op: Required[Literal["And", "Or"]]
    """Composite operator"""


IncludeAttributesStarrersFilters: TypeAlias = Union[
    IncludeAttributesStarrersFiltersUnionMember0,
    IncludeAttributesStarrersFiltersUnionMember1,
    IncludeAttributesStarrersFiltersUnionMember2,
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
    """Optional graph relationships and enrichment attributes"""

    contributors: IncludeAttributesContributors
    """Include repository contributors with cursor pagination"""

    owner: bool
    """Include repository owner information"""

    owner_devrank: Annotated[bool, PropertyInfo(alias="ownerDevrank")]
    """Include devrank data for the repository owner"""

    owner_professional: Annotated[bool, PropertyInfo(alias="ownerProfessional")]
    """
    Include LinkedIn professional profile for the repository owner (requires
    PROFESSIONAL service)
    """

    starrers: IncludeAttributesStarrers
    """Include users who starred the repository with cursor pagination"""


class RankByUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember3ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember3ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember3ExprUnionMember3ExprUnionMember0,
    RankByUnionMember3ExprUnionMember3ExprUnionMember3ExprUnionMember1,
    RankByUnionMember3ExprUnionMember3ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember3ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember3ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember3ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember3ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember3ExprUnionMember6ExprUnionMember0,
    RankByUnionMember3ExprUnionMember3ExprUnionMember6ExprUnionMember1,
    RankByUnionMember3ExprUnionMember3ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember3ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember3ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember3ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember3ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember3ExprUnionMember7ExprUnionMember0,
    RankByUnionMember3ExprUnionMember3ExprUnionMember7ExprUnionMember1,
    RankByUnionMember3ExprUnionMember3ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember3ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember3ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember3ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember3ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember3ExprUnionMember8ExprUnionMember0,
    RankByUnionMember3ExprUnionMember3ExprUnionMember8ExprUnionMember1,
    RankByUnionMember3ExprUnionMember3ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember3ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember3ExprUnionMember3ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember3ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember3ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember3ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember3ExprUnionMember9ExprUnionMember0,
    RankByUnionMember3ExprUnionMember3ExprUnionMember9ExprUnionMember1,
    RankByUnionMember3ExprUnionMember3ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember3ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember3ExprUnionMember3ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember3ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember3ExprUnionMember0,
    RankByUnionMember3ExprUnionMember3ExprUnionMember1,
    RankByUnionMember3ExprUnionMember3ExprUnionMember2,
    RankByUnionMember3ExprUnionMember3ExprUnionMember3,
    RankByUnionMember3ExprUnionMember3ExprUnionMember4,
    RankByUnionMember3ExprUnionMember3ExprUnionMember5,
    RankByUnionMember3ExprUnionMember3ExprUnionMember6,
    RankByUnionMember3ExprUnionMember3ExprUnionMember7,
    RankByUnionMember3ExprUnionMember3ExprUnionMember8,
    RankByUnionMember3ExprUnionMember3ExprUnionMember9,
]


class RankByUnionMember3ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember3ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember3ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember6ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember6ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember6ExprUnionMember3ExprUnionMember0,
    RankByUnionMember3ExprUnionMember6ExprUnionMember3ExprUnionMember1,
    RankByUnionMember3ExprUnionMember6ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember6ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember6ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember6ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember6ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember6ExprUnionMember6ExprUnionMember0,
    RankByUnionMember3ExprUnionMember6ExprUnionMember6ExprUnionMember1,
    RankByUnionMember3ExprUnionMember6ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember6ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember6ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember6ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember6ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember6ExprUnionMember7ExprUnionMember0,
    RankByUnionMember3ExprUnionMember6ExprUnionMember7ExprUnionMember1,
    RankByUnionMember3ExprUnionMember6ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember6ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember6ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember6ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember6ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember6ExprUnionMember8ExprUnionMember0,
    RankByUnionMember3ExprUnionMember6ExprUnionMember8ExprUnionMember1,
    RankByUnionMember3ExprUnionMember6ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember6ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember3ExprUnionMember6ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember6ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember6ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember6ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember6ExprUnionMember9ExprUnionMember0,
    RankByUnionMember3ExprUnionMember6ExprUnionMember9ExprUnionMember1,
    RankByUnionMember3ExprUnionMember6ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember6ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember3ExprUnionMember6ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember3ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember6ExprUnionMember0,
    RankByUnionMember3ExprUnionMember6ExprUnionMember1,
    RankByUnionMember3ExprUnionMember6ExprUnionMember2,
    RankByUnionMember3ExprUnionMember6ExprUnionMember3,
    RankByUnionMember3ExprUnionMember6ExprUnionMember4,
    RankByUnionMember3ExprUnionMember6ExprUnionMember5,
    RankByUnionMember3ExprUnionMember6ExprUnionMember6,
    RankByUnionMember3ExprUnionMember6ExprUnionMember7,
    RankByUnionMember3ExprUnionMember6ExprUnionMember8,
    RankByUnionMember3ExprUnionMember6ExprUnionMember9,
]


class RankByUnionMember3ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember7ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember7ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember7ExprUnionMember3ExprUnionMember0,
    RankByUnionMember3ExprUnionMember7ExprUnionMember3ExprUnionMember1,
    RankByUnionMember3ExprUnionMember7ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember7ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember7ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember7ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember7ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember7ExprUnionMember6ExprUnionMember0,
    RankByUnionMember3ExprUnionMember7ExprUnionMember6ExprUnionMember1,
    RankByUnionMember3ExprUnionMember7ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember7ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember7ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember7ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember7ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember7ExprUnionMember7ExprUnionMember0,
    RankByUnionMember3ExprUnionMember7ExprUnionMember7ExprUnionMember1,
    RankByUnionMember3ExprUnionMember7ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember7ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember7ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember7ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember7ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember7ExprUnionMember8ExprUnionMember0,
    RankByUnionMember3ExprUnionMember7ExprUnionMember8ExprUnionMember1,
    RankByUnionMember3ExprUnionMember7ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember7ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember3ExprUnionMember7ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember7ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember7ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember7ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember7ExprUnionMember9ExprUnionMember0,
    RankByUnionMember3ExprUnionMember7ExprUnionMember9ExprUnionMember1,
    RankByUnionMember3ExprUnionMember7ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember7ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember3ExprUnionMember7ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember3ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember7ExprUnionMember0,
    RankByUnionMember3ExprUnionMember7ExprUnionMember1,
    RankByUnionMember3ExprUnionMember7ExprUnionMember2,
    RankByUnionMember3ExprUnionMember7ExprUnionMember3,
    RankByUnionMember3ExprUnionMember7ExprUnionMember4,
    RankByUnionMember3ExprUnionMember7ExprUnionMember5,
    RankByUnionMember3ExprUnionMember7ExprUnionMember6,
    RankByUnionMember3ExprUnionMember7ExprUnionMember7,
    RankByUnionMember3ExprUnionMember7ExprUnionMember8,
    RankByUnionMember3ExprUnionMember7ExprUnionMember9,
]


class RankByUnionMember3ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember3ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember3ExprUnionMember8ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember8ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember8ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember8ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember8ExprUnionMember3ExprUnionMember0,
    RankByUnionMember3ExprUnionMember8ExprUnionMember3ExprUnionMember1,
    RankByUnionMember3ExprUnionMember8ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember8ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember8ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember3ExprUnionMember8ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember3ExprUnionMember8ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember3ExprUnionMember8ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember8ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember8ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember8ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember8ExprUnionMember6ExprUnionMember0,
    RankByUnionMember3ExprUnionMember8ExprUnionMember6ExprUnionMember1,
    RankByUnionMember3ExprUnionMember8ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember8ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember8ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember3ExprUnionMember8ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember8ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember8ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember8ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember8ExprUnionMember7ExprUnionMember0,
    RankByUnionMember3ExprUnionMember8ExprUnionMember7ExprUnionMember1,
    RankByUnionMember3ExprUnionMember8ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember8ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember8ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember3ExprUnionMember8ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember8ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember8ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember8ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember8ExprUnionMember8ExprUnionMember0,
    RankByUnionMember3ExprUnionMember8ExprUnionMember8ExprUnionMember1,
    RankByUnionMember3ExprUnionMember8ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember8ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember3ExprUnionMember8ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember3ExprUnionMember8ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember8ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember8ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember8ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember8ExprUnionMember9ExprUnionMember0,
    RankByUnionMember3ExprUnionMember8ExprUnionMember9ExprUnionMember1,
    RankByUnionMember3ExprUnionMember8ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember8ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember3ExprUnionMember8ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember3ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember8ExprUnionMember0,
    RankByUnionMember3ExprUnionMember8ExprUnionMember1,
    RankByUnionMember3ExprUnionMember8ExprUnionMember2,
    RankByUnionMember3ExprUnionMember8ExprUnionMember3,
    RankByUnionMember3ExprUnionMember8ExprUnionMember4,
    RankByUnionMember3ExprUnionMember8ExprUnionMember5,
    RankByUnionMember3ExprUnionMember8ExprUnionMember6,
    RankByUnionMember3ExprUnionMember8ExprUnionMember7,
    RankByUnionMember3ExprUnionMember8ExprUnionMember8,
    RankByUnionMember3ExprUnionMember8ExprUnionMember9,
]


class RankByUnionMember3ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember3ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember3ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember3ExprUnionMember9ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember9ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember9ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember9ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember9ExprUnionMember3ExprUnionMember0,
    RankByUnionMember3ExprUnionMember9ExprUnionMember3ExprUnionMember1,
    RankByUnionMember3ExprUnionMember9ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember9ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember9ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember3ExprUnionMember9ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember3ExprUnionMember9ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember3ExprUnionMember9ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember9ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember9ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember9ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember9ExprUnionMember6ExprUnionMember0,
    RankByUnionMember3ExprUnionMember9ExprUnionMember6ExprUnionMember1,
    RankByUnionMember3ExprUnionMember9ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember9ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember9ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember3ExprUnionMember9ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember9ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember9ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember9ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember9ExprUnionMember7ExprUnionMember0,
    RankByUnionMember3ExprUnionMember9ExprUnionMember7ExprUnionMember1,
    RankByUnionMember3ExprUnionMember9ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember9ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3ExprUnionMember9ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember3ExprUnionMember9ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember9ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember9ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember9ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember9ExprUnionMember8ExprUnionMember0,
    RankByUnionMember3ExprUnionMember9ExprUnionMember8ExprUnionMember1,
    RankByUnionMember3ExprUnionMember9ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember9ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember3ExprUnionMember9ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember3ExprUnionMember9ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember3ExprUnionMember9ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember3ExprUnionMember9ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember3ExprUnionMember9ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember9ExprUnionMember9ExprUnionMember0,
    RankByUnionMember3ExprUnionMember9ExprUnionMember9ExprUnionMember1,
    RankByUnionMember3ExprUnionMember9ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember3ExprUnionMember9ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember3ExprUnionMember9ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember3ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember9ExprUnionMember0,
    RankByUnionMember3ExprUnionMember9ExprUnionMember1,
    RankByUnionMember3ExprUnionMember9ExprUnionMember2,
    RankByUnionMember3ExprUnionMember9ExprUnionMember3,
    RankByUnionMember3ExprUnionMember9ExprUnionMember4,
    RankByUnionMember3ExprUnionMember9ExprUnionMember5,
    RankByUnionMember3ExprUnionMember9ExprUnionMember6,
    RankByUnionMember3ExprUnionMember9ExprUnionMember7,
    RankByUnionMember3ExprUnionMember9ExprUnionMember8,
    RankByUnionMember3ExprUnionMember9ExprUnionMember9,
]


class RankByUnionMember3ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember3ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember3ExprUnionMember0,
    RankByUnionMember3ExprUnionMember1,
    RankByUnionMember3ExprUnionMember2,
    RankByUnionMember3ExprUnionMember3,
    RankByUnionMember3ExprUnionMember4,
    RankByUnionMember3ExprUnionMember5,
    RankByUnionMember3ExprUnionMember6,
    RankByUnionMember3ExprUnionMember7,
    RankByUnionMember3ExprUnionMember8,
    RankByUnionMember3ExprUnionMember9,
]


class RankByUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember3ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember3ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember3ExprUnionMember3ExprUnionMember0,
    RankByUnionMember6ExprUnionMember3ExprUnionMember3ExprUnionMember1,
    RankByUnionMember6ExprUnionMember3ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember3ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember3ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember3ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember3ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember3ExprUnionMember6ExprUnionMember0,
    RankByUnionMember6ExprUnionMember3ExprUnionMember6ExprUnionMember1,
    RankByUnionMember6ExprUnionMember3ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember3ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember3ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember3ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember3ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember3ExprUnionMember7ExprUnionMember0,
    RankByUnionMember6ExprUnionMember3ExprUnionMember7ExprUnionMember1,
    RankByUnionMember6ExprUnionMember3ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember3ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember3ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember3ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember3ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember3ExprUnionMember8ExprUnionMember0,
    RankByUnionMember6ExprUnionMember3ExprUnionMember8ExprUnionMember1,
    RankByUnionMember6ExprUnionMember3ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember3ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember6ExprUnionMember3ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember3ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember3ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember3ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember3ExprUnionMember9ExprUnionMember0,
    RankByUnionMember6ExprUnionMember3ExprUnionMember9ExprUnionMember1,
    RankByUnionMember6ExprUnionMember3ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember3ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember6ExprUnionMember3ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember6ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember3ExprUnionMember0,
    RankByUnionMember6ExprUnionMember3ExprUnionMember1,
    RankByUnionMember6ExprUnionMember3ExprUnionMember2,
    RankByUnionMember6ExprUnionMember3ExprUnionMember3,
    RankByUnionMember6ExprUnionMember3ExprUnionMember4,
    RankByUnionMember6ExprUnionMember3ExprUnionMember5,
    RankByUnionMember6ExprUnionMember3ExprUnionMember6,
    RankByUnionMember6ExprUnionMember3ExprUnionMember7,
    RankByUnionMember6ExprUnionMember3ExprUnionMember8,
    RankByUnionMember6ExprUnionMember3ExprUnionMember9,
]


class RankByUnionMember6ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember6ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember6ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember6ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember6ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember6ExprUnionMember3ExprUnionMember0,
    RankByUnionMember6ExprUnionMember6ExprUnionMember3ExprUnionMember1,
    RankByUnionMember6ExprUnionMember6ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember6ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember6ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember6ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember6ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember6ExprUnionMember6ExprUnionMember0,
    RankByUnionMember6ExprUnionMember6ExprUnionMember6ExprUnionMember1,
    RankByUnionMember6ExprUnionMember6ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember6ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember6ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember6ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember6ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember6ExprUnionMember7ExprUnionMember0,
    RankByUnionMember6ExprUnionMember6ExprUnionMember7ExprUnionMember1,
    RankByUnionMember6ExprUnionMember6ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember6ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember6ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember6ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember6ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember6ExprUnionMember8ExprUnionMember0,
    RankByUnionMember6ExprUnionMember6ExprUnionMember8ExprUnionMember1,
    RankByUnionMember6ExprUnionMember6ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember6ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember6ExprUnionMember6ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember6ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember6ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember6ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember6ExprUnionMember9ExprUnionMember0,
    RankByUnionMember6ExprUnionMember6ExprUnionMember9ExprUnionMember1,
    RankByUnionMember6ExprUnionMember6ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember6ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember6ExprUnionMember6ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember6ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember6ExprUnionMember0,
    RankByUnionMember6ExprUnionMember6ExprUnionMember1,
    RankByUnionMember6ExprUnionMember6ExprUnionMember2,
    RankByUnionMember6ExprUnionMember6ExprUnionMember3,
    RankByUnionMember6ExprUnionMember6ExprUnionMember4,
    RankByUnionMember6ExprUnionMember6ExprUnionMember5,
    RankByUnionMember6ExprUnionMember6ExprUnionMember6,
    RankByUnionMember6ExprUnionMember6ExprUnionMember7,
    RankByUnionMember6ExprUnionMember6ExprUnionMember8,
    RankByUnionMember6ExprUnionMember6ExprUnionMember9,
]


class RankByUnionMember6ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember7ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember7ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember7ExprUnionMember3ExprUnionMember0,
    RankByUnionMember6ExprUnionMember7ExprUnionMember3ExprUnionMember1,
    RankByUnionMember6ExprUnionMember7ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember7ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember7ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember7ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember7ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember7ExprUnionMember6ExprUnionMember0,
    RankByUnionMember6ExprUnionMember7ExprUnionMember6ExprUnionMember1,
    RankByUnionMember6ExprUnionMember7ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember7ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember7ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember7ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember7ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember7ExprUnionMember7ExprUnionMember0,
    RankByUnionMember6ExprUnionMember7ExprUnionMember7ExprUnionMember1,
    RankByUnionMember6ExprUnionMember7ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember7ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember7ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember7ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember7ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember7ExprUnionMember8ExprUnionMember0,
    RankByUnionMember6ExprUnionMember7ExprUnionMember8ExprUnionMember1,
    RankByUnionMember6ExprUnionMember7ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember7ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember6ExprUnionMember7ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember7ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember7ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember7ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember7ExprUnionMember9ExprUnionMember0,
    RankByUnionMember6ExprUnionMember7ExprUnionMember9ExprUnionMember1,
    RankByUnionMember6ExprUnionMember7ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember7ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember6ExprUnionMember7ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember6ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember7ExprUnionMember0,
    RankByUnionMember6ExprUnionMember7ExprUnionMember1,
    RankByUnionMember6ExprUnionMember7ExprUnionMember2,
    RankByUnionMember6ExprUnionMember7ExprUnionMember3,
    RankByUnionMember6ExprUnionMember7ExprUnionMember4,
    RankByUnionMember6ExprUnionMember7ExprUnionMember5,
    RankByUnionMember6ExprUnionMember7ExprUnionMember6,
    RankByUnionMember6ExprUnionMember7ExprUnionMember7,
    RankByUnionMember6ExprUnionMember7ExprUnionMember8,
    RankByUnionMember6ExprUnionMember7ExprUnionMember9,
]


class RankByUnionMember6ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember6ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember6ExprUnionMember8ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember8ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember8ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember8ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember8ExprUnionMember3ExprUnionMember0,
    RankByUnionMember6ExprUnionMember8ExprUnionMember3ExprUnionMember1,
    RankByUnionMember6ExprUnionMember8ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember8ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember8ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember6ExprUnionMember8ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember6ExprUnionMember8ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember6ExprUnionMember8ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember8ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember8ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember8ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember8ExprUnionMember6ExprUnionMember0,
    RankByUnionMember6ExprUnionMember8ExprUnionMember6ExprUnionMember1,
    RankByUnionMember6ExprUnionMember8ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember8ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember8ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember6ExprUnionMember8ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember8ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember8ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember8ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember8ExprUnionMember7ExprUnionMember0,
    RankByUnionMember6ExprUnionMember8ExprUnionMember7ExprUnionMember1,
    RankByUnionMember6ExprUnionMember8ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember8ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember8ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember6ExprUnionMember8ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember8ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember8ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember8ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember8ExprUnionMember8ExprUnionMember0,
    RankByUnionMember6ExprUnionMember8ExprUnionMember8ExprUnionMember1,
    RankByUnionMember6ExprUnionMember8ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember8ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember6ExprUnionMember8ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember6ExprUnionMember8ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember8ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember8ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember8ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember8ExprUnionMember9ExprUnionMember0,
    RankByUnionMember6ExprUnionMember8ExprUnionMember9ExprUnionMember1,
    RankByUnionMember6ExprUnionMember8ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember8ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember6ExprUnionMember8ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember6ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember8ExprUnionMember0,
    RankByUnionMember6ExprUnionMember8ExprUnionMember1,
    RankByUnionMember6ExprUnionMember8ExprUnionMember2,
    RankByUnionMember6ExprUnionMember8ExprUnionMember3,
    RankByUnionMember6ExprUnionMember8ExprUnionMember4,
    RankByUnionMember6ExprUnionMember8ExprUnionMember5,
    RankByUnionMember6ExprUnionMember8ExprUnionMember6,
    RankByUnionMember6ExprUnionMember8ExprUnionMember7,
    RankByUnionMember6ExprUnionMember8ExprUnionMember8,
    RankByUnionMember6ExprUnionMember8ExprUnionMember9,
]


class RankByUnionMember6ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember6ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember6ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember6ExprUnionMember9ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember9ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember9ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember9ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember9ExprUnionMember3ExprUnionMember0,
    RankByUnionMember6ExprUnionMember9ExprUnionMember3ExprUnionMember1,
    RankByUnionMember6ExprUnionMember9ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember9ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember9ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember6ExprUnionMember9ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember6ExprUnionMember9ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember6ExprUnionMember9ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember9ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember9ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember9ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember9ExprUnionMember6ExprUnionMember0,
    RankByUnionMember6ExprUnionMember9ExprUnionMember6ExprUnionMember1,
    RankByUnionMember6ExprUnionMember9ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember9ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember9ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember6ExprUnionMember9ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember9ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember9ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember9ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember9ExprUnionMember7ExprUnionMember0,
    RankByUnionMember6ExprUnionMember9ExprUnionMember7ExprUnionMember1,
    RankByUnionMember6ExprUnionMember9ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember9ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6ExprUnionMember9ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember6ExprUnionMember9ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember9ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember9ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember9ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember9ExprUnionMember8ExprUnionMember0,
    RankByUnionMember6ExprUnionMember9ExprUnionMember8ExprUnionMember1,
    RankByUnionMember6ExprUnionMember9ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember9ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember6ExprUnionMember9ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember6ExprUnionMember9ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember6ExprUnionMember9ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember6ExprUnionMember9ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember6ExprUnionMember9ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember9ExprUnionMember9ExprUnionMember0,
    RankByUnionMember6ExprUnionMember9ExprUnionMember9ExprUnionMember1,
    RankByUnionMember6ExprUnionMember9ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember6ExprUnionMember9ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember6ExprUnionMember9ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember6ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember9ExprUnionMember0,
    RankByUnionMember6ExprUnionMember9ExprUnionMember1,
    RankByUnionMember6ExprUnionMember9ExprUnionMember2,
    RankByUnionMember6ExprUnionMember9ExprUnionMember3,
    RankByUnionMember6ExprUnionMember9ExprUnionMember4,
    RankByUnionMember6ExprUnionMember9ExprUnionMember5,
    RankByUnionMember6ExprUnionMember9ExprUnionMember6,
    RankByUnionMember6ExprUnionMember9ExprUnionMember7,
    RankByUnionMember6ExprUnionMember9ExprUnionMember8,
    RankByUnionMember6ExprUnionMember9ExprUnionMember9,
]


class RankByUnionMember6ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember6ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember6ExprUnionMember0,
    RankByUnionMember6ExprUnionMember1,
    RankByUnionMember6ExprUnionMember2,
    RankByUnionMember6ExprUnionMember3,
    RankByUnionMember6ExprUnionMember4,
    RankByUnionMember6ExprUnionMember5,
    RankByUnionMember6ExprUnionMember6,
    RankByUnionMember6ExprUnionMember7,
    RankByUnionMember6ExprUnionMember8,
    RankByUnionMember6ExprUnionMember9,
]


class RankByUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember3ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember3ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember3ExprUnionMember3ExprUnionMember0,
    RankByUnionMember7ExprUnionMember3ExprUnionMember3ExprUnionMember1,
    RankByUnionMember7ExprUnionMember3ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember3ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember3ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember3ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember3ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember3ExprUnionMember6ExprUnionMember0,
    RankByUnionMember7ExprUnionMember3ExprUnionMember6ExprUnionMember1,
    RankByUnionMember7ExprUnionMember3ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember3ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember3ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember3ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember3ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember3ExprUnionMember7ExprUnionMember0,
    RankByUnionMember7ExprUnionMember3ExprUnionMember7ExprUnionMember1,
    RankByUnionMember7ExprUnionMember3ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember3ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember3ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember3ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember3ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember3ExprUnionMember8ExprUnionMember0,
    RankByUnionMember7ExprUnionMember3ExprUnionMember8ExprUnionMember1,
    RankByUnionMember7ExprUnionMember3ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember3ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember7ExprUnionMember3ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember3ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember3ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember3ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember3ExprUnionMember9ExprUnionMember0,
    RankByUnionMember7ExprUnionMember3ExprUnionMember9ExprUnionMember1,
    RankByUnionMember7ExprUnionMember3ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember3ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember7ExprUnionMember3ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember7ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember3ExprUnionMember0,
    RankByUnionMember7ExprUnionMember3ExprUnionMember1,
    RankByUnionMember7ExprUnionMember3ExprUnionMember2,
    RankByUnionMember7ExprUnionMember3ExprUnionMember3,
    RankByUnionMember7ExprUnionMember3ExprUnionMember4,
    RankByUnionMember7ExprUnionMember3ExprUnionMember5,
    RankByUnionMember7ExprUnionMember3ExprUnionMember6,
    RankByUnionMember7ExprUnionMember3ExprUnionMember7,
    RankByUnionMember7ExprUnionMember3ExprUnionMember8,
    RankByUnionMember7ExprUnionMember3ExprUnionMember9,
]


class RankByUnionMember7ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember7ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember7ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember6ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember6ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember6ExprUnionMember3ExprUnionMember0,
    RankByUnionMember7ExprUnionMember6ExprUnionMember3ExprUnionMember1,
    RankByUnionMember7ExprUnionMember6ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember6ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember6ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember6ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember6ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember6ExprUnionMember6ExprUnionMember0,
    RankByUnionMember7ExprUnionMember6ExprUnionMember6ExprUnionMember1,
    RankByUnionMember7ExprUnionMember6ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember6ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember6ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember6ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember6ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember6ExprUnionMember7ExprUnionMember0,
    RankByUnionMember7ExprUnionMember6ExprUnionMember7ExprUnionMember1,
    RankByUnionMember7ExprUnionMember6ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember6ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember6ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember6ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember6ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember6ExprUnionMember8ExprUnionMember0,
    RankByUnionMember7ExprUnionMember6ExprUnionMember8ExprUnionMember1,
    RankByUnionMember7ExprUnionMember6ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember6ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember7ExprUnionMember6ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember6ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember6ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember6ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember6ExprUnionMember9ExprUnionMember0,
    RankByUnionMember7ExprUnionMember6ExprUnionMember9ExprUnionMember1,
    RankByUnionMember7ExprUnionMember6ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember6ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember7ExprUnionMember6ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember7ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember6ExprUnionMember0,
    RankByUnionMember7ExprUnionMember6ExprUnionMember1,
    RankByUnionMember7ExprUnionMember6ExprUnionMember2,
    RankByUnionMember7ExprUnionMember6ExprUnionMember3,
    RankByUnionMember7ExprUnionMember6ExprUnionMember4,
    RankByUnionMember7ExprUnionMember6ExprUnionMember5,
    RankByUnionMember7ExprUnionMember6ExprUnionMember6,
    RankByUnionMember7ExprUnionMember6ExprUnionMember7,
    RankByUnionMember7ExprUnionMember6ExprUnionMember8,
    RankByUnionMember7ExprUnionMember6ExprUnionMember9,
]


class RankByUnionMember7ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember7ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember7ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember7ExprUnionMember3ExprUnionMember0,
    RankByUnionMember7ExprUnionMember7ExprUnionMember3ExprUnionMember1,
    RankByUnionMember7ExprUnionMember7ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember7ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember7ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember7ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember7ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember7ExprUnionMember6ExprUnionMember0,
    RankByUnionMember7ExprUnionMember7ExprUnionMember6ExprUnionMember1,
    RankByUnionMember7ExprUnionMember7ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember7ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember7ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember7ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember7ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember7ExprUnionMember7ExprUnionMember0,
    RankByUnionMember7ExprUnionMember7ExprUnionMember7ExprUnionMember1,
    RankByUnionMember7ExprUnionMember7ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember7ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember7ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember7ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember7ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember7ExprUnionMember8ExprUnionMember0,
    RankByUnionMember7ExprUnionMember7ExprUnionMember8ExprUnionMember1,
    RankByUnionMember7ExprUnionMember7ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember7ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember7ExprUnionMember7ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember7ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember7ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember7ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember7ExprUnionMember9ExprUnionMember0,
    RankByUnionMember7ExprUnionMember7ExprUnionMember9ExprUnionMember1,
    RankByUnionMember7ExprUnionMember7ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember7ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember7ExprUnionMember7ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember7ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember7ExprUnionMember0,
    RankByUnionMember7ExprUnionMember7ExprUnionMember1,
    RankByUnionMember7ExprUnionMember7ExprUnionMember2,
    RankByUnionMember7ExprUnionMember7ExprUnionMember3,
    RankByUnionMember7ExprUnionMember7ExprUnionMember4,
    RankByUnionMember7ExprUnionMember7ExprUnionMember5,
    RankByUnionMember7ExprUnionMember7ExprUnionMember6,
    RankByUnionMember7ExprUnionMember7ExprUnionMember7,
    RankByUnionMember7ExprUnionMember7ExprUnionMember8,
    RankByUnionMember7ExprUnionMember7ExprUnionMember9,
]


class RankByUnionMember7ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember7ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember7ExprUnionMember8ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember8ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember8ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember8ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember8ExprUnionMember3ExprUnionMember0,
    RankByUnionMember7ExprUnionMember8ExprUnionMember3ExprUnionMember1,
    RankByUnionMember7ExprUnionMember8ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember8ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember8ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember7ExprUnionMember8ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember7ExprUnionMember8ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember7ExprUnionMember8ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember8ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember8ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember8ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember8ExprUnionMember6ExprUnionMember0,
    RankByUnionMember7ExprUnionMember8ExprUnionMember6ExprUnionMember1,
    RankByUnionMember7ExprUnionMember8ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember8ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember8ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember7ExprUnionMember8ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember8ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember8ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember8ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember8ExprUnionMember7ExprUnionMember0,
    RankByUnionMember7ExprUnionMember8ExprUnionMember7ExprUnionMember1,
    RankByUnionMember7ExprUnionMember8ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember8ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember8ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember7ExprUnionMember8ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember8ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember8ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember8ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember8ExprUnionMember8ExprUnionMember0,
    RankByUnionMember7ExprUnionMember8ExprUnionMember8ExprUnionMember1,
    RankByUnionMember7ExprUnionMember8ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember8ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember7ExprUnionMember8ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember7ExprUnionMember8ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember8ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember8ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember8ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember8ExprUnionMember9ExprUnionMember0,
    RankByUnionMember7ExprUnionMember8ExprUnionMember9ExprUnionMember1,
    RankByUnionMember7ExprUnionMember8ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember8ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember7ExprUnionMember8ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember7ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember8ExprUnionMember0,
    RankByUnionMember7ExprUnionMember8ExprUnionMember1,
    RankByUnionMember7ExprUnionMember8ExprUnionMember2,
    RankByUnionMember7ExprUnionMember8ExprUnionMember3,
    RankByUnionMember7ExprUnionMember8ExprUnionMember4,
    RankByUnionMember7ExprUnionMember8ExprUnionMember5,
    RankByUnionMember7ExprUnionMember8ExprUnionMember6,
    RankByUnionMember7ExprUnionMember8ExprUnionMember7,
    RankByUnionMember7ExprUnionMember8ExprUnionMember8,
    RankByUnionMember7ExprUnionMember8ExprUnionMember9,
]


class RankByUnionMember7ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember7ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember7ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember7ExprUnionMember9ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember9ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember9ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember9ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember9ExprUnionMember3ExprUnionMember0,
    RankByUnionMember7ExprUnionMember9ExprUnionMember3ExprUnionMember1,
    RankByUnionMember7ExprUnionMember9ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember9ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember9ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember7ExprUnionMember9ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember7ExprUnionMember9ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember7ExprUnionMember9ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember9ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember9ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember9ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember9ExprUnionMember6ExprUnionMember0,
    RankByUnionMember7ExprUnionMember9ExprUnionMember6ExprUnionMember1,
    RankByUnionMember7ExprUnionMember9ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember9ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember9ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember7ExprUnionMember9ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember9ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember9ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember9ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember9ExprUnionMember7ExprUnionMember0,
    RankByUnionMember7ExprUnionMember9ExprUnionMember7ExprUnionMember1,
    RankByUnionMember7ExprUnionMember9ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember9ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7ExprUnionMember9ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember7ExprUnionMember9ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember9ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember9ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember9ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember9ExprUnionMember8ExprUnionMember0,
    RankByUnionMember7ExprUnionMember9ExprUnionMember8ExprUnionMember1,
    RankByUnionMember7ExprUnionMember9ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember9ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember7ExprUnionMember9ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember7ExprUnionMember9ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember7ExprUnionMember9ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember7ExprUnionMember9ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember7ExprUnionMember9ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember9ExprUnionMember9ExprUnionMember0,
    RankByUnionMember7ExprUnionMember9ExprUnionMember9ExprUnionMember1,
    RankByUnionMember7ExprUnionMember9ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember7ExprUnionMember9ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember7ExprUnionMember9ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember7ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember9ExprUnionMember0,
    RankByUnionMember7ExprUnionMember9ExprUnionMember1,
    RankByUnionMember7ExprUnionMember9ExprUnionMember2,
    RankByUnionMember7ExprUnionMember9ExprUnionMember3,
    RankByUnionMember7ExprUnionMember9ExprUnionMember4,
    RankByUnionMember7ExprUnionMember9ExprUnionMember5,
    RankByUnionMember7ExprUnionMember9ExprUnionMember6,
    RankByUnionMember7ExprUnionMember9ExprUnionMember7,
    RankByUnionMember7ExprUnionMember9ExprUnionMember8,
    RankByUnionMember7ExprUnionMember9ExprUnionMember9,
]


class RankByUnionMember7ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember7ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember7ExprUnionMember0,
    RankByUnionMember7ExprUnionMember1,
    RankByUnionMember7ExprUnionMember2,
    RankByUnionMember7ExprUnionMember3,
    RankByUnionMember7ExprUnionMember4,
    RankByUnionMember7ExprUnionMember5,
    RankByUnionMember7ExprUnionMember6,
    RankByUnionMember7ExprUnionMember7,
    RankByUnionMember7ExprUnionMember8,
    RankByUnionMember7ExprUnionMember9,
]


class RankByUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember8ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember8ExprUnionMember3ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember3ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember3ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember3ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember3ExprUnionMember3ExprUnionMember0,
    RankByUnionMember8ExprUnionMember3ExprUnionMember3ExprUnionMember1,
    RankByUnionMember8ExprUnionMember3ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember3ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember8ExprUnionMember3ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember8ExprUnionMember3ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember8ExprUnionMember3ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember8ExprUnionMember3ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember3ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember3ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember3ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember3ExprUnionMember6ExprUnionMember0,
    RankByUnionMember8ExprUnionMember3ExprUnionMember6ExprUnionMember1,
    RankByUnionMember8ExprUnionMember3ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember3ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember8ExprUnionMember3ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember8ExprUnionMember3ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember3ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember3ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember3ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember3ExprUnionMember7ExprUnionMember0,
    RankByUnionMember8ExprUnionMember3ExprUnionMember7ExprUnionMember1,
    RankByUnionMember8ExprUnionMember3ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember3ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember8ExprUnionMember3ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember8ExprUnionMember3ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember3ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember3ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember3ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember3ExprUnionMember8ExprUnionMember0,
    RankByUnionMember8ExprUnionMember3ExprUnionMember8ExprUnionMember1,
    RankByUnionMember8ExprUnionMember3ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember3ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember8ExprUnionMember3ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember8ExprUnionMember3ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember3ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember3ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember3ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember3ExprUnionMember9ExprUnionMember0,
    RankByUnionMember8ExprUnionMember3ExprUnionMember9ExprUnionMember1,
    RankByUnionMember8ExprUnionMember3ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember3ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember8ExprUnionMember3ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember8ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember3ExprUnionMember0,
    RankByUnionMember8ExprUnionMember3ExprUnionMember1,
    RankByUnionMember8ExprUnionMember3ExprUnionMember2,
    RankByUnionMember8ExprUnionMember3ExprUnionMember3,
    RankByUnionMember8ExprUnionMember3ExprUnionMember4,
    RankByUnionMember8ExprUnionMember3ExprUnionMember5,
    RankByUnionMember8ExprUnionMember3ExprUnionMember6,
    RankByUnionMember8ExprUnionMember3ExprUnionMember7,
    RankByUnionMember8ExprUnionMember3ExprUnionMember8,
    RankByUnionMember8ExprUnionMember3ExprUnionMember9,
]


class RankByUnionMember8ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember8ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember8ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember8ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember8ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember8ExprUnionMember6ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember6ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember6ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember6ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember6ExprUnionMember3ExprUnionMember0,
    RankByUnionMember8ExprUnionMember6ExprUnionMember3ExprUnionMember1,
    RankByUnionMember8ExprUnionMember6ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember6ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember8ExprUnionMember6ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember8ExprUnionMember6ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember8ExprUnionMember6ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember8ExprUnionMember6ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember6ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember6ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember6ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember6ExprUnionMember6ExprUnionMember0,
    RankByUnionMember8ExprUnionMember6ExprUnionMember6ExprUnionMember1,
    RankByUnionMember8ExprUnionMember6ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember6ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember8ExprUnionMember6ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember8ExprUnionMember6ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember6ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember6ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember6ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember6ExprUnionMember7ExprUnionMember0,
    RankByUnionMember8ExprUnionMember6ExprUnionMember7ExprUnionMember1,
    RankByUnionMember8ExprUnionMember6ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember6ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember8ExprUnionMember6ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember8ExprUnionMember6ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember6ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember6ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember6ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember6ExprUnionMember8ExprUnionMember0,
    RankByUnionMember8ExprUnionMember6ExprUnionMember8ExprUnionMember1,
    RankByUnionMember8ExprUnionMember6ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember6ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember8ExprUnionMember6ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember8ExprUnionMember6ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember6ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember6ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember6ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember6ExprUnionMember9ExprUnionMember0,
    RankByUnionMember8ExprUnionMember6ExprUnionMember9ExprUnionMember1,
    RankByUnionMember8ExprUnionMember6ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember6ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember8ExprUnionMember6ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember8ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember6ExprUnionMember0,
    RankByUnionMember8ExprUnionMember6ExprUnionMember1,
    RankByUnionMember8ExprUnionMember6ExprUnionMember2,
    RankByUnionMember8ExprUnionMember6ExprUnionMember3,
    RankByUnionMember8ExprUnionMember6ExprUnionMember4,
    RankByUnionMember8ExprUnionMember6ExprUnionMember5,
    RankByUnionMember8ExprUnionMember6ExprUnionMember6,
    RankByUnionMember8ExprUnionMember6ExprUnionMember7,
    RankByUnionMember8ExprUnionMember6ExprUnionMember8,
    RankByUnionMember8ExprUnionMember6ExprUnionMember9,
]


class RankByUnionMember8ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember8ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember8ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember8ExprUnionMember7ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember7ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember7ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember7ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember7ExprUnionMember3ExprUnionMember0,
    RankByUnionMember8ExprUnionMember7ExprUnionMember3ExprUnionMember1,
    RankByUnionMember8ExprUnionMember7ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember7ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember8ExprUnionMember7ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember8ExprUnionMember7ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember8ExprUnionMember7ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember8ExprUnionMember7ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember7ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember7ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember7ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember7ExprUnionMember6ExprUnionMember0,
    RankByUnionMember8ExprUnionMember7ExprUnionMember6ExprUnionMember1,
    RankByUnionMember8ExprUnionMember7ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember7ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember8ExprUnionMember7ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember8ExprUnionMember7ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember7ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember7ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember7ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember7ExprUnionMember7ExprUnionMember0,
    RankByUnionMember8ExprUnionMember7ExprUnionMember7ExprUnionMember1,
    RankByUnionMember8ExprUnionMember7ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember7ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember8ExprUnionMember7ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember8ExprUnionMember7ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember7ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember7ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember7ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember7ExprUnionMember8ExprUnionMember0,
    RankByUnionMember8ExprUnionMember7ExprUnionMember8ExprUnionMember1,
    RankByUnionMember8ExprUnionMember7ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember7ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember8ExprUnionMember7ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember8ExprUnionMember7ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember7ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember7ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember7ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember7ExprUnionMember9ExprUnionMember0,
    RankByUnionMember8ExprUnionMember7ExprUnionMember9ExprUnionMember1,
    RankByUnionMember8ExprUnionMember7ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember7ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember8ExprUnionMember7ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember8ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember7ExprUnionMember0,
    RankByUnionMember8ExprUnionMember7ExprUnionMember1,
    RankByUnionMember8ExprUnionMember7ExprUnionMember2,
    RankByUnionMember8ExprUnionMember7ExprUnionMember3,
    RankByUnionMember8ExprUnionMember7ExprUnionMember4,
    RankByUnionMember8ExprUnionMember7ExprUnionMember5,
    RankByUnionMember8ExprUnionMember7ExprUnionMember6,
    RankByUnionMember8ExprUnionMember7ExprUnionMember7,
    RankByUnionMember8ExprUnionMember7ExprUnionMember8,
    RankByUnionMember8ExprUnionMember7ExprUnionMember9,
]


class RankByUnionMember8ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember8ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember8ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember8ExprUnionMember8ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember8ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember8ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember8ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember8ExprUnionMember3ExprUnionMember0,
    RankByUnionMember8ExprUnionMember8ExprUnionMember3ExprUnionMember1,
    RankByUnionMember8ExprUnionMember8ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember8ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember8ExprUnionMember8ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember8ExprUnionMember8ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember8ExprUnionMember8ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember8ExprUnionMember8ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember8ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember8ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember8ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember8ExprUnionMember6ExprUnionMember0,
    RankByUnionMember8ExprUnionMember8ExprUnionMember6ExprUnionMember1,
    RankByUnionMember8ExprUnionMember8ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember8ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember8ExprUnionMember8ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember8ExprUnionMember8ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember8ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember8ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember8ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember8ExprUnionMember7ExprUnionMember0,
    RankByUnionMember8ExprUnionMember8ExprUnionMember7ExprUnionMember1,
    RankByUnionMember8ExprUnionMember8ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember8ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember8ExprUnionMember8ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember8ExprUnionMember8ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember8ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember8ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember8ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember8ExprUnionMember8ExprUnionMember0,
    RankByUnionMember8ExprUnionMember8ExprUnionMember8ExprUnionMember1,
    RankByUnionMember8ExprUnionMember8ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember8ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember8ExprUnionMember8ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember8ExprUnionMember8ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember8ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember8ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember8ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember8ExprUnionMember9ExprUnionMember0,
    RankByUnionMember8ExprUnionMember8ExprUnionMember9ExprUnionMember1,
    RankByUnionMember8ExprUnionMember8ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember8ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember8ExprUnionMember8ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember8ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember8ExprUnionMember0,
    RankByUnionMember8ExprUnionMember8ExprUnionMember1,
    RankByUnionMember8ExprUnionMember8ExprUnionMember2,
    RankByUnionMember8ExprUnionMember8ExprUnionMember3,
    RankByUnionMember8ExprUnionMember8ExprUnionMember4,
    RankByUnionMember8ExprUnionMember8ExprUnionMember5,
    RankByUnionMember8ExprUnionMember8ExprUnionMember6,
    RankByUnionMember8ExprUnionMember8ExprUnionMember7,
    RankByUnionMember8ExprUnionMember8ExprUnionMember8,
    RankByUnionMember8ExprUnionMember8ExprUnionMember9,
]


class RankByUnionMember8ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember8ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember8ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember8ExprUnionMember9ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember9ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember9ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember9ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember9ExprUnionMember3ExprUnionMember0,
    RankByUnionMember8ExprUnionMember9ExprUnionMember3ExprUnionMember1,
    RankByUnionMember8ExprUnionMember9ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember9ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember8ExprUnionMember9ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember8ExprUnionMember9ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember8ExprUnionMember9ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember8ExprUnionMember9ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember9ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember9ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember9ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember9ExprUnionMember6ExprUnionMember0,
    RankByUnionMember8ExprUnionMember9ExprUnionMember6ExprUnionMember1,
    RankByUnionMember8ExprUnionMember9ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember9ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember8ExprUnionMember9ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember8ExprUnionMember9ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember9ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember9ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember9ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember9ExprUnionMember7ExprUnionMember0,
    RankByUnionMember8ExprUnionMember9ExprUnionMember7ExprUnionMember1,
    RankByUnionMember8ExprUnionMember9ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember9ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember8ExprUnionMember9ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember8ExprUnionMember9ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember9ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember9ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember9ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember9ExprUnionMember8ExprUnionMember0,
    RankByUnionMember8ExprUnionMember9ExprUnionMember8ExprUnionMember1,
    RankByUnionMember8ExprUnionMember9ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember9ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember8ExprUnionMember9ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember8ExprUnionMember9ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember8ExprUnionMember9ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember8ExprUnionMember9ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember8ExprUnionMember9ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember9ExprUnionMember9ExprUnionMember0,
    RankByUnionMember8ExprUnionMember9ExprUnionMember9ExprUnionMember1,
    RankByUnionMember8ExprUnionMember9ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember8ExprUnionMember9ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember8ExprUnionMember9ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember8ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember9ExprUnionMember0,
    RankByUnionMember8ExprUnionMember9ExprUnionMember1,
    RankByUnionMember8ExprUnionMember9ExprUnionMember2,
    RankByUnionMember8ExprUnionMember9ExprUnionMember3,
    RankByUnionMember8ExprUnionMember9ExprUnionMember4,
    RankByUnionMember8ExprUnionMember9ExprUnionMember5,
    RankByUnionMember8ExprUnionMember9ExprUnionMember6,
    RankByUnionMember8ExprUnionMember9ExprUnionMember7,
    RankByUnionMember8ExprUnionMember9ExprUnionMember8,
    RankByUnionMember8ExprUnionMember9ExprUnionMember9,
]


class RankByUnionMember8ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember8ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember8ExprUnionMember0,
    RankByUnionMember8ExprUnionMember1,
    RankByUnionMember8ExprUnionMember2,
    RankByUnionMember8ExprUnionMember3,
    RankByUnionMember8ExprUnionMember4,
    RankByUnionMember8ExprUnionMember5,
    RankByUnionMember8ExprUnionMember6,
    RankByUnionMember8ExprUnionMember7,
    RankByUnionMember8ExprUnionMember8,
    RankByUnionMember8ExprUnionMember9,
]


class RankByUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember9ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember9ExprUnionMember3ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember3ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember3ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember3ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember3ExprUnionMember3ExprUnionMember0,
    RankByUnionMember9ExprUnionMember3ExprUnionMember3ExprUnionMember1,
    RankByUnionMember9ExprUnionMember3ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember3ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember9ExprUnionMember3ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember9ExprUnionMember3ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember9ExprUnionMember3ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember9ExprUnionMember3ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember3ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember3ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember3ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember3ExprUnionMember6ExprUnionMember0,
    RankByUnionMember9ExprUnionMember3ExprUnionMember6ExprUnionMember1,
    RankByUnionMember9ExprUnionMember3ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember3ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember9ExprUnionMember3ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember9ExprUnionMember3ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember3ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember3ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember3ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember3ExprUnionMember7ExprUnionMember0,
    RankByUnionMember9ExprUnionMember3ExprUnionMember7ExprUnionMember1,
    RankByUnionMember9ExprUnionMember3ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember3ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember9ExprUnionMember3ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember9ExprUnionMember3ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember3ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember3ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember3ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember3ExprUnionMember8ExprUnionMember0,
    RankByUnionMember9ExprUnionMember3ExprUnionMember8ExprUnionMember1,
    RankByUnionMember9ExprUnionMember3ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember3ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember9ExprUnionMember3ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember9ExprUnionMember3ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember3ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember3ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember3ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember3ExprUnionMember9ExprUnionMember0,
    RankByUnionMember9ExprUnionMember3ExprUnionMember9ExprUnionMember1,
    RankByUnionMember9ExprUnionMember3ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember3ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember9ExprUnionMember3ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember9ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember3ExprUnionMember0,
    RankByUnionMember9ExprUnionMember3ExprUnionMember1,
    RankByUnionMember9ExprUnionMember3ExprUnionMember2,
    RankByUnionMember9ExprUnionMember3ExprUnionMember3,
    RankByUnionMember9ExprUnionMember3ExprUnionMember4,
    RankByUnionMember9ExprUnionMember3ExprUnionMember5,
    RankByUnionMember9ExprUnionMember3ExprUnionMember6,
    RankByUnionMember9ExprUnionMember3ExprUnionMember7,
    RankByUnionMember9ExprUnionMember3ExprUnionMember8,
    RankByUnionMember9ExprUnionMember3ExprUnionMember9,
]


class RankByUnionMember9ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember9ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember9ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember9ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember9ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember9ExprUnionMember6ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember6ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember6ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember6ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember6ExprUnionMember3ExprUnionMember0,
    RankByUnionMember9ExprUnionMember6ExprUnionMember3ExprUnionMember1,
    RankByUnionMember9ExprUnionMember6ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember6ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember9ExprUnionMember6ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember9ExprUnionMember6ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember9ExprUnionMember6ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember9ExprUnionMember6ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember6ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember6ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember6ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember6ExprUnionMember6ExprUnionMember0,
    RankByUnionMember9ExprUnionMember6ExprUnionMember6ExprUnionMember1,
    RankByUnionMember9ExprUnionMember6ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember6ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember9ExprUnionMember6ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember9ExprUnionMember6ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember6ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember6ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember6ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember6ExprUnionMember7ExprUnionMember0,
    RankByUnionMember9ExprUnionMember6ExprUnionMember7ExprUnionMember1,
    RankByUnionMember9ExprUnionMember6ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember6ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember9ExprUnionMember6ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember9ExprUnionMember6ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember6ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember6ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember6ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember6ExprUnionMember8ExprUnionMember0,
    RankByUnionMember9ExprUnionMember6ExprUnionMember8ExprUnionMember1,
    RankByUnionMember9ExprUnionMember6ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember6ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember9ExprUnionMember6ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember9ExprUnionMember6ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember6ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember6ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember6ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember6ExprUnionMember9ExprUnionMember0,
    RankByUnionMember9ExprUnionMember6ExprUnionMember9ExprUnionMember1,
    RankByUnionMember9ExprUnionMember6ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember6ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember9ExprUnionMember6ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember9ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember6ExprUnionMember0,
    RankByUnionMember9ExprUnionMember6ExprUnionMember1,
    RankByUnionMember9ExprUnionMember6ExprUnionMember2,
    RankByUnionMember9ExprUnionMember6ExprUnionMember3,
    RankByUnionMember9ExprUnionMember6ExprUnionMember4,
    RankByUnionMember9ExprUnionMember6ExprUnionMember5,
    RankByUnionMember9ExprUnionMember6ExprUnionMember6,
    RankByUnionMember9ExprUnionMember6ExprUnionMember7,
    RankByUnionMember9ExprUnionMember6ExprUnionMember8,
    RankByUnionMember9ExprUnionMember6ExprUnionMember9,
]


class RankByUnionMember9ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember9ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember9ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember9ExprUnionMember7ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember7ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember7ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember7ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember7ExprUnionMember3ExprUnionMember0,
    RankByUnionMember9ExprUnionMember7ExprUnionMember3ExprUnionMember1,
    RankByUnionMember9ExprUnionMember7ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember7ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember9ExprUnionMember7ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember9ExprUnionMember7ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember9ExprUnionMember7ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember9ExprUnionMember7ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember7ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember7ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember7ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember7ExprUnionMember6ExprUnionMember0,
    RankByUnionMember9ExprUnionMember7ExprUnionMember6ExprUnionMember1,
    RankByUnionMember9ExprUnionMember7ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember7ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember9ExprUnionMember7ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember9ExprUnionMember7ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember7ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember7ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember7ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember7ExprUnionMember7ExprUnionMember0,
    RankByUnionMember9ExprUnionMember7ExprUnionMember7ExprUnionMember1,
    RankByUnionMember9ExprUnionMember7ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember7ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember9ExprUnionMember7ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember9ExprUnionMember7ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember7ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember7ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember7ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember7ExprUnionMember8ExprUnionMember0,
    RankByUnionMember9ExprUnionMember7ExprUnionMember8ExprUnionMember1,
    RankByUnionMember9ExprUnionMember7ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember7ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember9ExprUnionMember7ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember9ExprUnionMember7ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember7ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember7ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember7ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember7ExprUnionMember9ExprUnionMember0,
    RankByUnionMember9ExprUnionMember7ExprUnionMember9ExprUnionMember1,
    RankByUnionMember9ExprUnionMember7ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember7ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember9ExprUnionMember7ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember9ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember7ExprUnionMember0,
    RankByUnionMember9ExprUnionMember7ExprUnionMember1,
    RankByUnionMember9ExprUnionMember7ExprUnionMember2,
    RankByUnionMember9ExprUnionMember7ExprUnionMember3,
    RankByUnionMember9ExprUnionMember7ExprUnionMember4,
    RankByUnionMember9ExprUnionMember7ExprUnionMember5,
    RankByUnionMember9ExprUnionMember7ExprUnionMember6,
    RankByUnionMember9ExprUnionMember7ExprUnionMember7,
    RankByUnionMember9ExprUnionMember7ExprUnionMember8,
    RankByUnionMember9ExprUnionMember7ExprUnionMember9,
]


class RankByUnionMember9ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember9ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember9ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember9ExprUnionMember8ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember8ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember8ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember8ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember8ExprUnionMember3ExprUnionMember0,
    RankByUnionMember9ExprUnionMember8ExprUnionMember3ExprUnionMember1,
    RankByUnionMember9ExprUnionMember8ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember8ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember9ExprUnionMember8ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember9ExprUnionMember8ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember9ExprUnionMember8ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember9ExprUnionMember8ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember8ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember8ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember8ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember8ExprUnionMember6ExprUnionMember0,
    RankByUnionMember9ExprUnionMember8ExprUnionMember6ExprUnionMember1,
    RankByUnionMember9ExprUnionMember8ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember8ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember9ExprUnionMember8ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember9ExprUnionMember8ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember8ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember8ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember8ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember8ExprUnionMember7ExprUnionMember0,
    RankByUnionMember9ExprUnionMember8ExprUnionMember7ExprUnionMember1,
    RankByUnionMember9ExprUnionMember8ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember8ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember9ExprUnionMember8ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember9ExprUnionMember8ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember8ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember8ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember8ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember8ExprUnionMember8ExprUnionMember0,
    RankByUnionMember9ExprUnionMember8ExprUnionMember8ExprUnionMember1,
    RankByUnionMember9ExprUnionMember8ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember8ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember9ExprUnionMember8ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember9ExprUnionMember8ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember8ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember8ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember8ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember8ExprUnionMember9ExprUnionMember0,
    RankByUnionMember9ExprUnionMember8ExprUnionMember9ExprUnionMember1,
    RankByUnionMember9ExprUnionMember8ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember8ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember9ExprUnionMember8ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember9ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember8ExprUnionMember0,
    RankByUnionMember9ExprUnionMember8ExprUnionMember1,
    RankByUnionMember9ExprUnionMember8ExprUnionMember2,
    RankByUnionMember9ExprUnionMember8ExprUnionMember3,
    RankByUnionMember9ExprUnionMember8ExprUnionMember4,
    RankByUnionMember9ExprUnionMember8ExprUnionMember5,
    RankByUnionMember9ExprUnionMember8ExprUnionMember6,
    RankByUnionMember9ExprUnionMember8ExprUnionMember7,
    RankByUnionMember9ExprUnionMember8ExprUnionMember8,
    RankByUnionMember9ExprUnionMember8ExprUnionMember9,
]


class RankByUnionMember9ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember9ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember9ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


class RankByUnionMember9ExprUnionMember9ExprUnionMember3ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember9ExprUnionMember3ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember9ExprUnionMember3ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember9ExprUnionMember3Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember9ExprUnionMember3ExprUnionMember0,
    RankByUnionMember9ExprUnionMember9ExprUnionMember3ExprUnionMember1,
    RankByUnionMember9ExprUnionMember9ExprUnionMember3ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember9ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember9ExprUnionMember9ExprUnionMember3Expr]]

    type: Required[Literal["Sum"]]


class RankByUnionMember9ExprUnionMember9ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByUnionMember9ExprUnionMember9ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByUnionMember9ExprUnionMember9ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember9ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember9ExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember9ExprUnionMember6Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember9ExprUnionMember6ExprUnionMember0,
    RankByUnionMember9ExprUnionMember9ExprUnionMember6ExprUnionMember1,
    RankByUnionMember9ExprUnionMember9ExprUnionMember6ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember9ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember9ExprUnionMember9ExprUnionMember6Expr]]

    type: Required[Literal["Max"]]


class RankByUnionMember9ExprUnionMember9ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember9ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember9ExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember9ExprUnionMember7Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember9ExprUnionMember7ExprUnionMember0,
    RankByUnionMember9ExprUnionMember9ExprUnionMember7ExprUnionMember1,
    RankByUnionMember9ExprUnionMember9ExprUnionMember7ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember9ExprUnionMember7(TypedDict, total=False):
    exprs: Required[Iterable[RankByUnionMember9ExprUnionMember9ExprUnionMember7Expr]]

    type: Required[Literal["Min"]]


class RankByUnionMember9ExprUnionMember9ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember9ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember9ExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember9ExprUnionMember8Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember9ExprUnionMember8ExprUnionMember0,
    RankByUnionMember9ExprUnionMember9ExprUnionMember8ExprUnionMember1,
    RankByUnionMember9ExprUnionMember9ExprUnionMember8ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember9ExprUnionMember8(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByUnionMember9ExprUnionMember9ExprUnionMember8Expr]

    type: Required[Literal["Log"]]


class RankByUnionMember9ExprUnionMember9ExprUnionMember9ExprUnionMember0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["Attr"]]


class RankByUnionMember9ExprUnionMember9ExprUnionMember9ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByUnionMember9ExprUnionMember9ExprUnionMember9ExprUnionMember2(TypedDict, total=False):
    field: Required[str]

    query: Required[str]

    type: Required[Literal["BM25"]]


RankByUnionMember9ExprUnionMember9ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember9ExprUnionMember9ExprUnionMember0,
    RankByUnionMember9ExprUnionMember9ExprUnionMember9ExprUnionMember1,
    RankByUnionMember9ExprUnionMember9ExprUnionMember9ExprUnionMember2,
]


class RankByUnionMember9ExprUnionMember9ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember9ExprUnionMember9ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember9ExprUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember9ExprUnionMember0,
    RankByUnionMember9ExprUnionMember9ExprUnionMember1,
    RankByUnionMember9ExprUnionMember9ExprUnionMember2,
    RankByUnionMember9ExprUnionMember9ExprUnionMember3,
    RankByUnionMember9ExprUnionMember9ExprUnionMember4,
    RankByUnionMember9ExprUnionMember9ExprUnionMember5,
    RankByUnionMember9ExprUnionMember9ExprUnionMember6,
    RankByUnionMember9ExprUnionMember9ExprUnionMember7,
    RankByUnionMember9ExprUnionMember9ExprUnionMember8,
    RankByUnionMember9ExprUnionMember9ExprUnionMember9,
]


class RankByUnionMember9ExprUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember9ExprUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByUnionMember9Expr: TypeAlias = Union[
    RankByUnionMember9ExprUnionMember0,
    RankByUnionMember9ExprUnionMember1,
    RankByUnionMember9ExprUnionMember2,
    RankByUnionMember9ExprUnionMember3,
    RankByUnionMember9ExprUnionMember4,
    RankByUnionMember9ExprUnionMember5,
    RankByUnionMember9ExprUnionMember6,
    RankByUnionMember9ExprUnionMember7,
    RankByUnionMember9ExprUnionMember8,
    RankByUnionMember9ExprUnionMember9,
]


class RankByUnionMember9(TypedDict, total=False):
    expr: Required[RankByUnionMember9Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankBy: TypeAlias = Union[
    RankByUnionMember0,
    RankByUnionMember1,
    RankByUnionMember2,
    RankByUnionMember3,
    RankByUnionMember4,
    RankByUnionMember5,
    RankByUnionMember6,
    RankByUnionMember7,
    RankByUnionMember8,
    RankByUnionMember9,
]
