from func import *

print("The KillSmoke shows the number of days without cigarettes.")

day_without_smoking = Load()
answer = input("Did you smoke today (y/n)?: ")

if(answer == 'y'):
    day_without_smoking = 0
else:
    day_without_smoking += 1

Save(day_without_smoking)

print(f"Days without smokking {day_without_smoking}")
#TODO Отредакатирова загрузку, скорее всего ошибка в расположении функций Load и Save