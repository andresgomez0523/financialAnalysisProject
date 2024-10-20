from scraper.constants import *
import requests


def get_html(ticker):

    url = MAIN_URL_PATH + ticker + '/financials/'

    headers = {'User-Agent': USER_AGENT}

    try:
        response = requests.get(url=url, headers=headers, timeout=10)
        response.raise_for_status()

    except requests.exceptions.HTTPError as errh:
        return "HTTP Error" + errh.args[0]

    return response.content
