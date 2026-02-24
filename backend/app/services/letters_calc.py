from app.utils.name_data import NameData
from app.utils.exceptions  import InvalidDataError, InvalidReducitonLevelError, InvalidCalculationParametersError
from app.utils import common
from collections import Counter

class LettersCalculator:
    def __init__(self, person: NameData):
        """Initialise Letters Calculator."""
        self.person = person

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
    

person = NameData("Thomas", "Hanks", "Jeffrey")
calculator = LettersCalculator(person)
