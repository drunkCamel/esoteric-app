import pytest
from app.utils.name_data import NameData
from app.utils.exceptions  import InvalidTypeError


@pytest.mark.unit
class TestNameData:
    def test_valid_name_data(self):
        name_data = NameData("Thomas", "Hanks", "Jeffrey")
        assert name_data.first_name == "Thomas"
        assert name_data.surname == "Hanks"
        assert name_data.second_name == "Jeffrey"
    

    def test_valid_name_data_without_second_name(self):
        name_data = NameData("Thomas", "Hanks")
        assert name_data.first_name == "Thomas"
        assert name_data.surname == "Hanks"
        assert name_data.second_name is None

    def test_invalid_first_name(self):
        with pytest.raises(InvalidTypeError):
            NameData("", "Hanks")

    def test_invalid_surname(self):
        with pytest.raises(InvalidTypeError):
            NameData("Thomas", "")

    def test_invalid_first_and_surname(self):
        with pytest.raises(InvalidTypeError):
            NameData("", "")

    def test_invalid_first_name_type(self):
        with pytest.raises(InvalidTypeError):
            NameData(123, "Hanks")
    
    def test_invalid_surname_type(self):
        with pytest.raises(InvalidTypeError):
            NameData("Thomas", 456)
    
    def test_invalid_second_name_type(self):
        with pytest.raises(InvalidTypeError):
            NameData("Thomas", "Hanks", 789)

    def test_invalid_second_name(self):
        name_data =  NameData("Thomas", "Hanks", "")
        assert name_data.second_name is None
    
    def test_invalid_second_name_none(self):
        """Test that second_name can be None without raising an error."""
        name_data = NameData("Thomas", "Hanks", None)
        assert name_data.second_name is None
    
    def test_invalid_second_name_whitespace(self):
        """Test that second_name with only whitespace is treated as None."""
        name_data = NameData("Thomas", "Hanks", "   ")
        assert name_data.second_name is None

    def test_invalid_second_name_whitespace_valid(self):
        """Test that second_name with valid whitespace is treated as valid."""
        name_data = NameData("Thomas", "Hanks", "  Jeffrey  ")
        assert name_data.second_name == "Jeffrey"
    
        
    def test_fullname_property(self):
        name_data = NameData("Thomas", "Hanks", "Jeffrey")
        assert name_data.fullname == "thomasjeffreyhanks"
    
    def test_fullname_property_without_second_name(self):
        name_data = NameData("Thomas", "Hanks")
        assert name_data.fullname == "thomashanks"


    def test_birthdate_list(self):
        name_data = NameData("Thomas", "Hanks", "Jeffrey")
        assert name_data.birthdate_list(1, 2, 3) == [[1], [2], [3]]
        assert name_data.birthdate_list(1, 2) == [[1], [2]]
        assert name_data.birthdate_list(1) == [[1]]
        assert name_data.birthdate_list() == []

    def test_extract_digits_from_list(self):
        name_data = NameData("Thomas", "Hanks", "Jeffrey")
        assert name_data.extract_digits_from_list('VOWEL_MAP') == [[6, 1], [1],[5, 5]]
        assert name_data.extract_digits_from_list('CONSONANT_MAP') == [[2, 8, 4, 1], [8, 5, 2, 1],[1, 6, 6, 9, 7]]
        assert name_data.extract_digits_from_list('SINGLE_DIGIT_MAP') == [[2, 8, 6, 4, 1, 1],[8, 1, 5, 2, 1], [1, 5, 6, 6, 9, 5, 7]]
        assert name_data.extract_digits_from_list('DOUBLE_DIGIT_MAP') == [[20, 8, 15, 13, 1, 19], [8, 1, 14, 11, 19],[10, 5, 6, 6, 18, 5, 25]]

    def test_extract_digits_from_list_invalid_type(self):
        name_data = NameData("Thomas", "Hanks", "Jeffrey")
        with pytest.raises(KeyError):
            name_data.extract_digits_from_list('INVALID_MAP')

    def test_extract_digits_from_list_no_matching_characters(self):
        name_data = NameData("123", "456", "789")
        assert name_data.extract_digits_from_list('VOWEL_MAP') == [[], [], []]
        assert name_data.extract_digits_from_list('CONSONANT_MAP') == [[], [], []]
        assert name_data.extract_digits_from_list('SINGLE_DIGIT_MAP') == [[], [], []]
        assert name_data.extract_digits_from_list('DOUBLE_DIGIT_MAP') == [[], [], []]

    
    def test_extract_digits_from_list_no_second_name(self):
        name_data = NameData("Thomas", "Hanks")
        assert name_data.extract_digits_from_list('VOWEL_MAP') == [[6, 1], [1]]
        assert name_data.extract_digits_from_list('CONSONANT_MAP') == [[2, 8, 4, 1], [8, 5, 2, 1]]
        assert name_data.extract_digits_from_list('SINGLE_DIGIT_MAP') == [[2, 8, 6, 4, 1, 1], [8, 1, 5, 2, 1]]
        assert name_data.extract_digits_from_list('DOUBLE_DIGIT_MAP') == [[20, 8, 15, 13, 1, 19], [8, 1, 14, 11, 19]]
