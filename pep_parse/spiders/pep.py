import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        numerical_index = response.xpath('//*[@id="numerical-index"]')
        tbody = numerical_index.css('tbody')
        pep_urls = tbody.css('a[href]::attr(href)')
        for pep_url in pep_urls:
            yield response.follow(pep_url, callback=self.parse_pep)

    def parse_pep(self, response):
        number_name = response.css('h1.page-title::text').get().split(' – ')
        status = response.css('dt:contains("Status") + dd abbr::text').get()
        data = {
            'number': number_name[0][4:],
            'name': number_name[1],
            'status': status
        }
        yield PepParseItem(data)
