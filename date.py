MONTH_CODES = {1:1, 2:4, 3:4, 4:0, 5:2, 6:5, 7:0, 8:3, 9:6, 10:1, 11:4, 12:6}
DAYS = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def get_day_of_the_week(month, day, year):
    last_two = year % 100
    step1 = last_two // 12
    step2 = last_two % 12
    step3 = step2 // 4
    step4 = day
    step5 = MONTH_CODES[month]
    if is_leap_year(year) and month in (1, 2):
        step5 += 6
    if 1600 <= year <= 1699:
        step5 += 6
    elif 1700 <= year <= 1799:
        step5 += 4
    elif 1800 <= year <= 1899:
        step5 += 2
    elif 2000 <= year <= 2099:
        step5 += 6
    elif 2100 <= year <= 2199:
        step5 += 4
    total = step1 + step2 + step3 + step4 + step5
    return DAYS[total % 7]

print(get_day_of_the_week(12, 25, 2022))
