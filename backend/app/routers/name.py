from fastapi import APIRouter
from app.schemas import NameInput, NameOutput
from app.utils.name_data import NameData 

router = APIRouter(prefix="/name", tags=["name"])

@router.post("/calculate", response_model = NameOutput)
async def calculate_birthdate(data: NameInput):
    namedata = NameData(first_name = data.first_name, 
                        surname = data.surname, 
                        second_name = data.second_name)
    fullname = namedata.fullname
    return NameOutput(
        first_name = namedata.first_name,
        surname = namedata.surname,
        second_name = namedata.second_name,
        fullname = fullname,
    )      
