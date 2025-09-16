def use_abs_function(x: int) -> int:
    """
    >>> use_abs_function(-2)
    2
    >>> use_abs_function(-3)
    3
    >>> use_abs_function(0)
    0
    >>> use_abs_function(2)
    2
    >>> use_abs_function(3)
    3
    """
    return(abs(x))
def use_pow_function(x: int, y: int) -> int:
    """
    >>> use_pow_function(-2, 3)
    -8
    >>> use_pow_function(-3, 2)
    9
    >>> use_pow_function(0, 2)
    0
    >>> use_pow_function(2, 3)
    8
    >>> use_pow_function(3, 2)
    9
    """
    return(pow(x,y))
def use_round_function(x: float, ndigits: int) -> float:
    """
    >>> use_round_function(2.71828, 3)
    2.718
    >>> use_round_function(2.71828, 4)
    2.7183
    >>> use_round_function(3.141592, 2)
    3.14
    >>> use_round_function(3.141592, 5)
    3.14159
    """
    return(round(x,ndigits))
def use_bin_function(x: int) -> str:
    """
    >>> use_bin_function(0)
    '0b0'
    >>> use_bin_function(1)
    '0b1'
    >>> use_bin_function(2)
    '0b10'
    >>> use_bin_function(3)
    '0b11'
    >>> use_bin_function(4)
    '0b100'
    >>> use_bin_function(5)
    '0b101'
    """
    return(bin(x))
def use_bool_function(x: int) -> bool:
    """
    >>> use_bool_function(0)
    False
    >>> use_bool_function(1)
    True
    >>> use_bool_function(2)
    True
    >>> use_bool_function(3)
    True
    >>> use_bool_function(4)
    True
    """
    return(bool(x))
def use_int_function(x: float) -> int:
    """
    >>> use_int_function(2.71828)
    2
    >>> use_int_function(3.141592)
    3
    >>> use_int_function(-2.71828)
    -2
    >>> use_int_function(-3.141592)
    -3
    """
    return(int(x))
def calculate_bmi(height: int, weight: int) -> float:
    """
    >>> calculate_bmi(216, 147)
    31.507201646090532
    >>> calculate_bmi(206, 113)
    26.628334433028563
    >>> calculate_bmi(211, 110)
    24.70744143213315
    """
    BMI=weight/(height/100)**2
    return(BMI)
def format_integer_with_dollar_sign_and_commas(x: int) -> str:
    """
    >>> format_integer_with_dollar_sign_and_commas(1000)
    '$1,000'
    >>> format_integer_with_dollar_sign_and_commas(1000000)
    '$1,000,000'
    >>> format_integer_with_dollar_sign_and_commas(1000000000)
    '$1,000,000,000'
    """
    return f"{x:,}"
def is_positive(x: int) -> bool:
    """
    >>> is_positive(-1)
    False
    >>> is_positive(0)
    False
    >>> is_positive(1)
    True
    """
    return(x>0)
def is_even(x: int) -> bool:
    """
    >>> is_even(0)
    True
    >>> is_even(1)
    False
    >>> is_even(2)
    True
    >>> is_even(3)
    False
    >>> is_even(4)
    True
    """
    return(x%2==0)
