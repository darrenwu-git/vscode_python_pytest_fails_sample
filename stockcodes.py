import pandas
import datetime
import site
import csv
import os


class StockCodes():
    def __init__(self):
        self.twse_codes_path = os.path.join(os.getcwd(), "twse_equities.csv")

    def get_stock_name(self, sid: str):
        with open(self.twse_codes_path, newline='') as twse:
            self.twse_codes = csv.reader(twse)
            for content in self.twse_codes:
                # the first column is id, second column is stock name
                if content[1] == sid:
                    return content[2]
        return 'NA'

def run(sid):
    pass
