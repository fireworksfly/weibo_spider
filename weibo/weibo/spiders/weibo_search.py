import scrapy
import sys
import os
from scrapy.utils.project import get_project_settings
from weibo.utils import util
BASE_URL = 'https://s.weibo.com/weibo?q=%s'


class WeiboSearchSpider(scrapy.Spider):
    name = 'weibo_search'
    allowed_domains = ['weibo.com']
    settings = get_project_settings()
    keyword_list = settings.get('KEYWORD_LIST')

    # 暂时只能通过list的方式来进行来添加关键词, 后面会通过txt的方式来进行添加
    if not isinstance(keyword_list, list):
        if not os.path.isabs(keyword_list):
            keyword_list = os.getcwd() + os.sep + keyword_list
        if not os.path.isfile(keyword_list):
            sys.exit('不存在%s文件' % keyword_list)
        keyword_list = util.get_keyword_list(keyword_list)

    def start_requests(self):
        for keyword in self.keyword_list:
            url = BASE_URL % keyword
            yield scrapy.Request(url=url,
                                 callback=self.parse,
                                 meta={
                                     'base_url': BASE_URL,
                                     'keyword': keyword
                                 })

    def parse(self, response, *args):
        base_url = response.meta.get('base_url')
        keyword = response.meta.get('base_url')
        for content in response.xpath('//div[@action-type="feed_list_item"]//p/text()'):

