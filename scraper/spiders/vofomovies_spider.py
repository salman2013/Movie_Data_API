from scrapy.spiders import Spider, CrawlSpider, Rule, Request
from scrapy.linkextractors import LinkExtractor

from scraper.helpers import clean, soupify
from scraper.items import VofomoviesItem


seen_ids = set()


class VofoMoviesCrawlSpider(CrawlSpider):
    name = 'vofomovies-crawl'
    allowed_domains = ['vofomovies.live', 'vofo-movies.co']
    start_urls = ['https://vofomovies.live/']
    listing_css = ['.nav-sidebar']

    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'Vofomovies.json'
    }

    rules = (
        Rule(LinkExtractor(restrict_css=listing_css), callback='parse_pagination', follow=True),
    )

    def parse_pagination(self, response):
        yield from VofoMoviesParseSpider().parse(response)
        
        if (not response.css('div:contains("Error Found")')) and response.css('.recommended-grid'):
            response.meta['page_no'] = response.meta.get('page_no', 0) + 1
            url = f'?page={response.meta["page_no"]}'

            yield response.follow(url, self.parse_pagination, meta=response.meta.copy())
     

class VofoMoviesParseSpider(Spider):
    name = 'vofomovies-parse'
    movie_url_t = 'https://vofo-movies.co/{}'
    
    def parse(self, response):
        for movie_s in response.css('.recommended-grid'):
            
            movie_id = self.movie_id(movie_s)

            if movie_id not in seen_ids:
                seen_ids.add(movie_id)
                movie = VofomoviesItem()

                movie['movie_id'] = movie_id
                movie['image'] = self.movie_image(movie_s)
                movie['name'] = self.movie_name(movie_s)
                movie['type'] = self.movie_type(movie_s)
                movie['url'] = self.movie_url(movie_s)
                movie['year'] = self.movie_year(movie_s)
                movie['meta'] = {'requests_queue': self.movie_requests(movie)}

                yield self.next_request_or_movie(movie)

    def parse_details(self, response):
        movie = response.meta['movie']
        movie['description'] = self.product_description(response)
        movie['image_urls'] = self.image_urls(response)

        return self.next_request_or_movie(movie)

    def movie_id(self, movie_s):
        return soupify(self.movie_name(movie_s).split(' ') + [self.movie_type(movie_s)], '_')

    def movie_url(self, movie_s):
        return self.movie_url_t.format(clean(movie_s.css('::attr(href)'))[0])

    def movie_name(self, movie_s):
        return clean(movie_s.css('.title::text'))[0]
    
    def movie_image(self, movie_s):
        return clean(movie_s.css('::attr(src)'))[0]
    
    def movie_year(self, movie_s):
        return clean(movie_s.css('.time p::text'))[0]
    
    def movie_type(self, movie_s):
        return clean(movie_s.css('.author::text'))[0]

    def product_description(self, response):
        return clean(response.css('#myList p ::text'))
    
    def image_urls(self, response):
        return clean(response.css('.show-top-grids .responsive::attr(src)'))

    def movie_requests(self, movie):
        return [Request(movie['url'], self.parse_details)]
    
    def next_request_or_movie(self, movie):
        if not movie['meta']['requests_queue']:
            del movie['meta']
            return movie

        request = movie['meta']['requests_queue'].pop()
        request.meta['movie'] = movie

        return request
