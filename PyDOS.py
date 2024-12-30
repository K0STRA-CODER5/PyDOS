# Моя мини-операционная система для работы с файлами
# Меняйте что хотите :)

import os
import time

# Отображение приветствия и команды
def Terminal():
    print("---------------[PyDOS 1.0]---------------")
    print("Copyright (C) K0STRA 2025")
    print("-----------------------------------------")
    
    while True:  
        command = input("Введите команду: ")  

        if command == "Помощь":
            print("-----------[Лист команд]--------------")
            print(" очистка - Очистка экрана")
            print(" калькулятор - Калькулятор")
            print(" создать файл - Создать файл в реальной системе")
            print(" создать папку - Создать новую директорию")
            print(" выход - Выход из программы")
            print(" информация - информация про систему")
        
        elif command == "очистка":
            os.system('cls' if os.name == 'nt' else 'clear')  # Очистка экрана для Windows или Unix систем
        
        elif command == "калькулятор":
            calculator()  # Запуск калькулятора

        elif command == "создать файл":
            create_file()  # Создание файла в текущей директории
        
        elif command == "создать папку":
            create_directory()  # Создание новой папки
        
        elif command == "выход":
            print("Выход из программы...")
            break  # Выход из цикла и завершение программы

        elif command == "информация":
            print("О программе PyDOS 1.0")
            print("--------------------------")
            print("PyDOS - Python Disk Operating System")
            print("Создано: K0STRA")
            print("--------------------------")
        
        else:
            print("Неизвестная команда. Для справки введите 'Помощь'.")
            
# Функция для создания файла
def create_file():
    file_name = input("Введите имя файла для создания: ")
    try:
        with open(file_name, 'w') as file:
            file.write("Файл создан в PyDOS!")
        print(f"Файл {file_name} успешно создан.")
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")

# Функция для создания директории
def create_directory():
    dir_name = input("Введите имя директории: ")
    try:
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
            print(f"Папка {dir_name} успешно создана.")
        else:
            print("Такая папка уже существует.")
    except Exception as e:
        print(f"Ошибка при создании папки: {e}")

# Функция калькулятора
def calculator():
    print("Простой калькулятор: (+, -, *, /, =)")
    while True:
        try:
            expression = input("Введите выражение (или 'выход' для выхода): ")
            if expression.lower() == 'выход':
                break
            result = eval(expression)
            print(f"Результат: {result}")
        except Exception as e:
            print(f"Ошибка: {e}")
            continue

# Функция для создания файла после установки
def create_system_file():
    file_path = 'System.txt'  # Поменяли на текстовый файл
    try:
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write("PyDOS 1.0 установлен успешно!")
        else:
            print("PyDOS уже установлен.")
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")

# Функция проверки наличия файла
def check_system_files():
    file_path = 'System.txt'  # Поменяли на текстовый файл

    if os.path.exists(file_path):
        Terminal()
    else:
        print("Запуск установщика...")
        installer()

# Установщик
def installer():
    print("Приветствуем вас в установке PyDOS! Для установки введите действие и нажмите ВВОД.")
    print("----------------------------")
    print("       Список действий")
    print("----------------------------")
    print("1.) Установить PyDOS 1.0")
    print("2.) Выход из установщика без установки PyDOS")
    print("----------------------------")

    command = input("Введите команду: ")

    if command == "1":
        print("Установка PyDOS...")
        time.sleep(3)
        print("Установка завершена успешно!")

        # Создание файла, который будет означать успешную установку
        create_system_file()

        input("Нажмите любую клавишу для выхода из установщика.")
    elif command == "2":
        print("Выход из установщика без установки.")
        input("Нажмите любую клавишу для выхода.")
    else:
        print("Неверная команда. Пожалуйста, выберите 1 или 2.")
        installer()

# Главная функция, которая запускает проверку файлов
def main():
    check_system_files()

# Запуск программы
if __name__ == "__main__":
    main()
