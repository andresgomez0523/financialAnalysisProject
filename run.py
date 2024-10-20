from scraper.scraper import Scraper


def run():
    scraper = Scraper()
    scraper.scrape(ticker='NFLX')
    scraper.save(doc_type='csv')


if __name__ == '__main__':
    run()
