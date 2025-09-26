#  F1 Analytics Project

Аналитический проект по данным Формулы-1 (2000–2020).  
Использует **SQLite + Python (SQLAlchemy, Pandas, Plotly, OpenPyXL)** для хранения, анализа и визуализации данных.

---

##  Структура проекта

```
F1-Analytics-Group/
├── db_create.py       # Создание базы данных SQLite
├── data_import.py     # Импорт CSV-файлов в базу
├── analytics.py       # Визуализация, аналитика и экспорт в Excel
├── insert_demo.py     # Добавление тестовой записи для динамического обновления графиков
├── config.py          # Конфигурация подключения к БД
├── requirements.txt   # Необходимые библиотеки
├── datasets/          # Исходные CSV-файлы (drivers, constructors, races, results и др.)
├── charts/            # Сгенерированные графики
├── exports/           # Сгенерированные Excel-отчёты
└── README.md          # Документация
```

---

##  Установка и запуск

Клонировать репозиторий:

```bash
git clone https://github.com/aru-nur-def/F1-Analytics-Group-2.git
cd F1-Analytics-Group
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

Создать базу данных:

```bash
python db_create.py
```

Импортировать данные:

```bash
python data_import.py
```

Запустить аналитику:

```bash
python analytics.py
```

Для демонстрации динамического обновления:

```bash
python insert_demo.py
python analytics.py
```

---

##  Возможности

- Построение графиков: **pie, bar, line, histogram, scatter**
- Интерактивные дашборды с анимацией по сезонам
- Автоматический экспорт в Excel с фильтрами и условным форматированием
- Лёгкое добавление новых данных в БД

---

##  Примеры графиков

<img width="523" height="411" alt="image" src="https://github.com/user-attachments/assets/dc359c13-81f9-454a-aba7-3f77f76a93a1" />
<img width="642" height="413" alt="image" src="https://github.com/user-attachments/assets/21ee133c-4178-47fc-be10-dee17a91e142" />



---

##  Технологии

- **Python 3.10**
- **SQLite + SQLAlchemy**
- **Pandas / Plotly Express**
- **OpenPyXL**

---

##  Автор

Aruzhan Saparkhankyzy  
[231768@astanait.edu.kz]



