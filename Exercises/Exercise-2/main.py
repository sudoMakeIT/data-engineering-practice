from tkinter import N
import requests
import pandas as pd
from bs4 import BeautifulSoup


def main():
    url = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'
    r = requests.get(url)

    if(r.status_code == 200):
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find('table')
        df = pd.read_html(str(table))[0]
        mod = df[df["Last modified"] == '2022-02-07 14:03']
        # print(mod['Name'].iloc[0])
        file = pd.read_csv(url+mod['Name'].iloc[0])
        print(file[file['HourlyDryBulbTemperature'] ==
              file['HourlyDryBulbTemperature'].max()])


if __name__ == '__main__':
    main()
