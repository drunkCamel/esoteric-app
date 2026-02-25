from fastapi import APIRouter
from app.schemas import BirthdateInput, BirthdateOutput
from app.utils.birthdate_data import BirthdateData 

router = APIRouter(prefix="/birthdate", tags=["birthdate"])

@router.post("/calculate", response_model = BirthdateOutput)
async def calculate_birthdate(data: BirthdateInput):
    birthdate = BirthdateData(day=data.day, month=data.month, year=data.year)
    birthdate_list = birthdate.birthdate_list(val_one=data.day, val_two=data.month, val_three=data.year)
    return BirthdateOutput(
        day=birthdate.day,
        month=birthdate.month,
        year=birthdate.year,
        birthdate_list=birthdate_list
    )

