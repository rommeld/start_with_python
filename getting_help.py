def round_to_two_places(num):
    """Return the given number rounded to two decimal places.

    >>> round_to_two_places(3.14159)
    3.14
    """
    return(round(num, 2))

# Put your test code here
print(round(31437, -2))

def to_smash(total_candies, total_friends = 3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.

    >>> to_smash(91)
    1
    """
    return total_candies % total_friends

round_to_two_places(9.9999)

x = -10
y = 5
# # Which of the two variables above has the smallest absolute value?
smallest_abs = min(abs(x), abs(y))
smallest_abs

def f(x):
    y = abs(x)
    return y

print(f(5))
