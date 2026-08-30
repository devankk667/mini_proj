from typing import Generic, TypeVar, Optional, List
from pydantic import BaseModel, Field

DataT = TypeVar("DataT")

class ResponseEnvelope(BaseModel, Generic[DataT]):
    success: bool = True
    data: Optional[DataT] = None
    message: Optional[str] = None
    errors: Optional[List[str]] = None

class PaginationMeta(BaseModel):
    page: int = 1
    page_size: int = 20
    total_items: int = 0
    total_pages: int = 0

class PaginatedResponse(BaseModel, Generic[DataT]):
    items: List[DataT]
    meta: PaginationMeta

class ErrorDetail(BaseModel):
    code: str
    message: str
    field: Optional[str] = None

class ErrorResponse(BaseModel):
    success: bool = False
    message: str
    errors: List[ErrorDetail] = Field(default_factory=list)
