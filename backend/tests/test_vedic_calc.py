import pytest
from app.utils.birthdate_data import BirthdateData
from app.services.vedic_calc import VedicCalc
from app.utils.exceptions  import InvalidValueError

birthdate = BirthdateData(9, 7, 1956)

@pytest.mark.unit
class TestVedicCalc:
    def test_calculate_vedic_square_number_sequance_years(self):
        vedic_calc = VedicCalc(birthdate)
        years_sequence = vedic_calc.vedic_square_number_sequance_years()
        expected_sequence = [2034, 2075, 2026, 2067, 2018, 2059, 2010, 2051, 2002, 
                             2003, 2035, 2076, 2027, 2068, 2019, 2060, 2011, 2043, 
                             2044, 2004, 2036, 2077, 2028, 2069, 2020, 2052, 2012, 
                             2013, 2045, 2005, 2037, 2078, 2029, 2061, 2021, 2053, 
                             2054, 2014, 2046, 2006, 2038, 2070, 2030, 2062, 2022, 
                             2023, 2055, 2015, 2047, 1998, 2039, 2071, 2031, 2063, 
                             2064, 2024, 2056, 2007, 2048, 1999, 2040, 2072, 2032, 
                             2033, 2065, 2016, 2057, 2008, 2049, 2000, 2041, 2073, 
                             2074, 2025, 2066, 2017, 2058, 2009, 2050, 2001, 2042]
        assert years_sequence == expected_sequence

