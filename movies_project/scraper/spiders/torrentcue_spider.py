from scrapy.spiders import Spider, CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from scraper.helpers import clean, soupify
from scraper.items import TorrentcueItem


seen_ids = set()


class TorrentcueCrawlSpider(CrawlSpider):
    name = 'torrentcue-crawl'
    allowed_domains = ['torrentcue.co']
    start_urls = ['https://torrentcue.co/']
    listing_css = ['.navbar-nav']
    
    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'Torrentcue.json'
    }

    rules = (
        Rule(LinkExtractor(restrict_css=listing_css), callback='parse_pagination', follow=True),
    )

    def parse_pagination(self, response):
        yield from TorrentcueParseSpider().parse(response)

        if (response.css('#table-breakpoint tbody tr')):
            response.meta['page_no'] = response.meta.get('page_no', 0) + 1
            url = f'?page={response.meta["page_no"]}'

            yield response.follow(url, self.parse_pagination, meta=response.meta.copy())
     

class TorrentcueParseSpider(Spider):
    name = 'torrentcue-parse'
    movie_url_t = 'https://torrentcue.co/{}'

    def parse(self, response):
        movie = TorrentcueItem()

        for movie_s in response.css('#table-breakpoint tbody tr'):
            movie_id = self.movie_id(movie_s)

            if movie_id not in seen_ids:
                seen_ids.add(movie_id)

                movie['movie_id'] = movie_id
                movie['heath'] = self.movie_heath(movie_s)
                movie['image'] = self.movie_image(movie_s)
                movie['language'] = self.movie_language(movie_s)
                movie['name'] = self.movie_name(movie_s)
                movie['type'] = self.movie_type(movie_s)
                movie['url'] = self.movie_url(movie_s)
                movie['year'] = self.movie_year(movie_s)

                yield movie

    def movie_id(self, movie_s):
        soup = self.movie_name(movie_s).split(' ') + [self.movie_language(movie_s)]
        return soupify(soup, '_')

    def movie_url(self, movie_s):
        return self.movie_url_t.format(clean(movie_s.css('td:nth-child(1) ::attr(href)'))[0])

    def movie_name(self, movie_s):
        return clean(movie_s.css('td:nth-child(1) span::text'))[0]
    
    def movie_image(self, movie_s):
        return clean(movie_s.css('td:nth-child(1) ::attr(src)'))[0]
    
    def movie_year(self, movie_s):
        return clean(movie_s.css('td:nth-child(2) ::text'))[0]
    
    def movie_type(self, movie_s):
        return clean(movie_s.css('td:nth-child(3) ::text'))[0]
    
    def movie_language(self, movie_s):
        return clean(movie_s.css('td:nth-child(4) ::text'))[0]

    def movie_heath(self, movie_s):
        return self.movie_url_t.format(clean(movie_s.css('td:nth-child(5) ::attr(src)'))[0])
