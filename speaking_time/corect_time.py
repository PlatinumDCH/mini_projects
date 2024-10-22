import time
def number_to_words(minutes):
    if minutes % 10 == 1 and minutes % 100 != 11:
        return f"{minutes} минута"
    elif minutes % 10 in {2, 3, 4} and minutes % 100 not in {12, 13, 14}:
        return f"{minutes} минуты"
    else:
        return f"{minutes} минут"


ti = time.localtime()
time_str = time.strftime('%H:%M', ti).split(':')

print(number_to_words(int(time_str[-1])))