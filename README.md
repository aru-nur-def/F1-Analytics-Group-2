# F1 Analytics Project

Аналитический проект по данным Формулы-1 (2000–2020).  
Использует **SQLite + Python (SQLAlchemy, Pandas, Plotly, OpenPyXL)** для хранения, анализа и визуализации данных.  

## Структура проекта
F1-Analytics-Group/
├── db_create.py # Создание базы данных SQLite
├── data_import.py # Импорт CSV-файлов в базу
├── analytics.py # Визуализация, аналитика и экспорт в Excel
├── insert_demo.py # Добавление тестовой записи для динамического обновления графиков
├── config.py # Конфигурация подключения к БД
├── requirements.txt # Необходимые библиотеки
├── datasets/ # Исходные CSV-файлы (drivers, constructors, races, results и др.)
├── charts/ # Сгенерированные графики
├── exports/ # Сгенерированные Excel-отчёты
└── README.md # Документация


##  Установка и запуск

1. Клонировать репозиторий:
```bash
git clone https://github.com/username/F1-Analytics-Group.git
cd F1-Analytics-Group

##  Возможности

Построение графиков: pie, bar, line, histogram, scatter

Интерактивные дашборды с анимацией по сезонам

Автоматический экспорт в Excel с фильтрами и условным форматированием

Лёгкое добавление новых данных в БД

##  Примеры графиков

<img width="777" height="614" alt="image" src="https://github.com/user-attachments/assets/18a459b4-87c8-4775-9ad1-4c878e3e4ad5" />


##  Технологии

Python 3.10

SQLite + SQLAlchemy

Pandas / Plotly Express

OpenPyXL



