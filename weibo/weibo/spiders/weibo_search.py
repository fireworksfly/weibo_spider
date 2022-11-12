import scrapy
import urllib.parse as code_parse
from scrapy.utils.project import get_project_settings

BASE_URL = 'https://weibo.com/'
CONCAT_URL = 'https://s.weibo.com/weibo?'
search_name = '许嵩'

if search_name != '':
    encode_name = code_parse.quote(search_name)


class WeiboSearchSpider(scrapy.Spider):
    name = 'weibo_search'
    allowed_domains = ['weibo.com']
    settings = get_project_settings().copy_to_dict()
    print(settings)
    start_urls = ['https://s.weibo.com/weibo?q=%E8%AE%B8%E5%B5%A9']

    def parse(self, response, *args):
        pass
