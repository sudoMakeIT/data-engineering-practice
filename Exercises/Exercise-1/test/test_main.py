import requests


def test_status():
    ut = requests.get(
        'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip')
    assert ut.status_code == 200
