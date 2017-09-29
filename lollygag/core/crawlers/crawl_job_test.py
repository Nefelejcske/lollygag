import unittest
from lollygag.core.crawlers.crawl_job import CrawlJob
from lollygag.utility.test_utils import Any, CallableMock


class CrawlJobTests(unittest.TestCase):

    def setUp(self):
        self.crawl_result = Any(link="", status_code=200, page_size=0, links=[])
        self.parser = Any(crawl=CallableMock(returns=self.crawl_result))
        self.crawler = Any(status=Any(urls_in_progress=[]), site_parser_factory=CallableMock(returns=self.parser))

    def test_crawl_site_returns_the_crawl_result_from_crawler(self):
        self.crawler.status.urls_in_progress.append("http://winnie_the_pooh")
        job = CrawlJob(self.crawler)
        result = job.crawl_site("http://winnie_the_pooh")
        self.assertTrue(result)
        self.assertEqual(result, self.crawl_result)

    def test_crawl_site_returns_none_on_interrupt(self):
        self.crawler.status.urls_in_progress.append("http://winnie_the_pooh")
        self.parser.crawl.args["raises"] = KeyboardInterrupt()
        with self.assertRaises(KeyboardInterrupt):
            job = CrawlJob(self.crawler)
            result = job.crawl_site("http://winnie_the_pooh")
            self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
