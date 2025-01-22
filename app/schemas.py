from pydantic import BaseModel


class WalletRequests(BaseModel):
    bandwidth: int
    energy: int
    balance: float
    address: str

    class Config:
        from_attributes = True
