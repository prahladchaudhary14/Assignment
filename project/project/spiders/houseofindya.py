import scrapy


class HouseofindyaSpider(scrapy.Spider):
    name = 'houseofindya'
    start_urls = [
        'https://www.houseofindya.com/zyra/necklace-sets/cat'
        ]

    def parse(self, response):
        links =response.css('ul#JsonProductList li a::attr(href)').extract()
        yield from response.follow_all(links,callback=self.parse_item)

    def parse_item(self, response):
        yield {
            'title':response.css('h1::text')[0].extract(),
            'price':response.css('h4 span::text')[1].extract(),
            'description':response.css('div#tab-1 p::text')[0].extract()+response.css('div#tab-1 p::text')[1].extract(),
            'img_links':response.css('img.lazySlider::attr(data-original)').extract()
        }
