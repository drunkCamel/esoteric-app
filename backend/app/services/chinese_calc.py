from app.utils.birthdate_data import BirthdateData
from app.utils import common
from collections import Counter
from lunardate import LunarDate
from datetime import datetime

class ChineseCalc:
    def __init__(self, birthdate: BirthdateData, current_year: datetime = datetime.now().year):
        self.birthdate = birthdate
        self.current_year = current_year


    zodiac_animals = [
        'Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake',
        'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig'
    ]
        
    @property
    def chinese_birth_day(self) -> BirthdateData:
        lunar_birthday = LunarDate.fromSolarDate(self.birthdate.year,self.birthdate.month,self.birthdate.day)
        return BirthdateData(lunar_birthday.day,lunar_birthday.month,lunar_birthday.year) 
    

    def calculating_lo_shu_square(self) -> dict[str, int]:
        lunar_birthday = [self.chinese_birth_day.day, self.chinese_birth_day.month, self.chinese_birth_day.year]

        digits = [digit for num in lunar_birthday for digit in common.number_to_digits(num)]
        counter = Counter(digits)
        # result_dict = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

        # for element in digits:
        #     if str(element) in result_dict.keys():
        #         result_dict[str(element)] += 1
        
        # return result_dict
        return dict(counter)    
    
    def calculating_chinese_zodiac_sign(self) -> str:
        """Get Chinese zodiac animal for birth year"""

        lunar_year = self.chinese_birth_day.year
        index = (lunar_year - 4) % 12
        return self.zodiac_animals[index]
    
    def calculate_chinese_enemy_sign(self) -> str:
        lunar_year = self.chinese_birth_day.year
        index = (lunar_year + 2) % 12

        return self.zodiac_animals[index]
    
    def calculate_chinese_friendly_sign_one(self) -> str:
        lunar_year = self.chinese_birth_day.year
        index = (lunar_year + 4) % 12

        return self.zodiac_animals[index]
    
    def calculate_chinese_friendly_sign_two(self) -> str:
        lunar_year = self.chinese_birth_day.year
        index = (lunar_year + 12) % 12

        return self.zodiac_animals[index]
    
        #   'Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake',
        # 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig'

    def calculate_current_chinese_zodiac_year(self) -> str:
        #this might create a issue since it doesnt check the month, day - needs do some testing
        return self.zodiac_animals[(self.current_year - 4) % 12]
    

birthday = BirthdateData(9 , 4, 1998)
calculator = ChineseCalc(birthday, current_year=2025)
print(calculator.calculate_current_chinese_zodiac_year())