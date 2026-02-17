import itertools

def number_to_digits(number_int: int ) -> list[int]:
    """Takes number splits it into singular strings and returns list of integer digits"""
    return [int(d) for d in str(number_int)] 

def calculate_digit_sum(number_int: int | int) -> int: 
    """Convert number to list of digits and sum them"""
    return sum(int(d) for d in str(number_int))


def recursive_digit(number_int: int) -> int:
    """Recursively reduce number to single digit"""
    if number_int <= 9:
        return number_int
    return recursive_digit(calculate_digit_sum(number_int))


def reduce_number_to_root(number_int: int) -> list[int]:
    """Recursive operation that divides and combines numbers, 
        each recuperation adding a number to the list."""
    if number_int <= 9:
        return [number_int]
    new_nested = calculate_digit_sum(number_int)
    return [number_int] + reduce_number_to_root(new_nested)


def calculate_all_reduction_values(lista):
    """
    Generate all reduction paths for all possibility sums.
    Returns unique numbers from all reduction sequences, sorted descending.
    """
    return sorted(
        set(item 
            for num in all_possibilites_digts_recursion_version(lista) 
            for item in reduce_number_to_root(num)
        ),
        reverse=True
    )

def all_possibilites_digts_recursion_version(namelist: list) -> list[int]:
    total = [sum(sublist) for sublist in namelist]
    current_sum = sum(total)

    if all(x < 10 for x in total) and len(total) > 1:
        if current_sum >= 10:
            return [current_sum, recursive_digit(current_sum)]
        return [current_sum]
    
    new_nested = [[calculate_digit_sum(s)] for s in total]
    return [current_sum] + all_possibilites_digts_recursion_version(new_nested)


def generate_repeated_digit_sequence(name_list: list, compare_list: list, length: int = 120) -> list[int]:
    output_list = []

    for char in itertools.cycle(name_list):
        if len(output_list) >= length:
            break
        if char in compare_list:
            value = compare_list[char]
            output_list.extend([value] * value)
    
    return output_list[:120]

def generate_number_sequence(start_year: int, length: int = 120, extra_value: int = 0) -> list[int]:
    """Generate a sequence of year digit sums.
    
    Args:
        start_year: Starting year for the sequence
        length: Number of elements to generate
        extra_value: Additional value to add to each digit sum
    
    Returns:
        list: Sequence of digit sums
    """
    result_list = []
    
    while len(result_list) < length:
        digit_sum = calculate_digit_sum(start_year) + extra_value
        result_list.append(digit_sum)
        start_year += 1  # Increment and recalculate each time!
    
    return result_list



def comparing_two_values(val_one: int, val_two:int, val_3:int) -> list[int]:
    total = []
    if val_one == val_two:
        total.append(val_one)
    else:
        if val_3 == 0:
            total.append(val_one)
        else:
            total.append(val_one)
            total.append(val_two)
    total.sort(reverse=True)
    return total
