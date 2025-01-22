from decimal import Decimal
from unittest.mock import AsyncMock, MagicMock

import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from tronpy.tron import TAddress

from app.service import add_wallet_request


@pytest.mark.asyncio
async def test_add_wallet_request():
    mock_session = AsyncMock(spec=AsyncSession)
    mock_session.add = MagicMock()
    mock_session.commit = AsyncMock()

    test_balance = Decimal("123.45")
    test_bandwidth = 1000
    test_energy = 500
    test_wallet_address = TAddress("fluffy cloud")

    wallet_request = await add_wallet_request(
        session=mock_session,
        balance=test_balance,
        bandwidth=test_bandwidth,
        energy=test_energy,
        wallet_address=test_wallet_address,
    )

    assert wallet_request.address == test_wallet_address
    assert wallet_request.balance == test_balance
    assert wallet_request.bandwidth == test_bandwidth
    assert wallet_request.energy == test_energy

    mock_session.add.assert_called_once_with(wallet_request)
    mock_session.commit.assert_awaited_once()
