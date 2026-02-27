from fastapi import APIRouter
from app.schemas import BirthdateInput, BirthdateOutput
from app.utils.birthdate_data import BirthdateData 
from app.services.numerology_calc import NumerologyCalculator
from app.services.chinese_calc import ChineseCalc
#from app.services.vedic_calc import VedicCalculator

router = APIRouter(prefix="/birthdate", tags=["birthdate"])

@router.post("/calculate", response_model = BirthdateOutput)
async def calculate_birthdate(data: BirthdateInput):
    birthdate = BirthdateData(day=data.day, month=data.month, year=data.year)
    birthdate_list = birthdate.birthdate_list(val_one=data.day, val_two=data.month, val_three=data.year)
    
    
    ## Lifepath
    lifepath_number = NumerologyCalculator(birthday=birthdate).calculate_lifepath() 
    
    ## Pinnacles
    pinnacle_one = NumerologyCalculator(birthday=birthdate).calculate_pinnacle_one()
    pinnacle_two = NumerologyCalculator(birthday=birthdate).calculate_pinnacle_two()
    pinnacle_three = NumerologyCalculator(birthday=birthdate).calculate_pinnacle_three()
    pinnacle_fourth = NumerologyCalculator(birthday=birthdate).calculate_pinnacle_fourth()

    ## Personal Year and Month
    personal_year = NumerologyCalculator(birthday=birthdate).calculate_personal_year()
    personal_month = NumerologyCalculator(birthday=birthdate).calculate_personal_month()

    ## Cycles
    cycle_one = NumerologyCalculator(birthday=birthdate).calculate_cycle_one()
    cycle_two = NumerologyCalculator(birthday=birthdate).calculate_cycle_two()
    cycle_three = NumerologyCalculator(birthday=birthdate).calculate_cycle_three()

    ## Pythagorean Life Cycle
    pythagoras_life_cycle = NumerologyCalculator(birthday=birthdate).calculate_pythagoras_life_cycle()

    ## Periodical Challenges
    periodical_challenge_one = NumerologyCalculator(birthday=birthdate).calculate_periodical_challange_one()
    periodical_challenge_two = NumerologyCalculator(birthday=birthdate).calculate_periodical_challange_two()
    periodical_challenge_three = NumerologyCalculator(birthday=birthdate).calculate_periodical_challange_three()
    periodical_challenge_four = NumerologyCalculator(birthday=birthdate).calculate_periodical_challange_fourth()
    
    ## Chinese Calculations
    lo_shu_square = ChineseCalc(birthdate=birthdate).calculating_lo_shu_square()
    chinese_zodiac_sign = ChineseCalc(birthdate=birthdate).calculating_chinese_zodiac_sign()
    chinese_enemy_sign = ChineseCalc(birthdate=birthdate).calculate_chinese_enemy_sign()
    chinese_friendly_sign_one = ChineseCalc(birthdate=birthdate).calculate_chinese_friendly_sign_one()
    chinese_friendly_sign_two = ChineseCalc(birthdate=birthdate).calculate_chinese_friendly_sign_two()
    chinese_current_year_zodiac_sign = ChineseCalc(birthdate=birthdate).calculate_current_chinese_zodiac_year()

    return BirthdateOutput(
        day=birthdate.day,
        month=birthdate.month,
        year=birthdate.year,
        birthdate_list=birthdate_list,
        
        ## Numerology Calculations
        lifepath_number=lifepath_number,
        pinnacle_one=pinnacle_one,
        pinnacle_two=pinnacle_two,
        pinnacle_three=pinnacle_three,
        pinnacle_fourth=pinnacle_fourth,
        personal_year=personal_year,
        personal_month=personal_month,
        cycle_one=cycle_one,
        cycle_two=cycle_two,
        cycle_three=cycle_three,
        pythagoras_life_cycle=pythagoras_life_cycle,
        periodical_challenge_one=periodical_challenge_one,
        periodical_challenge_two=periodical_challenge_two,
        periodical_challenge_three=periodical_challenge_three,
        periodical_challenge_four=periodical_challenge_four,

        ## Chinese Calculations
        lo_shu_square=lo_shu_square,
        chinese_zodiac_sign=chinese_zodiac_sign,
        chinese_enemy_sign=chinese_enemy_sign,
        chinese_friendly_sign_one=chinese_friendly_sign_one,
        chinese_friendly_sign_two=chinese_friendly_sign_two,
        chinese_current_year_zodiac_sign=chinese_current_year_zodiac_sign
    )

