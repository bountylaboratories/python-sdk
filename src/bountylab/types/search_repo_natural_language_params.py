# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "SearchRepoNaturalLanguageParams",
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
    "RankBySumExprUnionMember2ExprUnionMember4",
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
    "RankBySumExprUnionMember2ExprUnionMember8",
    "RankBySumExprUnionMember2ExprUnionMember8Expr",
    "RankBySumExprUnionMember2ExprUnionMember8ExprUnionMember0",
    "RankBySumExprUnionMember2ExprUnionMember8ExprUnionMember1",
    "RankBySumExprUnionMember3",
    "RankBySumExprUnionMember4",
    "RankBySumExprUnionMember5",
    "RankBySumExprUnionMember5Expr",
    "RankBySumExprUnionMember5ExprUnionMember0",
    "RankBySumExprUnionMember5ExprUnionMember1",
    "RankBySumExprUnionMember5ExprUnionMember2",
    "RankBySumExprUnionMember5ExprUnionMember2Expr",
    "RankBySumExprUnionMember5ExprUnionMember2ExprUnionMember0",
    "RankBySumExprUnionMember5ExprUnionMember2ExprUnionMember1",
    "RankBySumExprUnionMember5ExprUnionMember3",
    "RankBySumExprUnionMember5ExprUnionMember4",
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
    "RankBySumExprUnionMember5ExprUnionMember8",
    "RankBySumExprUnionMember5ExprUnionMember8Expr",
    "RankBySumExprUnionMember5ExprUnionMember8ExprUnionMember0",
    "RankBySumExprUnionMember5ExprUnionMember8ExprUnionMember1",
    "RankBySumExprUnionMember6",
    "RankBySumExprUnionMember6Expr",
    "RankBySumExprUnionMember6ExprUnionMember0",
    "RankBySumExprUnionMember6ExprUnionMember1",
    "RankBySumExprUnionMember6ExprUnionMember2",
    "RankBySumExprUnionMember6ExprUnionMember2Expr",
    "RankBySumExprUnionMember6ExprUnionMember2ExprUnionMember0",
    "RankBySumExprUnionMember6ExprUnionMember2ExprUnionMember1",
    "RankBySumExprUnionMember6ExprUnionMember3",
    "RankBySumExprUnionMember6ExprUnionMember4",
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
    "RankBySumExprUnionMember6ExprUnionMember8",
    "RankBySumExprUnionMember6ExprUnionMember8Expr",
    "RankBySumExprUnionMember6ExprUnionMember8ExprUnionMember0",
    "RankBySumExprUnionMember6ExprUnionMember8ExprUnionMember1",
    "RankBySumExprUnionMember7",
    "RankBySumExprUnionMember7Expr",
    "RankBySumExprUnionMember7ExprUnionMember0",
    "RankBySumExprUnionMember7ExprUnionMember1",
    "RankBySumExprUnionMember7ExprUnionMember2",
    "RankBySumExprUnionMember7ExprUnionMember2Expr",
    "RankBySumExprUnionMember7ExprUnionMember2ExprUnionMember0",
    "RankBySumExprUnionMember7ExprUnionMember2ExprUnionMember1",
    "RankBySumExprUnionMember7ExprUnionMember3",
    "RankBySumExprUnionMember7ExprUnionMember4",
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
    "RankBySumExprUnionMember7ExprUnionMember8",
    "RankBySumExprUnionMember7ExprUnionMember8Expr",
    "RankBySumExprUnionMember7ExprUnionMember8ExprUnionMember0",
    "RankBySumExprUnionMember7ExprUnionMember8ExprUnionMember1",
    "RankBySumExprUnionMember8",
    "RankBySumExprUnionMember8Expr",
    "RankBySumExprUnionMember8ExprUnionMember0",
    "RankBySumExprUnionMember8ExprUnionMember1",
    "RankBySumExprUnionMember8ExprUnionMember2",
    "RankBySumExprUnionMember8ExprUnionMember2Expr",
    "RankBySumExprUnionMember8ExprUnionMember2ExprUnionMember0",
    "RankBySumExprUnionMember8ExprUnionMember2ExprUnionMember1",
    "RankBySumExprUnionMember8ExprUnionMember3",
    "RankBySumExprUnionMember8ExprUnionMember4",
    "RankBySumExprUnionMember8ExprUnionMember5",
    "RankBySumExprUnionMember8ExprUnionMember5Expr",
    "RankBySumExprUnionMember8ExprUnionMember5ExprUnionMember0",
    "RankBySumExprUnionMember8ExprUnionMember5ExprUnionMember1",
    "RankBySumExprUnionMember8ExprUnionMember6",
    "RankBySumExprUnionMember8ExprUnionMember6Expr",
    "RankBySumExprUnionMember8ExprUnionMember6ExprUnionMember0",
    "RankBySumExprUnionMember8ExprUnionMember6ExprUnionMember1",
    "RankBySumExprUnionMember8ExprUnionMember7",
    "RankBySumExprUnionMember8ExprUnionMember7Expr",
    "RankBySumExprUnionMember8ExprUnionMember7ExprUnionMember0",
    "RankBySumExprUnionMember8ExprUnionMember7ExprUnionMember1",
    "RankBySumExprUnionMember8ExprUnionMember8",
    "RankBySumExprUnionMember8ExprUnionMember8Expr",
    "RankBySumExprUnionMember8ExprUnionMember8ExprUnionMember0",
    "RankBySumExprUnionMember8ExprUnionMember8ExprUnionMember1",
    "RankByMult",
    "RankByDiv",
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
    "RankByMaxExprUnionMember2ExprUnionMember4",
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
    "RankByMaxExprUnionMember2ExprUnionMember8",
    "RankByMaxExprUnionMember2ExprUnionMember8Expr",
    "RankByMaxExprUnionMember2ExprUnionMember8ExprUnionMember0",
    "RankByMaxExprUnionMember2ExprUnionMember8ExprUnionMember1",
    "RankByMaxExprUnionMember3",
    "RankByMaxExprUnionMember4",
    "RankByMaxExprUnionMember5",
    "RankByMaxExprUnionMember5Expr",
    "RankByMaxExprUnionMember5ExprUnionMember0",
    "RankByMaxExprUnionMember5ExprUnionMember1",
    "RankByMaxExprUnionMember5ExprUnionMember2",
    "RankByMaxExprUnionMember5ExprUnionMember2Expr",
    "RankByMaxExprUnionMember5ExprUnionMember2ExprUnionMember0",
    "RankByMaxExprUnionMember5ExprUnionMember2ExprUnionMember1",
    "RankByMaxExprUnionMember5ExprUnionMember3",
    "RankByMaxExprUnionMember5ExprUnionMember4",
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
    "RankByMaxExprUnionMember5ExprUnionMember8",
    "RankByMaxExprUnionMember5ExprUnionMember8Expr",
    "RankByMaxExprUnionMember5ExprUnionMember8ExprUnionMember0",
    "RankByMaxExprUnionMember5ExprUnionMember8ExprUnionMember1",
    "RankByMaxExprUnionMember6",
    "RankByMaxExprUnionMember6Expr",
    "RankByMaxExprUnionMember6ExprUnionMember0",
    "RankByMaxExprUnionMember6ExprUnionMember1",
    "RankByMaxExprUnionMember6ExprUnionMember2",
    "RankByMaxExprUnionMember6ExprUnionMember2Expr",
    "RankByMaxExprUnionMember6ExprUnionMember2ExprUnionMember0",
    "RankByMaxExprUnionMember6ExprUnionMember2ExprUnionMember1",
    "RankByMaxExprUnionMember6ExprUnionMember3",
    "RankByMaxExprUnionMember6ExprUnionMember4",
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
    "RankByMaxExprUnionMember6ExprUnionMember8",
    "RankByMaxExprUnionMember6ExprUnionMember8Expr",
    "RankByMaxExprUnionMember6ExprUnionMember8ExprUnionMember0",
    "RankByMaxExprUnionMember6ExprUnionMember8ExprUnionMember1",
    "RankByMaxExprUnionMember7",
    "RankByMaxExprUnionMember7Expr",
    "RankByMaxExprUnionMember7ExprUnionMember0",
    "RankByMaxExprUnionMember7ExprUnionMember1",
    "RankByMaxExprUnionMember7ExprUnionMember2",
    "RankByMaxExprUnionMember7ExprUnionMember2Expr",
    "RankByMaxExprUnionMember7ExprUnionMember2ExprUnionMember0",
    "RankByMaxExprUnionMember7ExprUnionMember2ExprUnionMember1",
    "RankByMaxExprUnionMember7ExprUnionMember3",
    "RankByMaxExprUnionMember7ExprUnionMember4",
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
    "RankByMaxExprUnionMember7ExprUnionMember8",
    "RankByMaxExprUnionMember7ExprUnionMember8Expr",
    "RankByMaxExprUnionMember7ExprUnionMember8ExprUnionMember0",
    "RankByMaxExprUnionMember7ExprUnionMember8ExprUnionMember1",
    "RankByMaxExprUnionMember8",
    "RankByMaxExprUnionMember8Expr",
    "RankByMaxExprUnionMember8ExprUnionMember0",
    "RankByMaxExprUnionMember8ExprUnionMember1",
    "RankByMaxExprUnionMember8ExprUnionMember2",
    "RankByMaxExprUnionMember8ExprUnionMember2Expr",
    "RankByMaxExprUnionMember8ExprUnionMember2ExprUnionMember0",
    "RankByMaxExprUnionMember8ExprUnionMember2ExprUnionMember1",
    "RankByMaxExprUnionMember8ExprUnionMember3",
    "RankByMaxExprUnionMember8ExprUnionMember4",
    "RankByMaxExprUnionMember8ExprUnionMember5",
    "RankByMaxExprUnionMember8ExprUnionMember5Expr",
    "RankByMaxExprUnionMember8ExprUnionMember5ExprUnionMember0",
    "RankByMaxExprUnionMember8ExprUnionMember5ExprUnionMember1",
    "RankByMaxExprUnionMember8ExprUnionMember6",
    "RankByMaxExprUnionMember8ExprUnionMember6Expr",
    "RankByMaxExprUnionMember8ExprUnionMember6ExprUnionMember0",
    "RankByMaxExprUnionMember8ExprUnionMember6ExprUnionMember1",
    "RankByMaxExprUnionMember8ExprUnionMember7",
    "RankByMaxExprUnionMember8ExprUnionMember7Expr",
    "RankByMaxExprUnionMember8ExprUnionMember7ExprUnionMember0",
    "RankByMaxExprUnionMember8ExprUnionMember7ExprUnionMember1",
    "RankByMaxExprUnionMember8ExprUnionMember8",
    "RankByMaxExprUnionMember8ExprUnionMember8Expr",
    "RankByMaxExprUnionMember8ExprUnionMember8ExprUnionMember0",
    "RankByMaxExprUnionMember8ExprUnionMember8ExprUnionMember1",
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
    "RankByMinExprUnionMember2ExprUnionMember4",
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
    "RankByMinExprUnionMember2ExprUnionMember8",
    "RankByMinExprUnionMember2ExprUnionMember8Expr",
    "RankByMinExprUnionMember2ExprUnionMember8ExprUnionMember0",
    "RankByMinExprUnionMember2ExprUnionMember8ExprUnionMember1",
    "RankByMinExprUnionMember3",
    "RankByMinExprUnionMember4",
    "RankByMinExprUnionMember5",
    "RankByMinExprUnionMember5Expr",
    "RankByMinExprUnionMember5ExprUnionMember0",
    "RankByMinExprUnionMember5ExprUnionMember1",
    "RankByMinExprUnionMember5ExprUnionMember2",
    "RankByMinExprUnionMember5ExprUnionMember2Expr",
    "RankByMinExprUnionMember5ExprUnionMember2ExprUnionMember0",
    "RankByMinExprUnionMember5ExprUnionMember2ExprUnionMember1",
    "RankByMinExprUnionMember5ExprUnionMember3",
    "RankByMinExprUnionMember5ExprUnionMember4",
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
    "RankByMinExprUnionMember5ExprUnionMember8",
    "RankByMinExprUnionMember5ExprUnionMember8Expr",
    "RankByMinExprUnionMember5ExprUnionMember8ExprUnionMember0",
    "RankByMinExprUnionMember5ExprUnionMember8ExprUnionMember1",
    "RankByMinExprUnionMember6",
    "RankByMinExprUnionMember6Expr",
    "RankByMinExprUnionMember6ExprUnionMember0",
    "RankByMinExprUnionMember6ExprUnionMember1",
    "RankByMinExprUnionMember6ExprUnionMember2",
    "RankByMinExprUnionMember6ExprUnionMember2Expr",
    "RankByMinExprUnionMember6ExprUnionMember2ExprUnionMember0",
    "RankByMinExprUnionMember6ExprUnionMember2ExprUnionMember1",
    "RankByMinExprUnionMember6ExprUnionMember3",
    "RankByMinExprUnionMember6ExprUnionMember4",
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
    "RankByMinExprUnionMember6ExprUnionMember8",
    "RankByMinExprUnionMember6ExprUnionMember8Expr",
    "RankByMinExprUnionMember6ExprUnionMember8ExprUnionMember0",
    "RankByMinExprUnionMember6ExprUnionMember8ExprUnionMember1",
    "RankByMinExprUnionMember7",
    "RankByMinExprUnionMember7Expr",
    "RankByMinExprUnionMember7ExprUnionMember0",
    "RankByMinExprUnionMember7ExprUnionMember1",
    "RankByMinExprUnionMember7ExprUnionMember2",
    "RankByMinExprUnionMember7ExprUnionMember2Expr",
    "RankByMinExprUnionMember7ExprUnionMember2ExprUnionMember0",
    "RankByMinExprUnionMember7ExprUnionMember2ExprUnionMember1",
    "RankByMinExprUnionMember7ExprUnionMember3",
    "RankByMinExprUnionMember7ExprUnionMember4",
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
    "RankByMinExprUnionMember7ExprUnionMember8",
    "RankByMinExprUnionMember7ExprUnionMember8Expr",
    "RankByMinExprUnionMember7ExprUnionMember8ExprUnionMember0",
    "RankByMinExprUnionMember7ExprUnionMember8ExprUnionMember1",
    "RankByMinExprUnionMember8",
    "RankByMinExprUnionMember8Expr",
    "RankByMinExprUnionMember8ExprUnionMember0",
    "RankByMinExprUnionMember8ExprUnionMember1",
    "RankByMinExprUnionMember8ExprUnionMember2",
    "RankByMinExprUnionMember8ExprUnionMember2Expr",
    "RankByMinExprUnionMember8ExprUnionMember2ExprUnionMember0",
    "RankByMinExprUnionMember8ExprUnionMember2ExprUnionMember1",
    "RankByMinExprUnionMember8ExprUnionMember3",
    "RankByMinExprUnionMember8ExprUnionMember4",
    "RankByMinExprUnionMember8ExprUnionMember5",
    "RankByMinExprUnionMember8ExprUnionMember5Expr",
    "RankByMinExprUnionMember8ExprUnionMember5ExprUnionMember0",
    "RankByMinExprUnionMember8ExprUnionMember5ExprUnionMember1",
    "RankByMinExprUnionMember8ExprUnionMember6",
    "RankByMinExprUnionMember8ExprUnionMember6Expr",
    "RankByMinExprUnionMember8ExprUnionMember6ExprUnionMember0",
    "RankByMinExprUnionMember8ExprUnionMember6ExprUnionMember1",
    "RankByMinExprUnionMember8ExprUnionMember7",
    "RankByMinExprUnionMember8ExprUnionMember7Expr",
    "RankByMinExprUnionMember8ExprUnionMember7ExprUnionMember0",
    "RankByMinExprUnionMember8ExprUnionMember7ExprUnionMember1",
    "RankByMinExprUnionMember8ExprUnionMember8",
    "RankByMinExprUnionMember8ExprUnionMember8Expr",
    "RankByMinExprUnionMember8ExprUnionMember8ExprUnionMember0",
    "RankByMinExprUnionMember8ExprUnionMember8ExprUnionMember1",
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
    "RankByLogExprUnionMember2ExprUnionMember4",
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
    "RankByLogExprUnionMember2ExprUnionMember8",
    "RankByLogExprUnionMember2ExprUnionMember8Expr",
    "RankByLogExprUnionMember2ExprUnionMember8ExprUnionMember0",
    "RankByLogExprUnionMember2ExprUnionMember8ExprUnionMember1",
    "RankByLogExprUnionMember3",
    "RankByLogExprUnionMember4",
    "RankByLogExprUnionMember5",
    "RankByLogExprUnionMember5Expr",
    "RankByLogExprUnionMember5ExprUnionMember0",
    "RankByLogExprUnionMember5ExprUnionMember1",
    "RankByLogExprUnionMember5ExprUnionMember2",
    "RankByLogExprUnionMember5ExprUnionMember2Expr",
    "RankByLogExprUnionMember5ExprUnionMember2ExprUnionMember0",
    "RankByLogExprUnionMember5ExprUnionMember2ExprUnionMember1",
    "RankByLogExprUnionMember5ExprUnionMember3",
    "RankByLogExprUnionMember5ExprUnionMember4",
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
    "RankByLogExprUnionMember5ExprUnionMember8",
    "RankByLogExprUnionMember5ExprUnionMember8Expr",
    "RankByLogExprUnionMember5ExprUnionMember8ExprUnionMember0",
    "RankByLogExprUnionMember5ExprUnionMember8ExprUnionMember1",
    "RankByLogExprUnionMember6",
    "RankByLogExprUnionMember6Expr",
    "RankByLogExprUnionMember6ExprUnionMember0",
    "RankByLogExprUnionMember6ExprUnionMember1",
    "RankByLogExprUnionMember6ExprUnionMember2",
    "RankByLogExprUnionMember6ExprUnionMember2Expr",
    "RankByLogExprUnionMember6ExprUnionMember2ExprUnionMember0",
    "RankByLogExprUnionMember6ExprUnionMember2ExprUnionMember1",
    "RankByLogExprUnionMember6ExprUnionMember3",
    "RankByLogExprUnionMember6ExprUnionMember4",
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
    "RankByLogExprUnionMember6ExprUnionMember8",
    "RankByLogExprUnionMember6ExprUnionMember8Expr",
    "RankByLogExprUnionMember6ExprUnionMember8ExprUnionMember0",
    "RankByLogExprUnionMember6ExprUnionMember8ExprUnionMember1",
    "RankByLogExprUnionMember7",
    "RankByLogExprUnionMember7Expr",
    "RankByLogExprUnionMember7ExprUnionMember0",
    "RankByLogExprUnionMember7ExprUnionMember1",
    "RankByLogExprUnionMember7ExprUnionMember2",
    "RankByLogExprUnionMember7ExprUnionMember2Expr",
    "RankByLogExprUnionMember7ExprUnionMember2ExprUnionMember0",
    "RankByLogExprUnionMember7ExprUnionMember2ExprUnionMember1",
    "RankByLogExprUnionMember7ExprUnionMember3",
    "RankByLogExprUnionMember7ExprUnionMember4",
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
    "RankByLogExprUnionMember7ExprUnionMember8",
    "RankByLogExprUnionMember7ExprUnionMember8Expr",
    "RankByLogExprUnionMember7ExprUnionMember8ExprUnionMember0",
    "RankByLogExprUnionMember7ExprUnionMember8ExprUnionMember1",
    "RankByLogExprUnionMember8",
    "RankByLogExprUnionMember8Expr",
    "RankByLogExprUnionMember8ExprUnionMember0",
    "RankByLogExprUnionMember8ExprUnionMember1",
    "RankByLogExprUnionMember8ExprUnionMember2",
    "RankByLogExprUnionMember8ExprUnionMember2Expr",
    "RankByLogExprUnionMember8ExprUnionMember2ExprUnionMember0",
    "RankByLogExprUnionMember8ExprUnionMember2ExprUnionMember1",
    "RankByLogExprUnionMember8ExprUnionMember3",
    "RankByLogExprUnionMember8ExprUnionMember4",
    "RankByLogExprUnionMember8ExprUnionMember5",
    "RankByLogExprUnionMember8ExprUnionMember5Expr",
    "RankByLogExprUnionMember8ExprUnionMember5ExprUnionMember0",
    "RankByLogExprUnionMember8ExprUnionMember5ExprUnionMember1",
    "RankByLogExprUnionMember8ExprUnionMember6",
    "RankByLogExprUnionMember8ExprUnionMember6Expr",
    "RankByLogExprUnionMember8ExprUnionMember6ExprUnionMember0",
    "RankByLogExprUnionMember8ExprUnionMember6ExprUnionMember1",
    "RankByLogExprUnionMember8ExprUnionMember7",
    "RankByLogExprUnionMember8ExprUnionMember7Expr",
    "RankByLogExprUnionMember8ExprUnionMember7ExprUnionMember0",
    "RankByLogExprUnionMember8ExprUnionMember7ExprUnionMember1",
    "RankByLogExprUnionMember8ExprUnionMember8",
    "RankByLogExprUnionMember8ExprUnionMember8Expr",
    "RankByLogExprUnionMember8ExprUnionMember8ExprUnionMember0",
    "RankByLogExprUnionMember8ExprUnionMember8ExprUnionMember1",
    "RankBySaturate",
    "RankBySaturateExpr",
    "RankBySaturateExprUnionMember0",
    "RankBySaturateExprUnionMember1",
    "RankBySaturateExprUnionMember2",
    "RankBySaturateExprUnionMember2Expr",
    "RankBySaturateExprUnionMember2ExprUnionMember0",
    "RankBySaturateExprUnionMember2ExprUnionMember1",
    "RankBySaturateExprUnionMember2ExprUnionMember2",
    "RankBySaturateExprUnionMember2ExprUnionMember2Expr",
    "RankBySaturateExprUnionMember2ExprUnionMember2ExprUnionMember0",
    "RankBySaturateExprUnionMember2ExprUnionMember2ExprUnionMember1",
    "RankBySaturateExprUnionMember2ExprUnionMember3",
    "RankBySaturateExprUnionMember2ExprUnionMember4",
    "RankBySaturateExprUnionMember2ExprUnionMember5",
    "RankBySaturateExprUnionMember2ExprUnionMember5Expr",
    "RankBySaturateExprUnionMember2ExprUnionMember5ExprUnionMember0",
    "RankBySaturateExprUnionMember2ExprUnionMember5ExprUnionMember1",
    "RankBySaturateExprUnionMember2ExprUnionMember6",
    "RankBySaturateExprUnionMember2ExprUnionMember6Expr",
    "RankBySaturateExprUnionMember2ExprUnionMember6ExprUnionMember0",
    "RankBySaturateExprUnionMember2ExprUnionMember6ExprUnionMember1",
    "RankBySaturateExprUnionMember2ExprUnionMember7",
    "RankBySaturateExprUnionMember2ExprUnionMember7Expr",
    "RankBySaturateExprUnionMember2ExprUnionMember7ExprUnionMember0",
    "RankBySaturateExprUnionMember2ExprUnionMember7ExprUnionMember1",
    "RankBySaturateExprUnionMember2ExprUnionMember8",
    "RankBySaturateExprUnionMember2ExprUnionMember8Expr",
    "RankBySaturateExprUnionMember2ExprUnionMember8ExprUnionMember0",
    "RankBySaturateExprUnionMember2ExprUnionMember8ExprUnionMember1",
    "RankBySaturateExprUnionMember3",
    "RankBySaturateExprUnionMember4",
    "RankBySaturateExprUnionMember5",
    "RankBySaturateExprUnionMember5Expr",
    "RankBySaturateExprUnionMember5ExprUnionMember0",
    "RankBySaturateExprUnionMember5ExprUnionMember1",
    "RankBySaturateExprUnionMember5ExprUnionMember2",
    "RankBySaturateExprUnionMember5ExprUnionMember2Expr",
    "RankBySaturateExprUnionMember5ExprUnionMember2ExprUnionMember0",
    "RankBySaturateExprUnionMember5ExprUnionMember2ExprUnionMember1",
    "RankBySaturateExprUnionMember5ExprUnionMember3",
    "RankBySaturateExprUnionMember5ExprUnionMember4",
    "RankBySaturateExprUnionMember5ExprUnionMember5",
    "RankBySaturateExprUnionMember5ExprUnionMember5Expr",
    "RankBySaturateExprUnionMember5ExprUnionMember5ExprUnionMember0",
    "RankBySaturateExprUnionMember5ExprUnionMember5ExprUnionMember1",
    "RankBySaturateExprUnionMember5ExprUnionMember6",
    "RankBySaturateExprUnionMember5ExprUnionMember6Expr",
    "RankBySaturateExprUnionMember5ExprUnionMember6ExprUnionMember0",
    "RankBySaturateExprUnionMember5ExprUnionMember6ExprUnionMember1",
    "RankBySaturateExprUnionMember5ExprUnionMember7",
    "RankBySaturateExprUnionMember5ExprUnionMember7Expr",
    "RankBySaturateExprUnionMember5ExprUnionMember7ExprUnionMember0",
    "RankBySaturateExprUnionMember5ExprUnionMember7ExprUnionMember1",
    "RankBySaturateExprUnionMember5ExprUnionMember8",
    "RankBySaturateExprUnionMember5ExprUnionMember8Expr",
    "RankBySaturateExprUnionMember5ExprUnionMember8ExprUnionMember0",
    "RankBySaturateExprUnionMember5ExprUnionMember8ExprUnionMember1",
    "RankBySaturateExprUnionMember6",
    "RankBySaturateExprUnionMember6Expr",
    "RankBySaturateExprUnionMember6ExprUnionMember0",
    "RankBySaturateExprUnionMember6ExprUnionMember1",
    "RankBySaturateExprUnionMember6ExprUnionMember2",
    "RankBySaturateExprUnionMember6ExprUnionMember2Expr",
    "RankBySaturateExprUnionMember6ExprUnionMember2ExprUnionMember0",
    "RankBySaturateExprUnionMember6ExprUnionMember2ExprUnionMember1",
    "RankBySaturateExprUnionMember6ExprUnionMember3",
    "RankBySaturateExprUnionMember6ExprUnionMember4",
    "RankBySaturateExprUnionMember6ExprUnionMember5",
    "RankBySaturateExprUnionMember6ExprUnionMember5Expr",
    "RankBySaturateExprUnionMember6ExprUnionMember5ExprUnionMember0",
    "RankBySaturateExprUnionMember6ExprUnionMember5ExprUnionMember1",
    "RankBySaturateExprUnionMember6ExprUnionMember6",
    "RankBySaturateExprUnionMember6ExprUnionMember6Expr",
    "RankBySaturateExprUnionMember6ExprUnionMember6ExprUnionMember0",
    "RankBySaturateExprUnionMember6ExprUnionMember6ExprUnionMember1",
    "RankBySaturateExprUnionMember6ExprUnionMember7",
    "RankBySaturateExprUnionMember6ExprUnionMember7Expr",
    "RankBySaturateExprUnionMember6ExprUnionMember7ExprUnionMember0",
    "RankBySaturateExprUnionMember6ExprUnionMember7ExprUnionMember1",
    "RankBySaturateExprUnionMember6ExprUnionMember8",
    "RankBySaturateExprUnionMember6ExprUnionMember8Expr",
    "RankBySaturateExprUnionMember6ExprUnionMember8ExprUnionMember0",
    "RankBySaturateExprUnionMember6ExprUnionMember8ExprUnionMember1",
    "RankBySaturateExprUnionMember7",
    "RankBySaturateExprUnionMember7Expr",
    "RankBySaturateExprUnionMember7ExprUnionMember0",
    "RankBySaturateExprUnionMember7ExprUnionMember1",
    "RankBySaturateExprUnionMember7ExprUnionMember2",
    "RankBySaturateExprUnionMember7ExprUnionMember2Expr",
    "RankBySaturateExprUnionMember7ExprUnionMember2ExprUnionMember0",
    "RankBySaturateExprUnionMember7ExprUnionMember2ExprUnionMember1",
    "RankBySaturateExprUnionMember7ExprUnionMember3",
    "RankBySaturateExprUnionMember7ExprUnionMember4",
    "RankBySaturateExprUnionMember7ExprUnionMember5",
    "RankBySaturateExprUnionMember7ExprUnionMember5Expr",
    "RankBySaturateExprUnionMember7ExprUnionMember5ExprUnionMember0",
    "RankBySaturateExprUnionMember7ExprUnionMember5ExprUnionMember1",
    "RankBySaturateExprUnionMember7ExprUnionMember6",
    "RankBySaturateExprUnionMember7ExprUnionMember6Expr",
    "RankBySaturateExprUnionMember7ExprUnionMember6ExprUnionMember0",
    "RankBySaturateExprUnionMember7ExprUnionMember6ExprUnionMember1",
    "RankBySaturateExprUnionMember7ExprUnionMember7",
    "RankBySaturateExprUnionMember7ExprUnionMember7Expr",
    "RankBySaturateExprUnionMember7ExprUnionMember7ExprUnionMember0",
    "RankBySaturateExprUnionMember7ExprUnionMember7ExprUnionMember1",
    "RankBySaturateExprUnionMember7ExprUnionMember8",
    "RankBySaturateExprUnionMember7ExprUnionMember8Expr",
    "RankBySaturateExprUnionMember7ExprUnionMember8ExprUnionMember0",
    "RankBySaturateExprUnionMember7ExprUnionMember8ExprUnionMember1",
    "RankBySaturateExprUnionMember8",
    "RankBySaturateExprUnionMember8Expr",
    "RankBySaturateExprUnionMember8ExprUnionMember0",
    "RankBySaturateExprUnionMember8ExprUnionMember1",
    "RankBySaturateExprUnionMember8ExprUnionMember2",
    "RankBySaturateExprUnionMember8ExprUnionMember2Expr",
    "RankBySaturateExprUnionMember8ExprUnionMember2ExprUnionMember0",
    "RankBySaturateExprUnionMember8ExprUnionMember2ExprUnionMember1",
    "RankBySaturateExprUnionMember8ExprUnionMember3",
    "RankBySaturateExprUnionMember8ExprUnionMember4",
    "RankBySaturateExprUnionMember8ExprUnionMember5",
    "RankBySaturateExprUnionMember8ExprUnionMember5Expr",
    "RankBySaturateExprUnionMember8ExprUnionMember5ExprUnionMember0",
    "RankBySaturateExprUnionMember8ExprUnionMember5ExprUnionMember1",
    "RankBySaturateExprUnionMember8ExprUnionMember6",
    "RankBySaturateExprUnionMember8ExprUnionMember6Expr",
    "RankBySaturateExprUnionMember8ExprUnionMember6ExprUnionMember0",
    "RankBySaturateExprUnionMember8ExprUnionMember6ExprUnionMember1",
    "RankBySaturateExprUnionMember8ExprUnionMember7",
    "RankBySaturateExprUnionMember8ExprUnionMember7Expr",
    "RankBySaturateExprUnionMember8ExprUnionMember7ExprUnionMember0",
    "RankBySaturateExprUnionMember8ExprUnionMember7ExprUnionMember1",
    "RankBySaturateExprUnionMember8ExprUnionMember8",
    "RankBySaturateExprUnionMember8ExprUnionMember8Expr",
    "RankBySaturateExprUnionMember8ExprUnionMember8ExprUnionMember0",
    "RankBySaturateExprUnionMember8ExprUnionMember8ExprUnionMember1",
]


class SearchRepoNaturalLanguageParams(TypedDict, total=False):
    query: Required[str]
    """Natural language query describing the repositories you want to find"""

    after: str
    """Cursor for pagination (from previous response pageInfo.endCursor)"""

    apply_filters_to_include_attributes: Annotated[bool, PropertyInfo(alias="applyFiltersToIncludeAttributes")]
    """
    When true, applies the LLM-generated filter to all user-returning
    includeAttributes (contributors, starrers). Alias for
    filterUserIncludeAttributes.
    """

    enable_pagination: Annotated[bool, PropertyInfo(alias="enablePagination")]
    """Enable cursor-based pagination to fetch results across multiple requests"""

    filter_user_include_attributes: Annotated[bool, PropertyInfo(alias="filterUserIncludeAttributes")]
    """
    [Deprecated: Use applyFiltersToIncludeAttributes] When true, applies the
    LLM-generated filter to all user-returning includeAttributes (contributors,
    starrers).
    """

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


class RankBySumExprUnionMember2ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankBySumExprUnionMember2ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

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


class RankBySumExprUnionMember2ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember2ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember2ExprUnionMember8Expr: TypeAlias = Union[
    RankBySumExprUnionMember2ExprUnionMember8ExprUnionMember0, RankBySumExprUnionMember2ExprUnionMember8ExprUnionMember1
]


class RankBySumExprUnionMember2ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankBySumExprUnionMember2ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankBySumExprUnionMember2Expr: TypeAlias = Union[
    RankBySumExprUnionMember2ExprUnionMember0,
    RankBySumExprUnionMember2ExprUnionMember1,
    RankBySumExprUnionMember2ExprUnionMember2,
    RankBySumExprUnionMember2ExprUnionMember3,
    RankBySumExprUnionMember2ExprUnionMember4,
    RankBySumExprUnionMember2ExprUnionMember5,
    RankBySumExprUnionMember2ExprUnionMember6,
    RankBySumExprUnionMember2ExprUnionMember7,
    RankBySumExprUnionMember2ExprUnionMember8,
]


class RankBySumExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankBySumExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankBySumExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

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


class RankBySumExprUnionMember5ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankBySumExprUnionMember5ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

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


class RankBySumExprUnionMember5ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember5ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember5ExprUnionMember8Expr: TypeAlias = Union[
    RankBySumExprUnionMember5ExprUnionMember8ExprUnionMember0, RankBySumExprUnionMember5ExprUnionMember8ExprUnionMember1
]


class RankBySumExprUnionMember5ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankBySumExprUnionMember5ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankBySumExprUnionMember5Expr: TypeAlias = Union[
    RankBySumExprUnionMember5ExprUnionMember0,
    RankBySumExprUnionMember5ExprUnionMember1,
    RankBySumExprUnionMember5ExprUnionMember2,
    RankBySumExprUnionMember5ExprUnionMember3,
    RankBySumExprUnionMember5ExprUnionMember4,
    RankBySumExprUnionMember5ExprUnionMember5,
    RankBySumExprUnionMember5ExprUnionMember6,
    RankBySumExprUnionMember5ExprUnionMember7,
    RankBySumExprUnionMember5ExprUnionMember8,
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


class RankBySumExprUnionMember6ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankBySumExprUnionMember6ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

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


class RankBySumExprUnionMember6ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember6ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember6ExprUnionMember8Expr: TypeAlias = Union[
    RankBySumExprUnionMember6ExprUnionMember8ExprUnionMember0, RankBySumExprUnionMember6ExprUnionMember8ExprUnionMember1
]


class RankBySumExprUnionMember6ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankBySumExprUnionMember6ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankBySumExprUnionMember6Expr: TypeAlias = Union[
    RankBySumExprUnionMember6ExprUnionMember0,
    RankBySumExprUnionMember6ExprUnionMember1,
    RankBySumExprUnionMember6ExprUnionMember2,
    RankBySumExprUnionMember6ExprUnionMember3,
    RankBySumExprUnionMember6ExprUnionMember4,
    RankBySumExprUnionMember6ExprUnionMember5,
    RankBySumExprUnionMember6ExprUnionMember6,
    RankBySumExprUnionMember6ExprUnionMember7,
    RankBySumExprUnionMember6ExprUnionMember8,
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


class RankBySumExprUnionMember7ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankBySumExprUnionMember7ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

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


class RankBySumExprUnionMember7ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember7ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember7ExprUnionMember8Expr: TypeAlias = Union[
    RankBySumExprUnionMember7ExprUnionMember8ExprUnionMember0, RankBySumExprUnionMember7ExprUnionMember8ExprUnionMember1
]


class RankBySumExprUnionMember7ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankBySumExprUnionMember7ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankBySumExprUnionMember7Expr: TypeAlias = Union[
    RankBySumExprUnionMember7ExprUnionMember0,
    RankBySumExprUnionMember7ExprUnionMember1,
    RankBySumExprUnionMember7ExprUnionMember2,
    RankBySumExprUnionMember7ExprUnionMember3,
    RankBySumExprUnionMember7ExprUnionMember4,
    RankBySumExprUnionMember7ExprUnionMember5,
    RankBySumExprUnionMember7ExprUnionMember6,
    RankBySumExprUnionMember7ExprUnionMember7,
    RankBySumExprUnionMember7ExprUnionMember8,
]


class RankBySumExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankBySumExprUnionMember7Expr]

    type: Required[Literal["Log"]]


class RankBySumExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankBySumExprUnionMember8ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember8ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember8ExprUnionMember2Expr: TypeAlias = Union[
    RankBySumExprUnionMember8ExprUnionMember2ExprUnionMember0, RankBySumExprUnionMember8ExprUnionMember2ExprUnionMember1
]


class RankBySumExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember8ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankBySumExprUnionMember8ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankBySumExprUnionMember8ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankBySumExprUnionMember8ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember8ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember8ExprUnionMember5Expr: TypeAlias = Union[
    RankBySumExprUnionMember8ExprUnionMember5ExprUnionMember0, RankBySumExprUnionMember8ExprUnionMember5ExprUnionMember1
]


class RankBySumExprUnionMember8ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember8ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankBySumExprUnionMember8ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember8ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember8ExprUnionMember6Expr: TypeAlias = Union[
    RankBySumExprUnionMember8ExprUnionMember6ExprUnionMember0, RankBySumExprUnionMember8ExprUnionMember6ExprUnionMember1
]


class RankBySumExprUnionMember8ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExprUnionMember8ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankBySumExprUnionMember8ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember8ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember8ExprUnionMember7Expr: TypeAlias = Union[
    RankBySumExprUnionMember8ExprUnionMember7ExprUnionMember0, RankBySumExprUnionMember8ExprUnionMember7ExprUnionMember1
]


class RankBySumExprUnionMember8ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankBySumExprUnionMember8ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


class RankBySumExprUnionMember8ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySumExprUnionMember8ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySumExprUnionMember8ExprUnionMember8Expr: TypeAlias = Union[
    RankBySumExprUnionMember8ExprUnionMember8ExprUnionMember0, RankBySumExprUnionMember8ExprUnionMember8ExprUnionMember1
]


class RankBySumExprUnionMember8ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankBySumExprUnionMember8ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankBySumExprUnionMember8Expr: TypeAlias = Union[
    RankBySumExprUnionMember8ExprUnionMember0,
    RankBySumExprUnionMember8ExprUnionMember1,
    RankBySumExprUnionMember8ExprUnionMember2,
    RankBySumExprUnionMember8ExprUnionMember3,
    RankBySumExprUnionMember8ExprUnionMember4,
    RankBySumExprUnionMember8ExprUnionMember5,
    RankBySumExprUnionMember8ExprUnionMember6,
    RankBySumExprUnionMember8ExprUnionMember7,
    RankBySumExprUnionMember8ExprUnionMember8,
]


class RankBySumExprUnionMember8(TypedDict, total=False):
    expr: Required[RankBySumExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankBySumExpr: TypeAlias = Union[
    RankBySumExprUnionMember0,
    RankBySumExprUnionMember1,
    RankBySumExprUnionMember2,
    RankBySumExprUnionMember3,
    RankBySumExprUnionMember4,
    RankBySumExprUnionMember5,
    RankBySumExprUnionMember6,
    RankBySumExprUnionMember7,
    RankBySumExprUnionMember8,
]


class RankBySum(TypedDict, total=False):
    exprs: Required[Iterable[RankBySumExpr]]

    type: Required[Literal["Sum"]]


class RankByMult(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByDiv(TypedDict, total=False):
    exprs: Required[Iterable[object]]

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


class RankByMaxExprUnionMember2ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByMaxExprUnionMember2ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

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


class RankByMaxExprUnionMember2ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember2ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember2ExprUnionMember8Expr: TypeAlias = Union[
    RankByMaxExprUnionMember2ExprUnionMember8ExprUnionMember0, RankByMaxExprUnionMember2ExprUnionMember8ExprUnionMember1
]


class RankByMaxExprUnionMember2ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankByMaxExprUnionMember2ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByMaxExprUnionMember2Expr: TypeAlias = Union[
    RankByMaxExprUnionMember2ExprUnionMember0,
    RankByMaxExprUnionMember2ExprUnionMember1,
    RankByMaxExprUnionMember2ExprUnionMember2,
    RankByMaxExprUnionMember2ExprUnionMember3,
    RankByMaxExprUnionMember2ExprUnionMember4,
    RankByMaxExprUnionMember2ExprUnionMember5,
    RankByMaxExprUnionMember2ExprUnionMember6,
    RankByMaxExprUnionMember2ExprUnionMember7,
    RankByMaxExprUnionMember2ExprUnionMember8,
]


class RankByMaxExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMaxExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByMaxExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

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


class RankByMaxExprUnionMember5ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByMaxExprUnionMember5ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

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


class RankByMaxExprUnionMember5ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember5ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember5ExprUnionMember8Expr: TypeAlias = Union[
    RankByMaxExprUnionMember5ExprUnionMember8ExprUnionMember0, RankByMaxExprUnionMember5ExprUnionMember8ExprUnionMember1
]


class RankByMaxExprUnionMember5ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankByMaxExprUnionMember5ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByMaxExprUnionMember5Expr: TypeAlias = Union[
    RankByMaxExprUnionMember5ExprUnionMember0,
    RankByMaxExprUnionMember5ExprUnionMember1,
    RankByMaxExprUnionMember5ExprUnionMember2,
    RankByMaxExprUnionMember5ExprUnionMember3,
    RankByMaxExprUnionMember5ExprUnionMember4,
    RankByMaxExprUnionMember5ExprUnionMember5,
    RankByMaxExprUnionMember5ExprUnionMember6,
    RankByMaxExprUnionMember5ExprUnionMember7,
    RankByMaxExprUnionMember5ExprUnionMember8,
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


class RankByMaxExprUnionMember6ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByMaxExprUnionMember6ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

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


class RankByMaxExprUnionMember6ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember6ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember6ExprUnionMember8Expr: TypeAlias = Union[
    RankByMaxExprUnionMember6ExprUnionMember8ExprUnionMember0, RankByMaxExprUnionMember6ExprUnionMember8ExprUnionMember1
]


class RankByMaxExprUnionMember6ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankByMaxExprUnionMember6ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByMaxExprUnionMember6Expr: TypeAlias = Union[
    RankByMaxExprUnionMember6ExprUnionMember0,
    RankByMaxExprUnionMember6ExprUnionMember1,
    RankByMaxExprUnionMember6ExprUnionMember2,
    RankByMaxExprUnionMember6ExprUnionMember3,
    RankByMaxExprUnionMember6ExprUnionMember4,
    RankByMaxExprUnionMember6ExprUnionMember5,
    RankByMaxExprUnionMember6ExprUnionMember6,
    RankByMaxExprUnionMember6ExprUnionMember7,
    RankByMaxExprUnionMember6ExprUnionMember8,
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


class RankByMaxExprUnionMember7ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByMaxExprUnionMember7ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

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


class RankByMaxExprUnionMember7ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember7ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember7ExprUnionMember8Expr: TypeAlias = Union[
    RankByMaxExprUnionMember7ExprUnionMember8ExprUnionMember0, RankByMaxExprUnionMember7ExprUnionMember8ExprUnionMember1
]


class RankByMaxExprUnionMember7ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankByMaxExprUnionMember7ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByMaxExprUnionMember7Expr: TypeAlias = Union[
    RankByMaxExprUnionMember7ExprUnionMember0,
    RankByMaxExprUnionMember7ExprUnionMember1,
    RankByMaxExprUnionMember7ExprUnionMember2,
    RankByMaxExprUnionMember7ExprUnionMember3,
    RankByMaxExprUnionMember7ExprUnionMember4,
    RankByMaxExprUnionMember7ExprUnionMember5,
    RankByMaxExprUnionMember7ExprUnionMember6,
    RankByMaxExprUnionMember7ExprUnionMember7,
    RankByMaxExprUnionMember7ExprUnionMember8,
]


class RankByMaxExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMaxExprUnionMember7Expr]

    type: Required[Literal["Log"]]


class RankByMaxExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByMaxExprUnionMember8ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember8ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember8ExprUnionMember2Expr: TypeAlias = Union[
    RankByMaxExprUnionMember8ExprUnionMember2ExprUnionMember0, RankByMaxExprUnionMember8ExprUnionMember2ExprUnionMember1
]


class RankByMaxExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember8ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMaxExprUnionMember8ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByMaxExprUnionMember8ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByMaxExprUnionMember8ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember8ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember8ExprUnionMember5Expr: TypeAlias = Union[
    RankByMaxExprUnionMember8ExprUnionMember5ExprUnionMember0, RankByMaxExprUnionMember8ExprUnionMember5ExprUnionMember1
]


class RankByMaxExprUnionMember8ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember8ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByMaxExprUnionMember8ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember8ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember8ExprUnionMember6Expr: TypeAlias = Union[
    RankByMaxExprUnionMember8ExprUnionMember6ExprUnionMember0, RankByMaxExprUnionMember8ExprUnionMember6ExprUnionMember1
]


class RankByMaxExprUnionMember8ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByMaxExprUnionMember8ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByMaxExprUnionMember8ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember8ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember8ExprUnionMember7Expr: TypeAlias = Union[
    RankByMaxExprUnionMember8ExprUnionMember7ExprUnionMember0, RankByMaxExprUnionMember8ExprUnionMember7ExprUnionMember1
]


class RankByMaxExprUnionMember8ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMaxExprUnionMember8ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


class RankByMaxExprUnionMember8ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMaxExprUnionMember8ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMaxExprUnionMember8ExprUnionMember8Expr: TypeAlias = Union[
    RankByMaxExprUnionMember8ExprUnionMember8ExprUnionMember0, RankByMaxExprUnionMember8ExprUnionMember8ExprUnionMember1
]


class RankByMaxExprUnionMember8ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankByMaxExprUnionMember8ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByMaxExprUnionMember8Expr: TypeAlias = Union[
    RankByMaxExprUnionMember8ExprUnionMember0,
    RankByMaxExprUnionMember8ExprUnionMember1,
    RankByMaxExprUnionMember8ExprUnionMember2,
    RankByMaxExprUnionMember8ExprUnionMember3,
    RankByMaxExprUnionMember8ExprUnionMember4,
    RankByMaxExprUnionMember8ExprUnionMember5,
    RankByMaxExprUnionMember8ExprUnionMember6,
    RankByMaxExprUnionMember8ExprUnionMember7,
    RankByMaxExprUnionMember8ExprUnionMember8,
]


class RankByMaxExprUnionMember8(TypedDict, total=False):
    expr: Required[RankByMaxExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByMaxExpr: TypeAlias = Union[
    RankByMaxExprUnionMember0,
    RankByMaxExprUnionMember1,
    RankByMaxExprUnionMember2,
    RankByMaxExprUnionMember3,
    RankByMaxExprUnionMember4,
    RankByMaxExprUnionMember5,
    RankByMaxExprUnionMember6,
    RankByMaxExprUnionMember7,
    RankByMaxExprUnionMember8,
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


class RankByMinExprUnionMember2ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByMinExprUnionMember2ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

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


class RankByMinExprUnionMember2ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember2ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember2ExprUnionMember8Expr: TypeAlias = Union[
    RankByMinExprUnionMember2ExprUnionMember8ExprUnionMember0, RankByMinExprUnionMember2ExprUnionMember8ExprUnionMember1
]


class RankByMinExprUnionMember2ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankByMinExprUnionMember2ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByMinExprUnionMember2Expr: TypeAlias = Union[
    RankByMinExprUnionMember2ExprUnionMember0,
    RankByMinExprUnionMember2ExprUnionMember1,
    RankByMinExprUnionMember2ExprUnionMember2,
    RankByMinExprUnionMember2ExprUnionMember3,
    RankByMinExprUnionMember2ExprUnionMember4,
    RankByMinExprUnionMember2ExprUnionMember5,
    RankByMinExprUnionMember2ExprUnionMember6,
    RankByMinExprUnionMember2ExprUnionMember7,
    RankByMinExprUnionMember2ExprUnionMember8,
]


class RankByMinExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMinExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByMinExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

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


class RankByMinExprUnionMember5ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByMinExprUnionMember5ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

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


class RankByMinExprUnionMember5ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember5ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember5ExprUnionMember8Expr: TypeAlias = Union[
    RankByMinExprUnionMember5ExprUnionMember8ExprUnionMember0, RankByMinExprUnionMember5ExprUnionMember8ExprUnionMember1
]


class RankByMinExprUnionMember5ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankByMinExprUnionMember5ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByMinExprUnionMember5Expr: TypeAlias = Union[
    RankByMinExprUnionMember5ExprUnionMember0,
    RankByMinExprUnionMember5ExprUnionMember1,
    RankByMinExprUnionMember5ExprUnionMember2,
    RankByMinExprUnionMember5ExprUnionMember3,
    RankByMinExprUnionMember5ExprUnionMember4,
    RankByMinExprUnionMember5ExprUnionMember5,
    RankByMinExprUnionMember5ExprUnionMember6,
    RankByMinExprUnionMember5ExprUnionMember7,
    RankByMinExprUnionMember5ExprUnionMember8,
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


class RankByMinExprUnionMember6ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByMinExprUnionMember6ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

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


class RankByMinExprUnionMember6ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember6ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember6ExprUnionMember8Expr: TypeAlias = Union[
    RankByMinExprUnionMember6ExprUnionMember8ExprUnionMember0, RankByMinExprUnionMember6ExprUnionMember8ExprUnionMember1
]


class RankByMinExprUnionMember6ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankByMinExprUnionMember6ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByMinExprUnionMember6Expr: TypeAlias = Union[
    RankByMinExprUnionMember6ExprUnionMember0,
    RankByMinExprUnionMember6ExprUnionMember1,
    RankByMinExprUnionMember6ExprUnionMember2,
    RankByMinExprUnionMember6ExprUnionMember3,
    RankByMinExprUnionMember6ExprUnionMember4,
    RankByMinExprUnionMember6ExprUnionMember5,
    RankByMinExprUnionMember6ExprUnionMember6,
    RankByMinExprUnionMember6ExprUnionMember7,
    RankByMinExprUnionMember6ExprUnionMember8,
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


class RankByMinExprUnionMember7ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByMinExprUnionMember7ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

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


class RankByMinExprUnionMember7ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember7ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember7ExprUnionMember8Expr: TypeAlias = Union[
    RankByMinExprUnionMember7ExprUnionMember8ExprUnionMember0, RankByMinExprUnionMember7ExprUnionMember8ExprUnionMember1
]


class RankByMinExprUnionMember7ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankByMinExprUnionMember7ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByMinExprUnionMember7Expr: TypeAlias = Union[
    RankByMinExprUnionMember7ExprUnionMember0,
    RankByMinExprUnionMember7ExprUnionMember1,
    RankByMinExprUnionMember7ExprUnionMember2,
    RankByMinExprUnionMember7ExprUnionMember3,
    RankByMinExprUnionMember7ExprUnionMember4,
    RankByMinExprUnionMember7ExprUnionMember5,
    RankByMinExprUnionMember7ExprUnionMember6,
    RankByMinExprUnionMember7ExprUnionMember7,
    RankByMinExprUnionMember7ExprUnionMember8,
]


class RankByMinExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMinExprUnionMember7Expr]

    type: Required[Literal["Log"]]


class RankByMinExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByMinExprUnionMember8ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember8ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember8ExprUnionMember2Expr: TypeAlias = Union[
    RankByMinExprUnionMember8ExprUnionMember2ExprUnionMember0, RankByMinExprUnionMember8ExprUnionMember2ExprUnionMember1
]


class RankByMinExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember8ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByMinExprUnionMember8ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByMinExprUnionMember8ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByMinExprUnionMember8ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember8ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember8ExprUnionMember5Expr: TypeAlias = Union[
    RankByMinExprUnionMember8ExprUnionMember5ExprUnionMember0, RankByMinExprUnionMember8ExprUnionMember5ExprUnionMember1
]


class RankByMinExprUnionMember8ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember8ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByMinExprUnionMember8ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember8ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember8ExprUnionMember6Expr: TypeAlias = Union[
    RankByMinExprUnionMember8ExprUnionMember6ExprUnionMember0, RankByMinExprUnionMember8ExprUnionMember6ExprUnionMember1
]


class RankByMinExprUnionMember8ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByMinExprUnionMember8ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByMinExprUnionMember8ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember8ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember8ExprUnionMember7Expr: TypeAlias = Union[
    RankByMinExprUnionMember8ExprUnionMember7ExprUnionMember0, RankByMinExprUnionMember8ExprUnionMember7ExprUnionMember1
]


class RankByMinExprUnionMember8ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByMinExprUnionMember8ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


class RankByMinExprUnionMember8ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByMinExprUnionMember8ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByMinExprUnionMember8ExprUnionMember8Expr: TypeAlias = Union[
    RankByMinExprUnionMember8ExprUnionMember8ExprUnionMember0, RankByMinExprUnionMember8ExprUnionMember8ExprUnionMember1
]


class RankByMinExprUnionMember8ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankByMinExprUnionMember8ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByMinExprUnionMember8Expr: TypeAlias = Union[
    RankByMinExprUnionMember8ExprUnionMember0,
    RankByMinExprUnionMember8ExprUnionMember1,
    RankByMinExprUnionMember8ExprUnionMember2,
    RankByMinExprUnionMember8ExprUnionMember3,
    RankByMinExprUnionMember8ExprUnionMember4,
    RankByMinExprUnionMember8ExprUnionMember5,
    RankByMinExprUnionMember8ExprUnionMember6,
    RankByMinExprUnionMember8ExprUnionMember7,
    RankByMinExprUnionMember8ExprUnionMember8,
]


class RankByMinExprUnionMember8(TypedDict, total=False):
    expr: Required[RankByMinExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByMinExpr: TypeAlias = Union[
    RankByMinExprUnionMember0,
    RankByMinExprUnionMember1,
    RankByMinExprUnionMember2,
    RankByMinExprUnionMember3,
    RankByMinExprUnionMember4,
    RankByMinExprUnionMember5,
    RankByMinExprUnionMember6,
    RankByMinExprUnionMember7,
    RankByMinExprUnionMember8,
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


class RankByLogExprUnionMember2ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByLogExprUnionMember2ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

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


class RankByLogExprUnionMember2ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember2ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember2ExprUnionMember8Expr: TypeAlias = Union[
    RankByLogExprUnionMember2ExprUnionMember8ExprUnionMember0, RankByLogExprUnionMember2ExprUnionMember8ExprUnionMember1
]


class RankByLogExprUnionMember2ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankByLogExprUnionMember2ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByLogExprUnionMember2Expr: TypeAlias = Union[
    RankByLogExprUnionMember2ExprUnionMember0,
    RankByLogExprUnionMember2ExprUnionMember1,
    RankByLogExprUnionMember2ExprUnionMember2,
    RankByLogExprUnionMember2ExprUnionMember3,
    RankByLogExprUnionMember2ExprUnionMember4,
    RankByLogExprUnionMember2ExprUnionMember5,
    RankByLogExprUnionMember2ExprUnionMember6,
    RankByLogExprUnionMember2ExprUnionMember7,
    RankByLogExprUnionMember2ExprUnionMember8,
]


class RankByLogExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByLogExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByLogExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

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


class RankByLogExprUnionMember5ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByLogExprUnionMember5ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

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


class RankByLogExprUnionMember5ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember5ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember5ExprUnionMember8Expr: TypeAlias = Union[
    RankByLogExprUnionMember5ExprUnionMember8ExprUnionMember0, RankByLogExprUnionMember5ExprUnionMember8ExprUnionMember1
]


class RankByLogExprUnionMember5ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankByLogExprUnionMember5ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByLogExprUnionMember5Expr: TypeAlias = Union[
    RankByLogExprUnionMember5ExprUnionMember0,
    RankByLogExprUnionMember5ExprUnionMember1,
    RankByLogExprUnionMember5ExprUnionMember2,
    RankByLogExprUnionMember5ExprUnionMember3,
    RankByLogExprUnionMember5ExprUnionMember4,
    RankByLogExprUnionMember5ExprUnionMember5,
    RankByLogExprUnionMember5ExprUnionMember6,
    RankByLogExprUnionMember5ExprUnionMember7,
    RankByLogExprUnionMember5ExprUnionMember8,
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


class RankByLogExprUnionMember6ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByLogExprUnionMember6ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

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


class RankByLogExprUnionMember6ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember6ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember6ExprUnionMember8Expr: TypeAlias = Union[
    RankByLogExprUnionMember6ExprUnionMember8ExprUnionMember0, RankByLogExprUnionMember6ExprUnionMember8ExprUnionMember1
]


class RankByLogExprUnionMember6ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankByLogExprUnionMember6ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByLogExprUnionMember6Expr: TypeAlias = Union[
    RankByLogExprUnionMember6ExprUnionMember0,
    RankByLogExprUnionMember6ExprUnionMember1,
    RankByLogExprUnionMember6ExprUnionMember2,
    RankByLogExprUnionMember6ExprUnionMember3,
    RankByLogExprUnionMember6ExprUnionMember4,
    RankByLogExprUnionMember6ExprUnionMember5,
    RankByLogExprUnionMember6ExprUnionMember6,
    RankByLogExprUnionMember6ExprUnionMember7,
    RankByLogExprUnionMember6ExprUnionMember8,
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


class RankByLogExprUnionMember7ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByLogExprUnionMember7ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

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


class RankByLogExprUnionMember7ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember7ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember7ExprUnionMember8Expr: TypeAlias = Union[
    RankByLogExprUnionMember7ExprUnionMember8ExprUnionMember0, RankByLogExprUnionMember7ExprUnionMember8ExprUnionMember1
]


class RankByLogExprUnionMember7ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankByLogExprUnionMember7ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByLogExprUnionMember7Expr: TypeAlias = Union[
    RankByLogExprUnionMember7ExprUnionMember0,
    RankByLogExprUnionMember7ExprUnionMember1,
    RankByLogExprUnionMember7ExprUnionMember2,
    RankByLogExprUnionMember7ExprUnionMember3,
    RankByLogExprUnionMember7ExprUnionMember4,
    RankByLogExprUnionMember7ExprUnionMember5,
    RankByLogExprUnionMember7ExprUnionMember6,
    RankByLogExprUnionMember7ExprUnionMember7,
    RankByLogExprUnionMember7ExprUnionMember8,
]


class RankByLogExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByLogExprUnionMember7Expr]

    type: Required[Literal["Log"]]


class RankByLogExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankByLogExprUnionMember8ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember8ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember8ExprUnionMember2Expr: TypeAlias = Union[
    RankByLogExprUnionMember8ExprUnionMember2ExprUnionMember0, RankByLogExprUnionMember8ExprUnionMember2ExprUnionMember1
]


class RankByLogExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember8ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankByLogExprUnionMember8ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankByLogExprUnionMember8ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankByLogExprUnionMember8ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember8ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember8ExprUnionMember5Expr: TypeAlias = Union[
    RankByLogExprUnionMember8ExprUnionMember5ExprUnionMember0, RankByLogExprUnionMember8ExprUnionMember5ExprUnionMember1
]


class RankByLogExprUnionMember8ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember8ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankByLogExprUnionMember8ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember8ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember8ExprUnionMember6Expr: TypeAlias = Union[
    RankByLogExprUnionMember8ExprUnionMember6ExprUnionMember0, RankByLogExprUnionMember8ExprUnionMember6ExprUnionMember1
]


class RankByLogExprUnionMember8ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankByLogExprUnionMember8ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankByLogExprUnionMember8ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember8ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember8ExprUnionMember7Expr: TypeAlias = Union[
    RankByLogExprUnionMember8ExprUnionMember7ExprUnionMember0, RankByLogExprUnionMember8ExprUnionMember7ExprUnionMember1
]


class RankByLogExprUnionMember8ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByLogExprUnionMember8ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


class RankByLogExprUnionMember8ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankByLogExprUnionMember8ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankByLogExprUnionMember8ExprUnionMember8Expr: TypeAlias = Union[
    RankByLogExprUnionMember8ExprUnionMember8ExprUnionMember0, RankByLogExprUnionMember8ExprUnionMember8ExprUnionMember1
]


class RankByLogExprUnionMember8ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankByLogExprUnionMember8ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByLogExprUnionMember8Expr: TypeAlias = Union[
    RankByLogExprUnionMember8ExprUnionMember0,
    RankByLogExprUnionMember8ExprUnionMember1,
    RankByLogExprUnionMember8ExprUnionMember2,
    RankByLogExprUnionMember8ExprUnionMember3,
    RankByLogExprUnionMember8ExprUnionMember4,
    RankByLogExprUnionMember8ExprUnionMember5,
    RankByLogExprUnionMember8ExprUnionMember6,
    RankByLogExprUnionMember8ExprUnionMember7,
    RankByLogExprUnionMember8ExprUnionMember8,
]


class RankByLogExprUnionMember8(TypedDict, total=False):
    expr: Required[RankByLogExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankByLogExpr: TypeAlias = Union[
    RankByLogExprUnionMember0,
    RankByLogExprUnionMember1,
    RankByLogExprUnionMember2,
    RankByLogExprUnionMember3,
    RankByLogExprUnionMember4,
    RankByLogExprUnionMember5,
    RankByLogExprUnionMember6,
    RankByLogExprUnionMember7,
    RankByLogExprUnionMember8,
]


class RankByLog(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankByLogExpr]

    type: Required[Literal["Log"]]


class RankBySaturateExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankBySaturateExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankBySaturateExprUnionMember2ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember2ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember2ExprUnionMember2Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember2ExprUnionMember2ExprUnionMember0,
    RankBySaturateExprUnionMember2ExprUnionMember2ExprUnionMember1,
]


class RankBySaturateExprUnionMember2ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankBySaturateExprUnionMember2ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankBySaturateExprUnionMember2ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankBySaturateExprUnionMember2ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankBySaturateExprUnionMember2ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember2ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember2ExprUnionMember5Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember2ExprUnionMember5ExprUnionMember0,
    RankBySaturateExprUnionMember2ExprUnionMember5ExprUnionMember1,
]


class RankBySaturateExprUnionMember2ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankBySaturateExprUnionMember2ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankBySaturateExprUnionMember2ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember2ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember2ExprUnionMember6Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember2ExprUnionMember6ExprUnionMember0,
    RankBySaturateExprUnionMember2ExprUnionMember6ExprUnionMember1,
]


class RankBySaturateExprUnionMember2ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankBySaturateExprUnionMember2ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankBySaturateExprUnionMember2ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember2ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember2ExprUnionMember7Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember2ExprUnionMember7ExprUnionMember0,
    RankBySaturateExprUnionMember2ExprUnionMember7ExprUnionMember1,
]


class RankBySaturateExprUnionMember2ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankBySaturateExprUnionMember2ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


class RankBySaturateExprUnionMember2ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember2ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember2ExprUnionMember8Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember2ExprUnionMember8ExprUnionMember0,
    RankBySaturateExprUnionMember2ExprUnionMember8ExprUnionMember1,
]


class RankBySaturateExprUnionMember2ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankBySaturateExprUnionMember2ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankBySaturateExprUnionMember2Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember2ExprUnionMember0,
    RankBySaturateExprUnionMember2ExprUnionMember1,
    RankBySaturateExprUnionMember2ExprUnionMember2,
    RankBySaturateExprUnionMember2ExprUnionMember3,
    RankBySaturateExprUnionMember2ExprUnionMember4,
    RankBySaturateExprUnionMember2ExprUnionMember5,
    RankBySaturateExprUnionMember2ExprUnionMember6,
    RankBySaturateExprUnionMember2ExprUnionMember7,
    RankBySaturateExprUnionMember2ExprUnionMember8,
]


class RankBySaturateExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankBySaturateExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankBySaturateExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankBySaturateExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankBySaturateExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankBySaturateExprUnionMember5ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember5ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember5ExprUnionMember2Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember5ExprUnionMember2ExprUnionMember0,
    RankBySaturateExprUnionMember5ExprUnionMember2ExprUnionMember1,
]


class RankBySaturateExprUnionMember5ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankBySaturateExprUnionMember5ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankBySaturateExprUnionMember5ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankBySaturateExprUnionMember5ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankBySaturateExprUnionMember5ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember5ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember5ExprUnionMember5Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember5ExprUnionMember5ExprUnionMember0,
    RankBySaturateExprUnionMember5ExprUnionMember5ExprUnionMember1,
]


class RankBySaturateExprUnionMember5ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankBySaturateExprUnionMember5ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankBySaturateExprUnionMember5ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember5ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember5ExprUnionMember6Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember5ExprUnionMember6ExprUnionMember0,
    RankBySaturateExprUnionMember5ExprUnionMember6ExprUnionMember1,
]


class RankBySaturateExprUnionMember5ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankBySaturateExprUnionMember5ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankBySaturateExprUnionMember5ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember5ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember5ExprUnionMember7Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember5ExprUnionMember7ExprUnionMember0,
    RankBySaturateExprUnionMember5ExprUnionMember7ExprUnionMember1,
]


class RankBySaturateExprUnionMember5ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankBySaturateExprUnionMember5ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


class RankBySaturateExprUnionMember5ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember5ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember5ExprUnionMember8Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember5ExprUnionMember8ExprUnionMember0,
    RankBySaturateExprUnionMember5ExprUnionMember8ExprUnionMember1,
]


class RankBySaturateExprUnionMember5ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankBySaturateExprUnionMember5ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankBySaturateExprUnionMember5Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember5ExprUnionMember0,
    RankBySaturateExprUnionMember5ExprUnionMember1,
    RankBySaturateExprUnionMember5ExprUnionMember2,
    RankBySaturateExprUnionMember5ExprUnionMember3,
    RankBySaturateExprUnionMember5ExprUnionMember4,
    RankBySaturateExprUnionMember5ExprUnionMember5,
    RankBySaturateExprUnionMember5ExprUnionMember6,
    RankBySaturateExprUnionMember5ExprUnionMember7,
    RankBySaturateExprUnionMember5ExprUnionMember8,
]


class RankBySaturateExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankBySaturateExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankBySaturateExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankBySaturateExprUnionMember6ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember6ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember6ExprUnionMember2Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember6ExprUnionMember2ExprUnionMember0,
    RankBySaturateExprUnionMember6ExprUnionMember2ExprUnionMember1,
]


class RankBySaturateExprUnionMember6ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankBySaturateExprUnionMember6ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankBySaturateExprUnionMember6ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankBySaturateExprUnionMember6ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankBySaturateExprUnionMember6ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember6ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember6ExprUnionMember5Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember6ExprUnionMember5ExprUnionMember0,
    RankBySaturateExprUnionMember6ExprUnionMember5ExprUnionMember1,
]


class RankBySaturateExprUnionMember6ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankBySaturateExprUnionMember6ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankBySaturateExprUnionMember6ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember6ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember6ExprUnionMember6Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember6ExprUnionMember6ExprUnionMember0,
    RankBySaturateExprUnionMember6ExprUnionMember6ExprUnionMember1,
]


class RankBySaturateExprUnionMember6ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankBySaturateExprUnionMember6ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankBySaturateExprUnionMember6ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember6ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember6ExprUnionMember7Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember6ExprUnionMember7ExprUnionMember0,
    RankBySaturateExprUnionMember6ExprUnionMember7ExprUnionMember1,
]


class RankBySaturateExprUnionMember6ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankBySaturateExprUnionMember6ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


class RankBySaturateExprUnionMember6ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember6ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember6ExprUnionMember8Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember6ExprUnionMember8ExprUnionMember0,
    RankBySaturateExprUnionMember6ExprUnionMember8ExprUnionMember1,
]


class RankBySaturateExprUnionMember6ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankBySaturateExprUnionMember6ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankBySaturateExprUnionMember6Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember6ExprUnionMember0,
    RankBySaturateExprUnionMember6ExprUnionMember1,
    RankBySaturateExprUnionMember6ExprUnionMember2,
    RankBySaturateExprUnionMember6ExprUnionMember3,
    RankBySaturateExprUnionMember6ExprUnionMember4,
    RankBySaturateExprUnionMember6ExprUnionMember5,
    RankBySaturateExprUnionMember6ExprUnionMember6,
    RankBySaturateExprUnionMember6ExprUnionMember7,
    RankBySaturateExprUnionMember6ExprUnionMember8,
]


class RankBySaturateExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankBySaturateExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankBySaturateExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankBySaturateExprUnionMember7ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember7ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember7ExprUnionMember2Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember7ExprUnionMember2ExprUnionMember0,
    RankBySaturateExprUnionMember7ExprUnionMember2ExprUnionMember1,
]


class RankBySaturateExprUnionMember7ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankBySaturateExprUnionMember7ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankBySaturateExprUnionMember7ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankBySaturateExprUnionMember7ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankBySaturateExprUnionMember7ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember7ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember7ExprUnionMember5Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember7ExprUnionMember5ExprUnionMember0,
    RankBySaturateExprUnionMember7ExprUnionMember5ExprUnionMember1,
]


class RankBySaturateExprUnionMember7ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankBySaturateExprUnionMember7ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankBySaturateExprUnionMember7ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember7ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember7ExprUnionMember6Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember7ExprUnionMember6ExprUnionMember0,
    RankBySaturateExprUnionMember7ExprUnionMember6ExprUnionMember1,
]


class RankBySaturateExprUnionMember7ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankBySaturateExprUnionMember7ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankBySaturateExprUnionMember7ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember7ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember7ExprUnionMember7Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember7ExprUnionMember7ExprUnionMember0,
    RankBySaturateExprUnionMember7ExprUnionMember7ExprUnionMember1,
]


class RankBySaturateExprUnionMember7ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankBySaturateExprUnionMember7ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


class RankBySaturateExprUnionMember7ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember7ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember7ExprUnionMember8Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember7ExprUnionMember8ExprUnionMember0,
    RankBySaturateExprUnionMember7ExprUnionMember8ExprUnionMember1,
]


class RankBySaturateExprUnionMember7ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankBySaturateExprUnionMember7ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankBySaturateExprUnionMember7Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember7ExprUnionMember0,
    RankBySaturateExprUnionMember7ExprUnionMember1,
    RankBySaturateExprUnionMember7ExprUnionMember2,
    RankBySaturateExprUnionMember7ExprUnionMember3,
    RankBySaturateExprUnionMember7ExprUnionMember4,
    RankBySaturateExprUnionMember7ExprUnionMember5,
    RankBySaturateExprUnionMember7ExprUnionMember6,
    RankBySaturateExprUnionMember7ExprUnionMember7,
    RankBySaturateExprUnionMember7ExprUnionMember8,
]


class RankBySaturateExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankBySaturateExprUnionMember7Expr]

    type: Required[Literal["Log"]]


class RankBySaturateExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


class RankBySaturateExprUnionMember8ExprUnionMember2ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember8ExprUnionMember2ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember8ExprUnionMember2Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember8ExprUnionMember2ExprUnionMember0,
    RankBySaturateExprUnionMember8ExprUnionMember2ExprUnionMember1,
]


class RankBySaturateExprUnionMember8ExprUnionMember2(TypedDict, total=False):
    exprs: Required[Iterable[RankBySaturateExprUnionMember8ExprUnionMember2Expr]]

    type: Required[Literal["Sum"]]


class RankBySaturateExprUnionMember8ExprUnionMember3(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Mult"]]


class RankBySaturateExprUnionMember8ExprUnionMember4(TypedDict, total=False):
    exprs: Required[Iterable[object]]

    type: Required[Literal["Div"]]


class RankBySaturateExprUnionMember8ExprUnionMember5ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember8ExprUnionMember5ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember8ExprUnionMember5Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember8ExprUnionMember5ExprUnionMember0,
    RankBySaturateExprUnionMember8ExprUnionMember5ExprUnionMember1,
]


class RankBySaturateExprUnionMember8ExprUnionMember5(TypedDict, total=False):
    exprs: Required[Iterable[RankBySaturateExprUnionMember8ExprUnionMember5Expr]]

    type: Required[Literal["Max"]]


class RankBySaturateExprUnionMember8ExprUnionMember6ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember8ExprUnionMember6ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember8ExprUnionMember6Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember8ExprUnionMember6ExprUnionMember0,
    RankBySaturateExprUnionMember8ExprUnionMember6ExprUnionMember1,
]


class RankBySaturateExprUnionMember8ExprUnionMember6(TypedDict, total=False):
    exprs: Required[Iterable[RankBySaturateExprUnionMember8ExprUnionMember6Expr]]

    type: Required[Literal["Min"]]


class RankBySaturateExprUnionMember8ExprUnionMember7ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember8ExprUnionMember7ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember8ExprUnionMember7Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember8ExprUnionMember7ExprUnionMember0,
    RankBySaturateExprUnionMember8ExprUnionMember7ExprUnionMember1,
]


class RankBySaturateExprUnionMember8ExprUnionMember7(TypedDict, total=False):
    base: Required[float]

    expr: Required[RankBySaturateExprUnionMember8ExprUnionMember7Expr]

    type: Required[Literal["Log"]]


class RankBySaturateExprUnionMember8ExprUnionMember8ExprUnionMember0(TypedDict, total=False):
    name: Required[Literal["ann", "stars", "issues_closed", "age", "recency"]]

    type: Required[Literal["Attr"]]


class RankBySaturateExprUnionMember8ExprUnionMember8ExprUnionMember1(TypedDict, total=False):
    type: Required[Literal["Const"]]

    value: Required[float]


RankBySaturateExprUnionMember8ExprUnionMember8Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember8ExprUnionMember8ExprUnionMember0,
    RankBySaturateExprUnionMember8ExprUnionMember8ExprUnionMember1,
]


class RankBySaturateExprUnionMember8ExprUnionMember8(TypedDict, total=False):
    expr: Required[RankBySaturateExprUnionMember8ExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankBySaturateExprUnionMember8Expr: TypeAlias = Union[
    RankBySaturateExprUnionMember8ExprUnionMember0,
    RankBySaturateExprUnionMember8ExprUnionMember1,
    RankBySaturateExprUnionMember8ExprUnionMember2,
    RankBySaturateExprUnionMember8ExprUnionMember3,
    RankBySaturateExprUnionMember8ExprUnionMember4,
    RankBySaturateExprUnionMember8ExprUnionMember5,
    RankBySaturateExprUnionMember8ExprUnionMember6,
    RankBySaturateExprUnionMember8ExprUnionMember7,
    RankBySaturateExprUnionMember8ExprUnionMember8,
]


class RankBySaturateExprUnionMember8(TypedDict, total=False):
    expr: Required[RankBySaturateExprUnionMember8Expr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankBySaturateExpr: TypeAlias = Union[
    RankBySaturateExprUnionMember0,
    RankBySaturateExprUnionMember1,
    RankBySaturateExprUnionMember2,
    RankBySaturateExprUnionMember3,
    RankBySaturateExprUnionMember4,
    RankBySaturateExprUnionMember5,
    RankBySaturateExprUnionMember6,
    RankBySaturateExprUnionMember7,
    RankBySaturateExprUnionMember8,
]


class RankBySaturate(TypedDict, total=False):
    expr: Required[RankBySaturateExpr]

    midpoint: Required[float]

    type: Required[Literal["Saturate"]]

    exponent: float


RankBy: TypeAlias = Union[
    RankByAttr, RankByConst, RankBySum, RankByMult, RankByDiv, RankByMax, RankByMin, RankByLog, RankBySaturate
]
