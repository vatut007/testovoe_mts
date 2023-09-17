**Тестовое задание для One Day Offer \| Innopolis**

Сервис позволяет парсить публичные тарифы МТС Связь ТВ и интернет. Состоит из
двух проектов: parser основанный на scrapy и rates_mts с помощью Django.

Технологии: Python,scrapy, scrapy-deploy, scrapy-playwright, Django.

Установка проекта с помощью Docker-compose:
1. Подготовить файлы для докер

Изменить файл scrapy.cfg директории rates_mts/parser
```
[settings]
default = rates_mts.settings

[deploy:local]
url = http://scrapyd:6800/
project = rates_mts
```
Изменить строчку в views.py директории rates_mts/rates_mts/rates
```
client = ScrapydClient(url='http://scrapyd:6800')
```
2. Перейти в директорию compose
```
cd infra
```
3. выполнить 
```
docker-compose up -d --build 
```
4. После запуска контенера выполнить
```
docker-compose exec -w /app/parser rates_mts scrapyd-deploy local -p rates_mts
```

После запуска проект будет доступен по адресу: http://localhost:8000/rates

Установка проекта в совокупности (Parser_web и Rates \_Mts) без докер:

1. Клонировать репозиторий:
```
Git clone
[git\@github.com:vatut007/testovoe_mts.git](git@github.com:vatut007/testovoe_mts.git)
```

2. Создать и активировать виртуальное окуружение:

```
python -m venv venv
```

Для linux:
```
source venv/bin/activate
```

Для windows:
```
source venv/scripts/activate
```

3. Обновить pip и установить зависимости из requirements.txt
```
python -m pip install --upgrade pip

pip install -r rates_mts/requirements.txt

pip install -r scrapyd/requirements.txt
```

Для работы проекта нужно запустить два сервиса Scrapyd и наш сервис.

Запуск Scrapyd
```
scrapyd
```

И в файле parser/scrapy.cfg
```
[settings]
default = rates_mts.settings

[deploy:local]
url = http://0.0.0.0:6800/
project = rates_mts
```
И в файле rates_mts/rates_mts/rates
```
client = ScrapydClient()

```
Далле запустить сервис scrapyd
```
scrapyd
```
Нужно передать spiders из проекта scrapy в сервис scrapyd. Для этого выполняется
команда в директории где находится setup.py scrapy.
```
cd rates_mts/parser

scrapyd-deploy local -p rates_mts
```

Далее в другом терминале нужно запустить наш сервис rates_mts
```
cd /rates_mts/rates_mts
```
```
python manage.py runserver
```

После запуска проект будет доступен по адресу: http://127.0.0.1:8000/rates
