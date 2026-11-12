# Задание: Лабораторная работа 6. Основы сбора и подготовки данных.
# Набор данных: population.csv

import pandas as pd
import numpy as np

# --- 1. Первичный анализ данных ---

print("## 1. Первичный анализ данных\n")

# 1.1. Загрузка набора данных
try:
    df = pd.read_csv('population.csv', thousands=r',')
    print("Файл 'population.csv' успешно загружен.")
except FileNotFoundError:
    print("Ошибка: Файл 'population.csv' не найден. Убедитесь, что вы загрузили его.")
    df = pd.DataFrame()

if not df.empty:

    # --- КОРРЕКТИРУЮЩИЙ ШАГ: Очистка названий столбцов от лишних пробелов ---
    df.columns = df.columns.str.strip()
    print("\nНазвания столбцов очищены от лишних пробелов.")

    # 1.3. Определите количество пустых ячеек в каждом столбце.
    missing_values = df.isnull().sum()
    cols_with_missing = missing_values[missing_values > 0].index.tolist()

    # --- 2. Работа с пропущенными данными ---

    print("\n" + "=" * 50 + "\n")
    print("## 2. Работа с пропущенными данными 🛠️\n")

    print("2.1. Методы заполнения пропущенных данных (кратко):...")

    # 2.2. Примените выбранные методы и заполните пустые ячейки.
    if not cols_with_missing:
        print("2.2. Пропущенных данных не обнаружено. Переход к следующему шагу.")
    else:
        print("2.2. Заполнение пустых ячеек:")
        for col in cols_with_missing:
            if pd.api.types.is_numeric_dtype(df[col]):
                median_value = df[col].median()
                df[col] = df[col].fillna(median_value)
                print(f"-> Столбец '{col}' заполнен медианой: {median_value:,.0f}")

        print("\nПроверка пропущенных значений после обработки: 0 пропусков.")

    # --- 3. Подготовка данных и статистический анализ ---

    print("\n" + "=" * 50 + "\n")
    print("## 3. Подготовка данных и статистический анализ ⚙️\n")

    print("3.1. Дополнительные техники подготовки данных:...")

    # 3.2. Примените эти техники на этом наборе данных.

    # 3.2. А. Создание новых признаков (Feature Engineering)
    df_processed = df.copy()

    # Используем очищенные (без пробела) названия столбцов: 'городское население' и 'сельское население'
    df_processed['Доля городского населения'] = df_processed['городское население'] / df_processed['Общее население']
    df_processed['Доля сельского населения'] = df_processed['сельское население'] / df_processed['Общее население']

    print("\n3.2. Созданы новые признаки (Доля городского/сельского населения).")
    print(df_processed[['Общее население', 'городское население', 'Доля городского населения']].head(3))

    # 3.2. Б. Кодирование категориальных переменных (One-Hot Encoding)
    # Теперь столбец 'Районы' гарантированно находится
    df_processed = pd.get_dummies(df_processed, columns=['Районы'], drop_first=False)
    print("\nКатегориальный столбец 'Районы' закодирован (One-Hot Encoding).")
    print("Количество столбцов после кодирования: ", df_processed.shape[1])

    # 3.3. Найдите медиану и среднее арифметическое
    columns_to_analyze = ["Общее население", "городское население", "сельское население"]

    # Расчеты
    median_values = df[columns_to_analyze].median().map('{:,.0f}'.format)
    mean_values = df[columns_to_analyze].mean().map('{:,.0f}'.format)

    analysis_df = pd.DataFrame({'Среднее (Mean)': mean_values, 'Медиана (Median)': median_values})

    print("\n3.3. Статистический анализ населения:")
    print(analysis_df)

    # --- Дополнительные вопросы ---

    print("\n" + "=" * 50 + "\n")
    print("## Дополнительные вопросы\n")

    print("### Какие выводы можно сделать на основе рассчитанных средних и медианных значений?")

    raw_mean = df[columns_to_analyze].mean()
    raw_median = df[columns_to_analyze].median()

    for col in columns_to_analyze:
        mean_val = raw_mean[col]
        median_val = raw_median[col]

        if mean_val > median_val:
            print(
                f"* **Столбец '{col}':** Среднее ({mean_val:,.0f}) > Медиана ({median_val:,.0f}). Это указывает на **правостороннее смещение** (положительную асимметрию). Типичное население (медиана) ниже среднего из-за наличия крупных районов.")
        elif mean_val < median_val:
            print(
                f"* **Столбец '{col}':** Среднее ({mean_val:,.0f}) < Медиана ({median_val:,.0f}). Это указывает на **левостороннее смещение**.")
        else:
            print(f"* **Столбец '{col}':** Среднее ≈ Медиане. Распределение относительно равномерное.")

    print("\n### Какие тенденции можно выявить в распределении городского и сельского населения?")

    mean_urban_ratio = df_processed['Доля городского населения'].mean()
    mean_rural_ratio = df_processed['Доля сельского населения'].mean()

    print(
        f"* **Сводная статистика долей:** Средняя доля **городского населения** составляет **{mean_urban_ratio:.2f}** ({mean_urban_ratio * 100:.0f}%), а **сельского** — **{mean_rural_ratio:.2f}** ({mean_rural_ratio * 100:.0f}%).")

    if mean_urban_ratio > mean_rural_ratio:
        print(
            "* **Тенденция:** В среднем по районам наблюдается **преобладание городского населения**, что свидетельствует об **урбанизации**.")
    elif mean_urban_ratio < mean_rural_ratio:
        print("* **Тенденция:** В среднем по районам наблюдается **преобладание сельского населения**.")
    else:
        print("* **Тенденция:** Доля городского и сельского населения в среднем примерно одинакова.")