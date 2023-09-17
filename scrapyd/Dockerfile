FROM mcr.microsoft.com/playwright/python:v1.37.0-jammy
RUN mkdir /app
COPY requirements.txt /app
RUN pip3 install -r /app/requirements.txt --no-cache-dir
COPY scrapyd.conf /etc/scrapyd/scrapyd.conf
CMD ["scrapyd"]