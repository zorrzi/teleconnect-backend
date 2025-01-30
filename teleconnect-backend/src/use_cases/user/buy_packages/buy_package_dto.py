from pydantic import BaseModel

class BuyPackageDTO(BaseModel):
    user_id: str
    package_id: str