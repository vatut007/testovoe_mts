import csv
import os.path
import time
from collections import namedtuple

from django.shortcuts import redirect, render
from scrapyd_client import ScrapydClient
import logging

client = ScrapydClient(url='http://scrapyd:6800')

Rates = namedtuple('Rates', 'Name Description Price Options Quota')


def run_parser(request):
    job_id = client.schedule('rates_mts', 'rates')
    parameters = {'job_id': job_id}
    request.session['parameters'] = parameters
    return redirect('rates_wait')


def rates_list(request):
    template = 'rates/rates.html'
    rates = []
    try:
        with open("../parser/result_for_web/rates_mts.csv",
                  encoding='utf-8') as r_file:
            file_reader = csv.DictReader(r_file, delimiter=',', strict=True)
            for row in file_reader:
                rates.append(Rates(Name=row['name'],
                                   Description=row['description'],
                                   Price=row['price'],
                                   Quota=row['quota'],
                                   Options=row['options']))
    except FileNotFoundError:
        logging.info('Файл не существует')
    context = {
        'rates': rates
    }
    return render(request, template, context=context)


def clear_results(request):
    try:
        os.remove('../parser/result_for_web/rates_mts.csv')
    except FileNotFoundError:
        logging.info('Файл не существует')
    return redirect('rates')


def waiting_for_pasring(request):
    parameters = request.session.pop('parameters', {})
    job_id = parameters.get('job_id')
    jobs = client.jobs('rates_mts')
    for job in jobs['finished']:
        if job['id'] == job_id:
            return redirect('rates')
    parameters = {'job_id': job_id}
    request.session['parameters'] = parameters
    time.sleep(3)
    return redirect('rates_wait')
