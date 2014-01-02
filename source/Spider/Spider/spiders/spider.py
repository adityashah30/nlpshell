from scrapy.spider import BaseSpider
from scrapy.selector import Selector

from Spider.items import SpiderItem


class Manspider(BaseSpider):

	name = "spider"
	allowed_domains = ["linux.die.net"]

	def __init__(self, *args, **kwargs): 
		super(Manspider, self).__init__(*args, **kwargs) 
		self.start_urls = [kwargs.get('start_url')]

	def parse(self, response):
		sel = Selector(response)
		sites = sel.xpath('/html/body/div/div/dl[1]/dt')
		items = []
		for site in sites:
			item = SpiderItem()
			item['title'] = site.xpath('a/text()').extract()
			item['link'] = site.xpath('a/@href').extract()
			items.append(item)
		return items
