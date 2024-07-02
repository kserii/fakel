from pydantic import BaseModel, Field, field_validator
from typing import List, Optional

from fakel.const import APP_SECRET


class DonutModel(BaseModel):
    is_donut: bool


class CommentsModel(BaseModel):
    count: int


class ObjectModel(BaseModel):
    inner_type: str = Field(alias='type')
    can_edit: int
    created_by: int
    can_delete: int
    donut: DonutModel
    comments: CommentsModel
    marked_as_ads: int
    compact_attachments_before_cut: int
    hash: str
    post_type: str = Field(alias='type')
    attachments: List = []
    date: int
    from_id: int
    id: int
    is_favorite: bool
    owner_id: int
    post_type: str
    text: str


class VKEventModel(BaseModel):
    group_id: int
    event_id: str
    v: str
    type: str
    object: Optional[ObjectModel] = None
    secret: str

    @field_validator('secret')
    def secret_must_match(cls, value):
        if value != APP_SECRET:
            raise ValueError("Поле 'secret' должно быть равно значению перменной окружения 'APP_SECRET'!")
        return value
