from app.utils.birthdate_data import BirthdateData
from app.utils import common


class VedicCalc:
    def __init__(self, birthdate: BirthdateData):
        self.birthdate = birthdate

        
    def vedic_square_number_sequance_years(self) -> list[int]:
        """
            Calculate list which would define 81 years ahead, including year of the birth. 
        """
        index_mapping = [
            36, 77, 28, 69, 20, 61, 12, 53, 4,
            5, 37, 78, 29, 70, 21, 62, 13, 45,
            46, 6, 38, 79, 30, 71, 22, 54, 14,
            15, 47, 7, 39, 80, 31, 63, 23, 55,
            56, 16, 48, 8, 40, 72, 32, 64, 24,
            25, 57, 17, 49, 0, 41, 73, 33, 65,
            66, 26, 58, 9, 50, 1, 42, 74, 34,
            35, 67, 18, 59, 10, 51, 2, 43, 75,
            76, 27, 68, 19, 60, 11, 52, 3, 44]
        
        return [self.birthdate.year + val for val in index_mapping]
            # List comprehension executes like this:
            # Iteration 1: val = 36 → 1956 + 36 = 1992
            # Iteration 2: val = 77 → 1956 + 77 = 2033
            # Iteration 3: val = 28 → 1956 + 28 = 1984
            # Iteration 4: val = 69 → 1956 + 69 = 2025
            # Iteration 5: val = 20 → 1956 + 20 = 1976
    
    
    def vedic_square_number_sequance_pesonal_years(self) -> list[int]:
        """
            Returns list of all 81 personal years, and for each index(personal_year) creates a new list 
            that includes all possibilites reduction to while personal_year > 9 
        """
        personal_years = []
        for year in self.vedic_square_number_sequance_years():
            total = self.birthdate.day + self.birthdate.month + common.calculate_digit_sum(year)
            personal_years.append(common.reduce_number_to_root(total))
        
        return personal_years
    
    
    def vedic_square_number_sequance_univeral_years(self) -> list[int]:
        """
            Returns list of all 81 univeral years, and for each index(univeral_years) creates a new list 
            that includes all possibilites reduction to while personal_year > 9 
        """
        univeral_years = []
        for year in self.vedic_square_number_sequance_years():
            total = common.calculate_digit_sum(year)
            univeral_years.append(common.reduce_number_to_root(total))
        return univeral_years
    


birthday = BirthdateData(9 , 4, 1998)
calculator = VedicCalc(birthday)