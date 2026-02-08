# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UserEmailBestEmailResponse", "Result"]


class Result(BaseModel):
    best_email: Optional[str] = FieldInfo(alias="bestEmail", default=None)
    """Best email address, or null if none available"""

    github_id: str = FieldInfo(alias="githubId")
    """GitHub node ID"""

    login: str
    """GitHub username"""

    other_candidates: List[str] = FieldInfo(alias="otherCandidates")
    """Deprecated. Always returns an empty array."""

    profile: Optional[Literal["WORK", "PERSONAL", "SCHOOL"]] = None
    """Whether the email is a work or personal address"""


class UserEmailBestEmailResponse(BaseModel):
    count: float
    """Number of results returned"""

    results: List[Result]
    """Array of best email results"""
