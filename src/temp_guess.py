"""
Homework 2: Where to live
===========================
Course:   CS 5001
Semester: UPDATE
Student:  YOUR NAME 

An application that provides recommendations on where to live based on temp ranges. 
"""

# Remember, keep it simple. You are really working on three different problems to solve
# One for each function you are completing/working on.
def get_number(prompt: str) -> int:
    """
    Gets a whole number based on the prompt given. 

    Warning: does no error checking (so assumes client enters the correct input).

    Examples:
        Assume 0 is entered by the client
        >> get_number("Enter a number between 0 and 5: ")      # doctest: +NORMALIZE_WHITESPACE
        Enter a number between 0 and 5: 
        0

        Assume -100 is entered by the client
        >> get_number("Enter a temp: ")                        # doctest: +NORMALIZE_WHITESPACE
        Enter a temp:
        -100

    Args:
        prompt (str): The prompt you want displayed

    Returns:
        int: a whole number
    """
    pass # replace with your code


# Note: the Examples in the docstrings are simple tests. We will learn
# how to build them ourselves and test against them in the future. 
# For now, use the examples to help you think through your logic and ask yourself did 
# we cover every "case"/situation
def check_lower(first: int, second: int) -> bool:
    """
    Checks to see if first is lower or equal to y. 

    Examples: 
        >>> check_lower(10, 12)
        True
        >>> check_lower(12, 11)
        False
        >>> check_lower(10, 10)
        True

    Args:
        first (int): the first value
        second (int): the second value

    Returns:
        bool: True if first is lower than second
    """
    pass # replace with your code


# if you find yourself trying to use stuff we haven't taught you
# you are probably making it too complicated. 
def get_cities(low: int, high: int) -> str:
    r"""Builds a string of cities separated by a new line character (\n)
    that fall within a given temperature.  


    | City | High | Low |
    | Beijing | 33 | -8 |
    | Boston | 28 | -7 |
    | Honolulu | 32 | 13 |
    | San Francisco | 27 | 6 |
    | Vancouver | 24  | 2 |

    Examples:
        >>> get_cities(-10, 28)
        'Boston\nSan Francisco\nVancouver\n'
        >>> get_cities(0, 20)
        'Unknown'
        >>> get_cities(12, 34)
        'Honolulu\n'
        >>> get_cities(5, 34)
        'Honolulu\nSan Francisco\n'

    Args:
        low (int): the lower temperature 
        high (int): the higher temperature

    Returns:
        str: a string of cities separated by \n or unknown
    """
    pass # replace with your code


def main():
    """
    Asks the client for two temperatures. Based on the values, it provides cities
    that meets the conditions. Temperatures are whole numbers only.

    | City | High | Low |
    | Beijing | 33 | -8 |
    | Boston | 28 | -7 |
    | Honolulu | 32 | 13 |
    | San Francisco | 27 | 6 |
    | Vancouver | 24  | 2 |

    Values can be in any order.

    Examples:
        >> main()                                       # doctest: +NORMALIZE_WHITESPACE
        Enter a temperature: 28
        Enter a second temperature: -10
        Boston
        San Francisco
        Vancouver
        >> main()                                       # doctest: +NORMALIZE_WHITESPACE
        Enter a temperature: 0
        Enter a second temperature: 20
        Unknown    
    """
    temp1 = get_number("Enter a temperature: ")
    temp2 = get_number("Enter a second temperature: ")

    if check_lower(temp1, temp2):
        low = temp1 
        high = temp2
    else:
        high = temp1
        low = temp2

    cities = get_cities(low, high)

    print(cities.strip())  # .strip() removes leading and trailing whitespace

    again = input("Run again (y or n)? ")
    if again.strip().lower() == 'y':
        main()  # discussion item: what does this do?
    else: 
        print("Good luck on the move!")


if __name__ == "__main__":
    main()
