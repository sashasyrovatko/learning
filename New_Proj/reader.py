import csv

import pandas as pd


class ReaderCsv:
    def __init__(self, filename):
        self.filename = filename
        self.list_file = []
        self.url_list = []

    def file_list(self):
        df = pd.read_csv(self.filename)
        self.list_file = df.values.tolist()
        return self.list_file

    def get_url_list(self):
        df = pd.read_csv(self.filename)
        self.url_list = df["url"]
        return self.url_list

    def write_data(self, data):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)


