# a bartender has a list of party attendees and their ages,
# and uses this function to determine whether or not to serve them.

# the function takes the values of the ages and returns a string saying if the variable (age) is >= or < 21
def legal_age(drinkers_age):
    yesNo_storage = [] #the list (empty brackets) stores a string (the bartender's response) for every age evaluated
    for number in drinkers_age:
        if number < 21:
            yesNo_storage.append("This " + str(number) + "-year-old is NOT of age")
        else:
            yesNo_storage.append("This " + str(number) + "-year-old IS of age")
    return yesNo_storage

#With a list of numbers put in directly as an argument
print legal_age([22, 56, 136])

#With a variable you create entered as an argument
sam = [22]
print legal_age(sam)

#With its value returned into a variable and that variable printed to the terminal
test_of_ages = legal_age(sam)
print test_of_ages
