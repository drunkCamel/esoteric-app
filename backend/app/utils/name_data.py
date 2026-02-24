from app.utils.exceptions  import InvalidTypeError

class NameData:
    """Initiating the name variable"""
    SINGLE_DIGIT_MAP = {
        'a': 1, 'j': 1, 's': 1,
        'b': 2, 'k': 2, 't': 2,
        'c': 3, 'l': 3, 'u': 3,
        'd': 4, 'm': 4, 'v': 4,
        'e': 5, 'n': 5, 'w': 5,
        'f': 6, 'o': 6, 'x': 6,
        'g': 7, 'p': 7, 'y': 7,
        'h': 8, 'q': 8, 'z': 8,
        'i': 9, 'r': 9
    }

    VOWEL_MAP = {'a': 1, 'e': 5, 'i': 9, 'o': 6, 'u': 3}
    CONSONANT_MAP = {'j': 1, 's': 1, 'b': 2, 'k': 2, 't': 2, 'c': 3, 'l': 3, 
        'd': 4, 'm': 4, 'v': 4, 'n': 5, 'w': 5, 'f': 6, 'x': 6,
        'g': 7, 'p': 7, 'y': 7, 'h': 8, 'q': 8, 'z': 8, 'r': 9}
    DOUBLE_DIGIT_MAP = {chr(i + 96): i for i in range(1, 27)} 


    def __init__(self, first_name: str, surname: str, second_name: str| None = None):
        
        # Validate first_name and surname (must be non-empty strings)
        if not isinstance(first_name, str) or not first_name.strip():
            raise InvalidTypeError("first_name must be a non-empty string")
        
        # Validate surname (must be non-empty string)
        if not isinstance(surname, str) or not surname.strip():
            raise InvalidTypeError("surname must be a non-empty string")
        
        # Validate second_name type (only if not None)
        if second_name is not None and not isinstance(second_name, str):
            raise InvalidTypeError("second_name must be a string or None")
        
        # Validate first_name and surname (must be non-empty strings) --- IGNORE ---
        if not all(isinstance(s, str) and s.strip() for s in [first_name, surname]):
            raise InvalidTypeError("first_name, surname must be a non-empty and string")
        

        self.first_name = first_name
        self.surname = surname

        # Convert empty or whitespace-only strings to None for second_name
        if second_name and second_name.strip():
            self.second_name = second_name.strip()
        else:
            self.second_name = None
        

    @property
    def fullname(self) -> list[str]:
        names =  [name for name in (self.first_name, self.second_name, self.surname) if name is not None]
        return ''.join(names).lower()
    

    def extract_digits_from_list(self,type:str) -> list[list[int]]:
        map_selector = {
            'VOWEL_MAP': self.VOWEL_MAP,
            'CONSONANT_MAP': self.CONSONANT_MAP,
            'SINGLE_DIGIT_MAP': self.SINGLE_DIGIT_MAP,
            'DOUBLE_DIGIT_MAP': self.DOUBLE_DIGIT_MAP
        }

        select_map = map_selector[type]

        names = [name.lower() for name in [self.first_name, self.surname, self.second_name] 
             if name is not None]
        
        return [[select_map[char] for char in element if char in select_map] 
                for element in names]

