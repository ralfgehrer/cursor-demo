from datetime import datetime

class Item(SQLModel, table=True):
    # ... existing fields ...
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow) 