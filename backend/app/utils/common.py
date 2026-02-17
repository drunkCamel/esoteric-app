from itertools import product
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
   # Get the sum of each sublist
    totals = [sum(sublist) for sublist in namelist]
    
    # For each total, create options [original, reduced]
    value_options = []
    for val in totals:
        reduced = recursive_digit(val)
        if val == reduced:
            # Single digit, only one option
            value_options.append([val])
        else:
            # Multi-digit, two options: original and reduced
            value_options.append([val, reduced])
    
    # Generate all combinations using product
    all_sums = set()
    for combo in product(*value_options):
        all_sums.add(sum(combo))
    
    # Return sorted descending
    return sorted(all_sums, reverse=True)


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


test = calculate_all_reduction_values([[13],[1],[25]])
print(test)