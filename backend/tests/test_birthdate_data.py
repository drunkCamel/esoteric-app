import pytest
from app.utils.birthdate_data import BirthdateData
from app.exceptions import InvalidDataError, InvalidTypeError


@pytest.mark.unit
class TestBirthdateData:
    def test_valid_birthdate(self):
        birthdate = BirthdateData(15, 5, 1990)
        assert birthdate.day == 15
        assert birthdate.month == 5
        assert birthdate.year == 1990

    def test_invalid_month(self):
        with pytest.raises(InvalidDataError):
            BirthdateData(15, 13, 1990)

    def test_invalid_day(self):
        with pytest.raises(InvalidDataError):
            BirthdateData(32, 5, 1990)

    def test_invalid_day_for_month(self):
        with pytest.raises(InvalidDataError):
            BirthdateData(31, 4, 1990)

    def test_leap_year(self):
        # Valid leap year date
        birthdate = BirthdateData(29, 2, 2020)
        assert birthdate.day == 29

        # Invalid leap year date
        with pytest.raises(InvalidDataError):
            BirthdateData(29, 2, 2021)

    def test_negative_year(self):
        with pytest.raises(InvalidDataError):
            BirthdateData(15, 5, -1990)

    def test_non_integer_input(self):
        with pytest.raises(InvalidTypeError):
            BirthdateData("15", 5, 1990)
        with pytest.raises(InvalidTypeError):
            BirthdateData(15, "5", 1990)
        with pytest.raises(InvalidTypeError):
            BirthdateData(15, 5, "1990")