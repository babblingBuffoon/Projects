
# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
#
# For example,
#
# [True,  True,  True,  False,
#  True,  True,  True,  True ,
#  True,  False, True,  False,
#  True,  False, False, True ,
#  True,  True,  True,  True ,
#  False, False, True,  True]
#
# The correct answer would be 17.
#
# Hint: Don't forget to check for bad values like null/undefined

# Pseudo code:
# - create a variable to keep track no. of sheep present start from 0.
# - iterate thorugh the array
# - check if values match true (present)
# - increase the counter by 1 for any true statment
# - return no of sheeps that are present and total no.

array = [True,  True,  True,  False,
         True,  True,  True,  True ,
         True,  False, True,  False,
         True,  False, False, True ,
         True,  True,  True,  True ,
         False, True,  True, "maybe" , "possible" , True]

# def sum_array(a):
#     sheepPresent = 0
#     for x in a: 
#         if x == True:
#             sheepPresent += 1 
#     return sheepPresent


# Alternative

def sum_array(a):
    return a.count(True)     



print(sum_array(array))