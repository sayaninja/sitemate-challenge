from pydantic import BaseModel
from datetime import datetime

# Issue Model
class IssueIn(BaseModel):
    title: str
    description: str

class Issue(IssueIn):
    id: int
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }