from pydantic import BaseModel

from card.schemas import CardPublicInfo

class SetPublicInfo(BaseModel):
    setId: int
    setName: str
    cards: list[CardPublicInfo] 