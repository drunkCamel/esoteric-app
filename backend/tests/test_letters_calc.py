import pytest
from app.utils.name_data import NameData
from app.services.letters_calc import LettersCalculator
from app.utils.exceptions  import InvalidValueError, InvalidDataError

@pytest.fixture
def person():
    return NameData("Thomas", "Hanks", "Jeffrey")

@pytest.mark.unit
class TestLettersCalculator:
    
    def test_calculate_soul_number(self, person):
        soul_calc = LettersCalculator(person).calculating_soul_number()
        expected_soul_number = [18, 9]
        assert soul_calc == expected_soul_number

    def test_calculate_realisation(self, person):
        realisation_calc = LettersCalculator(person).calculating_realisation()
        expected_realisation = [60, 51, 42, 33, 24, 15]
        assert realisation_calc == expected_realisation
    
    def test_calculate_expression_number(self, person):
        expression_calc = LettersCalculator(person).calculating_expression_number()
        expected_expression_number = [78, 69, 60, 51, 42, 33, 24, 15]
        assert expression_calc == expected_expression_number

    def test_calculate_name_aura(self, person):
        name_aura_calc = LettersCalculator(person).calculating_name_aura()
        expected_name_aura = [18]
        assert name_aura_calc == expected_name_aura
    
    def test_calculate_karmic_lesson(self, person):
        karmic_lesson_calc = LettersCalculator(person).calculating_karmic_lesson()
        expected_karmic_lesson = {2: 2, 8: 2, 6: 3, 4: 1, 1: 5, 5: 3, 9: 1, 7: 1}
        assert karmic_lesson_calc == expected_karmic_lesson

    def test_calcualte_name_year_transit(self, person):
        name_year_transit_calc = LettersCalculator(person).calculating_name_year_transit()
        expected_name_year_transit = [11, 15, 21, 21, 21, 21, 22, 22, 15, 19, 17, 17, 17, 17, 
                                      14, 14, 11, 18, 21, 21, 18, 18, 19, 19, 25, 18, 22, 18, 
                                      18, 18, 18, 15, 15, 14, 21, 21, 21, 21, 19, 13, 17, 17, 
                                      7, 11, 12, 13, 19, 19, 16, 16, 15, 22, 22, 22, 20, 20, 20, 
                                      23, 23, 16, 18, 18, 18, 18, 15, 12, 9, 8, 21, 21, 21, 23, 
                                      23, 23, 23, 23, 14, 18, 12, 16, 16, 16, 11, 11, 11, 18, 15, 
                                      15, 16, 16, 22, 22, 22, 15, 19, 19, 22, 22, 20, 17, 17, 16, 
                                      23, 23, 21, 17, 17, 17, 14, 14, 10, 14, 20, 20, 20, 20, 17, 11, 14, 21]
        assert name_year_transit_calc == expected_name_year_transit