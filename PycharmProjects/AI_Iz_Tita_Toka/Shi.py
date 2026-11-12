import requests
import sys
# Обновляем строку импорта
# Пробуем импортировать напрямую из g4f, как это часто бывает в обновленных версиях.
try:
    from g4f import Client, APIError, RateLimitError
except ImportError:
    # Если не сработало, используем исходный импорт, но это, вероятно, вызовет ошибку.
    # Это сделано для демонстрации, что вам нужно найти актуальный путь импорта.
    print("Внимание: Актуальные пути импорта для g4f.APIError и g4f.RateLimitError могут быть другими. Пожалуйста, проверьте документацию вашей версии g4f.")
    from g4f.client import Client
    # В качестве временного решения можно определить их как заглушки,
    # чтобы код не ломался на импорте, но вы не сможете их корректно ловить!
    # APIError = Exception
    # RateLimitError = Exception


# Инициализация клиента (пустой API ключ, если не требуется)
# Примечание: g4f — это неофициальная библиотека, и ее функциональность не гарантируется.
client = Client()


# Функция для генерации и сохранения изображения
def generate_and_save_image():
    """Запрашивает промпт у пользователя, генерирует изображение и сохраняет его."""

    # 1. Запрашиваем у пользователя текстовое описание (промпт) для генерации изображения
    prompt = input("Введите описание изображения: ")
    if not prompt:
        print("Описание не может быть пустым.")
        return

    print(f"Отправка запроса на генерацию изображения с промптом: '{prompt}'...")

    # **Ключевой момент:** Если прямой импорт из g4f не сработал,
    # и вы не можете найти актуальный путь,
    # используйте более общий блок except Exception.
    try:
        # 2. Отправляем запрос на генерацию изображения
        response = client.images.generate(
            model="flux",
            prompt=prompt,
            response_format="url"
        )

        # 3. Получаем URL сгенерированного изображения
        if response and response.data and len(response.data) > 0 and hasattr(response.data[0], 'url'):
            image_url = response.data[0].url
        else:
            print("Ошибка: Не удалось получить URL изображения. Неправильная структура ответа от API.")
            print(f"Полный ответ: {response}")
            return

        print(f"URL сгенерированного изображения: {image_url}")

        if not image_url:
            print("Ошибка: Получен пустой URL.")
            return

        # 4. Загружаем изображение по полученному URL
        print("Загрузка изображения...")
        image_response = requests.get(image_url, timeout=30)
        image_response.raise_for_status()  # Вызывает исключение для плохих ответов (4xx или 5xx)

        # 5. Сохраняем изображение
        file_name = "generated_image.jpg"
        with open(file_name, "wb") as file:
            file.write(image_response.content)

        print(f"Изображение успешно сохранено как {file_name}")

    # Блок except должен использовать импортированные классы.
    # Если импорт APIError и RateLimitError всё ещё не работает, замените их на Exception.
    except (APIError, RateLimitError) as e:
        # Если импорт не сработал, замените эту строку на:
        # except Exception as e:
        print(
            f"Ошибка API (g4f): Произошла ошибка при генерации изображения. Детали: {e}",
            file=sys.stderr)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка сети: Не удалось загрузить изображение по URL. Детали: {e}", file=sys.stderr)
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}", file=sys.stderr)


if __name__ == "__main__":
    generate_and_save_image()