import pytest
from app.utils.common import number_to_digits,calculate_digit_sum, recursive_digit, reduce_number_to_root, calculate_all_reduction_values, all_possibilites_digts_recursion_version, generate_repeated_digit_sequence


@pytest.mark.unit
def test_number_to_digits_unit():
    assert number_to_digits(1996) == [1, 9, 9, 6]
    assert number_to_digits(2000) == [2, 0, 0, 0]
    assert number_to_digits(1573) == [1, 5, 7, 3]
    assert number_to_digits(63) == [6, 3]
    assert number_to_digits(72) == [7, 2]
    assert number_to_digits(1343577114) == [1,3,4,3,5,7,7,1,1,4]
    assert number_to_digits(1034) == [1,0,3,4]

@pytest.mark.unit
def test_calculate_digit_sum_unit():
    assert calculate_digit_sum(1996) == 25
    assert calculate_digit_sum(2000) == 2
    assert calculate_digit_sum(1573) == 16
    assert calculate_digit_sum(63) == 9
    assert calculate_digit_sum(72) == 9
    assert calculate_digit_sum(1343577114) == 36
    assert calculate_digit_sum(1034) == 8

@pytest.mark.unit
def test_recursive_digit_unit():
    assert recursive_digit(9693) == 9
    assert recursive_digit(1984) == 4
    assert recursive_digit(3995) == 8
    assert recursive_digit(75) == 3
    assert recursive_digit(996) == 6
    assert recursive_digit(1343577114) == 9
    assert recursive_digit(5678) == 8

@pytest.mark.unit
def test_reduce_number_to_root_unit():
    assert reduce_number_to_root(8888) == [8888, 32, 5]
    assert reduce_number_to_root(1984) == [1984, 22, 4]
    assert reduce_number_to_root(3335) == [3335, 14, 5]
    assert reduce_number_to_root(98) == [98, 17, 8]
    assert reduce_number_to_root(678912345) == [678912345, 45, 9]
    assert reduce_number_to_root(1343577114) == [1343577114, 36, 9]
    assert reduce_number_to_root(5678) == [5678, 26, 8]
    assert reduce_number_to_root(75) == [75, 12, 3]

@pytest.mark.unit
def test_calculate_all_reduction_values_unit():
    assert calculate_all_reduction_values([[13],[1],[25]]) == [39, 30, 21, 12, 3]
    assert calculate_all_reduction_values([[9],[7],[21]]) == [37, 19, 10, 1]
    assert calculate_all_reduction_values([[20],[6],[26]]) == [52, 34, 16, 7]
    assert calculate_all_reduction_values([[28],[8],[14]]) == [50, 41, 23, 14, 5]
    assert calculate_all_reduction_values([[22],[11],[21]]) == [54, 45, 36, 27, 18, 9]



    
