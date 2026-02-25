from pydantic import BaseModel, Field

class BirthdateInput(BaseModel):
    day: int = Field(ge=1, le=31, description="Day of birth (1-31)")
    month: int = Field(ge=1, le=12, description="Month of birth (1-12)")
    year: int = Field(ge=1, le=9999, description="Year of birth (positive integer)")

class BirthdateOutput(BaseModel):
    day: int
    month: int
    year: int
    birthdate_list: list[list[int]]


class NameInput(BaseModel):
    first_name: str = Field(..., description="First name (non-empty string)")
    surname: str = Field(..., description="Surname (non-empty string)")
    second_name: str | None = Field(None, description="Second name (optional string)")

class NameOutput(BaseModel):
    first_name: str
    surname: str
    second_name: str | None
    fullname: str