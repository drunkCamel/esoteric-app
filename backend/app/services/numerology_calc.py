from app.utils.birthdate_data import BirthdateData
from app.services.letters_calc import LettersCalculator
from app.utils.name_data import NameData
from app.utils.exceptions  import InvalidDataError, InvalidReducitonLevelError, InvalidCalculationParametersError
from app.utils import common
from datetime import datetime

class NumerologyCalculator:
    def __init__(self, birthday: BirthdateData, 
                 current_year: datetime = datetime.now().year, current_month: datetime = datetime.now().month):
        """Initialise Numerology Calculator."""

        if not isinstance(current_month, int) or not isinstance(current_year, int):
            raise TypeError("current_month and current_year must be a integer value")
        # Current month validation
        if not 1 <= current_month <= 12:
            raise InvalidDataError(f"Current month must be between 1 and 12, got {current_month}")
        #Compositions that contains instances from other classes
        self.birthday = birthday
        self.current_year = current_year
        self.current_month = current_month
    



    #Life Path ------------------------------------
    def calculate_lifepath(self) -> list[int]:
        """Return the list of all lifepath possibilites from higest to the root """
        result = common.calculate_all_reduction_values(self.birthday.birthdate_list(self.birthday.day,self.birthday.month,common.calculate_digit_sum(self.birthday.year)))
        return result
    # Pinnacles -------------------------------------


    def calculate_pinnacle_one(self):
        return common.calculate_all_reduction_values(self.birthday.birthdate_list(self.birthday.day, self.birthday.month))
    

    def calculate_pinnacle_two(self):
        return common.calculate_all_reduction_values(self.birthday.birthdate_list(self.birthday.day, common.calculate_digit_sum(self.birthday.year)))
    

    def calculate_pinnacle_three(self):
        return sorted(
    set(item
        for a in self.calculate_pinnacle_one()
        for b in self.calculate_pinnacle_two()
        for item in common.reduce_number_to_root(a + b)
    ),
    reverse=True
    )       


    def calculate_pinnacle_fourth(self):
        return common.calculate_all_reduction_values(self.birthday.birthdate_list(self.birthday.month, common.calculate_digit_sum(self.birthday.year)))
    

    # Personal year ---------------------------------
    def calculate_personal_year(self) -> list[int]:
        """Return the list of all personal Years possibilites from higest to the root"""
        test = common.calculate_all_reduction_values(self.birthday.birthdate_list(self.birthday.day,self.birthday.month,common.calculate_digit_sum(self.current_year)))
        return test
    

    # Personal month
    def calculate_personal_month(self) -> list[int]:
        """Return the list of all personal Years possibilites from higest to the root"""
        return common.reduce_number_to_root(common.calculate_digit_sum(self.current_year) + self.birthday.day + self.birthday.month + self.current_month)


    # Cycles ---------------------------------
    def calculate_cycle_one(self) -> list[int]:
        """Return list of all cycles possibilites from higest to the root"""
        return common.reduce_number_to_root(self.birthday.month)
    

    def calculate_cycle_two(self) -> list[int]:
        """Return list of all cycles possibilites from higest to the root"""
        return common.reduce_number_to_root(self.birthday.day)  
    

    def calculate_cycle_three(self) -> list[int]:
        """Return list of all cycles possibilites from higest to the root"""
        number = sum(common.number_to_digits(self.birthday.year))
        return common.reduce_number_to_root(number)

    
    def calculate_pythagoras_life_cycle(self) -> list[int]:
        """ Return list, of the calculation day + month + year = seperated to a single digit list"""
        return common.number_to_digits(self.birthday.day * self.birthday.month * self.birthday.year)


    def calculate_periodical_challange_one(self) -> list[int]:
        ch_one = abs(self.birthday.day - self.birthday.month)
        ch_one_reduced = abs(common.calculate_digit_sum(self.birthday.day) - self.birthday.month)

        return common.comparing_two_values(ch_one,ch_one_reduced, int(str(self.birthday.day)[1]) if len(str(self.birthday.day)) > 1 else 0)
    
    
    def calculate_periodical_challange_two(self) -> list[int]:
        ch_two = abs(self.birthday.day - common.calculate_digit_sum(self.birthday.year))
        ch_two_reduced = abs(common.calculate_digit_sum(self.birthday.year) - common.calculate_digit_sum(self.birthday.day))
        
        return common.comparing_two_values(ch_two, ch_two_reduced, int(str(self.birthday.day)[1]) if len(str(self.birthday.day)) > 1 else 0)
    
    
    def calculate_periodical_challange_three(self) -> list[int]:
        ch_three = abs((abs(self.birthday.day - self.birthday.month)) - (abs(self.birthday.day - common.calculate_digit_sum(self.birthday.year))))
        ch_three_reduced = abs((abs(common.calculate_digit_sum(self.birthday.day) - self.birthday.month)) - (abs(common.calculate_digit_sum(self.birthday.year) - common.calculate_digit_sum(self.birthday.day))))

        return common.comparing_two_values(ch_three, ch_three_reduced, int(str(self.birthday.day)[1]) if len(str(self.birthday.day)) > 1 else 0)
    
    
    def calculate_periodical_challange_fourth(self) -> list[int]:
        ch_fourth = abs(common.calculate_digit_sum(self.birthday.year) - self.birthday.month)
        ch_fourth_reduced = abs(common.calculate_digit_sum(self.birthday.year) - common.recursive_digit(self.birthday.month))

        return common.comparing_two_values(ch_fourth, ch_fourth_reduced, int(str(self.birthday.month)[1]) if len(str(self.birthday.month)) > 1 else 0)

    #? destiny month number?? 
    # reduction number of (first_name + surname) + life path + current year + current month
    def destiny_month_number(self):
        pass

    def being_number_self(self):
        pass
    #?being number
    # personal number + personal month -  the thone of specifici month or day
    
    
    def calcualting_life_transits(self, name: NameData) -> list[int]:
        person = LettersCalculator(name) # NameData("Thomas", "Hanks", "Jeffrey")
        univeral_year_list = common.generate_number_sequence(self.birthday.year)
        personal_year_list = common.generate_number_sequence(self.birthday.year, extra_value=self.birthday.day + self.birthday.month)
        sum_of_year_transits = person.calculating_name_year_transit() 

        result = [val1 + val2 + val3 for val1,val2,val3 in zip(univeral_year_list,
                                                               personal_year_list,
                                                               sum_of_year_transits)]

        return result
        


birthday = BirthdateData(9 , 7, 1956)
calculator = NumerologyCalculator(birthday)
print(calculator.calcualting_life_transits(NameData("Thomas", "Hanks", "Jeffrey")))

