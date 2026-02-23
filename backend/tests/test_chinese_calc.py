import pytest
from app.utils.birthdate_data import BirthdateData
from app.services.chinese_calc import ChineseCalc
from app.utils.exceptions  import InvalidValueError

birthdate = BirthdateData(9, 7, 1956)

@pytest.mark.unit
class TestChineseCalc:
    def test_calculate_current_year(self):
        chinesebirthdate = ChineseCalc(birthdate, 2024)
        assert chinesebirthdate.current_year == 2024
    
    # a test which would check if the answer printint one of the 12 zodiac signs fromt the list

    def test_invalid_current_year(self):
        with pytest.raises(InvalidValueError):
            ChineseCalc(birthdate, current_year="2025")
            ChineseCalc(birthdate, current_year=2025.5)
            ChineseCalc(birthdate, current_year=-2025)
            ChineseCalc(birthdate, current_year=0)

    def test_calculate_chinese_birth_day(self):
        chinesebirthdate = ChineseCalc(birthdate)
        chinese_birth_day = chinesebirthdate.chinese_birth_day
        assert chinese_birth_day.day == 2
        assert chinese_birth_day.month == 6
        assert chinese_birth_day.year == 1956

    def test_calculate_chinese_zodiac_sign(self):
        chinesebirthdate = ChineseCalc(birthdate)
        zodiac_sign = chinesebirthdate.calculating_chinese_zodiac_sign()
        assert zodiac_sign == "Monkey"
    
    def test_calculate_chinese_enemy_sign(self):
        chinesebirthdate = ChineseCalc(birthdate)
        enemy_sign = chinesebirthdate.calculate_chinese_enemy_sign()
        assert enemy_sign == "Tiger"
    
    def test_calculate_chinese_friendly_sign_one(self):
        chinesebirthdate = ChineseCalc(birthdate)
        friendly_sign_one = chinesebirthdate.calculate_chinese_friendly_sign_one()
        assert friendly_sign_one == "Rat"
    
    def test_calculate_chinese_friendly_sign_two(self):
        chinesebirthdate = ChineseCalc(birthdate)
        friendly_sign_two = chinesebirthdate.calculate_chinese_friendly_sign_two()
        assert friendly_sign_two == "Dragon"

    def test_calculate_lo_shu_square(self):
        chinesebirthdate = ChineseCalc(birthdate)
        lo_shu_square = chinesebirthdate.calculating_lo_shu_square()
        expected_result = {2: 1, 6: 2, 1: 1, 9: 1, 5: 1}
        assert lo_shu_square == expected_result
    
    def test_calculate_current_chinese_zodiac_year(self):
        chinesebirthdate = ChineseCalc(birthdate, current_year=2025)
        current_zodiac_year = chinesebirthdate.calculate_current_chinese_zodiac_year()
        assert current_zodiac_year == "Snake"


