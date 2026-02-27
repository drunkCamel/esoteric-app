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

    ## Numerology Calculations
    lifepath_number: list[int]
    pinnacle_one: list[int] | None = None
    pinnacle_two: list[int] | None = None
    pinnacle_three: list[int] | None = None
    pinnacle_fourth: list[int] | None = None
    personal_year: list[int] | None = None
    personal_month: list[int] | None = None
    cycle_one: list[int] | None = None
    cycle_two: list[int] | None = None
    cycle_three: list[int] | None = None
    pythagoras_life_cycle: list[int] | None = None
    periodical_challenge_one: list[int] | None = None
    periodical_challenge_two: list[int] | None = None
    periodical_challenge_three: list[int] | None = None
    periodical_challenge_four: list[int] | None = None

    ## Chinese Calculations
    lunar_birth_day: dict[str, int] | None = None
    lo_shu_square: dict[int, int] | None = None
    chinese_zodiac_sign: str | None = None
    chinese_enemy_sign: str | None = None
    chinese_friendly_sign_one: str | None = None
    chinese_friendly_sign_two: str | None = None
    chinese_current_year_zodiac_sign: str | None = None


class NameInput(BaseModel):
    first_name: str = Field(..., description="First name (non-empty string)")
    surname: str = Field(..., description="Surname (non-empty string)")
    second_name: str | None = Field(None, description="Second name (optional string)")

class NameOutput(BaseModel):
    first_name: str
    surname: str
    second_name: str | None
    fullname: str