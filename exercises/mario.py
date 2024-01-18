""""
In a file called mario.py in a folder called mario-less, implement a program in python that recreates that pyramid, using hashes (#) for bricks, as in the below:

       #
      ##
     ###
    ####
   #####
  ######
 #######
########

But prompt the user for an int for the pyramid's actual height, so that the program can also output shorter pyramids like the below:

  #
 ##
###

Re-prompt the user, again and again as needed, if their input is not greater than 0 or not an int altogether.
Hints

*Hints
    Recall that you can get an int from a user with get_int, which is declared in cs50.h.
    Recall that you can print a string with printf, which is declared in stdio.h.

"""


# prompt the user for an number > 0 and check for a valid number
'''
while True:

    print("Please enter an number higher then 0 ")
    n = int(input())
    if n <= 0:
        print("This is not a valid number , please try again")
    else:
        i = 0
        while i < n:
            j = i
            while j < n:
                print(f"{j} ", end="")
                j = j + 1
            print("")
            i = i + 1
        print("Complete!")

    break
    
    '''



height = 8

x = 0
while x < height:
    j = 0
    while j < height:
        print("#" , end="")
        j = j + 1
    print()
    x = x + 1


# coment



