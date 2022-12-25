# KillSmokePy
>The console application I created allows you to track the number of days without smoking.
***
# Libraries:
1. pickle - used to save and load files in .dat file format.
2. os - used to check whether the file was created or not.
# Modules:
1. main.py - executable file. Calls func.py.
2. func.py - contains the main methods of the application.
3. data - this directory contains a .dat file that stores information about the remaining days without smoking
# Methods:
1. Load() - loads values from the .bat file, if the file size is 0, i.e. nothing has been written to it yet or this is the first run, then it returns 0, otherwise it returns the value that is in the file.
2. Save(arg1) - takes an argument that is equal to the number of days without smoking. Further saves it in a .bat file.
***
# Installation and launch:
To use it, you need to download the project, then go to the desired directory, via cd, then run the command in the console:
1. Mac|Linux -> python main.py
2. Windows -> python main.py or python3 main.py
***
# KillSmokePy
Созданное мной консольное приложение позволяет отслеживать количество дней без курения.
***
# Библиотеки:
1. pickle - используется для сохрания и загрузки файлов в формате .dat файла.
2. os - используется для проверки создан файл или нет.
# Модули:
1. main.py - запускаемый файл. Вызывает func.py.
2. func.py - содержит основные методы работы приложения.
3. data - этот каталог хранит в себе .dat файл в котором хранится информация о сохранившихся дней без курения
# Методы:
1. Load() - загружает значения из файла .bat, если размер файла 0, т.е в него еще ничего не записано или это первый запуск, то возвращает 0, иначе возвращает значение которое есть в файле.
2. Save(arg1) - принимает аргумент, который равен количеству дней без курения. Далее сохраняет его в .bat файл.
***
# Установка и запуск:
Для использования необходимо скачать проект, далее перейти в нужную директорию, через cd, далее запустить командой в консоли:
1. MAC|Linux -> python main.py
2. Windows -> python main.py или python3 main.py
