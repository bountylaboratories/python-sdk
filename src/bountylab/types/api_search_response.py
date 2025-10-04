# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["APISearchResponse"]


class APISearchResponse(BaseModel):
    message: Optional[str] = None

    service: Optional[str] = None
