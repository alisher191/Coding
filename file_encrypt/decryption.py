import pyAesCrypt
import os


# функция дешифрования файла
def decryption(file, password):

    # Задаем размер буфера
    buffer_size = 512 * 1024

    # Вызываем метод дешифрования
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    # Результат
    print(f"[Файл '{str(os.path.splitext(file)[0])}' расшифрован!]")

    # Удаляем исходный файл
    os.remove(file)


# Функция обхода по директориям
def walking_by_dirs(dir, password):

    # Перебираем все поддиректории в заданной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # Если находим файл, то дешифруем его
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)

        # Если находим директорию, то продолжаем поиск файлов
        else:
            walking_by_dirs(path, password)


password = input("Введите пароль для расшифровки: ")
dirs = input("Укажите директорию: ")
walking_by_dirs(dirs, password)
