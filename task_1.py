duration = int(input())

# duration = 53
# duration = 530
# duration = 5300
# duration = 53000
# duration = 530000

if duration <= 60:
    print('{} сек'.format(duration))
elif 60 < duration < 3600:
    minutes = duration // 60
    sec = duration - (minutes * 60)
    print('{} мин {} сек'.format(minutes, sec))
elif 3600 <= duration < 86400:
    hours = duration // 3600
    minutes = (duration - (hours * 3600)) // 60
    sec = duration - (hours * 3600) - (minutes * 60)
    print('{} час {} мин {} сек'.format(hours, minutes, sec))
elif 86400 <= duration <= 604800:
    days = duration // 86400
    hours = (duration - (days * 86400)) // 3600
    minutes = (duration - (days * 86400) - (hours * 3600)) // 60
    sec = duration - (days * 86400) - (hours * 3600) - (minutes * 60)
    print('{} дней {} час {} мин {} сек'.format(days, hours, minutes, sec))
