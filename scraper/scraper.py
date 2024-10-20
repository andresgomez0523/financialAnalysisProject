from bs4 import BeautifulSoup
from scraper.helpers import *
import pandas as pd
import numpy as np


class Scraper:

    def __init__(self):
        self.ticker = None
        self.income_statement = None

    def scrape(self, ticker):

        column_names = []
        rows = []

        html = get_html(ticker=ticker)
        soup = BeautifulSoup(html, 'html5lib')
        table_tag = soup.find('div', class_='table yf-1pgoo1f')

        for col_name_tag in table_tag.select('.column.yf-1ezv2n5'):
            column_names.append(col_name_tag.string)

        for row_tag in table_tag.select('.row.lv-0.yf-1xjz32c'):
            row = []
            for element in row_tag.select('.yf-1xjz32c')[1:]:
                row.append(element.string)
            rows.append(row)

        income_statement_df = pd.DataFrame(np.array(rows), columns=column_names)

        self.income_statement = income_statement_df
        self.ticker = ticker

    def save(self, doc_type):
        if doc_type == 'csv' and self.income_statement is not None:
            output_path = 'income_statements/' + self.ticker + '.csv'
            self.income_statement.to_csv(path_or_buf=output_path)

        else:
            pass
