import requests


def test_status():
    ut = requests.get(
        'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/')
    assert ut.status_code == 200
