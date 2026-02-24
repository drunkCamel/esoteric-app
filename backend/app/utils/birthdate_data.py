from app.utils.exceptions import InvalidDataError, InvalidTypeError


class BirthdateData:
    """Initiating the name date of birh"""
    def __init__(self, day: int, month: int, year:int):
 
        
        # type validation - check if day,month,year are integer values
        if not isinstance(day, int) or not isinstance(month,int) or not isinstance(year,int):
            raise InvalidTypeError("day, month, and year must be integers values")
        
        # range validation for year
        if year < 1 or year > 9999:
            raise InvalidDataError(f"Year must be a positive integer, got {year}")

        
        # range validation for month
        if month < 1 or month > 12:
            raise InvalidDataError(f"Month must be between 1 and 12, got {month}")
        
        if not self._is_valid_day(day, month, year):
            raise InvalidDataError(f"Day {day} is invalid for month {month} and year {year}")
        
        # range validaiton for day
        if not 1 <= day <= 31:
            raise InvalidDataError(f"Day must be between 1 and 31, got {day}")
        # this could be able expanded on November, April, June and September have 30 days, while February has 28 days/29 days in the leap years, all remaining have 31 days
        days_in_month = {
            1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
             
        
        if day > days_in_month[month]:
            raise InvalidDataError(f"Day {day} is invalid for month {month}")
        self.day = day
        self.month = month
        self.year = year

    def _is_valid_day(self, day:int, month:int, year:int) -> bool:
        """Validate the day based on month and leap year"""
        if day < 1 or day > 31:
            return False
        
        day_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

        if self._is_leap(year):
            day_in_month[1] = 29
        
        return day <= day_in_month[month - 1]

    def _is_leap(self, year:int) -> bool:
        """Check if year is a leap yer"""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)