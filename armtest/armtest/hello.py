import requests

x = 100

y = [10, 20, 30]


def hello(name):
    return f'Hello, {name}!'


def url_len(url):
    return len(requests.get(url).content)
