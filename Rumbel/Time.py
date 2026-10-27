AllMinutes = []
AllSeconds = []
AllHours = []


Minutes, Seconds, Hours = Time(minutes, seconds)
def addTime(minutes, seconds):
    global AllMinutes, AllSeconds, AllHours

    if minutes.isdigit() and seconds.isdigit():
        minutes = int(minutes)
        seconds = int(seconds)
        if minutes < 0 or minutes > 59 or seconds < 0 or seconds > 59:
            print("ошибка время указанно не правильно")
            return None

        AllSeconds.append(seconds)
        AllMinutes.append(minutes)

        total_seconds = sum(AllSeconds)
        if total_seconds > 59:
            extra_minutes = total_seconds // 60
            remaining_seconds = total_seconds % 60

            AllMinutes.append(extra_minutes)
            AllSeconds = [remaining_seconds]
        else:
            AllSeconds = [total_seconds]

        total_minutes = sum(AllMinutes)
        if total_minutes > 59:
            extra_hours = total_minutes // 60
            remaining_minutes = total_minutes % 60

            AllHours.append(extra_hours)
            AllMinutes = [remaining_minutes]
            AllSeconds = [sum(AllHours)]
        else:
            AllMinutes = [total_minutes]
        return AllMinutes, AllSeconds, AllHours
    else:
        print('Ошибка: это не число!')
        return None

while True:
    minutes, seconds = input("Введите время").split(" ")
    print(minutes, seconds)

    Minutes, Seconds, Hours = addTime(minutes, seconds)
    print(f'Все время {Hours}:{Minutes}:{Seconds}')
