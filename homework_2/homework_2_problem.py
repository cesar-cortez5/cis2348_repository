import datetime

def date_parser(dates):
    current_date = datetime.datetime.now()
    current_date_string = str(current_date)

    current_year = int(current_date_string[0:4])
    current_month = int(current_date_string[5:7])
    current_day = int(current_date_string[8:10])

    print(current_day, current_month, current_year)

    month_dict = {"January": 1,
                  "February": 2,
                  "March": 3,
                  "April": 4,
                  "May": 5,
                  "June": 6,
                  "July": 7,
                  "August": 8,
                  "September": 9,
                  "October": 10,
                  "November": 11,
                  "December": 12,
                  }

    print(month_dict.keys())

    new_dates = []

    for date in dates:
        for month in month_dict.keys():
            for day in range(0, 32):
                for year in range(1000, 3000):
                    date_find = date.find(f"{month} {day}, {year}")
                    if date_find != -1:
                        if year < current_year:
                            new_dates.append(date)
                        elif year == current_year:
                            if month < current_month:
                                new_dates.append(date)
                            elif month == current_month:
                                if day < current_day or day == current_day:
                                    new_dates.append()
                    else:
                        continue

        if date == "-1":
            break

    for date in new_dates:
        dates_separate = date.split()
        month_returned = dates_separate[0]
        day_returned = dates_separate[1]
        day_returned = day_returned.replace(',', '')
        year_returned = dates_separate[2]

        print(f"{month_dict[month_returned]}/{day_returned}/{year_returned}")


with open('input_dates.txt', 'r') as f:
    contents = f.read()
