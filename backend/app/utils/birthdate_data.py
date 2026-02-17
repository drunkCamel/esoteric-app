from app.exceptions import InvalidDataError

class BirthdateData:
    """Initiating the name date of birh"""
    def __init__(self, day: int, month: int, year:int):
 
        # type validation
        if not isinstance(day, int) or not isinstance(month,int) or not isinstance(year,int):
            raise TypeError("day, month, and year must be integers values")
        # range validation for month
        if not 1 <= month <= 12:
            raise InvalidDataError(f"Month must be between 1 and 12, got {month}")
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