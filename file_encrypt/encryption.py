import pyAesCrypt
import os


# функция шифрования файла
def encryption(file, password):

    # Задаем размер буфера
    buffer_size = 512 * 1024

    # Вызываем метод шифрования
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    # Результат
    print(f"[Файл '{str(os.path.splitext(file)[0])}' зашифрован!]")

    # Удаляем исходный файл
    os.remove(file)


# Функция обхода по директориям
def walking_by_dirs(dir, password):

     # Перебираем все поддиректории в заданной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # Если находим файл, то шифруем его
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)

        # Если находим директорию, то продолжаем поиск файлов
        else:
            walking_by_dirs(path, password)


password = input("Введите пароль для шифрования: ")
dirs = input("Укажите директорию: ")
walking_by_dirs(dirs, password)
