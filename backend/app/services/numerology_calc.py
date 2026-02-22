from app.utils.birthdate_data import BirthdateData
from app.utils.name_data import NameData
from app.exceptions import InvalidDataError, InvalidReducitonLevelError, InvalidCalculationParametersError
from app.utils import common
from collections import Counter
from datetime import datetime

class NumerologyCalculator:
    def __init__(self, birthday: BirthdateData, person: NameData, 
                 current_year: datetime = datetime.now().year, current_month: datetime = datetime.now().month):
        """Initialise Numerology Calculator."""

        if not isinstance(current_month, int) or not isinstance(current_year, int):
            raise TypeError("current_month and current_year must be a integer value")
        # Current month validation
        if not 1 <= current_month <= 12:
            raise InvalidDataError(f"Current month must be between 1 and 12, got {current_month}")
        #Compositions that contains instances from other classes
        self.birthday = birthday
        self.person = person
        self.current_year = current_year
        self.current_month = current_month
    



    #Life Path ------------------------------------
    def calculate_lifepath(self) -> list[int]:
        """Return the list of all lifepath possibilites from higest to the root """
        result = common.calculate_all_reduction_values(self.person.birthdate_list(self.birthday.day,self.birthday.month,common.calculate_digit_sum(self.birthday.year)))
        return result
    # Pinnacles -------------------------------------


    def calculate_pinnacle_one(self):
        return common.calculate_all_reduction_values(self.person.birthdate_list(self.birthday.day, self.birthday.month))
    

    def calculate_pinnacle_two(self):
        return common.calculate_all_reduction_values(self.person.birthdate_list(self.birthday.day, common.calculate_digit_sum(self.birthday.year)))
    

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
        return common.calculate_all_reduction_values(self.person.birthdate_list(self.birthday.month, common.calculate_digit_sum(self.birthday.year)))
    

    # Personal year ---------------------------------
    def calculate_personal_year(self) -> list[int]:
        """Return the list of all personal Years possibilites from higest to the root"""
        test = common.calculate_all_reduction_values(self.person.birthdate_list(self.birthday.day,self.birthday.month,common.calculate_digit_sum(self.current_year)))
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

    def calculating_soul_number(self) -> list[int]:
        """
            Calculate total vowels list converted to digits with all calculation possibilities reduction level
        """
        return common.all_possibilites_digts_recursion_version(self.person.extract_digits_from_list('VOWEL_MAP'))
    
    
    def calculating_realisation(self) -> list[int]:
        """
            Calculate total consonants list converted to digits with all calculation possibilities reduction level
        """
        return common.all_possibilites_digts_recursion_version(self.person.extract_digits_from_list('CONSONANT_MAP'))
    
    
    def calculating_expression_number(self) -> list[int]:
        """
            Calculate total vowels and consonants list combined together and converted to digits with all calculation possibilities reduction level
        """
        return common.all_possibilites_digts_recursion_version(self.person.extract_digits_from_list('SINGLE_DIGIT_MAP'))
    
    
    def calculating_name_aura(self) -> list[int]:
        """
            Calculate the length of fullname
        """
        return [len(self.person.fullname)]

    
    def calculating_name_year_transit(self) -> list[int]:
        result = []
        digit_first_name_length_list = common.generate_repeated_digit_sequence(
            self.person.first_name.lower(),self.person.SINGLE_DIGIT_MAP)
        if self.person.second_name != None and self.person.second_name != "":
            digit_second_name_length_list = common.generate_repeated_digit_sequence(
            self.person.second_name.lower(),self.person.SINGLE_DIGIT_MAP)
        digit_surname_length_list = common.generate_repeated_digit_sequence(
            self.person.surname.lower(),self.person.SINGLE_DIGIT_MAP)

        if self.person.second_name != None and self.person.second_name != "":
            result = [val1 + val2 + val3 for val1,val2,val3 in zip(digit_first_name_length_list,
                                                               digit_second_name_length_list,
                                                               digit_surname_length_list)]
        else:
            result = [val1 + val2 for val1,val2 in zip(digit_first_name_length_list,
                                                        digit_surname_length_list)]
        
        return result
    
    
    def calcualting_life_transits(self) -> list[int]:
        univeral_year_list = common.generate_number_sequence(self.birthday.year)
        personal_year_list = common.generate_number_sequence(self.birthday.year, extra_value=self.birthday.day + self.birthday.month)
        sum_of_year_transits = self.calculating_name_year_transit() 

        result = [val1 + val2 + val3 for val1,val2,val3 in zip(univeral_year_list,
                                                               personal_year_list,
                                                               sum_of_year_transits)]

        return result
        
    
    def calculating_karmic_lesson(self) -> dict[str, int]:
        """
            Calculate the dict of karmic lessons
        """
        #result_dict = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
        person_list = [self.person.SINGLE_DIGIT_MAP[char] for char in self.person.fullname if char in self.person.SINGLE_DIGIT_MAP]

        # for element in person_list:
        #     if str(element) in result_dict.keys():
        #         result_dict[str(element)] += 1
        counter = Counter(person_list)

        return dict(counter)
    



birthday = BirthdateData(9 , 4, 1998)
person = NameData("Thomas", "Hanks", "Jeffrey")
calculator = NumerologyCalculator(birthday, person)

