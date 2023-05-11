import pandas as pd


class CheckerPrice:
    def __init__(self, filename, reader, open_url):
        self.filename = filename
        self.reader = reader
        self.open_url = open_url

    def compare_prices(self, model_dict):
        df = pd.read_csv(self.filename)
        changes_models = []

        for model, current_price in model_dict.items():
            current_price = float(current_price.replace(',', ''))
            previous_price = df.loc[df['Model'] == model, 'Price'].values
            if len(previous_price) > 0:
                previous_price = str(previous_price[0])
                previous_price = float(previous_price.replace(',', ''))
                if current_price < previous_price and (previous_price - current_price) / previous_price >= 0.1:
                    changes_models.append(model)

        print(changes_models)