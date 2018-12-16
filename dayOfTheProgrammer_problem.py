
def dayOfProgrammer(year):
    if year < 1700 or year > 2700:
        raise ValueError("Input can't be lower than 1700 or higher than 2700!")

    # Julian Calendar
    if 1700 <= year <= 1917:
        if year % 4 == 0:
            sumDays = 244
        else:
            sumDays = 243
    # Particular case in 1918
    elif year == 1918:
        sumDays = 31 + 15 + 31 + 30 + 31 + 30 + 31 + 31
    # Gregorian calendar
    else:
        if year % 4 == 0 and year % 100 != 0:
            sumDays = 244
        elif year % 400 == 0:
            sumDays = 244
        else:
            sumDays = 243

    progDate = 256 - sumDays
    progDay = str(progDate) + "." + "09" + "." + str(year)

    return progDay

def main():
    year = int(input("Enter a year: "))
    print(dayOfProgrammer(year))

if __name__ == "__main__":
    main()