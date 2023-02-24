import os

from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scraper.spiders.vofomovies_spider import VofoMoviesCrawlSpider


class Command(BaseCommand):
    help = "Crawl VofoMovies Spider"

    def handle(self, *args, **options):
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'scraper.settings')
        process = CrawlerProcess(settings=get_project_settings())

        process.crawl(VofoMoviesCrawlSpider)
        process.start()
