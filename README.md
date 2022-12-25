# KillSmokePy
The console application I created allows you to track the number of days without smoking.
***
# Libraries:
pickle - used to save and load files in .dat file format.
os - used to check whether the file was created or not.
# Modules:
main.py - executable file. Calls func.py.
func.py - contains the main methods of the application.
data - this directory contains a .dat file that stores information about the remaining days without smoking
# Methods:
Load() - loads values from the .bat file, if the file size is 0, i.e. nothing has been written to it yet or this is the first run, then it returns 0, otherwise it returns the value that is in the file.
Save(arg1) - takes an argument that is equal to the number of days without smoking. Further saves it in a .bat file.
***
# Installation and launch:
To use it, you need to download the project, then go to the desired directory, via cd, then run the command in the console:
Mac|Linux -> python main.py
Windows -> python main.py or python3 main.py
***
# KillSmokePy
Созданное мной консольное приложение позволяет отслеживать количество дней без курения.
***
# Библиотеки:
pickle - используется для сохрания и загрузки файлов в формате .dat файла.
os - используется для проверки создан файл или нет.
# Модули:
main.py - запускаемый файл. Вызывает func.py.
func.py - содержит основные методы работы приложения.
data - этот каталог хранит в себе .dat файл в котором хранится информация о сохранившихся дней без курения
# Методы:
Load() - загружает значения из файла .bat, если размер файла 0, т.е в него еще ничего не записано или это первый запуск, то возвращает 0, иначе возвращает значение которое есть в файле.
Save(arg1) - принимает аргумент, который равен количеству дней без курения. Далее сохраняет его в .bat файл.
***
# Установка и запуск:
Для использования необходимо скачать проект, далее перейти в нужную директорию, через cd, далее запустить командой в консоли:
MAC|Linux -> python main.py
Windows -> python main.py или python3 main.py
