from django.http import HttpResponse
from scrapyd_client import ScrapydClient

client = ScrapydClient()


def run_parser(request):
    status = client.schedule('rates_mts', 'rates')
    return HttpResponse(f'{type(status)}')
