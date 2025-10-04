# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .. import _resource
from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.api_search_response import APISearchResponse
from ..types.api_retrieve_example_response import APIRetrieveExampleResponse
from ..types.api_retrieve_raw_data_response import APIRetrieveRawDataResponse

__all__ = ["APIResource", "AsyncAPIResource"]


class APIResource(_resource.SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> APIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bountylaboratories/python-sdk#accessing-raw-response-data-eg-headers
        """
        return APIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bountylaboratories/python-sdk#with_streaming_response
        """
        return APIResourceWithStreamingResponse(self)

    def retrieve_example(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIRetrieveExampleResponse:
        """Example endpoint that requires API key and logs credit consumption"""
        return self._get(
            "/api/example",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIRetrieveExampleResponse,
        )

    def retrieve_raw_data(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIRetrieveRawDataResponse:
        """Raw data endpoint that requires RAW service access"""
        return self._get(
            "/api/raw",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIRetrieveRawDataResponse,
        )

    def search(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APISearchResponse:
        """Search endpoint that requires SEARCH service access"""
        return self._get(
            "/api/search",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APISearchResponse,
        )


class AsyncAPIResource(_resource.AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAPIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/bountylaboratories/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/bountylaboratories/python-sdk#with_streaming_response
        """
        return AsyncAPIResourceWithStreamingResponse(self)

    async def retrieve_example(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIRetrieveExampleResponse:
        """Example endpoint that requires API key and logs credit consumption"""
        return await self._get(
            "/api/example",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIRetrieveExampleResponse,
        )

    async def retrieve_raw_data(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIRetrieveRawDataResponse:
        """Raw data endpoint that requires RAW service access"""
        return await self._get(
            "/api/raw",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIRetrieveRawDataResponse,
        )

    async def search(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APISearchResponse:
        """Search endpoint that requires SEARCH service access"""
        return await self._get(
            "/api/search",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APISearchResponse,
        )


class APIResourceWithRawResponse:
    def __init__(self, api: APIResource) -> None:
        self._api = api

        self.retrieve_example = to_raw_response_wrapper(
            api.retrieve_example,
        )
        self.retrieve_raw_data = to_raw_response_wrapper(
            api.retrieve_raw_data,
        )
        self.search = to_raw_response_wrapper(
            api.search,
        )


class AsyncAPIResourceWithRawResponse:
    def __init__(self, api: AsyncAPIResource) -> None:
        self._api = api

        self.retrieve_example = async_to_raw_response_wrapper(
            api.retrieve_example,
        )
        self.retrieve_raw_data = async_to_raw_response_wrapper(
            api.retrieve_raw_data,
        )
        self.search = async_to_raw_response_wrapper(
            api.search,
        )


class APIResourceWithStreamingResponse:
    def __init__(self, api: APIResource) -> None:
        self._api = api

        self.retrieve_example = to_streamed_response_wrapper(
            api.retrieve_example,
        )
        self.retrieve_raw_data = to_streamed_response_wrapper(
            api.retrieve_raw_data,
        )
        self.search = to_streamed_response_wrapper(
            api.search,
        )


class AsyncAPIResourceWithStreamingResponse:
    def __init__(self, api: AsyncAPIResource) -> None:
        self._api = api

        self.retrieve_example = async_to_streamed_response_wrapper(
            api.retrieve_example,
        )
        self.retrieve_raw_data = async_to_streamed_response_wrapper(
            api.retrieve_raw_data,
        )
        self.search = async_to_streamed_response_wrapper(
            api.search,
        )
