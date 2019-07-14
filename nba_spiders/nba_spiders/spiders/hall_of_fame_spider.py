import scrapy
import re


class HallOfFameSpider(scrapy.Spider):
    name = "hall_of_fame"

    start_urls = [
        'https://en.wikipedia.org/wiki/List_of_players_in_the_Naismith_Memorial_Basketball_Hall_of_Fame'
    ]

    def parse(self, response):
        player_rows = response.css('table.wikitable tr')[1:]

        for player_row in player_rows:
            player_data = player_row.css('td')
            player_achievements = player_data[3].css('td::text, td *::text, br').getall()

            yield {
                'inclusion_year': player_data[0].css('td::text').get(),
                'name': player_data[1].css('span span span a::text').get(),
                'position': player_data[2].css('td::text').get(),
                'achievements': re.split('<br>|;',''.join(player_achievements)),
            }
