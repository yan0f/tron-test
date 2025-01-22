from decimal import Decimal

from sqlalchemy.ext.asyncio import AsyncSession
from tronpy import AsyncTron
from tronpy.tron import TAddress

from app import models
from app.models import WalletRequests


async def add_wallet_request(
    session: AsyncSession, balance: Decimal, bandwidth: int, energy: int, wallet_address: TAddress
) -> WalletRequests:
    wallet_request = models.WalletRequests(address=wallet_address, balance=balance, bandwidth=bandwidth, energy=energy)
    session.add(wallet_request)
    await session.commit()
    return wallet_request


async def get_account_info_by_address(wallet_address):
    async with AsyncTron(network="nile") as client:
        account = await client.get_account(wallet_address)
        resource = await client.get_account_resource(wallet_address)
        bandwidth = await client.get_bandwidth(wallet_address)

    balance = Decimal(account.get("balance", 0)) / 1_000_000
    energy = resource.get("EnergyLimit", 0) - resource.get("EnergyUsed", 0)
    return balance, bandwidth, energy
