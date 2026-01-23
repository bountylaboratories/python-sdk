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

    value: Required[Union[str, float, SequenceNotStr[str], Iterable[float]]]
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

    value: Required[Union[str, float, SequenceNotStr[str], Iterable[float]]]
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

    value: Required[Union[str, float, SequenceNotStr[str], Iterable[float]]]
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

    value: Required[Union[str, float, SequenceNotStr[str], Iterable[float]]]
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

    value: Required[Union[str, float, SequenceNotStr[str], Iterable[float]]]
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

    value: Required[Union[str, float, SequenceNotStr[str], Iterable[float]]]
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

    value: Required[Union[str, float, SequenceNotStr[str], Iterable[float]]]
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

    value: Required[Union[str, float, SequenceNotStr[str], Iterable[float]]]
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

    value: Required[Union[str, float, SequenceNotStr[str], Iterable[float]]]
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

    value: Required[Union[str, float, SequenceNotStr[str], Iterable[float]]]
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

    value: Required[Union[str, float, SequenceNotStr[str], Iterable[float]]]
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

    value: Required[Union[str, float, SequenceNotStr[str], Iterable[float]]]
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
