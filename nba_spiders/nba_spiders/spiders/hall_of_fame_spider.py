import scrapy


class HallOfFameSpider(scrapy.Spider):
    name = "hall_of_fame"

    start_urls = [
        'https://en.wikipedia.org/wiki/List_of_players_in_the_Naismith_Memorial_Basketball_Hall_of_Fame'
    ]

    def parse(self, response):
        filename = 'hall_of_fame.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
