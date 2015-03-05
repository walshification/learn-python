# While Loops

# 1. Make sure that you use while-loops sparingly. Ususally a for-loop is 
#   better.
# 2. Review your while statements and make sure that the boolean test will
#   become False at some point.
# 3. When in doubt, print out your test variable at the top and bottom of the
#   while-loop to see what it's doing.

# # Original loop
# i = 0
# numbers = []

# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)

#     i = i + 1
#     print "Numbers now: ", numbers
#     print "At the bottom i is %d" % i

# print "The numbers: "

# for num in numbers:
#     print num

# Study Drills

# 1. Convert this while-loop to a function that you can call, and replace 6 in the test (i < 6) with a variable.
# def while_looper():
#     i = 0
#     numbers = []
#     incor = 6

#     while i < limit:
#         print "At the top i is %d" % i
#         numbers.append(i)

#         i = i + 1
#         print "Numbers now: ", numbers
#         print "At the bottom i is %d" % i

#     print "The numbers: "

#     for num in numbers:
#         print num

# 2. Use this function to rewrite the script to try different numbers.
# def while_looper(start_number, end_number):
#     i = start_number
#     numbers = []
#     limit = end_number

#     while i < limit:
#         print "At the top i is %d" % i
#         numbers.append(i)

#         i = i + 1
#         print "Numbers now: ", numbers
#         print "At the bottom i is %d" % i

#     print "The numbers: "

#     for num in numbers:
#         print num

# 3. Add another variable to the function arguments you can pass in that lets 
#   you change the +1 on line 8 so you can change how much it increments by.
# def while_looper(start_number, end_number, incrementor):
#     i = start_number
#     numbers = []
#     limit = end_number

#     while i < limit:
#         print "At the top i is %d" % i
#         numbers.append(i)

#         i += incrementor
#         print "Numbers now: ", numbers
#         print "At the bottom i is %d" % i

#     print "The numbers: "

#     for num in numbers:
#         print num

# 4. Rewrite the script again to use this function to see what effect it has.
def while_looper(start_number, end_number, incrementor):
    i = start_number
    numbers = []
    limit = end_number

    while i < limit:
        print "At the top i is %d" % i
        numbers.append(i)

        i += incrementor
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

while_looper(0, 6, 1)

# 5. Write it to use for-loops and range. Do you need the incrementor in the 
#   middle anymore? What happens if you do not get rid of it?
def for_looper(start_number, end_number):
    numbers = []

    for i in range(start_number, end_number):
        numbers.append(i)
        print "Numbers now: ", numbers

    print "The numbers: "
    for num in numbers:
        print num

# Must increment by 1.
for_looper(0, 6)
