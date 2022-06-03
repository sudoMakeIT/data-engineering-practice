import requests
import os
import asyncio
import aiohttp

download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
]


def main():
    # create folder
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    # get file
    for download_uri in download_uris:
        r = requests.get(download_uri, allow_redirects=True)
        if r.status_code == 200:
            # write file
            open('downloads/' + download_uri.split('/')
                 [-1], 'wb').write(r.content)
            # unzip file
            os.system('unzip downloads/' + download_uri.split('/')
                      [-1] + ' -d downloads')
            # delete zip file
            os.remove('downloads/' + download_uri.split('/')[-1])


async def main_async():
    print("getting files")
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    async with aiohttp.ClientSession() as session:
        for download_uri in download_uris:
            async with session.get(download_uri) as response:
                if response.status == 200:
                    # write file
                    open('downloads/' + download_uri.split('/')[-1], 'wb').write(await response.read())
                    # unzip file
                    os.system('unzip downloads/' +
                              download_uri.split('/')[-1] + ' -d downloads')
                    # delete zip file
                    os.remove('downloads/' + download_uri.split('/')[-1])


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_async())
