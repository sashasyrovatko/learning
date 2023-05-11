import csv
from datetime import date

import pandas as pd


class ReaderCsv:
    def __init__(self, filename):
        self.filename = filename
        self.list_file = []
        self.url_list = []

    def file_list(self):
        df = pd.read_csv(self.filename, encoding='windows-1251' )
        self.list_file = df.values.tolist()
        return self.list_file

    def get_url_list(self):
        df = pd.read_csv(self.filename, encoding='windows-1251')
        self.url_list = df["url"]
        return self.url_list

    def write_data(self, data):
        df = pd.DataFrame.from_dict(data, orient='index', columns=['Price'])
        df.index.name = 'Model'
        df.reset_index(inplace=True)
        df['Date'] = date.today()
        # df['ID'] = range(1, len(df) + 1)
        df.to_csv("output.csv", index=False)
        print("Done")

