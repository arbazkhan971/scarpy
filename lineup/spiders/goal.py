# -*- coding: utf-8 -*-
import scrapy


class GoalSpider(scrapy.Spider):
    name = 'goal'
    allowed_domains = ['www.goal.com/en-in/match/las-palmas-v-valencia/lineups/8jih1ewoiscndoh57bu018vhm']
    start_urls = ['http://www.goal.com/en-in/match/las-palmas-v-valencia/lineups/8jih1ewoiscndoh57bu018vhm/']

    def parse(self, response):
        names=response.xpath('//*[@class="widget-match-lineups__name"]/text()').extract()
        
        yield{'Names':names}
