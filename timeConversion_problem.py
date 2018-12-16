def timeConversion(s):
    '''Takes 12-hour input{hh:mm:ssAM|PM} and returns the 24-hour equivalent'''

    hours_12, minutes_12, seconds_12 = s.strip(':').strip('AM').strip('PM').split(":")

    if int(hours_12) > 12 or int(hours_12) < 1:
        raise ValueError("Input must be in 12 hour format AM/PM")
    elif int(minutes_12) > 59 or int(minutes_12) < 0:
        raise ValueError("Invalid time input")
    elif int(seconds_12) > 59 or int(seconds_12) < 0:
        raise ValueError("Invalid time input")

    if 'PM' in s:
        if int(hours_12) == 12:
            hours_24 = '12'
        else:
            hours_24 = str(int(hours_12) + 12)
    elif 'AM' in s:
        hours_24 = str(hours_12)
        if int(hours_24) < 10:
            hours_24 = '0' + str(hours_12).strip('0')
        if int(hours_24) == 12:
            hours_24 = '00'
    else:
        raise ValueError("Input string not formatted correctly")

    milit_hour = str(hours_24) + ':' + str(minutes_12) + ':' + str(seconds_12)

    return milit_hour

if __name__ == '__main__':

    s = input("Input should be formatted like (hh:mm:ss:AM/PM)\n")
    result = timeConversion(s)

    print(result)