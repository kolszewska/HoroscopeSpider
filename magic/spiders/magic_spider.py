import scrapy


class MagicSpider(scrapy.Spider):
    name = 'magic'

    def start_requests(self):
        urls = [
            'https://magia.onet.pl/horoskop/zodiakalny-dzienny/lew',
            'https://magia.onet.pl/horoskop/zodiakalny-dzienny/baran',
            'https://magia.onet.pl/horoskop/zodiakalny-dzienny/strzelec',
            'https://magia.onet.pl/horoskop/zodiakalny-dzienny/skorpion',
            'https://magia.onet.pl/horoskop/zodiakalny-dzienny/bliznieta'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title = response.selector.xpath('//div[@id="detail"]//h3/text()').getall()[1].strip()
        details = response.selector.xpath('//div[@id="detail"]//p/text()').getall()[1].strip()
        print('****** Twój horoskop w pracy na dziś to: ******\n')
        print(title + '\n')
        print(details + '\n')
        print('\n\n')
