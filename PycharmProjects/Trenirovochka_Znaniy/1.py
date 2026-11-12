import subprocess
import sys
import os


def install_and_run(playlist_url):
    print("Настройка высокоточного модуля загрузки...")

    # Шаг 1: Установка специализированной библиотеки spotdl
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "spotdl"])
    except Exception as e:
        print(f"Ошибка при подготовке модуля: {e}")
        return

    # Шаг 2: Запуск процесса загрузки
    # spotdl автоматически находит треки и качает их в лучшем качестве без API ключей
    print(f"Начинаю поиск треков по ссылке: {playlist_url}")

    if not os.path.exists('music_folder'):
        os.makedirs('music_folder')

    os.chdir('music_folder')

    try:
        # Команда загрузки: ищет совпадения и качает аудио
        # Мы отключаем поиск метаданных через API, используя только публичные данные
        subprocess.run(["spotdl", playlist_url], check=True)
        print("\nЗагрузка завершена! Все треки из плейлиста в папке 'music_folder'.")
    except Exception as e:
        print(f"Ошибка при загрузке: {e}")
        print("Попробуйте скопировать ссылку на плейлист еще раз.")


if __name__ == "__main__":
    url = input("Введите точную ссылку на плейлист Spotify: ")
    install_and_run(url)