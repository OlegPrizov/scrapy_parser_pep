# Scrapy parser Pep

## Описание
Этот парсер умеет:
1. Собирать данные о документах PEP, считать их количество в каждом статусе и 
общее количество PEP.
2. Выводить эти данные в двух таблицах:
    1. В первом файле список всех PEP: номер, название и статус.
    2. Во втором файле сводку по статусам PEP — сколько найдено документов в каждом статусе и общее количество всех документов.

## Стек
1. Python 3.9.6
2. Scrapy 2.5.1

### Запуск проекта

- Клонируйте репозиторий и перейдите в него:

```bash
git clone git@github.com:OlegPrizov/scrapy_parser_pep.git
cd scrapy_parser_pep
```

- Cоздайте и активируйте виртуальное окружение:

```bash
python3 -m venv venv
source venv/bin/activate
```

- Обновите `pip` и установите зависимости из файла `requirements.txt`:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

- Запустите парсер:
```bash
scrapy crawl pep
```

- Заберите два файла с результатами из созданной директории 
results (она будет находиться в директории scrapy_parser_pep)

### Автор

[Олег Призов](https://github.com/OlegPrizov)
dockerhub_username: olegprizov

