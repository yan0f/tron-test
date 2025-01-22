from typing import Annotated

from fastapi import Body, Depends, FastAPI, HTTPException, status
from fastapi_pagination import Page, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from tronpy.exceptions import AddressNotFound, BadAddress
from tronpy.tron import TAddress

from . import models
from .database import async_session
from .schemas import WalletRequests
from .service import add_wallet_request, get_account_info_by_address

app = FastAPI()
add_pagination(app)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


@app.get("/latest", response_model=Page[WalletRequests])
async def get_latest_wallet_requests(session: AsyncSession = Depends(get_session)):
    return await paginate(session, select(models.WalletRequests))


@app.post("/account_info", response_model=WalletRequests, response_model_exclude={"address"})
async def get_account_info(
    wallet_address: Annotated[TAddress, Body(embed=True)], session: AsyncSession = Depends(get_session)
):
    try:
        balance, bandwidth, energy = await get_account_info_by_address(wallet_address)
    except (AddressNotFound, BadAddress):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="account not found on-chain")
    wallet_request = await add_wallet_request(session, balance, bandwidth, energy, wallet_address)

    return wallet_request
