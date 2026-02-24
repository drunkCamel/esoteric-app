import pytest
from app.utils.birthdate_data import BirthdateData
from app.services.vedic_calc import VedicCalc
from app.utils.exceptions  import InvalidValueError, InvalidDataError

@pytest.fixture
def birthdate():
    return BirthdateData(9, 7, 1956)


@pytest.mark.unit
class TestVedicCalc:
    def test_calculate_vedic_square_number_sequance_years(self, birthdate):
        years_sequence = VedicCalc(birthdate).vedic_square_number_sequance_years()
        expected_sequence = [1992, 2033, 1984, 2025, 1976, 2017, 1968, 2009, 1960, 
                             1961, 1993, 2034, 1985, 2026, 1977, 2018, 1969, 2001, 
                             2002, 1962, 1994, 2035, 1986, 2027, 1978, 2010, 1970, 
                             1971, 2003, 1963, 1995, 2036, 1987, 2019, 1979, 2011, 
                             2012, 1972, 2004, 1964, 1996, 2028, 1988, 2020, 1980, 
                             1981, 2013, 1973, 2005, 1956, 1997, 2029, 1989, 2021, 
                             2022, 1982, 2014, 1965, 2006, 1957, 1998, 2030, 1990, 
                             1991, 2023, 1974, 2015, 1966, 2007, 1958, 1999, 2031, 
                             2032, 1983, 2024, 1975, 2016, 1967, 2008, 1959, 2000]
        assert years_sequence == expected_sequence

    def test_vedic_square_sequence_personal_year(self, birthdate):
        personal_years = VedicCalc(birthdate).vedic_square_sequence_personal_year()
        expected_personal_years = [[37, 10, 1], [24, 6], [38, 11, 2], [25, 7], [39, 12, 3], [26, 8], [40, 4], [27, 9], [32, 5], 
                                   [33, 6], [38, 11, 2], [25, 7], [39, 12, 3], [26, 8], [40, 4], [27, 9], [41, 5], [19, 10, 1], 
                                   [20, 2], [34, 7], [39, 12, 3], [26, 8], [40, 4], [27, 9], [41, 5], [19, 10, 1], [33, 6], 
                                   [34, 7], [21, 3], [35, 8], [40, 4], [27, 9], [41, 5], [28, 10, 1], [42, 6], [20, 2], 
                                   [21, 3], [35, 8], [22, 4], [36, 9], [41, 5], [28, 10, 1], [42, 6], [20, 2], [34, 7], 
                                   [35, 8], [22, 4], [36, 9], [23, 5], [37, 10, 1], [42, 6], [29, 11, 2], [43, 7], [21, 3], 
                                   [22, 4], [36, 9], [23, 5], [37, 10, 1], [24, 6], [38, 11, 2], [43, 7], [21, 3], [35, 8], 
                                   [36, 9], [23, 5], [37, 10, 1], [24, 6], [38, 11, 2], [25, 7], [39, 12, 3], [44, 8], [22, 4], 
                                   [23, 5], [37, 10, 1], [24, 6], [38, 11, 2], [25, 7], [39, 12, 3], [26, 8], [40, 4], [18, 9]]
        assert personal_years == expected_personal_years

    def test_vedic_square_number_sequance_univeral_years(self, birthdate):
        univeral_years = VedicCalc(birthdate).vedic_square_number_sequance_univeral_years()
        expected_univeral_years = [[21, 3], [8], [22, 4], [9], [23, 5], [10, 1], [24, 6], [11, 2], [16, 7], 
                                   [17, 8], [22, 4], [9], [23, 5], [10, 1], [24, 6], [11, 2], [25, 7], [3], 
                                   [4], [18, 9], [23, 5], [10, 1], [24, 6], [11, 2], [25, 7], [3], [17, 8], 
                                   [18, 9], [5], [19, 10, 1], [24, 6], [11, 2], [25, 7], [12, 3], [26, 8], [4], 
                                   [5], [19, 10, 1], [6], [20, 2], [25, 7], [12, 3], [26, 8], [4], [18, 9], 
                                   [19, 10, 1], [6], [20, 2], [7], [21, 3], [26, 8], [13, 4], [27, 9], [5], 
                                   [6], [20, 2], [7], [21, 3], [8], [22, 4], [27, 9], [5], [19, 10, 1], 
                                   [20, 2], [7], [21, 3], [8], [22, 4], [9], [23, 5], [28, 10, 1], [6], 
                                   [7], [21, 3], [8], [22, 4], [9], [23, 5], [10, 1], [24, 6], [2]]
        assert univeral_years == expected_univeral_years

    def test_invalid_birthdate_data_error(self):
        with pytest.raises(InvalidDataError):
            VedicCalc(BirthdateData(day=32, month=1, year=1956))
            VedicCalc(BirthdateData(day=0, month=1, year=1956))
            VedicCalc(BirthdateData(day=15, month=13, year=1956))
            VedicCalc(BirthdateData(day=15, month=0, year=1956))
            VedicCalc(BirthdateData(day=15, month=1, year=-1956))
    

