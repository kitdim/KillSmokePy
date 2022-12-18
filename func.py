import pickle
import os

def Load():
    with open(FILENAME, 'wb') as file:
        pass
    with open(FILENAME, 'rb') as file:
        if os.stat(FILENAME).st_size == 0:
            days = 0
        else:
            days = pickle.load(file)

    return days

def Save(day_without_smoking):
    with open(FILENAME, 'wb') as file:
        pickle.dump(day_without_smoking, file)

FILENAME = "data\\days.dat"
