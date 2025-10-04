# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bountylab import Bountylab, AsyncBountylab
from tests.utils import assert_matches_type
from bountylab.types import APISearchResponse, APIRetrieveExampleResponse, APIRetrieveRawDataResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPI:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_example(self, client: Bountylab) -> None:
        api = client.api.retrieve_example()
        assert_matches_type(APIRetrieveExampleResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_example(self, client: Bountylab) -> None:
        response = client.api.with_raw_response.retrieve_example()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(APIRetrieveExampleResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_example(self, client: Bountylab) -> None:
        with client.api.with_streaming_response.retrieve_example() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(APIRetrieveExampleResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_raw_data(self, client: Bountylab) -> None:
        api = client.api.retrieve_raw_data()
        assert_matches_type(APIRetrieveRawDataResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_raw_data(self, client: Bountylab) -> None:
        response = client.api.with_raw_response.retrieve_raw_data()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(APIRetrieveRawDataResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_raw_data(self, client: Bountylab) -> None:
        with client.api.with_streaming_response.retrieve_raw_data() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(APIRetrieveRawDataResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: Bountylab) -> None:
        api = client.api.search()
        assert_matches_type(APISearchResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Bountylab) -> None:
        response = client.api.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(APISearchResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Bountylab) -> None:
        with client.api.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(APISearchResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAPI:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_example(self, async_client: AsyncBountylab) -> None:
        api = await async_client.api.retrieve_example()
        assert_matches_type(APIRetrieveExampleResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_example(self, async_client: AsyncBountylab) -> None:
        response = await async_client.api.with_raw_response.retrieve_example()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(APIRetrieveExampleResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_example(self, async_client: AsyncBountylab) -> None:
        async with async_client.api.with_streaming_response.retrieve_example() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(APIRetrieveExampleResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_raw_data(self, async_client: AsyncBountylab) -> None:
        api = await async_client.api.retrieve_raw_data()
        assert_matches_type(APIRetrieveRawDataResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_raw_data(self, async_client: AsyncBountylab) -> None:
        response = await async_client.api.with_raw_response.retrieve_raw_data()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(APIRetrieveRawDataResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_raw_data(self, async_client: AsyncBountylab) -> None:
        async with async_client.api.with_streaming_response.retrieve_raw_data() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(APIRetrieveRawDataResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncBountylab) -> None:
        api = await async_client.api.search()
        assert_matches_type(APISearchResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncBountylab) -> None:
        response = await async_client.api.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(APISearchResponse, api, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncBountylab) -> None:
        async with async_client.api.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(APISearchResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True
