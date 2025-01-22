from decimal import Decimal

import pytest
from fastapi_pagination import add_pagination
from httpx import ASGITransport, AsyncClient
from tronpy.tron import TAddress

from app.main import app, get_session
from app.service import add_wallet_request
from tests.conftest import override_get_session, TestSessionLocal

app.dependency_overrides[get_session] = override_get_session


@pytest.mark.asyncio
async def test_get_latest_rows():
    async with TestSessionLocal() as session:
        await add_wallet_request(
            session=session,
            balance=Decimal("100.5"),
            bandwidth=2000,
            energy=1500,
            wallet_address=TAddress("TBNHWckSxxzHbJgMeUaYin4ABMcLvmWiPz"),
        )
        await add_wallet_request(
            session=session,
            balance=Decimal("50.75"),
            bandwidth=1000,
            energy=800,
            wallet_address=TAddress("TDqGdq76PDHrEXfEPMmNa2ayc7E4PKzfS1"),
        )

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        add_pagination(app)
        response = await client.get("/latest")

    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 2  # Total number of records
    assert len(data["items"]) == 2  # Number of items in the response
    assert data["items"][0]["address"] == "TBNHWckSxxzHbJgMeUaYin4ABMcLvmWiPz"
    assert data["items"][0]["balance"] == 100.5
    assert data["items"][0]["bandwidth"] == 2000
    assert data["items"][0]["energy"] == 1500

    assert data["items"][1]["address"] == "TDqGdq76PDHrEXfEPMmNa2ayc7E4PKzfS1"
    assert data["items"][1]["balance"] == 50.75
    assert data["items"][1]["bandwidth"] == 1000
    assert data["items"][1]["energy"] == 800
