# Catalog Product Upload from CSV

This project is a web application that allows you to upload product data from a CSV file and save it to a database. The application also provides a catalog page to display the uploaded products and a detail page for each product.

## Features

1. Create a Phone model in models.py with the following fields:
   - id: Primary key
   - name: Product name
   - price: Product price
   - image: Product image
   - release_date: Product release date
   - lte_exists: Indicates if the product supports LTE
   - slug: Slugified version of the product name

2. Implement a management command import_phones in import_phones.py to transfer data from a CSV file to the Phone model.

3. Create a catalog page /catalog that displays all the uploaded products.

4. Create a product detail page /catalog/<slug> that displays the details of a specific product.

5. Implement sorting functionality on the catalog page to allow users to sort products by name (alphabetical order) and price (ascending and descending).

## Usage

1. Install the dependencies:

   pip install -r requirements.txt

2. Create the database migrations:

   python manage.py makemigrations
   python manage.py migrate

3. Import the product data from the CSV file:

   python manage.py import_phones

4. Start the development server:

   python manage.py runserver

5. Access the application in your web browser:
   - Catalog page: http://127.0.0.1:8000/catalog
   - Product detail page: http://127.0.0.1:8000/catalog/<slug>

## Implementation Details

1. The Phone model is defined in models.py with the required fields.
2. The import_phones.py file contains the management command import_phones to load the product data from a CSV file into the Phone model.
3. The catalog page /catalog is implemented in the views.py file, and it displays all the uploaded products.
4. The product detail page /catalog/<slug> is also implemented in the views.py file, and it displays the details of a specific product.
5. The sorting functionality is implemented by processing the sort parameter from the request.GET data in the views.py file.




# Выгрузка каталога товаров из csv-файла с сохранением всех позиций в базе данных

## Задание

Есть некоторый [csv-файл](./phones.csv), который выгружается с сайта-партнера. Этот сайт занимается продажей телефонов.

Мы же являемся их региональными представителями, поэтому нам необходимо взять данные из этого файла и отобразить их на нашем сайте на странице каталога, с их предварительным сохранением в базу данных.

## Реализация

Что необходимо сделать

- В файле `models.py` нашего приложения создаём модель Phone с полями `id`, `name`, `price`, `image`, `release_date`, `lte_exists` и `slug`. Поле `id` — должно быть основным ключом модели.
- Значение поля `slug` должно устанавливаться слагифицированным значением поля `name`.
- Написать скрипт для переноса данных из csv-файла в модель `Phone`.
  Скрипт необходимо разместить в файле `import_phones.py` в методе `handle(self, *args, **options)`.
  Подробнее про подобные скрипты (django command) можно почитать [здесь](https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/) и [здесь](https://habr.com/ru/post/415049/).
- При запросе `<имя_сайта>/catalog` должна открываться страница с отображением всех телефонов.
- При запросе `<имя_сайта>/catalog/iphone-x` должна открываться страница с отображением информации по телефону. `iphone-x` — это для примера, это значние берётся из `slug`.
- В каталоге необходимо добавить возможность менять порядок отображения товаров: по названию в алфавитном порядке и по цене по убыванию и по возрастанию.

Шаблоны подготовлены, ваша задача — ознакомиться с ними и корректно написать логику.

## Ожидаемый результат

![Каталог с телефонами](res/catalog.png)

## Подсказка

Для переноса данных из файла в модель можно выбрать один из способов:

- воспользоваться стандартной библиотекой языка Python: `csv` (рекомендуется).
- построчно пройтись по файлу и для каждой строки сделать соответствующую запись в БД.

Для реализации сортировки можно брать параметр `sort` из `request.GET`.

Пример запросов:

- `<имя_сайта>/catalog?sort=name` — сортировка по названию;
- `<имя_сайта>/catalog?sort=min_price` — сначала отображать дешёвые.

## Документация по проекту

Для запуска проекта необходимо

Установить зависимости:

```bash
pip install -r requirements.txt
```

Выполнить следующие команды:

- Команда для создания миграций приложения для базы данных

```bash
python manage.py migrate
```

- Команда для загрузки данных из csv в БД

```bash
python manage.py import_phones
```

- Команда для запуска приложения

```bash
python manage.py runserver
```

- При создании моделей или их изменении необходимо выполнить следующие команды:

```bash
python manage.py makemigrations
python manage.py migrate
```
