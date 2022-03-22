import datetime
import myMonths
import pandas #command: pip install pandas

"""
Input name and birthday
Outputs data as Dataframe from Pandas library
"""

firstName = "Petr"
lastName = "Novak"
birthday = "16.01.2001"

#translates month from int to string
def translateMonth(month = datetime.datetime.today().month):
    for key, value in myMonths.MONTHS.items() : 
        if month == key:
            return value

#slice birthday, translate month, return int day + year + string month
def formatBirthday(birthday):
    day = int(birthday[0:2])
    month = birthday[3:5]
    year = int(birthday[6:10])

    if month[0:1] == "0":
        month = translateMonth(int(month[1:2]))
    else:
        month = translateMonth(int(month))

    return [day, month, year]

myDataframe = pandas.DataFrame(
    {
        "Jmeno": [
            firstName + " " + lastName
        ],
        "Den narozeni": [
            str(formatBirthday(birthday)[0]) + "." + formatBirthday(birthday)[1] + " " + str(formatBirthday(birthday)[2])
            ],
    }
)

print(myDataframe)