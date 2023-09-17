FROM python:3.10-slim
RUN mkdir /app
COPY requirements.txt /app
RUN pip3 install -r /app/requirements.txt --no-cache-dir
COPY ./rates_mts /app/rates_mts
COPY ./parser /app/parser
COPY settings.py /app/parser/rates_mts
WORKDIR /app/rates_mts
CMD ["gunicorn", "rates_mts.wsgi:application", "--bind", "0:8000" ]