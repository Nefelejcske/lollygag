import sys
import argparse
import threading
import requests
from lollygag.core.parsers.link_parser import LinkParser
from lollygag.core.crawlers.domain_crawler import DomainCrawler
from lollygag.services.config_service import ConfigService
from lollygag.services.print_service import PrintService
from lollygag.services.work.work_service import WorkService
from lollygag.dependency_injection.inject import Inject
try:
    import Queue
except ImportError:
    import queue as Queue


class Services(object):
    # pylint: disable=too-few-public-methods
    requests = requests
    site_parser_factory = LinkParser
    argparse = argparse.ArgumentParser
    config_service = ConfigService
    log_service = PrintService
    work_service = WorkService
    threading = threading
    queue = Queue.Queue
    logging_output = sys.stdout
    crawler_factory = DomainCrawler

    def __init__(self):
        self.__dict__ = Services.__dict__


def register_services(services=None):
    assert services is dict or services is None
    if not services:
        services = Services.__dict__
    Inject.register_features(**services)


register_services()
