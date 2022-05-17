"""
Program to convert arabic numbers into romans
by: Deivy Peña - ID: 1099429
"""

# Arrays to convert from integer to roman number (through a control var)

integers = [1000000, 900000, 500000, 400000, 100000, 90000, 50000, 40000, 10000, 9000, 5000, 4000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 3, 2, 1]
romans = ["M̄", "C̄M̄", "D̄", "C̄D̄", "C̄", "X̄C̄", "L̄", "X̄L̄", "X̄", "MX̄", "V̄", "MV̄", "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "III", "II", "I"]

#Function to make the conversion
def IntegerToRoman(intNumber):
    realInteger = int(intNumber)
    conversion = ""
    i = 0
    while (realInteger > 0):
        for _ in range(realInteger // integers[i]):
            conversion += romans[i]
            realInteger -= integers[i]
        i += 1
    return conversion

#Function to validate input
def InputValidation(input):
    if (str(input).isnumeric()):
        if(int(input) > 0 and int(input) <= 1000000):
            return True
        else:
            return False
    else:
        return False

# Function declare to be used as a Main
def Main():
    arabicNumber = input("Type an arabic number in the interval: [1, 1000000]: ")
    while (True):
        if(InputValidation(arabicNumber)):
            break
        else:
            arabicNumber = input("Wrong format, be sure that you are typing an integer in the interval: [1, 1000000]\nType it again: ")
    return arabicNumber + " in Roman is: " + IntegerToRoman(arabicNumber)

#print(Main())
#LastCommit 10: 41 PM 16/5/2022