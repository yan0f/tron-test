from decimal import Decimal

from sqlalchemy import DECIMAL
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class WalletRequests(Base):
    __tablename__ = "wallet_requests"

    id: Mapped[int] = mapped_column(primary_key=True)
    balance: Mapped[Decimal] = mapped_column(DECIMAL())
    bandwidth: Mapped[int] = mapped_column()
    energy: Mapped[int] = mapped_column()
    address: Mapped[str] = mapped_column()
