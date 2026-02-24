import pytest
from app.utils.birthdate_data import BirthdateData
from app.utils.name_data import NameData
from app.services.numerology_calc import NumerologyCalculator
from app.utils.exceptions  import InvalidValueError, InvalidDataError

@pytest.fixture
def birthdate():
    return BirthdateData(9, 7, 1956)

@pytest.fixture
def name():
    return NameData("Thomas", "Hanks", "Jeffrey")

@pytest.fixture 
def numerology_calc(birthdate):
    return NumerologyCalculator(birthdate)


@pytest.mark.unit
class TestNumerologyCalculator:
  
    def test_calculate_lifepath(self, numerology_calc):

        lifepath_calc = numerology_calc.calculate_lifepath()
        expected_lifepath = [37, 19, 10, 1]
        assert lifepath_calc == expected_lifepath

    def test_calculate_pinnacle_one(self, numerology_calc):
        pinnacle_calc = numerology_calc.calculate_pinnacle_one()
        expected_pinancle = [16, 7]
        assert pinnacle_calc == expected_pinancle
    
    def test_calculate_pinnacle_two(self, numerology_calc):
        pinnacle_calc = numerology_calc.calculate_pinnacle_two()
        expected_pinnacle = [30, 12, 3]
        assert pinnacle_calc == expected_pinnacle


    def test_calculate_pinnacle_three(self, numerology_calc):
        pinnacle_calc = numerology_calc.calculate_pinnacle_three()
        expected_pinnacle = [46, 37, 28, 19, 10, 1]
        assert pinnacle_calc == expected_pinnacle


    def test_calculate_pinnacle_fourth(self, numerology_calc):
        pinnacle_calc = numerology_calc.calculate_pinnacle_fourth()
        expected_pinnacle = [28, 10, 1]
        assert pinnacle_calc == expected_pinnacle

    def test_calculate_personal_year(self, numerology_calc):
        personal_calc = numerology_calc.calculate_personal_year()
        expected_personal_year = [26, 17, 8]
        assert personal_calc == expected_personal_year

    def test_calculate_personal_month(self, numerology_calc):
        personal_month_calc = numerology_calc.calculate_personal_month()
        expected_personal_month = [28, 10, 1]
        assert personal_month_calc == expected_personal_month
        

    def test_calcualte_cycle_one(self, numerology_calc):
        cycle_one_calc = numerology_calc.calculate_cycle_one()
        expected_cycle_one = [7]
        assert cycle_one_calc == expected_cycle_one

    def test_calcualte_cycle_two(self, numerology_calc):
        cycle_two_calc = numerology_calc.calculate_cycle_two()
        expected_cycle_two = [9]
        assert cycle_two_calc == expected_cycle_two

    def test_calculate_cycle_three(self, numerology_calc):
        cycle_three_calc = numerology_calc.calculate_cycle_three()
        expected_cycle_three = [21,3]
        assert cycle_three_calc == expected_cycle_three

    def test_caculate_pythagoras_life_cycle(self, numerology_calc):
        life_cycle_calc = numerology_calc.calculate_pythagoras_life_cycle()
        expected_life_cycle = [1, 2, 3, 2, 2, 8]
        assert life_cycle_calc == expected_life_cycle

    def test_calculate_periodical_challange_one(self, numerology_calc):
        periodical_challange_one_calc = numerology_calc.calculate_periodical_challange_one()
        expected_challange_one = [2]
        assert periodical_challange_one_calc == expected_challange_one

    def test_calculate_periodical_challange_two(self, numerology_calc):
        periodical_challange_two_calc = numerology_calc.calculate_periodical_challange_two()
        expected_challange_two = [12]
        assert periodical_challange_two_calc == expected_challange_two

    def test_calculate_periodical_challange_three(self, numerology_calc):
        periodical_challange_three_calc = numerology_calc.calculate_periodical_challange_three()
        expected_challange_three = [10]
        assert periodical_challange_three_calc == expected_challange_three

    def test_calculate_periodical_challange_four(self, numerology_calc):
        periodical_challange_four_calc = numerology_calc.calculate_periodical_challange_fourth()
        expected_challange_four = [14]
        assert periodical_challange_four_calc == expected_challange_four

    def test_calculate_life_transits(self, numerology_calc, name):
        life_transit_calc = numerology_calc.calcualting_life_transits(name)
        expected_life_transits = [69, 75, 83, 85, 69, 71, 74, 76, 71, 77, 77, 79, 81, 83, 64, 66, 65, 
                                  74, 79, 81, 80, 82, 85, 87, 77, 72, 78, 76, 78, 80, 82, 81, 83, 84, 
                                  75, 77, 79, 81, 81, 77, 83, 85, 77, 83, 32, 35, 43, 45, 44, 46, 47, 
                                  56, 58, 60, 42, 44, 46, 51, 53, 48, 52, 54, 56, 58, 39, 38, 37, 38, 
                                  53, 55, 57, 61, 63, 65, 49, 51, 44, 50, 46, 52, 54, 56, 53, 55, 39, 
                                  48, 47, 49, 52, 54, 62, 64, 66, 61, 49, 51, 56, 58, 58, 57, 59, 60, 
                                  69, 71, 53, 51, 53, 55, 54, 56, 54, 60, 68, 70, 54, 56, 55, 51, 56, 65]
        assert life_transit_calc == expected_life_transits

