from func import *

print("The KillSmoke shows the number of days without cigarettes.")

day_without_smoking = Load()
answer = input("Did you smoke today (y/n)?: ")

print(f"Days without smokking {day_without_smoking}")

if(answer == 'y'):
    day_without_smoking = 0
day_without_smoking += 1

Save(day_without_smoking)