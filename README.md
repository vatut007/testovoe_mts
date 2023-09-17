**Тестовое задание для One Day Offer \| Innopolis**

Сервис позволяет парсить публичные тарифы МТС Связь ТВ и интернет. Состоит из
двух проектов: parser основанный на scrapy и rates_mts с помощью Django.

Технологии: Python,scrapy, scrapy-deploy, scrapy-playwright, Django.

Установка проекта в совокупности (Parser_web и Rates \_Mts):

1. Клонировать репозиторий:

Git clone
[git\@github.com:vatut007/testovoe_mts.git](git@github.com:vatut007/testovoe_mts.git)

2. Создать и активировать виртуальное окуружение:

python -m venv venv

Для linux:

source venv/bin/activate

Для windows:

source venv/scripts/activate

3. Обновить pip и установить зависимости из requirements.txt

python -m pip install --upgrade pip

pip install –r rates_mts/requirements.txt

pip install –r parser/requirements.txt

Для работы проекта нужно запустить два сервиса Scrapyd и наш сервис.

Запуск Scrapyd

scrapyd

Нужно передать spiders из проекта scrapy в сервис scrapyd. Для этого выполняется
команда в директории где находится setup.py scrapy.

cd parser

scrapyd-deploy local –p rates_mts

Далее в другом терминале нужно запустить наш сервис rates_mts

cd ../rates_mts

python manage.py runserver

После запуска проект будет доступен по адресу: http://127.0.0.1:8000/rates
