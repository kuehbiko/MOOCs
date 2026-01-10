# https://cs50.harvard.edu/python/2022/psets/3/outdated/

# input: prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636
# output: the same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again.
# assumptions: Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

months = ["January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"
          ]

while True: # loop forever
    date = input("Date: ")

    try:
        if "/" in date: # if format is "mm/dd/yyyy"
            month, day, year = date.split("/")

        elif "," in date: # in format is month day, year
            monthday, year = date.split(",")
            month, day = monthday.split(" ")

            month = months.index(month.title()) + 1 # change month name to number

        year = int(year)
        month = int(month)
        day = int(day)

        if (month <= 12) and (day <= 31): # check month number <=12 and day number <=31
            print(f"{year}-{month:02}-{day:02}")
            break

    except Exception: # catches all exceptions
        pass
