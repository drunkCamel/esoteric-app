import pytest
from app.utils.birthdate_data import BirthdateData
from app.utils.name_data import NameData
from app.services.numerology_calc import NumerologyCalculator
from app.utils.exceptions  import InvalidValueError, InvalidDataError


birthdate = BirthdateData(9, 7, 1956)
name = NameData("Thomas", "Hanks", "Jeffrey")

