# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["APIRetrieveExampleResponse"]


class APIRetrieveExampleResponse(BaseModel):
    credits_used: Optional[float] = FieldInfo(alias="creditsUsed", default=None)

    message: Optional[str] = None
