from http import HTTPStatus

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_read_organization(client: AsyncClient, headers: dict[str, str]):
    response = await client.get("/api/v1/organizations/1", headers=headers)
    assert response.status_code == HTTPStatus.OK
    assert response.json()["id"] == 1


@pytest.mark.asyncio
async def test_search_organizations_by_name(client: AsyncClient, headers: dict[str, str]):
    response = await client.get("/api/v1/organizations/", params={"name": "Рога"}, headers=headers)
    assert response.status_code == HTTPStatus.OK
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
