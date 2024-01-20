def make_negative( number ):
    return number if number < 0 else -number

# option 2 - absolute value function
# def make_negative( number ):
#    return -abs(number)


print(make_negative(3))