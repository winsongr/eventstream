# hits the api http://0.0.0.0:8000/ with 10k requests per second

import requests
from concurrent.futures import ThreadPoolExecutor

url = "http://0.0.0.0:8000/"


def fetch_url():
    response = requests.get(url)
    print(response.text)


with ThreadPoolExecutor(max_workers=100) as executor:
    for _ in range(10000):
        executor.submit(fetch_url)
