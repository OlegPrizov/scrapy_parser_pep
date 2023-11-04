import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        for url in response.css('#numerical-index tbody a[href]::attr(href)'):
            yield response.follow(url, callback=self.parse_pep)

    def parse_pep(self, response):
        number_name = response.css('h1.page-title::text').get().split(' – ')
        status = response.css('dt:contains("Status") + dd abbr::text').get()
        yield PepParseItem(
            dict(
                number=number_name[0][4:],
                name=number_name[1],
                status=status
            )
        )
